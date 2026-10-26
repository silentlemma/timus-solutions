import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {

    static final int BOARD_WIDTH = 8;
    static final int CELL_COUNT = 64;
    static final int LAST_COORDINATE = BOARD_WIDTH - 1;
    static final int DIRECTION_COUNT = 4;
    static final int PLAYER_SHIFT = 56;
    static final long BOX_BITS = 0x00ffffffffffffffL;
    static final int MAX_BOXES = 36;
    static final int MATCHING_SIZE = MAX_BOXES + 1;
    static final int MAX_PLAN_LENGTH = 10000;
    static final int UNREACHABLE_DISTANCE = 10000;
    static final int LETTER_CASE_OFFSET = 32;
    static final int INITIAL_HASH_SIZE = 65536;
    static final int HASH_LOAD_NUMERATOR = 7;
    static final int HASH_LOAD_DENOMINATOR = 10;
    static final int HASH_SHIFT_FIRST = 30;
    static final int HASH_SHIFT_SECOND = 27;
    static final int HASH_SHIFT_LAST = 31;
    static final long HASH_MULTIPLIER_FIRST = 0xbf58476d1ce4e5b9L;
    static final long HASH_MULTIPLIER_SECOND = 0x94d049bb133111ebL;
    static final int DISTANCE_QUEUE_SIZE = 128;
    static final int DISTANCE_QUEUE_MASK = DISTANCE_QUEUE_SIZE - 1;
    static final int BYTE_BITS = 8;
    static final int BYTE_VALUES = 256;
    static final int BYTE_MASK = BYTE_VALUES - 1;
    static final int REGION_WIDTH = 3;
    static final int SMALL_PATTERN_SIZE = 3;
    static final int LARGE_PATTERN_SIZE = 5;
    static final int PATTERN_SIZE_COUNT = LARGE_PATTERN_SIZE + 1;
    static final int PRIORITY_SCALE = 100;
    static final int PACKING_WEIGHT = 30;
    static final int INITIAL_EXPANSIONS = 128;
    static final int ROTATED_EXPANSIONS = 64;
    static final int SMALL_BOX_EXPANSIONS = 4000;
    static final int MANY_BOX_EXPANSIONS = 256;
    static final int UNBOUNDED_EXPANSIONS = 2147483647;
    static final int NODE_CAP = 600000;
    static final double FAST_SECONDS = 1.0;
    static final int CLOCK_CHECK_MASK = 255;
    static final int ROTATION_COUNT = 4;
    static final int SYMMETRY_COUNT = 8;
    static final int REFLECTION_FLAG = 4;
    static final int ROTATION_MASK = 3;
    static final int GEOMETRY_COMPONENTS = 4;
    static final int PLAYER_COMPONENT = 3;
    static final int DIRECTION_PROBE_CELL = 27;

    static final int NONE = -1;
    static final int INITIAL_CAPACITY = 16;
    static final long NANOSECONDS_PER_SECOND = 1000000000L;
    static final long STARTED = System.nanoTime();
    static final int[] DIRECTION_STEP = {-BOARD_WIDTH, BOARD_WIDTH, -1, 1};
    static final String DIRECTION_LETTER = "udlr";
    static final String ROTATED_LETTER = "lrdu";
    static boolean fastMode = true;
    static boolean reverseMode;
    static long floorMask, goalMask, initialBoxes, liveCells;
    static int initialPlayer;

    // The fast budget includes input and preprocessing, just as in the reference.
    static boolean timeUp() {
        return (System.nanoTime() - STARTED) > FAST_SECONDS * NANOSECONDS_PER_SECOND;
    }

    static int lowestCell(long mask) {
        return Long.numberOfTrailingZeros(mask);
    }

    static int countBits(long mask) {
        return Long.bitCount(mask);
    }

    static long cellBit(int cell) {
        return 1L << cell;
    }

    // The wall border prevents horizontal shifts from wrapping into usable cells.
    static long shift(long mask, int direction) {
        return direction == 0
                ? mask >>> BOARD_WIDTH
                : direction == 1 ? mask << BOARD_WIDTH : direction == 2 ? mask >>> 1 : mask << 1;
    }

    static long neighbors(long cells) {
        return (cells << BOARD_WIDTH) | (cells >>> BOARD_WIDTH) | (cells << 1) | (cells >>> 1);
    }

    // The destination is constrained for pushes, the first player step for pulls.
    static long movable(
            long boxes, long reachable, long empty, long live, int direction, boolean pull) {
        return boxes
                & (pull
                        ? shift(reachable & shift(empty, direction ^ 1) & live, direction ^ 1)
                        : shift(reachable, direction) & shift(empty & live, direction ^ 1));
    }

    static long liveClosure(long targets, long floor, boolean reverse) {
        long previous;
        do {
            previous = targets;
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                targets |=
                        (reverse
                                        ? shift(targets & shift(floor, direction), direction)
                                        : shift(targets, direction) & shift(floor, direction ^ 1))
                                & floor;
            }
        } while (targets != previous);
        return targets;
    }

    static int statePlayer(long state) {
        return (int) (state >>> PLAYER_SHIFT);
    }

    static boolean contains(long cells, int cell) {
        return cell >= 0 && cell < CELL_COUNT && (cells & cellBit(cell)) != 0;
    }

    static long reachableCells(long reachable, long floorMask) {
        for (; ; ) {
            long expandedReachable = (reachable | neighbors(reachable)) & floorMask;
            if (expandedReachable == reachable) return reachable;
            reachable = expandedReachable;
        }
    }

    // Playable boxes fit below the top byte; it stores the lowest reachable cell.
    static long stateKey(long boxMask, long reachable) {
        return boxMask | ((long) lowestCell(reachable) << PLAYER_SHIFT);
    }

    static long stateBoxes(long state) {
        return state & BOX_BITS;
    }

    // Mix all key bits before linear probing in a power-of-two hash table.
    static long hashKey(long state) {
        state ^= state >>> HASH_SHIFT_FIRST;
        state *= HASH_MULTIPLIER_FIRST;
        state ^= state >>> HASH_SHIFT_SECOND;
        state *= HASH_MULTIPLIER_SECOND;
        return state ^ (state >>> HASH_SHIFT_LAST);
    }

    // A clockwise quarter turn changes search ties without changing legal moves.
    static int rotateCell(int cell) {
        return (cell % BOARD_WIDTH) * BOARD_WIDTH + LAST_COORDINATE - cell / BOARD_WIDTH;
    }

    static long rotateMask(long boxMask) {
        long result = 0;
        for (; boxMask != 0; boxMask &= boxMask - 1)
            result |= cellBit(rotateCell(lowestCell(boxMask)));
        return result;
    }

    // Erase every geometrically movable box to a fixed point, ignoring player access.
    // A remaining box outside the target is a deadlock.
    static long frozenBoxes(long boxMask) {
        return eraseBoxes(boxMask, 0, false);
    }

    // Restrict pushes to a corral only when removing outside movable boxes enables
    // no extra boundary push and every available boundary push goes inward.
    static long restrictCorral(long boxMask, long reachable) {
        long unseen = floorMask & ~(boxMask | reachable), fixed = frozenBoxes(boxMask);
        while (unseen != 0) {
            long corral = reachableCells(unseen & -unseen, floorMask & ~(boxMask | reachable));
            unseen &= ~corral;
            long border = boxMask & neighbors(corral);
            if (((border & ~goalMask) | (corral & goalMask)) == 0) continue;
            long reduced = border | fixed,
                    relaxed = reachableCells(reachable, floorMask & ~reduced);
            boolean independent = true;
            int pushCount = 0;
            for (int direction = 0; direction < DIRECTION_COUNT && independent; direction++) {
                long possible =
                        movable(border, relaxed, floorMask & ~reduced, liveCells, direction, false);
                long actual =
                        movable(
                                border,
                                reachable,
                                floorMask & ~boxMask,
                                liveCells,
                                direction,
                                false);
                if (possible != actual || (shift(possible, direction) & ~corral) != 0)
                    independent = false;
                pushCount += countBits(possible);
            }
            if (independent && pushCount != 0) {
                return border;
            }
        }
        return boxMask;
    }

    // Erase boxes movable from the expanding player component until it stops growing.
    // Any remaining box outside the target proves an access deadlock.
    static long inaccessibleBoxes(long boxMask, long reachable) {
        return eraseBoxes(boxMask, reachable, true);
    }

    // Without access checks every empty cell can supply the player's support.
    static long eraseBoxes(long boxes, long reachable, boolean checkAccess) {
        for (; ; ) {
            long empty = floorMask & ~boxes, removable = 0;
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                removable |=
                        movable(
                                boxes,
                                checkAccess ? reachable : empty,
                                empty,
                                liveCells,
                                direction,
                                reverseMode);
            }
            if (removable == 0) return boxes;
            boxes &= ~removable;
            if (checkAccess) reachable = reachableCells(reachable, floorMask & ~boxes);
        }
    }

    // Zero values mark empty slots, so zero keys need no special treatment.
    static final class LongIntMap {
        long[] keys = new long[INITIAL_CAPACITY];
        int[] values = new int[INITIAL_CAPACITY];
        int size;

        int slot(long key) {
            int mask = keys.length - 1;
            int slot = (int) hashKey(key) & mask;
            while (values[slot] != 0 && keys[slot] != key) {
                slot = (slot + 1) & mask;
            }
            return slot;
        }

        int get(long key) {
            return values[slot(key)];
        }

        void put(long key, int value) {
            if (size * HASH_LOAD_DENOMINATOR > keys.length * HASH_LOAD_NUMERATOR) {
                long[] oldKeys = keys;
                int[] oldValues = values;
                keys = new long[oldKeys.length * 2];
                values = new int[keys.length];
                for (int index = 0; index < oldKeys.length; index++) {
                    if (oldValues[index] != 0) {
                        int slot = slot(oldKeys[index]);
                        keys[slot] = oldKeys[index];
                        values[slot] = oldValues[index];
                    }
                }
            }
            int slot = slot(key);
            if (values[slot] == 0) {
                size++;
                keys[slot] = key;
            }
            values[slot] = value;
        }
    }

    // Cache objects stay compact; only primitive keys and indices enter the hash table.
    static final class Cache<T> {
        final LongIntMap index = new LongIntMap();
        Object[] values = new Object[INITIAL_CAPACITY];
        int size;

        @SuppressWarnings("unchecked")
        T get(long key) {
            int id = index.get(key);
            return id == 0 ? null : (T) values[id - 1];
        }

        void put(long key, T value) {
            if (size == values.length) {
                values = Arrays.copyOf(values, size * 2);
            }
            values[size++] = value;
            index.put(key, size);
        }
    }

    // Primitive queues are used only while building one retrograde table.
    static final class LongList {
        long[] values = new long[INITIAL_CAPACITY];
        int size;

        void add(long value) {
            if (size == values.length) {
                values = Arrays.copyOf(values, size + size / 2);
            }
            values[size++] = value;
        }
    }

    // Parallel node arrays retain the first parent without allocating node objects.
    static long[] nodeStates = new long[INITIAL_CAPACITY];
    static int[] nodeParents = new int[INITIAL_CAPACITY];
    static byte[] nodeMoves = new byte[INITIAL_CAPACITY];
    static int[] nodeCosts = new int[INITIAL_CAPACITY];
    static int nodeCount;
    static int[] hashTable = new int[0];

    static void rehash() {
        hashTable = new int[hashTable.length == 0 ? INITIAL_HASH_SIZE : hashTable.length * 2];
        for (int id = 0; id < nodeCount; id++) {
            hashTable[nodeSlot(nodeStates[id])] = id + 1;
        }
    }

    static int nodeSlot(long state) {
        int mask = hashTable.length - 1;
        int slot = (int) hashKey(state) & mask;
        while (hashTable[slot] != 0 && nodeStates[hashTable[slot] - 1] != state) {
            slot = (slot + 1) & mask;
        }
        return slot;
    }

    static void prepareHash() {
        if (hashTable.length == 0
                || nodeCount * HASH_LOAD_DENOMINATOR > hashTable.length * HASH_LOAD_NUMERATOR) {
            rehash();
        }
    }

    static int insert(long state, int parent, int move) {
        prepareHash();
        int slot = nodeSlot(state);
        if (hashTable[slot] != 0) {
            return NONE;
        }
        if (nodeCount == nodeStates.length) {
            int capacity = nodeCount + nodeCount / 2;
            nodeStates = Arrays.copyOf(nodeStates, capacity);
            nodeParents = Arrays.copyOf(nodeParents, capacity);
            nodeMoves = Arrays.copyOf(nodeMoves, capacity);
            nodeCosts = Arrays.copyOf(nodeCosts, capacity);
        }
        int id = nodeCount++;
        hashTable[slot] = id + 1;
        nodeStates[id] = state;
        nodeParents[id] = parent;
        nodeMoves[id] = (byte) move;
        return id;
    }

    // Compare (score, -id) for probes, and (score, cost, id) for exact-length A*.
    static final class MinHeap {
        int[] scores = new int[INITIAL_CAPACITY];
        int[] ids = new int[INITIAL_CAPACITY];
        int[] costs;
        int size;
        final boolean exact;

        MinHeap(boolean exact) {
            this.exact = exact;
            if (exact) {
                costs = new int[INITIAL_CAPACITY];
            }
        }

        boolean before(int score, int cost, int id, int slot) {
            if (score != scores[slot]) {
                return score < scores[slot];
            }
            if (exact && cost != costs[slot]) {
                return cost < costs[slot];
            }
            return exact ? id < ids[slot] : id > ids[slot];
        }

        void set(int slot, int score, int cost, int id) {
            scores[slot] = score;
            ids[slot] = id;
            if (exact) {
                costs[slot] = cost;
            }
        }

        void copy(int target, int source) {
            set(target, scores[source], exact ? costs[source] : 0, ids[source]);
        }

        void add(int score, int cost, int id) {
            if (size == scores.length) {
                int capacity = size + size / 2;
                scores = Arrays.copyOf(scores, capacity);
                ids = Arrays.copyOf(ids, capacity);
                if (exact) {
                    costs = Arrays.copyOf(costs, capacity);
                }
            }
            int slot = size++;
            while (slot > 0) {
                int parent = (slot - 1) / 2;
                if (!before(score, cost, id, parent)) {
                    break;
                }
                copy(slot, parent);
                slot = parent;
            }
            set(slot, score, cost, id);
        }

        void remove() {
            --size;
            int score = scores[size], cost = exact ? costs[size] : 0, id = ids[size];
            int slot = 0;
            while (slot * 2 + 1 < size) {
                int child = slot * 2 + 1;
                if (child + 1 < size
                        && before(
                                scores[child + 1],
                                exact ? costs[child + 1] : 0,
                                ids[child + 1],
                                child)) {
                    child++;
                }
                if (before(score, cost, id, child)) {
                    break;
                }
                copy(slot, child);
                slot = child;
            }
            set(slot, score, cost, id);
        }
    }

    static final class FailedWalk extends RuntimeException {
        private static final long serialVersionUID = 1L;
    }

    // Breadth-first walks use exactly the reference's up, down, left, right order.
    static String shortestWalk(long boxMask, int player, int destination) {
        int[] distance = new int[CELL_COUNT];
        int[] previousCell = new int[CELL_COUNT];
        int[] previousDirection = new int[CELL_COUNT];
        walk(boxMask, player, destination, distance, previousCell, previousDirection);
        if (distance[destination] < 0) throw new FailedWalk();
        StringBuilder plan = new StringBuilder();
        for (int cell = destination; cell != player; cell = previousCell[cell]) {
            plan.append(DIRECTION_LETTER.charAt(previousDirection[cell]));
        }
        return plan.reverse().toString();
    }

    // Walking is never nested, so both searches reuse this BFS queue.
    static final int[] walkQueue = new int[CELL_COUNT];

    static long walk(
            long boxes,
            int player,
            int destination,
            int[] distance,
            int[] previousCell,
            int[] previousDirection) {
        int[] queue = walkQueue;
        Arrays.fill(distance, NONE);
        distance[player] = 0;
        queue[0] = player;
        int tail = 1;
        long reachable = 0, free = floorMask & ~boxes;
        for (int head = 0; head < tail && (destination < 0 || distance[destination] < 0); head++) {
            int cell = queue[head];
            reachable |= cellBit(cell);
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                int next = cell + DIRECTION_STEP[direction];
                if (contains(free, next) && distance[next] < 0) {
                    distance[next] = distance[cell] + 1;
                    if (previousCell != null) {
                        previousCell[next] = cell;
                        previousDirection[next] = direction;
                    }
                    queue[tail++] = next;
                }
            }
        }
        return reachable;
    }

    // Reverse pulls become forward pushes in chain order; walks use the actual player.
    static String reconstructPlan(int id) {
        int length = 0;
        for (int node = id; nodeParents[node] != NONE; node = nodeParents[node]) {
            length++;
        }
        int[] pushes = new int[length];
        for (int index = 0; nodeParents[id] != NONE; id = nodeParents[id], index++) {
            pushes[reverseMode ? index : length - 1 - index] = nodeMoves[id] & BYTE_MASK;
        }
        long boxMask = initialBoxes;
        int player = initialPlayer;
        StringBuilder plan = new StringBuilder();
        for (int encodedPush : pushes) {
            int cell = encodedPush / DIRECTION_COUNT;
            int direction = encodedPush % DIRECTION_COUNT;
            if (reverseMode) {
                cell += DIRECTION_STEP[direction];
                direction ^= 1;
            }
            plan.append(shortestWalk(boxMask, player, cell - DIRECTION_STEP[direction]));
            plan.append((char) (DIRECTION_LETTER.charAt(direction) - LETTER_CASE_OFFSET));
            boxMask ^= cellBit(cell) | cellBit(cell + DIRECTION_STEP[direction]);
            player = cell;
        }
        return plan.toString();
    }

    static int boxCrossingPenalty, goalCount, packingWeight, patternSize;
    static final int[] goals = new int[MAX_BOXES];
    static long targetBoxes, movedBox, parentFrozenBoxes;
    static boolean useRegional;
    static Region[] regions = new Region[DIRECTION_COUNT];
    static int regionCount;
    static Cache<short[]> distanceCache = new Cache<>();
    static LongIntMap heuristicCache = new LongIntMap();
    static Cache<long[]> packing = new Cache<>();
    static Cache<Pattern> patterns = new Cache<>();
    static final int[][] binomial = new int[MATCHING_SIZE][PATTERN_SIZE_COUNT];

    // A strip projection records the union of player components that can solve it.
    static final class Region {
        long mask, regionFloor, active;
        long[] solvablePlayers;
        final int[][] packedBytes = new int[BOARD_WIDTH][BYTE_VALUES];
        final int[] rows = new int[BOARD_WIDTH];
        int rowCount;

        int index(long boxMask) {
            int packed = 0;
            for (int rowIndex = 0; rowIndex < rowCount; rowIndex++) {
                packed |=
                        packedBytes[rowIndex][
                                (int) (boxMask >>> (rows[rowIndex] * BYTE_BITS)) & BYTE_MASK];
            }
            return packed;
        }

        void add(LongList queue, long boxMask, long reachable) {
            int packed = index(boxMask);
            if ((solvablePlayers[packed] & reachable) != 0) {
                return;
            }
            reachable = reachableCells(reachable, regionFloor & ~boxMask);
            solvablePlayers[packed] |= reachable;
            queue.add(stateKey(boxMask, reachable));
        }

        void build(long regionMask) {
            regionFloor = floorMask;
            active = liveClosure(goalMask, regionFloor, false);
            mask = regionMask & active;
            int[] cells = new int[countBits(mask)];
            int cellCount = 0;
            for (long remaining = mask; remaining != 0; remaining &= remaining - 1) {
                cells[cellCount++] = lowestCell(remaining);
            }
            solvablePlayers = new long[1 << cellCount];
            for (int row = 0; row < BOARD_WIDTH; row++) {
                int[] masks = new int[BOARD_WIDTH];
                boolean used = false;
                for (int cellIndex = 0; cellIndex < cellCount; cellIndex++) {
                    if (cells[cellIndex] / BOARD_WIDTH == row) {
                        masks[cells[cellIndex] % BOARD_WIDTH] = 1 << cellIndex;
                        used = true;
                    }
                }
                if (!used) {
                    continue;
                }
                rows[rowCount] = row;
                for (int byteValue = 1; byteValue < BYTE_VALUES; byteValue++) {
                    packedBytes[rowCount][byteValue] =
                            packedBytes[rowCount][byteValue & (byteValue - 1)]
                                    | masks[lowestCell(byteValue)];
                }
                rowCount++;
            }
            LongList queue = new LongList();
            long rootBoxes = goalMask & mask, todo = regionFloor & ~rootBoxes;
            while (todo != 0) {
                long reachable = reachableCells(todo & -todo, regionFloor & ~rootBoxes);
                add(queue, rootBoxes, reachable);
                todo &= ~reachable;
            }
            long outside = active & ~mask;
            for (int head = 0; head < queue.size; head++) {
                long state = queue.values[head];
                long boxMask = stateBoxes(state);
                long reachable =
                        reachableCells(cellBit(statePlayer(state)), regionFloor & ~boxMask);
                long emptyCells = regionFloor & ~boxMask;
                for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                    long movableBoxes =
                            movable(boxMask, reachable, emptyCells, active, direction, true);
                    while (movableBoxes != 0) {
                        int cell = lowestCell(movableBoxes);
                        movableBoxes &= movableBoxes - 1;
                        int nextCell = cell + DIRECTION_STEP[direction];
                        long nextBoxes = (boxMask ^ cellBit(cell)) | (cellBit(nextCell) & mask);
                        add(queue, nextBoxes, cellBit(nextCell + DIRECTION_STEP[direction]));
                    }
                    if (countBits(boxMask) < countBits(initialBoxes)) {
                        movableBoxes =
                                movable(outside, reachable, emptyCells, mask, direction, true);
                        while (movableBoxes != 0) {
                            int cell = lowestCell(movableBoxes);
                            movableBoxes &= movableBoxes - 1;
                            int nextCell = cell + DIRECTION_STEP[direction];
                            add(
                                    queue,
                                    boxMask | cellBit(nextCell),
                                    cellBit(nextCell + DIRECTION_STEP[direction]));
                        }
                    }
                }
            }
        }
    }

    static void buildRegions() {
        for (int axis = 0; axis < 2; axis++) {
            for (int side = 0; side < 2; side++) {
                int minimum = BOARD_WIDTH, maximum = 0;
                for (long remaining = floorMask; remaining != 0; remaining &= remaining - 1) {
                    int cell = lowestCell(remaining);
                    int coordinate = axis != 0 ? cell / BOARD_WIDTH : cell % BOARD_WIDTH;
                    minimum = Math.min(minimum, coordinate);
                    maximum = Math.max(maximum, coordinate);
                }
                long regionMask = 0;
                for (long remaining = liveCells; remaining != 0; remaining &= remaining - 1) {
                    int cell = lowestCell(remaining);
                    int coordinate = axis != 0 ? cell / BOARD_WIDTH : cell % BOARD_WIDTH;
                    if (side != 0
                            ? coordinate > maximum - REGION_WIDTH
                            : coordinate < minimum + REGION_WIDTH) {
                        regionMask |= cellBit(cell);
                    }
                }
                if (regionMask == 0) {
                    continue;
                }
                boolean duplicate = false;
                for (int index = 0; index < regionCount; index++) {
                    if (regions[index].mask == regionMask) {
                        duplicate = true;
                    }
                }
                if (!duplicate) {
                    Region region = new Region();
                    region.build(regionMask);
                    regions[regionCount++] = region;
                }
            }
        }
    }

    static boolean regionGood(long boxMask, long reachable) {
        if (regionCount == 0) {
            buildRegions();
        }
        for (int index = 0; index < regionCount; index++) {
            Region region = regions[index];
            if ((region.solvablePlayers[region.index(boxMask)] & reachable) == 0) {
                return false;
            }
        }
        return true;
    }

    // Pull-erase goal boxes from each final player component, retaining fixed boxes.
    // Consecutive mask/component pairs preserve the reference's residue order.
    static boolean packingGood(long boxMask, long reachable, long fixed) {
        long[] results = packing.get(fixed);
        if (results == null) {
            LongList pairs = new LongList();
            long todo = floorMask & ~goalMask;
            while (todo != 0) {
                long remainingGoals = goalMask;
                long reachableFromGoals = reachableCells(todo & -todo, floorMask & ~goalMask);
                todo &= ~reachableFromGoals;
                for (; ; ) {
                    long emptyCells = floorMask & ~remainingGoals, movableBoxes = 0;
                    for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                        movableBoxes |=
                                movable(
                                        remainingGoals,
                                        reachableFromGoals,
                                        emptyCells,
                                        floorMask,
                                        direction,
                                        true);
                    }
                    movableBoxes &= ~fixed;
                    if (movableBoxes == 0) {
                        break;
                    }
                    remainingGoals &= ~movableBoxes;
                    reachableFromGoals =
                            reachableCells(reachableFromGoals, floorMask & ~remainingGoals);
                }
                pairs.add(remainingGoals);
                pairs.add(reachableFromGoals);
            }
            results = Arrays.copyOf(pairs.values, pairs.size);
            packing.put(fixed, results);
        }
        for (int index = 0; index < results.length; index += 2) {
            if ((results[index] & ~boxMask) == 0 && (results[index + 1] & reachable) != 0) {
                return true;
            }
        }
        return false;
    }

    // Dense combinatorial ranks avoid hashing every small box subset.
    static final class Pattern {
        long[] solvablePlayers;
        long floorMask, goals, liveCells;
        int subsetSize, cellCount;
        final int[] cellIndex = new int[CELL_COUNT];

        int rank(long boxMask) {
            int rank = 0, size = 1;
            for (; boxMask != 0; boxMask &= boxMask - 1) {
                rank += binomial[cellIndex[lowestCell(boxMask)]][size++];
            }
            return rank;
        }

        void add(LongList queue, long boxMask, long reachable) {
            int index = rank(boxMask);
            if ((solvablePlayers[index] & reachable) != 0) {
                return;
            }
            reachable = reachableCells(reachable, floorMask & ~boxMask);
            solvablePlayers[index] |= reachable;
            queue.add(stateKey(boxMask, reachable));
        }

        // Increasing-cell recursion visits target subsets in the nested-loop order.
        void roots(LongList queue, long remaining, int needed, long boxMask) {
            if (needed == 0) {
                if (reverseMode) {
                    add(queue, boxMask, cellBit(initialPlayer));
                    return;
                }
                long emptyCells = floorMask & ~boxMask;
                while (emptyCells != 0) {
                    long reachable = reachableCells(emptyCells & -emptyCells, floorMask & ~boxMask);
                    add(queue, boxMask, reachable);
                    emptyCells &= ~reachable;
                }
                return;
            }
            while (remaining != 0) {
                long cell = remaining & -remaining;
                remaining &= remaining - 1;
                roots(queue, remaining, needed - 1, boxMask | cell);
            }
        }
    }

    // Frozen goal boxes become walls before the subset retrograde BFS is built.
    static Pattern getPattern(long fixed) {
        Pattern table = patterns.get(fixed);
        if (table != null) {
            return table;
        }
        table = new Pattern();
        patterns.put(fixed, table);
        table.floorMask = floorMask & ~fixed;
        table.goals = targetBoxes & ~fixed;
        table.subsetSize = Math.min(patternSize, countBits(table.goals));
        if (table.subsetSize < 1) {
            return table;
        }
        table.liveCells = liveClosure(table.goals, table.floorMask, reverseMode);
        Arrays.fill(table.cellIndex, NONE);
        for (long remaining = table.liveCells; remaining != 0; remaining &= remaining - 1) {
            table.cellIndex[lowestCell(remaining)] = table.cellCount++;
        }
        table.solvablePlayers = new long[binomial[table.cellCount][table.subsetSize]];
        LongList queue = new LongList();
        table.roots(queue, table.goals, table.subsetSize, 0);
        for (int head = 0; head < queue.size; head++) {
            long state = queue.values[head];
            long boxMask = stateBoxes(state);
            long reachable =
                    reachableCells(cellBit(statePlayer(state)), table.floorMask & ~boxMask);
            long emptyCells = table.floorMask & ~boxMask;
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                long movableBoxes =
                        movable(
                                boxMask,
                                reachable,
                                emptyCells,
                                table.floorMask,
                                direction,
                                !reverseMode);
                while (movableBoxes != 0) {
                    int cell = lowestCell(movableBoxes);
                    movableBoxes &= movableBoxes - 1;
                    int nextCell = cell + DIRECTION_STEP[direction];
                    table.add(
                            queue,
                            boxMask ^ cellBit(cell) ^ cellBit(nextCell),
                            cellBit(reverseMode ? cell : nextCell + DIRECTION_STEP[direction]));
                }
            }
        }
        return table;
    }

    static final int[] patternBoxIndices = new int[MAX_BOXES];

    // Enumerate in increasing-cell order, accumulating the same combinatorial rank.
    // Unchanged frozen boxes allow skipping subsets without the moved box.
    static boolean checkSubsets(
            Pattern table,
            long reachable,
            int boxCount,
            int start,
            int chosen,
            int rank,
            int moved,
            boolean containsMoved) {
        if (chosen == table.subsetSize) {
            return (moved >= 0 && !containsMoved) || (table.solvablePlayers[rank] & reachable) != 0;
        }
        for (int index = start; index < boxCount; index++) {
            int cellIndex = patternBoxIndices[index];
            if (!checkSubsets(
                    table,
                    reachable,
                    boxCount,
                    index + 1,
                    chosen + 1,
                    rank + binomial[cellIndex][chosen + 1],
                    moved,
                    containsMoved || cellIndex == moved)) {
                return false;
            }
        }
        return true;
    }

    static boolean patternGood(long boxMask, long reachable, long fixed) {
        Pattern table = getPattern(fixed);
        if (table.subsetSize < 1) {
            return true;
        }
        if (((boxMask & ~fixed) & ~table.liveCells) != 0) {
            return false;
        }
        int moved =
                movedBox != 0 && fixed == parentFrozenBoxes
                        ? table.cellIndex[lowestCell(movedBox)]
                        : NONE;
        if ((movedBox & fixed) != 0 || table.subsetSize == 1) {
            moved = NONE;
        }
        int boxCount = 0;
        for (long remaining = boxMask & ~fixed; remaining != 0; remaining &= remaining - 1) {
            patternBoxIndices[boxCount++] = table.cellIndex[lowestCell(remaining)];
        }
        return checkSubsets(table, reachable, boxCount, 0, 0, 0, moved, false);
    }

    // Matching scratch arrays are reused; no search call recursively evaluates a heuristic.
    static final int[] distanceQueue = new int[DISTANCE_QUEUE_SIZE];
    static final boolean[] distanceQueued = new boolean[CELL_COUNT];
    static final short[] computedDistances = new short[MAX_BOXES * CELL_COUNT];
    static final int[] boxCells = new int[MATCHING_SIZE];
    static final int[] boxPotential = new int[MATCHING_SIZE];
    static final int[] goalPotential = new int[MATCHING_SIZE];
    static final int[] matchedBox = new int[MATCHING_SIZE];
    static final int[] previousGoal = new int[MATCHING_SIZE];
    static final int[] slack = new int[MATCHING_SIZE];
    static final boolean[] visitedGoal = new boolean[MATCHING_SIZE];

    // Distances fit in shorts, including the unreachable sentinel and crossing penalties.
    // Cache only the actual goal rows, conditioned on the frozen boxes.
    static short[] distances(long boxMask, long frozen) {
        short[] table = boxCrossingPenalty == 0 ? distanceCache.get(frozen) : null;
        if (table != null) {
            return table;
        }
        table = boxCrossingPenalty == 0 ? new short[goalCount * CELL_COUNT] : computedDistances;
        long available = floorMask & ~frozen;
        for (int goal = 0; goal < goalCount; goal++) {
            int offset = goal * CELL_COUNT;
            Arrays.fill(table, offset, offset + CELL_COUNT, (short) UNREACHABLE_DISTANCE);
            table[offset + goals[goal]] = 0;
            if ((frozen & cellBit(goals[goal])) != 0) {
                continue;
            }
            int head = 0, tail = 1;
            distanceQueue[0] = goals[goal];

            Arrays.fill(distanceQueued, false);
            distanceQueued[goals[goal]] = true;
            while (head != tail) {
                int cell = distanceQueue[head];
                head = (head + 1) & DISTANCE_QUEUE_MASK;
                distanceQueued[cell] = false;
                for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                    int nextCell = cell + DIRECTION_STEP[direction];
                    int supportCell =
                            reverseMode
                                    ? cell - DIRECTION_STEP[direction]
                                    : nextCell + DIRECTION_STEP[direction];
                    if (!contains(available, nextCell) || !contains(available, supportCell)) {
                        continue;
                    }
                    int crossings =
                            ((boxMask & cellBit(cell)) != 0 ? 1 : 0)
                                    + ((boxMask & cellBit(supportCell)) != 0 ? 1 : 0);
                    int distance = table[offset + cell] + 1 + boxCrossingPenalty * crossings;
                    if (distance < table[offset + nextCell]) {
                        table[offset + nextCell] = (short) distance;
                        if (!distanceQueued[nextCell]) {
                            distanceQueue[tail] = nextCell;
                            tail = (tail + 1) & DISTANCE_QUEUE_MASK;
                            distanceQueued[nextCell] = true;
                        }
                    }
                }
            }
        }
        if (boxCrossingPenalty == 0) {
            distanceCache.put(frozen, table);
        }
        return table;
    }

    // Adding two encodes both a dead estimate and a zero estimate as nonempty map values.
    static int cacheEstimate(long boxMask, int estimate) {
        heuristicCache.put(boxMask, estimate + 2);
        return estimate;
    }

    // Component-dependent deadlocks precede the box-only cache and Hungarian matching.
    static int heuristic(long boxMask, long reachable) {
        if ((inaccessibleBoxes(boxMask, reachable) & ~targetBoxes) != 0) {
            return NONE;
        }
        long frozen = frozenBoxes(boxMask);
        if ((frozen & ~targetBoxes) != 0) {
            return NONE;
        }
        if (useRegional
                && (!packingGood(boxMask, reachable, frozen) || !regionGood(boxMask, reachable))) {
            return NONE;
        }
        if (patternSize != 0 && !patternGood(boxMask, reachable, frozen)) {
            return NONE;
        }
        int cached = heuristicCache.get(boxMask);
        if (cached != 0) {
            return cached - 2;
        }
        short[] table = distances(boxMask, frozen);
        int boxCount = 0;
        for (long remaining = boxMask; remaining != 0; remaining &= remaining - 1) {
            boxCells[++boxCount] = lowestCell(remaining);
        }
        Arrays.fill(boxPotential, 0);
        Arrays.fill(goalPotential, 0);
        Arrays.fill(matchedBox, 0);
        Arrays.fill(previousGoal, 0);
        for (int box = 1; box <= boxCount; box++) {
            matchedBox[0] = box;
            int currentGoal = 0;
            Arrays.fill(slack, UNREACHABLE_DISTANCE);
            Arrays.fill(visitedGoal, false);
            do {
                visitedGoal[currentGoal] = true;
                int currentBox = matchedBox[currentGoal];
                int adjustment = UNREACHABLE_DISTANCE, nextGoal = 0;
                for (int goal = 1; goal <= boxCount; goal++) {
                    if (!visitedGoal[goal]) {
                        int cost = table[(goal - 1) * CELL_COUNT + boxCells[currentBox]];
                        int reducedCost = cost - boxPotential[currentBox] - goalPotential[goal];
                        if (reducedCost < slack[goal]) {
                            slack[goal] = reducedCost;
                            previousGoal[goal] = currentGoal;
                        }
                        if (slack[goal] < adjustment) {
                            adjustment = slack[goal];
                            nextGoal = goal;
                        }
                    }
                }
                if (adjustment >= UNREACHABLE_DISTANCE) {
                    return cacheEstimate(boxMask, NONE);
                }
                for (int goal = 0; goal <= boxCount; goal++) {
                    if (visitedGoal[goal]) {
                        boxPotential[matchedBox[goal]] += adjustment;
                        goalPotential[goal] -= adjustment;
                    } else {
                        slack[goal] -= adjustment;
                    }
                }
                currentGoal = nextGoal;
            } while (matchedBox[currentGoal] != 0);
            do {
                int nextGoal = previousGoal[currentGoal];
                matchedBox[currentGoal] = matchedBox[nextGoal];
                currentGoal = nextGoal;
            } while (currentGoal != 0);
        }
        for (int goal = 1; goal <= boxCount; goal++) {
            if (table[(goal - 1) * CELL_COUNT + boxCells[matchedBox[goal]]]
                    >= UNREACHABLE_DISTANCE) {
                return cacheEstimate(boxMask, NONE);
            }
        }
        return cacheEstimate(boxMask, -goalPotential[0]);
    }

    static void clearSearch() {
        nodeCount = 0;
        hashTable = new int[0];
        heuristicCache = new LongIntMap();
        distanceCache = new Cache<>();
        patterns = new Cache<>();
    }

    // Remember rejected states only in fast mode; insertion IDs break all heap ties.
    static void add(
            MinHeap open,
            long boxMask,
            long reachable,
            int parent,
            int encodedPush,
            int pushDepth) {
        long state = stateKey(boxMask, reachable);
        prepareHash();
        if (hashTable[nodeSlot(state)] != 0) {
            return;
        }
        int estimate = heuristic(boxMask, reachable);
        if (estimate >= 0 && useRegional && packingWeight != 0) {
            long fixed = boxMask & goalMask;
            packingGood(boxMask, reachable, fixed);
            int missingGoals = MAX_BOXES;
            long[] residues = packing.get(fixed);
            for (int index = 0; index < residues.length; index += 2) {
                missingGoals = Math.min(missingGoals, countBits(residues[index] & ~boxMask));
            }
            estimate += packingWeight * missingGoals;
        }
        if (estimate < 0) {
            if (fastMode) {
                int id = insert(state, NONE, 0);
                nodeCosts[id] = NONE;
            }
            return;
        }
        int id = insert(state, parent, encodedPush);
        nodeCosts[id] = pushDepth;
        int score = PRIORITY_SCALE * (estimate - (useRegional ? pushDepth : 0));
        open.add(score, 0, id);
    }

    static String attempt(
            boolean pullSearch,
            int crossingPenalty,
            boolean regional,
            int tableSize,
            int expansionLimit) {
        reverseMode = pullSearch;
        boxCrossingPenalty = crossingPenalty;
        useRegional = regional;
        patternSize = tableSize;
        movedBox = parentFrozenBoxes = 0;
        goalCount = 0;
        clearSearch();
        targetBoxes = reverseMode ? initialBoxes : goalMask;
        for (long remaining = targetBoxes; remaining != 0; remaining &= remaining - 1) {
            goals[goalCount++] = lowestCell(remaining);
        }
        liveCells = liveClosure(targetBoxes, floorMask, reverseMode);
        MinHeap open = new MinHeap(false);
        if (reverseMode) {
            long todo = floorMask & ~goalMask;
            while (todo != 0) {
                long reachable = reachableCells(todo & -todo, floorMask & ~goalMask);
                add(open, goalMask, reachable, NONE, 0, 0);
                todo &= ~reachable;
            }
        } else {
            add(
                    open,
                    initialBoxes,
                    reachableCells(cellBit(initialPlayer), floorMask & ~initialBoxes),
                    NONE,
                    0,
                    0);
        }
        String plan = search(open, expansionLimit);
        return plan.length() > MAX_PLAN_LENGTH ? "" : plan;
    }

    // Cheap forward and reverse probes precede four rotated forward restarts.
    static String cheapProbes() {
        String plan = attempt(false, 1, false, 0, INITIAL_EXPANSIONS);
        if (plan.isEmpty()) {
            plan = attempt(true, 0, false, 0, INITIAL_EXPANSIONS);
        }
        if (plan.isEmpty()) {
            long savedFloor = floorMask, savedGoals = goalMask, savedBoxes = initialBoxes;
            int savedPlayer = initialPlayer, turns = 0;
            for (int turn = 1; turn <= ROTATION_COUNT && plan.isEmpty(); turn++) {
                floorMask = rotateMask(floorMask);
                goalMask = rotateMask(goalMask);
                initialBoxes = rotateMask(initialBoxes);
                initialPlayer = rotateCell(initialPlayer);
                plan = attempt(false, 2, false, 0, ROTATED_EXPANSIONS);
                turns = turn;
            }
            floorMask = savedFloor;
            goalMask = savedGoals;
            initialBoxes = savedBoxes;
            initialPlayer = savedPlayer;
            for (int turn = 0; turn < turns; turn++) {
                plan = mapPlan(plan, ROTATED_LETTER);
            }
        }
        return plan;
    }

    static String mapPlan(String plan, String directions) {
        char[] letters = plan.toCharArray();
        for (int index = 0; index < letters.length; index++) {
            int caseOffset = letters[index] < 'a' ? LETTER_CASE_OFFSET : 0;
            int direction = DIRECTION_LETTER.indexOf((char) (letters[index] + caseOffset));
            letters[index] = (char) (directions.charAt(direction) - caseOffset);
        }
        return new String(letters);
    }

    // A reflection followed by quarter turns enumerates all eight board symmetries.
    static int transformCell(int cell, int symmetry) {
        if ((symmetry & REFLECTION_FLAG) != 0) {
            cell = (cell / BOARD_WIDTH) * BOARD_WIDTH + LAST_COORDINATE - cell % BOARD_WIDTH;
        }
        for (int turn = 0; turn < (symmetry & ROTATION_MASK); turn++) {
            cell = rotateCell(cell);
        }
        return cell;
    }

    static long transformMask(long boxMask, int symmetry) {
        long result = 0;
        for (; boxMask != 0; boxMask &= boxMask - 1) {
            result |= cellBit(transformCell(lowestCell(boxMask), symmetry));
        }
        return result;
    }

    static boolean geometryBefore(long[] state, long[] best) {
        for (int index = 0; index < GEOMETRY_COMPONENTS; index++) {
            int comparison = Long.compareUnsigned(state[index], best[index]);
            if (comparison != 0) {
                return comparison < 0;
            }
        }
        return false;
    }

    // Regional and packing tests use the lexicographically least unsigned geometry.
    static String runFast() {
        String plan = cheapProbes();
        if (plan.isEmpty()) {
            long savedFloor = floorMask, savedGoals = goalMask, savedBoxes = initialBoxes;
            int savedPlayer = initialPlayer, bestSymmetry = 0;
            long[] bestGeometry = {floorMask, goalMask, initialBoxes, initialPlayer};
            for (int symmetry = 1; symmetry < SYMMETRY_COUNT; symmetry++) {
                long[] state = {
                    transformMask(savedFloor, symmetry),
                    transformMask(savedGoals, symmetry),
                    transformMask(savedBoxes, symmetry),
                    transformCell(savedPlayer, symmetry)
                };
                if (geometryBefore(state, bestGeometry)) {
                    bestGeometry = state;
                    bestSymmetry = symmetry;
                }
            }
            floorMask = bestGeometry[0];
            goalMask = bestGeometry[1];
            initialBoxes = bestGeometry[2];
            initialPlayer = (int) bestGeometry[PLAYER_COMPONENT];
            packing = new Cache<>();
            regions = new Region[DIRECTION_COUNT];
            regionCount = 0;
            packingWeight = PACKING_WEIGHT;
            plan = attempt(false, 0, true, 0, UNBOUNDED_EXPANSIONS);
            int[] inverseDirection = new int[DIRECTION_COUNT];
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                int transformedStep =
                        transformCell(
                                        DIRECTION_PROBE_CELL + DIRECTION_STEP[direction],
                                        bestSymmetry)
                                - transformCell(DIRECTION_PROBE_CELL, bestSymmetry);
                for (int other = 0; other < DIRECTION_COUNT; other++) {
                    if (DIRECTION_STEP[other] == transformedStep) {
                        inverseDirection[other] = direction;
                    }
                }
            }
            StringBuilder directions = new StringBuilder();
            for (int direction : inverseDirection) {
                directions.append(DIRECTION_LETTER.charAt(direction));
            }
            plan = mapPlan(plan, directions.toString());
            floorMask = savedFloor;
            goalMask = savedGoals;
            initialBoxes = savedBoxes;
            initialPlayer = savedPlayer;
        }
        return plan;
    }

    // Drop all fast-search storage before allocating the fallback's subset tables.
    static void release() {
        nodeStates = new long[INITIAL_CAPACITY];
        nodeParents = new int[INITIAL_CAPACITY];
        nodeMoves = new byte[INITIAL_CAPACITY];
        nodeCosts = new int[INITIAL_CAPACITY];
        clearSearch();
        packing = new Cache<>();
        regions = new Region[DIRECTION_COUNT];
        regionCount = 0;
    }

    // Exact player positions allow cheaper paths to reopen states under the move limit.
    static String lengthFallback() {
        reverseMode = false;
        boxCrossingPenalty = patternSize = 0;
        movedBox = 0;
        clearSearch();
        MinHeap open = new MinHeap(true);
        insert(stateKey(initialBoxes, cellBit(initialPlayer)), NONE, 0);
        nodeCosts[0] = 0;
        open.add(0, 0, 0);
        return search(open, UNBOUNDED_EXPANSIONS);
    }

    // Exact search reopens cheaper states; probe search retains the first parent.
    static void addExact(MinHeap open, long boxes, int player, int parent, int move, int cost) {
        if (cost > MAX_PLAN_LENGTH) return;
        long state = stateKey(boxes, cellBit(player));
        prepareHash();
        int id = hashTable[nodeSlot(state)] - 1;
        if (id >= 0 && nodeCosts[id] <= cost) return;
        int estimate = heuristic(boxes, reachableCells(cellBit(player), floorMask & ~boxes));
        if (estimate < 0 || cost + estimate > MAX_PLAN_LENGTH) return;
        if (id < 0) {
            id = insert(state, parent, move);
        } else {
            nodeParents[id] = parent;
            nodeMoves[id] = (byte) move;
        }
        nodeCosts[id] = cost;
        open.add(cost + estimate, cost, id);
    }

    // Only probes use corrals, expansion budgets and the fast-mode clock cap.
    static String search(MinHeap open, int expansionLimit) {
        int expanded = 0;
        long initialReach = reachableCells(cellBit(initialPlayer), floorMask & ~initialBoxes);
        int[] walkDistance = open.exact ? new int[CELL_COUNT] : null;
        while (open.size != 0
                && (open.exact
                        || (expanded < expansionLimit
                                && (!fastMode
                                        || (nodeCount < NODE_CAP
                                                && !((expanded & CLOCK_CHECK_MASK) == 0
                                                        && timeUp())))))) {
            int id = open.ids[0], pathCost = open.exact ? open.costs[0] : 0;
            open.remove();
            if (open.exact && pathCost != nodeCosts[id]) continue;
            long boxes = stateBoxes(nodeStates[id]);
            int player = statePlayer(nodeStates[id]);
            long reachable = open.exact ? 0 : reachableCells(cellBit(player), floorMask & ~boxes);
            if (boxes == (open.exact ? goalMask : targetBoxes)
                    && (!reverseMode || (reachable & initialReach) != 0)) {
                return reconstructPlan(id);
            }
            if (open.exact) {
                reachable = walk(boxes, player, NONE, walkDistance, null, null);
            } else {
                expanded++;
            }
            if (patternSize != 0) parentFrozenBoxes = frozenBoxes(boxes);
            long allowed = open.exact || reverseMode ? boxes : restrictCorral(boxes, reachable);
            for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
                long remaining =
                        movable(
                                allowed,
                                reachable,
                                floorMask & ~boxes,
                                liveCells,
                                direction,
                                reverseMode);
                while (remaining != 0) {
                    int cell = lowestCell(remaining);
                    remaining &= remaining - 1;
                    int nextCell = cell + DIRECTION_STEP[direction];
                    long nextBoxes = boxes ^ cellBit(cell) ^ cellBit(nextCell);
                    int move = cell * DIRECTION_COUNT + direction;
                    if (open.exact) {
                        int cost = pathCost + walkDistance[cell - DIRECTION_STEP[direction]] + 1;
                        addExact(open, nextBoxes, cell, id, move, cost);
                    } else {
                        int nextPlayer = reverseMode ? nextCell + DIRECTION_STEP[direction] : cell;
                        long nextReach =
                                reachableCells(cellBit(nextPlayer), floorMask & ~nextBoxes);
                        movedBox = cellBit(nextCell);
                        add(open, nextBoxes, nextReach, id, move, nodeCosts[id] + 1);
                    }
                }
            }
        }
        return "";
    }

    // Retry the probes, then escalate from three-box to five-box tables and exact A*.
    static String runSafe() {
        String plan = cheapProbes();
        if (plan.isEmpty()) {
            plan =
                    attempt(
                            false,
                            0,
                            false,
                            SMALL_PATTERN_SIZE,
                            countBits(initialBoxes) <= 10
                                    ? SMALL_BOX_EXPANSIONS
                                    : MANY_BOX_EXPANSIONS);
        }
        if (plan.isEmpty()) {
            plan = attempt(false, 0, false, LARGE_PATTERN_SIZE, UNBOUNDED_EXPANSIONS);
        }
        if (plan.isEmpty()) {
            plan = lengthFallback();
        }
        return plan;
    }

    static long originalFloor, originalGoals, originalBoxes;
    static int originalPlayer;

    static boolean valid(String plan) {
        if (plan.length() > MAX_PLAN_LENGTH) {
            return false;
        }
        long boxMask = originalBoxes;
        int player = originalPlayer;
        for (int index = 0; index < plan.length(); index++) {
            char letter = plan.charAt(index);
            boolean push = letter < 'a';
            char lowercase = push ? (char) (letter + LETTER_CASE_OFFSET) : letter;
            int direction = DIRECTION_LETTER.indexOf(lowercase);
            if (direction < 0) {
                return false;
            }
            int nextCell = player + DIRECTION_STEP[direction];
            if (nextCell < 0
                    || nextCell >= CELL_COUNT
                    || (originalFloor & cellBit(nextCell)) == 0) {
                return false;
            }
            if ((boxMask & cellBit(nextCell)) != 0) {
                int boxDestination = nextCell + DIRECTION_STEP[direction];
                if (!push
                        || boxDestination < 0
                        || boxDestination >= CELL_COUNT
                        || (originalFloor & cellBit(boxDestination)) == 0
                        || (boxMask & cellBit(boxDestination)) != 0) {
                    return false;
                }
                boxMask ^= cellBit(nextCell) | cellBit(boxDestination);
            } else if (push) {
                return false;
            }
            player = nextCell;
        }
        return boxMask == originalGoals;
    }

    // Read board bytes directly, retaining spaces and ignoring empty lines and CRLF.
    static void readBoard() throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int row = 0, column = 0, tile;
        while ((tile = input.read()) != NONE) {
            if (tile == '\r') {
                continue;
            }
            if (tile == '\n') {
                if (column != 0) {
                    row++;
                    column = 0;
                }
                continue;
            }
            if (column < BOARD_WIDTH) {
                int cell = row * BOARD_WIDTH + column;
                if (tile != '#') {
                    floorMask |= cellBit(cell);
                }
                if (tile == '.' || tile == '*' || tile == '+') {
                    goalMask |= cellBit(cell);
                }
                if (tile == '$' || tile == '*') {
                    initialBoxes |= cellBit(cell);
                }
                if (tile == '@' || tile == '+') {
                    initialPlayer = cell;
                }
            }
            column++;
        }
    }

    public static void main(String[] args) throws IOException {
        readBoard();
        floorMask = reachableCells(cellBit(initialPlayer), floorMask);
        goalMask &= floorMask;
        initialBoxes &= floorMask;
        originalFloor = floorMask;
        originalGoals = goalMask;
        originalBoxes = initialBoxes;
        originalPlayer = initialPlayer;
        String plan = "";
        if (initialBoxes != goalMask) {
            // Pascal recurrence supplies the ranks used by the subset tables.
            for (int availableCells = 0; availableCells <= MAX_BOXES; availableCells++) {
                for (int subsetSize = 0; subsetSize <= LARGE_PATTERN_SIZE; subsetSize++) {
                    binomial[availableCells][subsetSize] =
                            subsetSize == 0
                                    ? 1
                                    : availableCells == 0
                                            ? 0
                                            : binomial[availableCells - 1][subsetSize - 1]
                                                    + binomial[availableCells - 1][subsetSize];
                }
            }
            try {
                plan = runFast();
            } catch (FailedWalk failure) {
                plan = "";
            }
            if (!valid(plan)) {
                release();
                fastMode = false;
                floorMask = originalFloor;
                goalMask = originalGoals;
                initialBoxes = originalBoxes;
                initialPlayer = originalPlayer;
                plan = runSafe();
            }
        }
        System.out.println(plan);
    }
}
