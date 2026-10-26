#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <queue>
#include <string>
#include <utility>
#include <vector>

using namespace std;
using Bitboard = uint64_t;

const int BOARD_WIDTH = 8;
const int CELL_COUNT = 64;
const int DIRECTIONS = 4;
const int MAX_BOXES = 36;
const int MAX_SUBSET = 4;
const int UNREACHABLE = 1000000;
const int ESTIMATE_WEIGHT = 20;
const int PLAYER_SHIFT = 56;
const Bitboard BOX_BITS = (Bitboard(1) << PLAYER_SHIFT) - 1;
const int INITIAL_SLOTS = 1 << 16;
const Bitboard HASH_MULTIPLIER = 0x9E3779B97F4A7C15ULL;
const int HASH_SHIFT = 20;
const int LETTER_CASE = 'a' - 'A';
const int STEP[DIRECTIONS] = {-BOARD_WIDTH, BOARD_WIDTH, -1, 1};
const char *LETTERS = "udlr";

Bitboard floorCells, goals, startBoxes, liveCells;
int startPlayer;
int goalCount;
int pushDistance[MAX_BOXES][CELL_COUNT]; // pushes of a lone box from a cell to goal j

Bitboard bit(int cell) { return Bitboard(1) << cell; }
int lowest(Bitboard mask) { return __builtin_ctzll(mask); }
// The walls around the floor keep shifted bits from wrapping onto floor cells.
Bitboard shift(Bitboard mask, int direction) {
    return direction == 0   ? mask >> BOARD_WIDTH
           : direction == 1 ? mask << BOARD_WIDTH
           : direction == 2 ? mask >> 1
                            : mask << 1;
}
// All cells reachable from seed through free cells.
Bitboard reach(Bitboard seed, Bitboard free) {
    for (;;) {
        Bitboard grown =
            (seed | seed << BOARD_WIDTH | seed >> BOARD_WIDTH | seed << 1 | seed >> 1) & free;
        if (grown == seed)
            return seed;
        seed = grown;
    }
}

// Remove every box that can move along some axis, ignoring the player, until
// nothing changes; what stays is frozen. A frozen box off a goal is a deadlock.
Bitboard frozenBoxes(Bitboard boxes) {
    for (;;) {
        Bitboard empty = floorCells & ~boxes, emptyLive = empty & liveCells, movable = 0;
        for (int direction = 0; direction < DIRECTIONS; direction++)
            movable |= boxes & shift(empty, direction) & shift(emptyLive, direction ^ 1);
        if (!movable)
            return boxes;
        boxes &= ~movable;
    }
}

// The same with the player: remove the boxes the player can push, letting the
// area grow as they go; a box that stays off a goal can never be moved again.
Bitboard stuckBoxes(Bitboard boxes, Bitboard area) {
    for (;;) {
        Bitboard emptyLive = floorCells & ~boxes & liveCells, movable = 0;
        for (int direction = 0; direction < DIRECTIONS; direction++)
            movable |= boxes & shift(area, direction) & shift(emptyLive, direction ^ 1);
        if (!movable)
            return boxes;
        boxes &= ~movable;
        area = reach(area, floorCells & ~boxes);
    }
}

// A corral is an area the player cannot enter, with an unfinished box on its
// border or a goal inside. If every push of its border boxes goes inward and can
// be done now, and removing the outside boxes would allow no other, try only those.
Bitboard corralBoxes(Bitboard boxes, Bitboard area) {
    Bitboard unseen = floorCells & ~(boxes | area), fixed = frozenBoxes(boxes);
    while (unseen) {
        Bitboard corral = reach(unseen & -unseen, floorCells & ~(boxes | area));
        unseen &= ~corral;
        Bitboard border =
            boxes & (corral << 1 | corral >> 1 | corral << BOARD_WIDTH | corral >> BOARD_WIDTH);
        if (!((border & ~goals) | (corral & goals)))
            continue;
        Bitboard reduced = border | fixed, relaxed = reach(area, floorCells & ~reduced);
        bool inward = true;
        int pushes = 0;
        for (int direction = 0; direction < DIRECTIONS && inward; direction++) {
            Bitboard possible = border & shift(relaxed, direction) &
                                shift(floorCells & ~reduced & liveCells, direction ^ 1);
            Bitboard actual = border & shift(area, direction) &
                              shift(floorCells & ~boxes & liveCells, direction ^ 1);
            if (possible != actual || (shift(possible, direction) & ~corral))
                inward = false;
            pushes += __builtin_popcountll(possible);
        }
        if (inward && pushes)
            return border;
    }
    return boxes;
}

// The estimate: the minimum total push distance of the boxes to distinct goals
// (the Hungarian method), or -1 if some box can reach no free goal.
int matching(Bitboard boxes) {
    int cell[MAX_BOXES + 1], count = 0;
    for (; boxes; boxes &= boxes - 1)
        cell[++count] = lowest(boxes);
    vector<int> boxPotential(count + 1), goalPotential(count + 1), matched(count + 1),
        previous(count + 1);
    for (int box = 1; box <= count; box++) {
        matched[0] = box;
        int goal = 0;
        vector<int> slack(count + 1, UNREACHABLE);
        vector<char> visited(count + 1, 0);
        do {
            visited[goal] = 1;
            int current = matched[goal], delta = UNREACHABLE, next = 0;
            for (int j = 1; j <= count; j++)
                if (!visited[j]) {
                    int reduced = pushDistance[j - 1][cell[current]] - boxPotential[current] -
                                  goalPotential[j];
                    if (reduced < slack[j])
                        slack[j] = reduced, previous[j] = goal;
                    if (slack[j] < delta)
                        delta = slack[j], next = j;
                }
            if (delta >= UNREACHABLE / 2)
                return -1;
            for (int j = 0; j <= count; j++)
                if (visited[j])
                    boxPotential[matched[j]] += delta, goalPotential[j] -= delta;
                else
                    slack[j] -= delta;
            goal = next;
        } while (matched[goal]);
        do {
            int next = previous[goal];
            matched[goal] = matched[next];
            goal = next;
        } while (goal);
    }
    int total = 0;
    for (int j = 1; j <= count; j++) {
        if (pushDistance[j - 1][cell[matched[j]]] >= UNREACHABLE)
            return -1;
        total += pushDistance[j - 1][cell[matched[j]]];
    }
    return total;
}

// Subset tables: for every set of k boxes on live cells, the player cells from
// which those boxes alone can still be put on k goals. Built by pulls from every
// k goals; a set is ranked in the combinatorial number system of live cells.
int liveIndex[CELL_COUNT], liveCount, binomial[MAX_BOXES + 1][MAX_SUBSET + 1];
vector<Bitboard> solvableFrom[MAX_SUBSET + 1];
vector<pair<Bitboard, Bitboard>> tableQueue;

int subsetRank(Bitboard boxes) {
    int rank = 0, position = 1;
    for (; boxes; boxes &= boxes - 1)
        rank += binomial[liveIndex[lowest(boxes)]][position++];
    return rank;
}
void addToTable(int k, Bitboard boxes, Bitboard seed) {
    Bitboard area = reach(seed, floorCells & ~boxes);
    Bitboard &cells = solvableFrom[k][subsetRank(boxes)];
    if (cells & area)
        return;
    cells |= area;
    tableQueue.push_back({boxes, area});
}
void addGoalSubsets(int k, const vector<int> &goalCells, int from, int left, Bitboard boxes) {
    if (!left) {
        for (Bitboard free = floorCells & ~boxes; free;) {
            Bitboard area = reach(free & -free, floorCells & ~boxes);
            addToTable(k, boxes, area);
            free &= ~area;
        }
        return;
    }
    for (int i = from; i < (int)goalCells.size(); i++)
        addGoalSubsets(k, goalCells, i + 1, left - 1, boxes | bit(goalCells[i]));
}
void buildTable(int k) {
    solvableFrom[k].assign(binomial[liveCount][k], 0);
    tableQueue.clear();
    vector<int> goalCells;
    for (Bitboard rest = goals; rest; rest &= rest - 1)
        goalCells.push_back(lowest(rest));
    addGoalSubsets(k, goalCells, 0, k, 0);
    for (size_t head = 0; head < tableQueue.size(); head++) {
        Bitboard boxes = tableQueue[head].first, area = tableQueue[head].second;
        for (Bitboard rest = boxes; rest; rest &= rest - 1) {
            int box = lowest(rest);
            for (int direction = 0; direction < DIRECTIONS; direction++) {
                // the player at `to` pulls the box there and steps back to `back`
                int to = box - STEP[direction], back = to - STEP[direction];
                if (area >> to & 1 && (floorCells & ~boxes) >> back & 1 && liveCells >> to & 1)
                    addToTable(k, boxes ^ bit(box) ^ bit(to), bit(back));
            }
        }
    }
}
// Every subset of k boxes that contains the moved box must be solvable alone.
bool subsetsSolvable(int k, const int *cells, int count, int from, int left, Bitboard subset,
                     Bitboard area) {
    if (!left)
        return (solvableFrom[k][subsetRank(subset)] & area) != 0;
    for (int i = from; i < count; i++)
        if (!subsetsSolvable(k, cells, count, i + 1, left - 1, subset | bit(cells[i]), area))
            return false;
    return true;
}

// The states seen so far: an open-addressing set of keys (a key is never 0).
vector<Bitboard> slots(INITIAL_SLOTS);
size_t usedSlots = 0;
bool insertKey(Bitboard key) {
    if (2 * (usedSlots + 1) > slots.size()) {
        vector<Bitboard> old(slots.size() * 2);
        old.swap(slots);
        usedSlots = 0;
        for (Bitboard oldKey : old)
            if (oldKey)
                insertKey(oldKey);
    }
    size_t mask = slots.size() - 1, i = (key * HASH_MULTIPLIER) >> HASH_SHIFT & mask;
    for (; slots[i]; i = (i + 1) & mask)
        if (slots[i] == key)
            return false;
    slots[i] = key;
    usedSlots++;
    return true;
}

// The player's steps between pushes: a breadth-first walk.
string walk(Bitboard boxes, int from, int to) {
    int previous[CELL_COUNT], direction[CELL_COUNT], queue[CELL_COUNT], head = 0, tail = 0;
    fill(previous, previous + CELL_COUNT, -1);
    previous[from] = from;
    queue[tail++] = from;
    while (head < tail && previous[to] < 0) {
        int cell = queue[head++];
        for (int d = 0; d < DIRECTIONS; d++) {
            int next = cell + STEP[d];
            if ((floorCells & ~boxes) >> next & 1 && previous[next] < 0)
                previous[next] = cell, direction[next] = d, queue[tail++] = next;
        }
    }
    string steps;
    for (int cell = to; cell != from; cell = previous[cell])
        steps += LETTERS[direction[cell]];
    reverse(steps.begin(), steps.end());
    return steps;
}

struct Node {
    Bitboard key; // the boxes and, above them, the lowest cell of the player's area
    int parent, move, pushes;
};

int main() {
    string line;
    int row = 0;
    while (getline(cin, line)) {
        if (!line.empty() && line.back() == '\r')
            line.pop_back();
        if (line.empty())
            continue;
        for (int column = 0; column < (int)line.size() && column < BOARD_WIDTH; column++) {
            char tile = line[column];
            int cell = row * BOARD_WIDTH + column;
            if (tile != '#')
                floorCells |= bit(cell);
            if (tile == '.' || tile == '*' || tile == '+')
                goals |= bit(cell);
            if (tile == '$' || tile == '*')
                startBoxes |= bit(cell);
            if (tile == '@' || tile == '+')
                startPlayer = cell;
        }
        row++;
    }
    floorCells = reach(bit(startPlayer), floorCells);
    goals &= floorCells, startBoxes &= floorCells;
    if (startBoxes == goals) {
        puts("");
        return 0;
    }
    // push distances by pulls from every goal; live cells reach some goal
    for (Bitboard rest = goals; rest; rest &= rest - 1) {
        int j = goalCount++, queue[CELL_COUNT], head = 0, tail = 0;
        fill(pushDistance[j], pushDistance[j] + CELL_COUNT, UNREACHABLE);
        pushDistance[j][lowest(rest)] = 0;
        queue[tail++] = lowest(rest);
        while (head < tail) {
            int cell = queue[head++];
            for (int d = 0; d < DIRECTIONS; d++) {
                int from = cell - STEP[d], player = from - STEP[d];
                if (floorCells >> from & 1 && floorCells >> player & 1 &&
                    pushDistance[j][from] == UNREACHABLE)
                    pushDistance[j][from] = pushDistance[j][cell] + 1, queue[tail++] = from;
            }
        }
        for (int cell = 0; cell < CELL_COUNT; cell++)
            if (pushDistance[j][cell] < UNREACHABLE)
                liveCells |= bit(cell);
    }
    for (int cell = 0; cell < CELL_COUNT; cell++)
        if (liveCells >> cell & 1)
            liveIndex[cell] = liveCount++;
    for (int n = 0; n <= MAX_BOXES; n++)
        for (int k = 0; k <= MAX_SUBSET; k++)
            binomial[n][k] = k == 0 ? 1 : n == 0 ? 0 : binomial[n - 1][k - 1] + binomial[n - 1][k];
    for (int k = 2; k <= MAX_SUBSET; k++)
        buildTable(k);

    // Best-first search over pushes by pushes + ESTIMATE_WEIGHT * estimate.
    vector<Node> nodes;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> open;
    auto add = [&](Bitboard boxes, int player, int parent, int move, int pushes) {
        Bitboard area = reach(bit(player), floorCells & ~boxes);
        Bitboard key = boxes | Bitboard(lowest(area)) << PLAYER_SHIFT;
        if (!insertKey(key))
            return;
        bool alive = !(frozenBoxes(boxes) & ~goals) && !(stuckBoxes(boxes, area) & ~goals);
        if (parent >= 0) {
            int moved = move / DIRECTIONS + STEP[move % DIRECTIONS], cells[MAX_BOXES], count = 0;
            for (Bitboard rest = boxes & ~bit(moved); rest; rest &= rest - 1)
                cells[count++] = lowest(rest);
            for (int k = 2; k <= MAX_SUBSET && alive; k++)
                if (count + 1 >= k)
                    alive = subsetsSolvable(k, cells, count, 0, k - 1, bit(moved), area);
        }
        int estimate = alive ? matching(boxes) : -1;
        if (estimate < 0)
            return;
        nodes.push_back({key, parent, move, pushes});
        open.push({pushes + ESTIMATE_WEIGHT * estimate, (int)nodes.size() - 1});
    };
    add(startBoxes, startPlayer, -1, 0, 0);
    int solved = -1;
    while (!open.empty()) {
        int id = open.top().second;
        open.pop();
        Bitboard boxes = nodes[id].key & BOX_BITS;
        if (boxes == goals) {
            solved = id;
            break;
        }
        Bitboard area = reach(bit(nodes[id].key >> PLAYER_SHIFT), floorCells & ~boxes);
        Bitboard emptyLive = floorCells & ~boxes & liveCells, allowed = corralBoxes(boxes, area);
        for (int d = 0; d < DIRECTIONS; d++)
            for (Bitboard can = allowed & shift(area, d) & shift(emptyLive, d ^ 1); can;
                 can &= can - 1) {
                int box = lowest(can);
                add(boxes ^ bit(box) ^ bit(box + STEP[d]), box, id, box * DIRECTIONS + d,
                    nodes[id].pushes + 1);
            }
    }
    vector<int> moves;
    for (int id = solved; id > 0; id = nodes[id].parent)
        moves.push_back(nodes[id].move);
    reverse(moves.begin(), moves.end());
    string plan;
    Bitboard boxes = startBoxes;
    int player = startPlayer;
    for (int move : moves) {
        int box = move / DIRECTIONS, d = move % DIRECTIONS;
        plan += walk(boxes, player, box - STEP[d]);
        plan += char(LETTERS[d] - LETTER_CASE);
        boxes ^= bit(box) ^ bit(box + STEP[d]);
        player = box;
    }
    puts(plan.c_str());
}
