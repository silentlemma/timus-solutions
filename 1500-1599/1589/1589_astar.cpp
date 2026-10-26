#include <algorithm>
#include <array>
#include <chrono>
#include <cstddef>
#include <cstdint>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;
using Bitboard = uint64_t;

const int BOARD_WIDTH = 8;
const int CELL_COUNT = 64;
const int LAST_COORDINATE = BOARD_WIDTH - 1;
const int DIRECTION_COUNT = 4;
const int PLAYER_SHIFT = 56;
const Bitboard BOX_BITS = 0x00ffffffffffffffULL;
const int MAX_BOXES = 36;
const int MATCHING_SIZE = MAX_BOXES + 1;
const int MAX_PLAN_LENGTH = 10000;
const int UNREACHABLE_DISTANCE = 10000;
const int LETTER_CASE_OFFSET = 32;
const int INITIAL_HASH_SIZE = 65536;
const int HASH_LOAD_NUMERATOR = 7;
const int HASH_LOAD_DENOMINATOR = 10;
const int HASH_SHIFT_FIRST = 30;
const int HASH_SHIFT_SECOND = 27;
const int HASH_SHIFT_LAST = 31;
const Bitboard HASH_MULTIPLIER_FIRST = 0xbf58476d1ce4e5b9ULL;
const Bitboard HASH_MULTIPLIER_SECOND = 0x94d049bb133111ebULL;
const int DISTANCE_QUEUE_SIZE = 128;
const int DISTANCE_QUEUE_MASK = DISTANCE_QUEUE_SIZE - 1;
const int BYTE_BITS = 8;
const int BYTE_VALUES = 256;
const int BYTE_MASK = BYTE_VALUES - 1;
const int REGION_WIDTH = 3;
const int SMALL_PATTERN_SIZE = 3;
const int FOUR_BOX_PATTERN_SIZE = 4;
const int LARGE_PATTERN_SIZE = 5;
const int PATTERN_SIZE_COUNT = LARGE_PATTERN_SIZE + 1;
const int PRIORITY_SCALE = 100;
const int PACKING_WEIGHT = 30;
const int INITIAL_EXPANSIONS = 128;
const int ROTATED_EXPANSIONS = 64;
const int SMALL_BOX_EXPANSIONS = 4000;
const int MANY_BOX_EXPANSIONS = 256;
const int UNBOUNDED_EXPANSIONS = 2147483647;
const size_t NODE_CAP = 600000;
const double FAST_SECONDS = 1.0;
const int CLOCK_CHECK_MASK = 255;
const int ROTATION_COUNT = 4;
const int SYMMETRY_COUNT = 8;
const int REFLECTION_FLAG = 4;
const int ROTATION_MASK = 3;
const int GEOMETRY_COMPONENTS = 4;
const int PLAYER_COMPONENT = 3;
const int DIRECTION_PROBE_CELL = 27;
const auto STARTED = chrono::steady_clock::now();

struct FailedWalk {};
// The fast mode is capped and remembers rejected states.
bool fastMode = true;

// The fast budget includes input and preprocessing; check it every clock block.
bool timeUp() {
    return chrono::duration<double>(chrono::steady_clock::now() - STARTED).count() > FAST_SECONDS;
}
const int DIRECTION_STEP[DIRECTION_COUNT] = {-BOARD_WIDTH, BOARD_WIDTH, -1, 1};
const char *DIRECTION_LETTER = "udlr";
int lowestCell(Bitboard mask) { return __builtin_ctzll(mask); }
int countBits(Bitboard mask) { return __builtin_popcountll(mask); }
Bitboard cellBit(int cell) { return Bitboard(1) << cell; }
// The wall border prevents horizontal shifts from wrapping into usable cells.
Bitboard shift(Bitboard mask, int direction) {
    return direction == 0   ? mask >> BOARD_WIDTH
           : direction == 1 ? mask << BOARD_WIDTH
           : direction == 2 ? mask >> 1
                            : mask << 1;
}
// Expand a player component until no adjacent free cell remains.
Bitboard reachableCells(Bitboard reachable, Bitboard floorMask) {
    for (;;) {
        Bitboard expandedReachable =
            (reachable | (reachable << BOARD_WIDTH) | (reachable >> BOARD_WIDTH) |
             (reachable << 1) | (reachable >> 1)) &
            floorMask;
        if (expandedReachable == reachable)
            return reachable;
        reachable = expandedReachable;
    }
}
// Playable boxes fit below the top byte; it stores the lowest reachable cell.
Bitboard stateKey(Bitboard boxMask, Bitboard reachable) {
    return boxMask | (Bitboard(lowestCell(reachable)) << PLAYER_SHIFT);
}
Bitboard stateBoxes(Bitboard state) { return state & BOX_BITS; }
// Mix all key bits before linear probing in a power-of-two hash table.
Bitboard hashKey(Bitboard state) {
    state ^= state >> HASH_SHIFT_FIRST;
    state *= HASH_MULTIPLIER_FIRST;
    state ^= state >> HASH_SHIFT_SECOND;
    state *= HASH_MULTIPLIER_SECOND;
    return state ^ (state >> HASH_SHIFT_LAST);
}
// A clockwise quarter turn changes search ties without changing legal moves.
int rotateCell(int cell) {
    return (cell % BOARD_WIDTH) * BOARD_WIDTH + LAST_COORDINATE - cell / BOARD_WIDTH;
}
Bitboard rotateMask(Bitboard boxMask) {
    Bitboard result = 0;
    for (; boxMask; boxMask &= boxMask - 1)
        result |= cellBit(rotateCell(lowestCell(boxMask)));
    return result;
}

Bitboard floorMask, goalMask, initialBoxes, liveCells;
int initialPlayer;

bool reverseMode = false;
// Erase every geometrically movable box to a fixed point, ignoring player access.
// A remaining box outside the target is a deadlock.
Bitboard frozenBoxes(Bitboard boxMask) {
    Bitboard previous;
    do {
        previous = boxMask;
        Bitboard emptyCells = floorMask & ~boxMask, removable = 0;
        for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
            if (!reverseMode)
                removable |=
                    shift(emptyCells, direction) & shift(emptyCells & liveCells, direction ^ 1);
            else
                removable |= shift((emptyCells & shift(emptyCells, direction ^ 1)) & liveCells,
                                   direction ^ 1);
        }
        boxMask &= ~removable;
    } while (boxMask != previous);
    return boxMask;
}
struct Node {
    Bitboard state;
    uint32_t parent;
    uint16_t move;
};
vector<Node> nodes;
vector<uint32_t> hashTable;

// Store node indices plus one, reserving zero for an empty hash slot.
void rehash() {
    hashTable.assign(hashTable.empty() ? INITIAL_HASH_SIZE : hashTable.size() * 2, 0);
    for (unsigned i = 0; i < nodes.size(); i++) {
        size_t slot = hashKey(nodes[i].state) & (hashTable.size() - 1);
        while (hashTable[slot])
            slot = (slot + 1) & (hashTable.size() - 1);
        hashTable[slot] = i + 1;
    }
}
// Keep the first parent of each key; insertion order also breaks search ties.
int insert(Bitboard state, unsigned parent, int move) {
    if (hashTable.empty() ||
        nodes.size() * HASH_LOAD_DENOMINATOR > hashTable.size() * HASH_LOAD_NUMERATOR)
        rehash();
    size_t slot = hashKey(state) & (hashTable.size() - 1);
    while (hashTable[slot]) {
        if (nodes[hashTable[slot] - 1].state == state)
            return -1;
        slot = (slot + 1) & (hashTable.size() - 1);
    }
    hashTable[slot] = unsigned(nodes.size()) + 1;
    nodes.push_back({state, parent, (uint16_t)move});
    return int(nodes.size()) - 1;
}
// Breadth-first walks use the same up, down, left, right order as search.
string shortestWalk(Bitboard boxMask, int &player, int destination) {
    int queue[CELL_COUNT], previousCell[CELL_COUNT], previousDirection[CELL_COUNT], tail = 1;
    fill(previousCell, previousCell + CELL_COUNT, -1);
    queue[0] = player;
    previousCell[player] = player;
    for (int head = 0; head < tail && previousCell[destination] < 0; head++)
        for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
            int nextCell = queue[head] + DIRECTION_STEP[direction];
            if (nextCell >= 0 && nextCell < CELL_COUNT && (floorMask & cellBit(nextCell)) &&
                !(boxMask & cellBit(nextCell)) && previousCell[nextCell] < 0) {
                previousCell[nextCell] = queue[head];
                previousDirection[nextCell] = direction;
                queue[tail++] = nextCell;
            }
        }
    if (previousCell[destination] < 0)
        throw FailedWalk{};
    string plan;
    for (int nextCell = destination; nextCell != player; nextCell = previousCell[nextCell])
        plan += DIRECTION_LETTER[previousDirection[nextCell]];
    std::reverse(plan.begin(), plan.end());
    player = destination;
    return plan;
}
// Follow stored pushes; reverse pulls become forward pushes in chain order.
// Rebuild each intervening walk from the actual player position.
string reconstructPlan(int id) {
    vector<int> pushes;
    for (; nodes[id].parent != UINT32_MAX; id = nodes[id].parent)
        pushes.push_back(nodes[id].move);
    if (!reverseMode)
        std::reverse(pushes.begin(), pushes.end());
    Bitboard boxMask = initialBoxes;
    int player = initialPlayer;
    string plan;
    for (int encodedPush : pushes) {
        int cell = encodedPush / DIRECTION_COUNT, direction = encodedPush % DIRECTION_COUNT;
        if (reverseMode) {
            cell += DIRECTION_STEP[direction];
            direction ^= 1;
        }
        plan += shortestWalk(boxMask, player, cell - DIRECTION_STEP[direction]);
        plan += char(DIRECTION_LETTER[direction] - LETTER_CASE_OFFSET);
        boxMask ^= cellBit(cell) | cellBit(cell + DIRECTION_STEP[direction]);
        player = cell;
    }
    return plan;
}
int boxCrossingPenalty = 0;
int goals[MAX_BOXES], goalCount;
Bitboard targetBoxes;

// Restrict pushes to a corral only when removing outside movable boxes enables
// no extra boundary push and every available boundary push goes inward.
Bitboard restrictCorral(Bitboard boxMask, Bitboard reachable) {
    Bitboard unseen = floorMask & ~(boxMask | reachable), fixed = frozenBoxes(boxMask);
    while (unseen) {
        Bitboard corral = reachableCells(unseen & -unseen, floorMask & ~(boxMask | reachable));
        unseen &= ~corral;
        Bitboard border = boxMask & ((corral << 1) | (corral >> 1) | (corral << BOARD_WIDTH) |
                                     (corral >> BOARD_WIDTH));
        if (!((border & ~goalMask) | (corral & goalMask)))
            continue;
        Bitboard reduced = border | fixed,
                 relaxed = reachableCells(reachable, floorMask & ~reduced);
        bool independent = true;
        int pushCount = 0;
        for (int direction = 0; direction < DIRECTION_COUNT && independent; direction++) {
            Bitboard possible = border & shift(relaxed, direction) &
                                shift((floorMask & ~reduced) & liveCells, direction ^ 1);
            Bitboard actual = border & shift(reachable, direction) &
                              shift((floorMask & ~boxMask) & liveCells, direction ^ 1);
            if (possible != actual || (shift(possible, direction) & ~corral))
                independent = false;
            pushCount += countBits(possible);
        }
        if (independent && pushCount) {
            return border;
        }
    }
    return boxMask;
}

// Project boxes onto a boundary strip; other boxes disappear into a supply.
// Each subset records the union of player components that can solve it.
struct Region {
    Bitboard mask, regionFloor, active;
    vector<int> cells;
    vector<Bitboard> solvablePlayers;
    int packedBytes[BOARD_WIDTH][BYTE_VALUES] = {}, rows[BOARD_WIDTH], rowCount = 0;
    int index(Bitboard boxMask) const {
        int packed = 0;
        for (int rowIndex = 0; rowIndex < rowCount; rowIndex++)
            packed |= packedBytes[rowIndex][(boxMask >> (rows[rowIndex] * BYTE_BITS)) & BYTE_MASK];
        return packed;
    }
    bool good(Bitboard boxMask, Bitboard reachable) {
        return solvablePlayers[index(boxMask)] & reachable;
    }
    void build(Bitboard regionMask) {
        regionFloor = floorMask;
        active = goalMask;
        Bitboard previous;
        do {
            previous = active;
            for (int direction = 0; direction < DIRECTION_COUNT; direction++)
                active |=
                    shift(active, direction) & shift(regionFloor, direction ^ 1) & regionFloor;
        } while (active != previous);
        regionMask &= active;
        mask = regionMask;
        for (Bitboard remaining = regionMask; remaining; remaining &= remaining - 1)
            cells.push_back(lowestCell(remaining));
        solvablePlayers.assign(size_t(1) << cells.size(), 0);
        for (int row = 0; row < BOARD_WIDTH; row++) {
            int masks[BOARD_WIDTH] = {};
            bool used = false;
            for (int cellIndex = 0; cellIndex < (int)cells.size(); cellIndex++)
                if (cells[cellIndex] / BOARD_WIDTH == row) {
                    masks[cells[cellIndex] % BOARD_WIDTH] = 1 << cellIndex;
                    used = true;
                }
            if (!used)
                continue;
            rows[rowCount] = row;
            for (int byteValue = 1; byteValue < BYTE_VALUES; byteValue++)
                packedBytes[rowCount][byteValue] =
                    packedBytes[rowCount][byteValue & (byteValue - 1)] |
                    masks[lowestCell(byteValue)];
            rowCount++;
        }
        vector<Bitboard> queue;
        auto add = [&](Bitboard boxMask, Bitboard reachable) {
            int packed = index(boxMask);
            if (solvablePlayers[packed] & reachable)
                return;
            reachable = reachableCells(reachable, regionFloor & ~boxMask);
            solvablePlayers[packed] |= reachable;
            queue.push_back(stateKey(boxMask, reachable));
        };
        Bitboard boxMask = goalMask & mask, todo = regionFloor & ~boxMask;
        while (todo) {
            Bitboard reachable = reachableCells(todo & -todo, regionFloor & ~boxMask);
            add(boxMask, reachable);
            todo &= ~reachable;
        }
        Bitboard outside = active & ~mask;
        for (size_t head = 0; head < queue.size(); head++) {
            Bitboard boxMask = stateBoxes(queue[head]),
                     reachable = reachableCells(cellBit(queue[head] >> PLAYER_SHIFT),
                                                regionFloor & ~boxMask),
                     emptyCells = regionFloor & ~boxMask;
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                Bitboard movableBoxes =
                    boxMask &
                    shift(reachable & shift(emptyCells, direction ^ 1) & active, direction ^ 1);
                while (movableBoxes) {
                    int cell = lowestCell(movableBoxes);
                    movableBoxes &= movableBoxes - 1;
                    int nextCell = cell + DIRECTION_STEP[direction];
                    Bitboard nextBoxes = (boxMask ^ cellBit(cell)) | (cellBit(nextCell) & mask);
                    add(nextBoxes, cellBit(nextCell + DIRECTION_STEP[direction]));
                }
                if (countBits(boxMask) < countBits(initialBoxes)) {
                    Bitboard movableBoxes =
                        outside &
                        shift(reachable & shift(emptyCells, direction ^ 1) & mask, direction ^ 1);
                    while (movableBoxes) {
                        int cell = lowestCell(movableBoxes);
                        movableBoxes &= movableBoxes - 1;
                        int nextCell = cell + DIRECTION_STEP[direction];
                        add(boxMask | cellBit(nextCell),
                            cellBit(nextCell + DIRECTION_STEP[direction]));
                    }
                }
            }
        }
    }
};

vector<Region> regions;
bool useRegional = false;
// Use the live cells in each three-cell boundary strip, skipping duplicates.
void buildRegions() {
    for (int axis = 0; axis < 2; axis++)
        for (int side = 0; side < 2; side++) {
            int minimum = BOARD_WIDTH, maximum = 0;
            for (Bitboard remaining = floorMask; remaining; remaining &= remaining - 1) {
                int cell = lowestCell(remaining),
                    coordinate = axis ? cell / BOARD_WIDTH : cell % BOARD_WIDTH;
                minimum = min(minimum, coordinate);
                maximum = max(maximum, coordinate);
            }
            Bitboard regionMask = 0;
            for (Bitboard remaining = liveCells; remaining; remaining &= remaining - 1) {
                int cell = lowestCell(remaining),
                    coordinate = axis ? cell / BOARD_WIDTH : cell % BOARD_WIDTH;
                if (side ? coordinate > maximum - REGION_WIDTH
                         : coordinate < minimum + REGION_WIDTH)
                    regionMask |= cellBit(cell);
            }
            if (!regionMask)
                continue;
            bool duplicate = false;
            for (const auto &region : regions)
                if (region.mask == regionMask)
                    duplicate = true;
            if (duplicate)
                continue;
            Region region;
            region.build(regionMask);
            regions.push_back(std::move(region));
        }
}
// Build regional retrograde tables lazily; every projection must be solvable.
bool regionGood(Bitboard boxMask, Bitboard reachable) {
    if (regions.empty())
        buildRegions();
    for (auto &region : regions)
        if (!region.good(boxMask, reachable)) {
            return false;
        }
    return true;
}
struct GoalDistances {
    int values[MAX_BOXES][CELL_COUNT];
};
unordered_map<Bitboard, GoalDistances> distanceCache;
unordered_map<Bitboard, int> heuristicCache;
// Erase boxes movable from the expanding player component until it stops growing.
// Any remaining box outside the target proves an access deadlock.
Bitboard inaccessibleBoxes(Bitboard boxMask, Bitboard reachable) {
    for (;;) {
        Bitboard emptyCells = floorMask & ~boxMask, removable = 0;
        for (int direction = 0; direction < DIRECTION_COUNT; direction++)
            removable |=
                reverseMode
                    ? boxMask & shift(reachable & shift(emptyCells, direction ^ 1) & liveCells,
                                      direction ^ 1)
                    : boxMask & shift(reachable, direction) &
                          shift(emptyCells & liveCells, direction ^ 1);
        if (!removable)
            return boxMask;
        boxMask &= ~removable;
        reachable = reachableCells(reachable, floorMask & ~boxMask);
    }
}

unordered_map<Bitboard, vector<pair<Bitboard, Bitboard>>> packing;
int packingWeight = 0;
// Pull-erase goal boxes from every final player component, retaining fixed boxes.
// A compatible residue must be present now and its player region must intersect.
bool packingGood(Bitboard boxMask, Bitboard reachable, Bitboard fixed) {
    auto it = packing.find(fixed);
    if (it == packing.end()) {
        vector<pair<Bitboard, Bitboard>> results;
        Bitboard todo = floorMask & ~goalMask;
        while (todo) {
            Bitboard remainingGoals = goalMask,
                     reachableFromGoals = reachableCells(todo & -todo, floorMask & ~goalMask);
            todo &= ~reachableFromGoals;
            for (;;) {
                Bitboard emptyCells = floorMask & ~remainingGoals, movableBoxes = 0;
                for (int direction = 0; direction < DIRECTION_COUNT; direction++)
                    movableBoxes |=
                        remainingGoals &
                        shift(reachableFromGoals & shift(emptyCells, direction ^ 1), direction ^ 1);
                movableBoxes &= ~fixed;
                if (!movableBoxes)
                    break;
                remainingGoals &= ~movableBoxes;
                reachableFromGoals =
                    reachableCells(reachableFromGoals, floorMask & ~remainingGoals);
            }
            results.push_back({remainingGoals, reachableFromGoals});
        }
        it = packing.emplace(fixed, results).first;
    }
    for (auto packingResult : it->second)
        if (!(packingResult.first & ~boxMask) && (packingResult.second & reachable))
            return true;
    return false;
}

int patternSize = 0, binomial[MATCHING_SIZE][PATTERN_SIZE_COUNT];
// A fixed-box-conditioned subset table stores all solvable player components.
struct Pattern {
    vector<Bitboard> solvablePlayers;
    Bitboard floorMask, goals, liveCells;
    int subsetSize, cellCount, cellIndex[CELL_COUNT];
};
unordered_map<Bitboard, Pattern> patterns;
Bitboard movedBox = 0, parentFrozenBoxes = 0;
// The combinatorial number system densely ranks sorted live-cell subsets.
int rankPattern(Bitboard boxMask, const Pattern &table) {
    int rank = 0, subsetSize = 1;
    for (; boxMask; boxMask &= boxMask - 1)
        rank += binomial[table.cellIndex[lowestCell(boxMask)]][subsetSize++];
    return rank;
}
// Remove frozen goal boxes from the floor and enumerate all target subsets.
// Retrograde BFS marks every component that can reach one of those subsets.
Pattern &getPattern(Bitboard fixed) {
    auto it = patterns.find(fixed);
    if (it != patterns.end())
        return it->second;
    Pattern &table = patterns[fixed];
    table.floorMask = floorMask & ~fixed;
    table.goals = targetBoxes & ~fixed;
    table.subsetSize = min(patternSize, countBits(table.goals));
    if (table.subsetSize < 1)
        return table;
    table.liveCells = table.goals;
    Bitboard previous;
    do {
        previous = table.liveCells;
        for (int direction = 0; direction < DIRECTION_COUNT; direction++)
            table.liveCells |=
                reverseMode
                    ? shift(table.liveCells & shift(table.floorMask, direction), direction) &
                          table.floorMask
                    : shift(table.liveCells, direction) & shift(table.floorMask, direction ^ 1) &
                          table.floorMask;
    } while (table.liveCells != previous);
    fill(table.cellIndex, table.cellIndex + CELL_COUNT, -1);
    for (Bitboard remaining = table.liveCells; remaining; remaining &= remaining - 1)
        table.cellIndex[lowestCell(remaining)] = table.cellCount++;
    table.solvablePlayers.assign(binomial[table.cellCount][table.subsetSize], 0);
    vector<Bitboard> queue;
    auto add = [&](Bitboard boxMask, Bitboard reachable) {
        int index = rankPattern(boxMask, table);
        if (table.solvablePlayers[index] & reachable)
            return;
        reachable = reachableCells(reachable, table.floorMask & ~boxMask);
        table.solvablePlayers[index] |= reachable;
        queue.push_back(stateKey(boxMask, reachable));
    };
    int goalCells[MAX_BOXES], goalCount = 0;
    for (Bitboard remaining = table.goals; remaining; remaining &= remaining - 1)
        goalCells[goalCount++] = lowestCell(remaining);
    auto root = [&](Bitboard boxMask) {
        if (reverseMode) {
            add(boxMask, cellBit(initialPlayer));
            return;
        }
        Bitboard emptyCells = table.floorMask & ~boxMask;
        while (emptyCells) {
            Bitboard reachable =
                reachableCells(emptyCells & -emptyCells, table.floorMask & ~boxMask);
            add(boxMask, reachable);
            emptyCells &= ~reachable;
        }
    };
    for (int first = 0; first < goalCount; first++)
        if (table.subsetSize == 1)
            root(cellBit(goalCells[first]));
        else
            for (int second = first + 1; second < goalCount; second++)
                if (table.subsetSize == 2)
                    root(cellBit(goalCells[first]) | cellBit(goalCells[second]));
                else
                    for (int third = second + 1; third < goalCount; third++)
                        if (table.subsetSize == SMALL_PATTERN_SIZE)
                            root(cellBit(goalCells[first]) | cellBit(goalCells[second]) |
                                 cellBit(goalCells[third]));
                        else
                            for (int fourth = third + 1; fourth < goalCount; fourth++)
                                if (table.subsetSize == FOUR_BOX_PATTERN_SIZE)
                                    root(cellBit(goalCells[first]) | cellBit(goalCells[second]) |
                                         cellBit(goalCells[third]) | cellBit(goalCells[fourth]));
                                else
                                    for (int fifth = fourth + 1; fifth < goalCount; fifth++)
                                        root(
                                            cellBit(goalCells[first]) | cellBit(goalCells[second]) |
                                            cellBit(goalCells[third]) | cellBit(goalCells[fourth]) |
                                            cellBit(goalCells[fifth]));
    for (size_t head = 0; head < queue.size(); head++) {
        Bitboard boxMask = stateBoxes(queue[head]),
                 reachable = reachableCells(cellBit(queue[head] >> PLAYER_SHIFT),
                                            table.floorMask & ~boxMask),
                 emptyCells = table.floorMask & ~boxMask;
        for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
            Bitboard movableBoxes =
                reverseMode
                    ? boxMask & shift(reachable, direction) & shift(emptyCells, direction ^ 1)
                    : boxMask & shift(reachable & shift(emptyCells, direction ^ 1), direction ^ 1);
            while (movableBoxes) {
                int cell = lowestCell(movableBoxes);
                movableBoxes &= movableBoxes - 1;
                int nextCell = cell + DIRECTION_STEP[direction];
                add(boxMask ^ cellBit(cell) ^ cellBit(nextCell),
                    cellBit(reverseMode ? cell : nextCell + DIRECTION_STEP[direction]));
            }
        }
    }
    return table;
}
// Test every remaining-box subset, retaining player-component information.
// With unchanged frozen boxes, only subsets containing the moved box need retesting.
bool patternGood(Bitboard boxMask, Bitboard reachable, Bitboard fixed) {
    Pattern &table = getPattern(fixed);
    if (table.subsetSize < 1)
        return true;
    if ((boxMask & ~fixed) & ~table.liveCells)
        return false;
    int moved = movedBox && fixed == parentFrozenBoxes ? table.cellIndex[lowestCell(movedBox)] : -1;
    if (movedBox & fixed)
        moved = -1;
    int boxIndices[MAX_BOXES], boxCount = 0;
    for (Bitboard remaining = boxMask & ~fixed; remaining; remaining &= remaining - 1)
        boxIndices[boxCount++] = table.cellIndex[lowestCell(remaining)];
    for (int first = 0; first < boxCount; first++)
        if (table.subsetSize == 1) {
            if (!(table.solvablePlayers[boxIndices[first]] & reachable))
                return false;
        } else
            for (int second = first + 1; second < boxCount; second++) {
                int pairRank = boxIndices[first] + binomial[boxIndices[second]][2];
                if (table.subsetSize == 2) {
                    if (moved >= 0 && boxIndices[first] != moved && boxIndices[second] != moved)
                        continue;
                    if (!(table.solvablePlayers[pairRank] & reachable))
                        return false;
                } else
                    for (int third = second + 1; third < boxCount; third++)
                        if (table.subsetSize == SMALL_PATTERN_SIZE) {
                            if (moved >= 0 && boxIndices[first] != moved &&
                                boxIndices[second] != moved && boxIndices[third] != moved)
                                continue;
                            if (!(table.solvablePlayers[pairRank + binomial[boxIndices[third]]
                                                                           [SMALL_PATTERN_SIZE]] &
                                  reachable))
                                return false;
                        } else
                            for (int fourth = third + 1; fourth < boxCount; fourth++)
                                if (table.subsetSize == FOUR_BOX_PATTERN_SIZE) {
                                    if (moved >= 0 && boxIndices[first] != moved &&
                                        boxIndices[second] != moved && boxIndices[third] != moved &&
                                        boxIndices[fourth] != moved)
                                        continue;
                                    if (!(table.solvablePlayers[pairRank +
                                                                binomial[boxIndices[third]]
                                                                        [SMALL_PATTERN_SIZE] +
                                                                binomial[boxIndices[fourth]]
                                                                        [FOUR_BOX_PATTERN_SIZE]] &
                                          reachable))
                                        return false;
                                } else
                                    for (int fifth = fourth + 1; fifth < boxCount; fifth++) {
                                        if (moved >= 0 && boxIndices[first] != moved &&
                                            boxIndices[second] != moved &&
                                            boxIndices[third] != moved &&
                                            boxIndices[fourth] != moved &&
                                            boxIndices[fifth] != moved)
                                            continue;
                                        if (!(table.solvablePlayers
                                                  [pairRank +
                                                   binomial[boxIndices[third]][SMALL_PATTERN_SIZE] +
                                                   binomial[boxIndices[fourth]]
                                                           [FOUR_BOX_PATTERN_SIZE] +
                                                   binomial[boxIndices[fifth]]
                                                           [LARGE_PATTERN_SIZE]] &
                                              reachable))
                                            return false;
                                    }
            }
    return true;
}
// Apply component-dependent deadlock tests before looking up the box-only cache.
// The estimate is a minimum-cost assignment of boxes to distinct targets.
int heuristic(Bitboard boxMask, Bitboard reachable) {
    if (inaccessibleBoxes(boxMask, reachable) & ~targetBoxes)
        return -1;
    Bitboard frozen = frozenBoxes(boxMask);
    if (frozen & ~targetBoxes)
        return -1;
    if (useRegional &&
        (!packingGood(boxMask, reachable, frozen) || !regionGood(boxMask, reachable)))
        return -1;
    if (patternSize && !patternGood(boxMask, reachable, frozen))
        return -1;
    auto cached = heuristicCache.find(boxMask);
    if (cached != heuristicCache.end())
        return cached->second;
    GoalDistances computedDistances;
    GoalDistances *distanceTable;
    if (!boxCrossingPenalty) {
        auto it = distanceCache.find(frozen);
        if (it != distanceCache.end())
            distanceTable = &it->second;
        else
            distanceTable = &computedDistances;
    } else
        distanceTable = &computedDistances;
    if (distanceTable == &computedDistances) {
        Bitboard available = floorMask & ~frozen;
        for (int j = 0; j < goalCount; j++) {
            int *cellDistance = computedDistances.values[j];
            fill(cellDistance, cellDistance + CELL_COUNT, UNREACHABLE_DISTANCE);
            cellDistance[goals[j]] = 0;
            if (frozen & cellBit(goals[j]))
                continue;
            if (!boxCrossingPenalty) {
                int queue[CELL_COUNT], head = 0, tail = 1;
                queue[0] = goals[j];
                while (head < tail) {
                    int cell = queue[head++];
                    for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                        int nextCell = cell + DIRECTION_STEP[direction],
                            supportCell = reverseMode ? cell - DIRECTION_STEP[direction]
                                                      : nextCell + DIRECTION_STEP[direction];
                        if (nextCell < 0 || nextCell >= CELL_COUNT || supportCell < 0 ||
                            supportCell >= CELL_COUNT || !(available & cellBit(nextCell)) ||
                            !(available & cellBit(supportCell)) ||
                            cellDistance[nextCell] < UNREACHABLE_DISTANCE)
                            continue;
                        cellDistance[nextCell] = cellDistance[cell] + 1;
                        queue[tail++] = nextCell;
                    }
                }
            } else {

                // Queue-based relaxation charges for crossing occupied box and support cells.
                int queue[DISTANCE_QUEUE_SIZE], head = 0, tail = 1;
                bool queued[CELL_COUNT] = {};
                queue[0] = goals[j];
                queued[goals[j]] = true;
                while (head != tail) {
                    int cell = queue[head];
                    head = (head + 1) & DISTANCE_QUEUE_MASK;
                    queued[cell] = false;
                    int distance = cellDistance[cell];
                    for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                        int nextCell = cell + DIRECTION_STEP[direction],
                            supportCell = reverseMode ? cell - DIRECTION_STEP[direction]
                                                      : nextCell + DIRECTION_STEP[direction];
                        if (nextCell < 0 || nextCell >= CELL_COUNT || supportCell < 0 ||
                            supportCell >= CELL_COUNT || !(available & cellBit(nextCell)) ||
                            !(available & cellBit(supportCell)))
                            continue;
                        int cost = 1 + boxCrossingPenalty * ((boxMask & cellBit(cell)) != 0) +
                                   boxCrossingPenalty * ((boxMask & cellBit(supportCell)) != 0);
                        int nextDistance = distance + cost;
                        if (nextDistance < cellDistance[nextCell]) {
                            cellDistance[nextCell] = nextDistance;
                            if (!queued[nextCell]) {
                                queue[tail] = nextCell;
                                tail = (tail + 1) & DISTANCE_QUEUE_MASK;
                                queued[nextCell] = true;
                            }
                        }
                    }
                }
            }
        }
        if (!boxCrossingPenalty)
            distanceTable = &distanceCache.emplace(frozen, computedDistances).first->second;
    }
    int boxCells[MATCHING_SIZE], boxCount = 0;
    for (Bitboard remainingBoxes = boxMask; remainingBoxes; remainingBoxes &= remainingBoxes - 1)
        boxCells[++boxCount] = lowestCell(remainingBoxes);
    int boxPotential[MATCHING_SIZE] = {}, goalPotential[MATCHING_SIZE] = {},
        matchedBox[MATCHING_SIZE] = {}, previousGoal[MATCHING_SIZE] = {};
    for (int i = 1; i <= boxCount; i++) {
        matchedBox[0] = i;
        int currentGoal = 0, slack[MATCHING_SIZE];
        fill(slack, slack + MATCHING_SIZE, UNREACHABLE_DISTANCE);
        bool visitedGoal[MATCHING_SIZE] = {};
        do {
            visitedGoal[currentGoal] = true;
            int currentBox = matchedBox[currentGoal], adjustment = UNREACHABLE_DISTANCE,
                nextGoal = 0;
            for (int j = 1; j <= boxCount; j++)
                if (!visitedGoal[j]) {
                    int cost = distanceTable->values[j - 1][boxCells[currentBox]];
                    int reducedCost = cost - boxPotential[currentBox] - goalPotential[j];
                    if (reducedCost < slack[j]) {
                        slack[j] = reducedCost;
                        previousGoal[j] = currentGoal;
                    }
                    if (slack[j] < adjustment) {
                        adjustment = slack[j];
                        nextGoal = j;
                    }
                }
            if (adjustment >= UNREACHABLE_DISTANCE)
                return heuristicCache[boxMask] = -1;
            for (int j = 0; j <= boxCount; j++)
                if (visitedGoal[j]) {
                    boxPotential[matchedBox[j]] += adjustment;
                    goalPotential[j] -= adjustment;
                } else
                    slack[j] -= adjustment;
            currentGoal = nextGoal;
        } while (matchedBox[currentGoal]);
        do {
            int nextGoal = previousGoal[currentGoal];
            matchedBox[currentGoal] = matchedBox[nextGoal];
            currentGoal = nextGoal;
        } while (currentGoal);
    }
    for (int j = 1; j <= boxCount; j++)
        if (distanceTable->values[j - 1][boxCells[matchedBox[j]]] >= UNREACHABLE_DISTANCE)
            return heuristicCache[boxMask] = -1;
    return heuristicCache[boxMask] = -goalPotential[0];
}

// Search push or pull states, keeping the first visit and preferring newer ties.
string attempt(bool pullSearch, int crossingPenalty, bool regional, int tableSize,
               int expansionLimit) {
    reverseMode = pullSearch;
    boxCrossingPenalty = crossingPenalty;
    useRegional = regional;
    patternSize = tableSize;
    movedBox = parentFrozenBoxes = 0;
    goalCount = 0;

    nodes.clear();
    hashTable.clear();
    heuristicCache.clear();
    distanceCache.clear();
    patterns.clear();

    targetBoxes = reverseMode ? initialBoxes : goalMask;
    for (Bitboard remaining = targetBoxes; remaining; remaining &= remaining - 1)
        goals[goalCount++] = lowestCell(remaining);
    liveCells = targetBoxes;
    Bitboard previous;
    do {
        previous = liveCells;
        for (int direction = 0; direction < DIRECTION_COUNT; direction++)
            liveCells |=
                reverseMode
                    ? shift(liveCells & shift(floorMask, direction), direction) & floorMask
                    : shift(liveCells, direction) & shift(floorMask, direction ^ 1) & floorMask;
    } while (liveCells != previous);
    using Entry = pair<int, int>;
    priority_queue<Entry, vector<Entry>, greater<Entry>> open;
    vector<int> depth;
    auto add = [&](Bitboard boxMask, Bitboard reachable, unsigned parent, int encodedPush,
                   int pushDepth) {
        Bitboard state = stateKey(boxMask, reachable);
        if (hashTable.empty() ||
            nodes.size() * HASH_LOAD_DENOMINATOR > hashTable.size() * HASH_LOAD_NUMERATOR)
            rehash();
        size_t slot = hashKey(state) & (hashTable.size() - 1);
        while (hashTable[slot]) {
            if (nodes[hashTable[slot] - 1].state == state)
                return;
            slot = (slot + 1) & (hashTable.size() - 1);
        }
        int estimate = heuristic(boxMask, reachable);
        if (estimate >= 0 && useRegional && packingWeight) {
            Bitboard fixed = boxMask & goalMask;
            packingGood(boxMask, reachable, fixed);
            int missingGoals = MAX_BOXES;
            for (auto entry : packing[fixed])
                missingGoals = min(missingGoals, countBits(entry.first & ~boxMask));
            estimate += packingWeight * missingGoals;
        }
        if (estimate < 0) {
            if (fastMode) {
                insert(state, UINT32_MAX, 0);
                depth.push_back(-1);
            }
            return;
        }
        int id = insert(state, parent, encodedPush);
        depth.push_back(pushDepth);
        int score = PRIORITY_SCALE * (estimate - (useRegional ? pushDepth : 0));
        open.push({score, -id});
    };
    if (reverseMode) {
        Bitboard todo = floorMask & ~goalMask;
        while (todo) {
            Bitboard reachable = reachableCells(todo & -todo, floorMask & ~goalMask);
            add(goalMask, reachable, UINT32_MAX, 0, 0);
            todo &= ~reachable;
        }
    } else
        add(initialBoxes, reachableCells(cellBit(initialPlayer), floorMask & ~initialBoxes),
            UINT32_MAX, 0, 0);
    int expanded = 0, solved = -1;
    Bitboard initialReach = reachableCells(cellBit(initialPlayer), floorMask & ~initialBoxes);
    while (!open.empty() && expanded < expansionLimit &&
           (!fastMode ||
            (nodes.size() < NODE_CAP && !((expanded & CLOCK_CHECK_MASK) == 0 && timeUp())))) {
        int id = -open.top().second;
        open.pop();
        Bitboard boxMask = stateBoxes(nodes[id].state),
                 reachable =
                     reachableCells(cellBit(nodes[id].state >> PLAYER_SHIFT), floorMask & ~boxMask);
        if (boxMask == targetBoxes && (!reverseMode || (reachable & initialReach))) {
            solved = id;
            break;
        }
        expanded++;
        if (patternSize)
            parentFrozenBoxes = frozenBoxes(boxMask);
        Bitboard emptyCells = floorMask & ~boxMask,
                 allowed = !reverseMode ? restrictCorral(boxMask, reachable) : boxMask;
        for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
            Bitboard movable =
                reverseMode
                    ? boxMask & shift(reachable & shift(emptyCells, direction ^ 1) & liveCells,
                                      direction ^ 1)
                    : allowed & shift(reachable, direction) &
                          shift(emptyCells & liveCells, direction ^ 1);
            while (movable) {
                int cell = lowestCell(movable);
                movable &= movable - 1;
                int nextCell = cell + DIRECTION_STEP[direction];
                Bitboard nextBoxes = boxMask ^ cellBit(cell) ^ cellBit(nextCell);
                Bitboard nextReachable = reachableCells(
                    cellBit(reverseMode ? nextCell + DIRECTION_STEP[direction] : cell),
                    floorMask & ~nextBoxes);
                movedBox = cellBit(nextCell);
                add(nextBoxes, nextReachable, id, cell * DIRECTION_COUNT + direction,
                    depth[id] + 1);
            }
        }
    }

    string plan = solved >= 0 ? reconstructPlan(solved) : "";
    if (plan.size() > MAX_PLAN_LENGTH)
        plan.clear();
    return plan;
}
// Cheap forward and reverse probes precede four rotated forward restarts.
string cheapProbes() {
    string plan = attempt(false, 1, false, 0, INITIAL_EXPANSIONS);
    if (plan.empty())
        plan = attempt(true, 0, false, 0, INITIAL_EXPANSIONS);
    if (plan.empty()) {
        Bitboard savedFloor = floorMask, savedGoals = goalMask, savedBoxes = initialBoxes;
        int savedPlayer = initialPlayer, turns = 0;

        for (int i = 1; i <= ROTATION_COUNT && plan.empty(); i++) {
            floorMask = rotateMask(floorMask);
            goalMask = rotateMask(goalMask);
            initialBoxes = rotateMask(initialBoxes);
            initialPlayer = rotateCell(initialPlayer);
            plan = attempt(false, 2, false, 0, ROTATED_EXPANSIONS);
            turns = i;
        }
        floorMask = savedFloor;
        goalMask = savedGoals;
        initialBoxes = savedBoxes;
        initialPlayer = savedPlayer;
        for (int i = 0; i < turns; i++)
            for (char &letter : plan) {
                bool upper = letter < 'a';
                char lowercase = upper ? char(letter + LETTER_CASE_OFFSET) : letter;
                int direction = 0;
                while (DIRECTION_LETTER[direction] != lowercase)
                    direction++;
                letter = "lrdu"[direction];
                if (upper)
                    letter = char(letter - LETTER_CASE_OFFSET);
            }
    }
    return plan;
}
// Regional and packing tests on the least symmetric geometry follow the probes.
string runFast() {
    string plan = cheapProbes();
    if (plan.empty()) {
        Bitboard savedFloor = floorMask, savedGoals = goalMask, savedBoxes = initialBoxes;
        int savedPlayer = initialPlayer, bestSymmetry = 0;
        // Choose the lexicographically least floor, goals, boxes, player geometry.
        array<Bitboard, GEOMETRY_COMPONENTS> bestGeometry = {floorMask, goalMask, initialBoxes,
                                                             Bitboard(initialPlayer)};
        auto transformCell = [](int cell, int symmetry) {
            if (symmetry & REFLECTION_FLAG)
                cell = (cell / BOARD_WIDTH) * BOARD_WIDTH + LAST_COORDINATE - cell % BOARD_WIDTH;
            for (int j = 0; j < (symmetry & ROTATION_MASK); j++)
                cell = rotateCell(cell);
            return cell;
        };
        auto transformMask = [&](Bitboard boxMask, int symmetry) {
            Bitboard result = 0;
            for (; boxMask; boxMask &= boxMask - 1)
                result |= cellBit(transformCell(lowestCell(boxMask), symmetry));
            return result;
        };
        for (int symmetry = 1; symmetry < SYMMETRY_COUNT; symmetry++) {
            array<Bitboard, GEOMETRY_COMPONENTS> state = {
                transformMask(savedFloor, symmetry), transformMask(savedGoals, symmetry),
                transformMask(savedBoxes, symmetry),
                Bitboard(transformCell(savedPlayer, symmetry))};
            if (state < bestGeometry) {
                bestGeometry = state;
                bestSymmetry = symmetry;
            }
        }
        floorMask = bestGeometry[0];
        goalMask = bestGeometry[1];
        initialBoxes = bestGeometry[2];
        initialPlayer = int(bestGeometry[PLAYER_COMPONENT]);
        packing.clear();
        regions.clear();
        packingWeight = PACKING_WEIGHT;
        plan = attempt(false, 0, true, 0, UNBOUNDED_EXPANSIONS);
        int inverseDirection[DIRECTION_COUNT];
        for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
            int transformedStep =
                transformCell(DIRECTION_PROBE_CELL + DIRECTION_STEP[direction], bestSymmetry) -
                transformCell(DIRECTION_PROBE_CELL, bestSymmetry);
            for (int j = 0; j < DIRECTION_COUNT; j++)
                if (DIRECTION_STEP[j] == transformedStep)
                    inverseDirection[j] = direction;
        }
        for (char &letter : plan) {
            bool upper = letter < 'a';
            char lowercase = upper ? char(letter + LETTER_CASE_OFFSET) : letter;
            int direction = 0;
            while (DIRECTION_LETTER[direction] != lowercase)
                direction++;
            letter = DIRECTION_LETTER[inverseDirection[direction]];
            if (upper)
                letter = char(letter - LETTER_CASE_OFFSET);
        }
        floorMask = savedFloor;
        goalMask = savedGoals;
        initialBoxes = savedBoxes;
        initialPlayer = savedPlayer;
    }
    return plan;
}

// Release all fast-search storage before constructing fallback tables.
void release() {
    vector<Node>().swap(nodes);
    vector<uint32_t>().swap(hashTable);
    decltype(heuristicCache)().swap(heuristicCache);
    decltype(distanceCache)().swap(distanceCache);
    decltype(packing)().swap(packing);
    decltype(regions)().swap(regions);
}
// Use exact player positions and walking-plus-push costs when short plans fail.
// A* reopens cheaper states and rejects costs or lower bounds beyond the move limit.
string lengthFallback() {
    reverseMode = false;
    boxCrossingPenalty = patternSize = 0;
    movedBox = 0;
    nodes.clear();
    hashTable.clear();
    heuristicCache.clear();
    distanceCache.clear();
    patterns.clear();
    vector<int> cost;
    using Entry = pair<int, pair<int, int>>;
    priority_queue<Entry, vector<Entry>, greater<Entry>> open;
    insert(stateKey(initialBoxes, cellBit(initialPlayer)), UINT32_MAX, 0);
    cost.push_back(0);
    open.push({0, {0, 0}});
    while (!open.empty()) {
        int pathCost = open.top().second.first, id = open.top().second.second;
        open.pop();
        if (pathCost != cost[id])
            continue;
        Bitboard boxMask = stateBoxes(nodes[id].state);
        int player = int(nodes[id].state >> PLAYER_SHIFT);
        if (boxMask == goalMask) {
            return reconstructPlan(id);
        }
        int walkDistance[CELL_COUNT], queue[CELL_COUNT], tail = 1;
        fill(walkDistance, walkDistance + CELL_COUNT, -1);
        walkDistance[player] = 0;
        queue[0] = player;
        Bitboard reachable = 0;
        for (int head = 0; head < tail; head++) {
            int cell = queue[head];
            reachable |= cellBit(cell);
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                int nextCell = cell + DIRECTION_STEP[direction];
                if (nextCell >= 0 && nextCell < CELL_COUNT && (floorMask & cellBit(nextCell)) &&
                    !(boxMask & cellBit(nextCell)) && walkDistance[nextCell] < 0) {
                    walkDistance[nextCell] = walkDistance[cell] + 1;
                    queue[tail++] = nextCell;
                }
            }
        }
        for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
            Bitboard movableBoxes = boxMask & shift(reachable, direction) &
                                    shift((floorMask & ~boxMask) & liveCells, direction ^ 1);
            while (movableBoxes) {
                int cell = lowestCell(movableBoxes);
                movableBoxes &= movableBoxes - 1;
                int nextCell = cell + DIRECTION_STEP[direction],
                    nextCost = pathCost + walkDistance[cell - DIRECTION_STEP[direction]] + 1;
                if (nextCost > MAX_PLAN_LENGTH)
                    continue;
                Bitboard nextBoxes = boxMask ^ cellBit(cell) ^ cellBit(nextCell),
                         state = stateKey(nextBoxes, cellBit(cell));
                if (hashTable.empty() ||
                    nodes.size() * HASH_LOAD_DENOMINATOR > hashTable.size() * HASH_LOAD_NUMERATOR)
                    rehash();
                size_t slot = hashKey(state) & (hashTable.size() - 1);
                int nextId = -1;
                while (hashTable[slot]) {
                    int candidate = hashTable[slot] - 1;
                    if (nodes[candidate].state == state) {
                        nextId = candidate;
                        break;
                    }
                    slot = (slot + 1) & (hashTable.size() - 1);
                }
                if (nextId >= 0 && cost[nextId] <= nextCost)
                    continue;
                int estimate =
                    heuristic(nextBoxes, reachableCells(cellBit(cell), floorMask & ~nextBoxes));
                if (estimate < 0 || nextCost + estimate > MAX_PLAN_LENGTH)
                    continue;
                if (nextId < 0) {
                    nextId = insert(state, id, cell * DIRECTION_COUNT + direction);
                    cost.push_back(nextCost);
                } else {
                    nodes[nextId].parent = id;
                    nodes[nextId].move = uint16_t(cell * DIRECTION_COUNT + direction);
                    cost[nextId] = nextCost;
                }
                open.push({nextCost + estimate, {nextCost, nextId}});
            }
        }
    }
    return "";
}

string runSafe() {
    string plan = cheapProbes();
    // Escalate from three-box to five-box deadlock tables before exact-player A*.
    if (plan.empty())
        plan = attempt(false, 0, false, SMALL_PATTERN_SIZE,
                       countBits(initialBoxes) <= 10 ? SMALL_BOX_EXPANSIONS : MANY_BOX_EXPANSIONS);
    if (plan.empty())
        plan = attempt(false, 0, false, LARGE_PATTERN_SIZE, UNBOUNDED_EXPANSIONS);
    if (plan.empty())
        plan = lengthFallback();
    return plan;
}

Bitboard originalFloor, originalGoals, originalBoxes;
int originalPlayer;

// Replay every step, including push letter case, and require the exact goal mask.
bool valid(const string &plan) {
    if (plan.size() > MAX_PLAN_LENGTH)
        return false;
    Bitboard boxMask = originalBoxes;
    int player = originalPlayer;
    for (char letter : plan) {
        bool push = letter < 'a';
        char lowercase = push ? char(letter + LETTER_CASE_OFFSET) : letter;
        int direction = 0;
        while (direction < DIRECTION_COUNT && DIRECTION_LETTER[direction] != lowercase)
            direction++;
        if (direction == DIRECTION_COUNT)
            return false;
        int nextCell = player + DIRECTION_STEP[direction];
        if (nextCell < 0 || nextCell >= CELL_COUNT || !(originalFloor >> nextCell & 1))
            return false;
        if (boxMask >> nextCell & 1) {
            int boxDestination = nextCell + DIRECTION_STEP[direction];
            if (!push || boxDestination < 0 || boxDestination >= CELL_COUNT ||
                !(originalFloor >> boxDestination & 1) || (boxMask >> boxDestination & 1))
                return false;
            boxMask ^= (Bitboard(1) << nextCell) | (Bitboard(1) << boxDestination);
        } else if (push)
            return false;
        player = nextCell;
    }
    return boxMask == originalGoals;
}

int main() {
    string line;
    int row = 0;
    Bitboard floorMask = 0, goalMask = 0, initialBoxes = 0;
    int initialPlayer = 0;
    while (getline(cin, line)) {
        if (!line.empty() && line.back() == '\r')
            line.pop_back();
        if (line.empty())
            continue;
        for (int column = 0; column < (int)line.size() && column < BOARD_WIDTH; column++) {
            char tile = line[column];
            int cell = row * BOARD_WIDTH + column;
            if (tile != '#')
                floorMask |= Bitboard(1) << cell;
            if (tile == '.' || tile == '*' || tile == '+')
                goalMask |= Bitboard(1) << cell;
            if (tile == '$' || tile == '*')
                initialBoxes |= Bitboard(1) << cell;
            if (tile == '@' || tile == '+')
                initialPlayer = cell;
        }
        row++;
    }
    floorMask = reachableCells(Bitboard(1) << initialPlayer, floorMask);
    goalMask &= floorMask;
    initialBoxes &= floorMask;
    originalFloor = floorMask, originalGoals = goalMask, originalBoxes = initialBoxes,
    originalPlayer = initialPlayer;
    if (initialBoxes == goalMask) {
        cout << '\n';
        return 0;
    }
    ::floorMask = floorMask, ::goalMask = goalMask, ::initialBoxes = initialBoxes,
    ::initialPlayer = initialPlayer;
    // Pascal recurrence supplies the subset ranks used by pattern tables.
    for (int availableCells = 0; availableCells <= MAX_BOXES; availableCells++)
        for (int subsetSize = 0; subsetSize <= LARGE_PATTERN_SIZE; subsetSize++)
            binomial[availableCells][subsetSize] =
                subsetSize == 0       ? 1
                : availableCells == 0 ? 0
                                      : binomial[availableCells - 1][subsetSize - 1] +
                                            binomial[availableCells - 1][subsetSize];
    string plan;
    try {
        plan = runFast();
    } catch (const FailedWalk &) {
        plan.clear();
    }
    if (!valid(plan)) {
        release();
        fastMode = false;
        ::floorMask = floorMask, ::goalMask = goalMask, ::initialBoxes = initialBoxes,
        ::initialPlayer = initialPlayer;
        plan = runSafe();
    }
    cout << plan << '\n';
    return 0;
}
