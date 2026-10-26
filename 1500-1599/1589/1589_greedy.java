import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class Main {
    static final int BOARD_WIDTH = 8;
    static final int CELL_COUNT = 64;
    static final int DIRECTIONS = 4;
    static final int MAX_BOXES = 36;
    static final int MAX_SUBSET = 4;
    static final int SUBSET_STRIDE = MAX_SUBSET + 1;
    static final int UNREACHABLE = 1000000;
    static final int ESTIMATE_WEIGHT = 20;
    static final int PLAYER_SHIFT = 56;
    static final long BOX_BITS = (1L << PLAYER_SHIFT) - 1;
    static final int INITIAL_SLOTS = 65536;
    static final int INITIAL_CAPACITY = 1024;
    static final long HASH_MULTIPLIER = 0x9E3779B97F4A7C15L;
    static final int HASH_SHIFT = 20;
    static final int LETTER_CASE = 'a' - 'A';
    static final int[] STEP = {-BOARD_WIDTH, BOARD_WIDTH, -1, 1};
    static final String LETTERS = "udlr";

    static long floorCells;
    static long goals;
    static long startBoxes;
    static long liveCells;
    static int startPlayer;
    static int goalCount;
    static final int[] pushDistance = new int[MAX_BOXES * CELL_COUNT];

    static long bit(int cell) {
        return 1L << cell;
    }

    static int lowest(long mask) {
        return Long.numberOfTrailingZeros(mask);
    }

    // Enclosing walls keep shifted bits from wrapping onto floor cells.
    static long shift(long mask, int direction) {
        return direction == 0
                ? mask >>> BOARD_WIDTH
                : direction == 1 ? mask << BOARD_WIDTH : direction == 2 ? mask >>> 1 : mask << 1;
    }

    static long reach(long seed, long free) {
        for (; ; ) {
            long grown =
                    (seed | seed << BOARD_WIDTH | seed >>> BOARD_WIDTH | seed << 1 | seed >>> 1)
                            & free;
            if (grown == seed) {
                return seed;
            }
            seed = grown;
        }
    }

    // Remove movable boxes until only frozen boxes remain.
    static long frozenBoxes(long boxes) {
        for (; ; ) {
            long empty = floorCells & ~boxes;
            long emptyLive = empty & liveCells;
            long movable =
                    boxes
                            & ((empty >>> BOARD_WIDTH & emptyLive << BOARD_WIDTH)
                                    | (empty << BOARD_WIDTH & emptyLive >>> BOARD_WIDTH)
                                    | (empty >>> 1 & emptyLive << 1)
                                    | (empty << 1 & emptyLive >>> 1));
            if (movable == 0) {
                return boxes;
            }
            boxes &= ~movable;
        }
    }

    // Removing pushable boxes grows the area available to the player.
    static long stuckBoxes(long boxes, long area) {
        for (; ; ) {
            long emptyLive = floorCells & ~boxes & liveCells;
            long movable =
                    boxes
                            & ((area >>> BOARD_WIDTH & emptyLive << BOARD_WIDTH)
                                    | (area << BOARD_WIDTH & emptyLive >>> BOARD_WIDTH)
                                    | (area >>> 1 & emptyLive << 1)
                                    | (area << 1 & emptyLive >>> 1));
            if (movable == 0) {
                return boxes;
            }
            boxes &= ~movable;
            area = reach(area, floorCells & ~boxes);
        }
    }

    // Restrict pushes to a corral only when all its possible pushes go inward
    // and are already available, even after removing boxes outside its border.
    static long corralBoxes(long boxes, long area) {
        long unseen = floorCells & ~(boxes | area);
        long fixed = frozenBoxes(boxes);
        while (unseen != 0) {
            long corral = reach(unseen & -unseen, floorCells & ~(boxes | area));
            unseen &= ~corral;
            long border =
                    boxes
                            & (corral << 1
                                    | corral >>> 1
                                    | corral << BOARD_WIDTH
                                    | corral >>> BOARD_WIDTH);
            if (((border & ~goals) | (corral & goals)) == 0) {
                continue;
            }
            long reduced = border | fixed;
            long relaxed = reach(area, floorCells & ~reduced);
            boolean inward = true;
            int pushes = 0;
            for (int direction = 0; direction < DIRECTIONS && inward; direction++) {
                long possible =
                        border
                                & shift(relaxed, direction)
                                & shift(floorCells & ~reduced & liveCells, direction ^ 1);
                long actual =
                        border
                                & shift(area, direction)
                                & shift(floorCells & ~boxes & liveCells, direction ^ 1);
                if (possible != actual || (shift(possible, direction) & ~corral) != 0) {
                    inward = false;
                }
                pushes += Long.bitCount(possible);
            }
            if (inward && pushes != 0) {
                return border;
            }
        }
        return boxes;
    }

    static final int[] matchingDistance = new int[CELL_COUNT * MAX_BOXES];
    static final int[] matchingCells = new int[MAX_BOXES + 1];
    static final int[] boxPotential = new int[MAX_BOXES + 1];
    static final int[] goalPotential = new int[MAX_BOXES + 1];
    static final int[] matched = new int[MAX_BOXES + 1];
    static final int[] matchingPrevious = new int[MAX_BOXES + 1];
    static final int[] slack = new int[MAX_BOXES + 1];

    // Hungarian matching gives the minimum total distance to distinct goals.
    static int matching(long boxes) {
        int count = 0;
        for (; boxes != 0; boxes &= boxes - 1) {
            matchingCells[++count] = lowest(boxes);
        }
        Arrays.fill(boxPotential, 0, count + 1, 0);
        Arrays.fill(goalPotential, 0, count + 1, 0);
        Arrays.fill(matched, 0, count + 1, 0);
        Arrays.fill(matchingPrevious, 0, count + 1, 0);
        long allGoals = (1L << (count + 1)) - 1;
        for (int box = 1; box <= count; box++) {
            matched[0] = box;
            int goal = 0;
            Arrays.fill(slack, 0, count + 1, UNREACHABLE);
            long visited = 0;
            do {
                visited |= bit(goal);
                int current = matched[goal];
                int distanceOffset = matchingCells[current] * MAX_BOXES;
                int delta = UNREACHABLE;
                int next = 0;
                long unvisited = allGoals & ~visited;
                for (long rest = unvisited; rest != 0; rest &= rest - 1) {
                    int candidate = lowest(rest);
                    int reduced =
                            matchingDistance[distanceOffset + candidate - 1]
                                    - boxPotential[current]
                                    - goalPotential[candidate];
                    if (reduced < slack[candidate]) {
                        slack[candidate] = reduced;
                        matchingPrevious[candidate] = goal;
                    }
                    if (slack[candidate] < delta) {
                        delta = slack[candidate];
                        next = candidate;
                    }
                }
                if (delta >= UNREACHABLE / 2) {
                    return -1;
                }
                if (delta != 0) {
                    for (long rest = visited; rest != 0; rest &= rest - 1) {
                        int candidate = lowest(rest);
                        boxPotential[matched[candidate]] += delta;
                        goalPotential[candidate] -= delta;
                    }
                    for (long rest = unvisited; rest != 0; rest &= rest - 1) {
                        slack[lowest(rest)] -= delta;
                    }
                }
                goal = next;
            } while (matched[goal] != 0);
            do {
                int next = matchingPrevious[goal];
                matched[goal] = matched[next];
                goal = next;
            } while (goal != 0);
        }
        int total = 0;
        for (int j = 1; j <= count; j++) {
            int distance = pushDistance[(j - 1) * CELL_COUNT + matchingCells[matched[j]]];
            if (distance >= UNREACHABLE) {
                return -1;
            }
            total += distance;
        }
        return total;
    }

    static final int[] liveIndex = new int[CELL_COUNT];
    static int liveCount;
    static final int[] binomial = new int[(MAX_BOXES + 1) * SUBSET_STRIDE];
    static final long[][] solvableFrom = new long[MAX_SUBSET + 1][];
    static long[] tableBoxes = new long[INITIAL_CAPACITY];
    static long[] tableAreas = new long[INITIAL_CAPACITY];
    static int tableSize;
    static final int[] goalCells = new int[MAX_BOXES];

    static int subsetRank(long boxes) {
        int rank = 0;
        int position = 1;
        for (; boxes != 0; boxes &= boxes - 1) {
            rank += binomial[liveIndex[lowest(boxes)] * SUBSET_STRIDE + position++];
        }
        return rank;
    }

    static void addToTable(int size, long boxes, long seed) {
        long area = reach(seed, floorCells & ~boxes);
        int rank = subsetRank(boxes);
        if ((solvableFrom[size][rank] & area) != 0) {
            return;
        }
        solvableFrom[size][rank] |= area;
        if (tableSize == tableBoxes.length) {
            tableBoxes = Arrays.copyOf(tableBoxes, tableSize * 2);
            tableAreas = Arrays.copyOf(tableAreas, tableSize * 2);
        }
        tableBoxes[tableSize] = boxes;
        tableAreas[tableSize++] = area;
    }

    static void addGoalSubsets(int size, int from, int left, long boxes) {
        if (left == 0) {
            for (long free = floorCells & ~boxes; free != 0; ) {
                long area = reach(free & -free, floorCells & ~boxes);
                addToTable(size, boxes, area);
                free &= ~area;
            }
            return;
        }
        for (int i = from; i < goalCount; i++) {
            addGoalSubsets(size, i + 1, left - 1, boxes | bit(goalCells[i]));
        }
    }

    // Reverse pulls mark every player area that solves a small subset of boxes.
    static void buildTable(int size) {
        solvableFrom[size] = new long[binomial[liveCount * SUBSET_STRIDE + size]];
        tableSize = 0;
        addGoalSubsets(size, 0, size, 0);
        for (int head = 0; head < tableSize; head++) {
            long boxes = tableBoxes[head];
            long area = tableAreas[head];
            for (long rest = boxes; rest != 0; rest &= rest - 1) {
                int box = lowest(rest);
                for (int direction = 0; direction < DIRECTIONS; direction++) {
                    int to = box - STEP[direction];
                    int back = to - STEP[direction];
                    if ((area >>> to & 1) != 0
                            && ((floorCells & ~boxes) >>> back & 1) != 0
                            && (liveCells >>> to & 1) != 0) {
                        addToTable(size, boxes ^ bit(box) ^ bit(to), bit(back));
                    }
                }
            }
        }
    }

    static final int TRIPLE_SIZE = 3;
    static final int[] subsetFirst = new int[MAX_BOXES];
    static final int[] subsetSecond = new int[MAX_BOXES];
    static final int[] subsetThird = new int[MAX_BOXES];
    static final int[] movedRank = new int[MAX_SUBSET + 1];
    static int beforeMoved;

    // Insert the moved box into each sorted subset without rebuilding its mask.
    static int prepareSubsets(long boxes, int moved) {
        int count = 0;
        beforeMoved = 0;
        int movedOffset = liveIndex[moved] * SUBSET_STRIDE;
        for (int size = 1; size <= MAX_SUBSET; size++) {
            movedRank[size] = binomial[movedOffset + size];
        }
        for (long rest = boxes & ~bit(moved); rest != 0; rest &= rest - 1) {
            int cell = lowest(rest);
            int offset = liveIndex[cell] * SUBSET_STRIDE;
            if (cell < moved) {
                beforeMoved++;
            } else {
                offset++;
            }
            subsetFirst[count] = binomial[offset + 1];
            subsetSecond[count] = binomial[offset + 2];
            subsetThird[count++] = binomial[offset + TRIPLE_SIZE];
        }
        return count;
    }

    // The loops preserve the recursive enumeration and its first failing subset.
    static boolean subsetsSolvable(int size, int count, long area) {
        long[] table = solvableFrom[size];
        if (size == 2) {
            for (int first = 0; first < count; first++) {
                int rank = subsetFirst[first] + movedRank[first < beforeMoved ? 2 : 1];
                if ((table[rank] & area) == 0) {
                    return false;
                }
            }
        } else if (size == TRIPLE_SIZE) {
            for (int first = 0; first < count; first++) {
                int position = first < beforeMoved ? 2 : 1;
                for (int second = first + 1; second < count; second++) {
                    int rank =
                            subsetFirst[first]
                                    + subsetSecond[second]
                                    + movedRank[position + (second < beforeMoved ? 1 : 0)];
                    if ((table[rank] & area) == 0) {
                        return false;
                    }
                }
            }
        } else {
            for (int first = 0; first < count; first++) {
                int position = first < beforeMoved ? 2 : 1;
                for (int second = first + 1; second < count; second++) {
                    int movedPosition = position + (second < beforeMoved ? 1 : 0);
                    int pairRank = subsetFirst[first] + subsetSecond[second];
                    int third = second + 1;
                    int rank = pairRank + movedRank[movedPosition + 1];
                    for (; third < beforeMoved; third++) {
                        if ((table[rank + subsetThird[third]] & area) == 0) {
                            return false;
                        }
                    }
                    rank = pairRank + movedRank[movedPosition];
                    for (; third < count; third++) {
                        if ((table[rank + subsetThird[third]] & area) == 0) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }

    static final int INTERIOR_WIDTH = BOARD_WIDTH - 2;
    static final long INTERIOR_MASK = (1L << INTERIOR_WIDTH) - 1;
    static final int PACKED_PLAYER_SHIFT = INTERIOR_WIDTH * INTERIOR_WIDTH;
    static final int INTEGER_BITS = Integer.SIZE;
    static final int SEGMENT_SHIFT = 16;
    static final int SEGMENT_SIZE = 1 << SEGMENT_SHIFT;
    static final int SEGMENT_MASK = SEGMENT_SIZE - 1;
    static final int UNMOVED = 32768;
    static final long INTEGER_MASK = 0xffffffffL;
    static int[][] slotLow = {new int[INITIAL_SLOTS]};
    static short[][] slotHigh = {new short[INITIAL_SLOTS]};
    static int slotCount = INITIAL_SLOTS;
    static int usedSlots;
    static final int LOAD_SLACK = 4;

    // Six interior rows and the player fit in six bytes. Hash the original key.
    static long packKey(long key) {
        long packed = (key >>> PLAYER_SHIFT) << PACKED_PLAYER_SHIFT;
        for (int row = 0; row < INTERIOR_WIDTH; row++) {
            packed |=
                    ((key >>> ((row + 1) * BOARD_WIDTH + 1)) & INTERIOR_MASK)
                            << (row * INTERIOR_WIDTH);
        }
        return packed;
    }

    static long unpackKey(long packed) {
        long key = (packed >>> PACKED_PLAYER_SHIFT) << PLAYER_SHIFT;
        for (int row = 0; row < INTERIOR_WIDTH; row++) {
            key |=
                    ((packed >>> (row * INTERIOR_WIDTH)) & INTERIOR_MASK)
                            << ((row + 1) * BOARD_WIDTH + 1);
        }
        return key;
    }

    // Mark old entries, then relocate them in place, displacing unprocessed keys.
    // Segments avoid retaining a second full table during growth.
    static void growSlots() {
        int oldSegments = slotLow.length;
        slotLow = Arrays.copyOf(slotLow, oldSegments * 2);
        slotHigh = Arrays.copyOf(slotHigh, oldSegments * 2);
        for (int segment = 0; segment < oldSegments; segment++) {
            short[] high = slotHigh[segment];
            for (int offset = 0; offset < SEGMENT_SIZE; offset++) {
                if (high[offset] != 0) {
                    high[offset] = (short) (high[offset] | UNMOVED);
                }
            }
        }
        for (int segment = oldSegments; segment < slotLow.length; segment++) {
            slotLow[segment] = new int[SEGMENT_SIZE];
            slotHigh[segment] = new short[SEGMENT_SIZE];
        }
        slotCount *= 2;
        int mask = slotCount - 1;
        for (int segment = 0; segment < oldSegments; segment++) {
            for (int offset = 0; offset < SEGMENT_SIZE; offset++) {
                if (slotHigh[segment][offset] >= 0) {
                    continue;
                }
                long packed =
                        (slotLow[segment][offset] & INTEGER_MASK)
                                | (long) (slotHigh[segment][offset] & (UNMOVED - 1))
                                        << INTEGER_BITS;
                slotHigh[segment][offset] = 0;
                for (; ; ) {
                    long key = unpackKey(packed);
                    int index = (int) ((key * HASH_MULTIPLIER) >>> HASH_SHIFT) & mask;
                    while (slotHigh[index >>> SEGMENT_SHIFT][index & SEGMENT_MASK] > 0) {
                        index = (index + 1) & mask;
                    }
                    int targetSegment = index >>> SEGMENT_SHIFT;
                    int targetOffset = index & SEGMENT_MASK;
                    int displacedHigh = slotHigh[targetSegment][targetOffset];
                    long displaced =
                            (slotLow[targetSegment][targetOffset] & INTEGER_MASK)
                                    | (long) (displacedHigh & (UNMOVED - 1)) << INTEGER_BITS;
                    slotLow[targetSegment][targetOffset] = (int) packed;
                    slotHigh[targetSegment][targetOffset] = (short) (packed >>> INTEGER_BITS);
                    if (displacedHigh == 0) {
                        break;
                    }
                    packed = displaced;
                }
            }
        }
    }

    // Keys are nonzero; leave a quarter of the slots empty for probing.
    static boolean insertKey(long key) {
        if (usedSlots + 1 > slotCount - slotCount / LOAD_SLACK) {
            growSlots();
        }
        long packed = packKey(key);
        int low = (int) packed;
        short high = (short) (packed >>> INTEGER_BITS);
        int mask = slotCount - 1;
        int index = (int) ((key * HASH_MULTIPLIER) >>> HASH_SHIFT) & mask;
        for (; ; ) {
            int segment = index >>> SEGMENT_SHIFT;
            int offset = index & SEGMENT_MASK;
            if (slotHigh[segment][offset] == 0) {
                slotLow[segment][offset] = low;
                slotHigh[segment][offset] = high;
                usedSlots++;
                return true;
            }
            if (slotHigh[segment][offset] == high && slotLow[segment][offset] == low) {
                return false;
            }
            index = (index + 1) & mask;
        }
    }

    static final int[] walkPrevious = new int[CELL_COUNT];
    static final int[] walkDirection = new int[CELL_COUNT];
    static final int[] cellQueue = new int[CELL_COUNT];
    static final char[] walkSteps = new char[CELL_COUNT];

    static void walk(StringBuilder plan, long boxes, int from, int to) {
        int head = 0;
        int tail = 0;
        Arrays.fill(walkPrevious, -1);
        walkPrevious[from] = from;
        cellQueue[tail++] = from;
        while (head < tail && walkPrevious[to] < 0) {
            int cell = cellQueue[head++];
            for (int direction = 0; direction < DIRECTIONS; direction++) {
                int next = cell + STEP[direction];
                if (((floorCells & ~boxes) >>> next & 1) != 0 && walkPrevious[next] < 0) {
                    walkPrevious[next] = cell;
                    walkDirection[next] = direction;
                    cellQueue[tail++] = next;
                }
            }
        }
        int count = 0;
        for (int cell = to; cell != from; cell = walkPrevious[cell]) {
            walkSteps[count++] = LETTERS.charAt(walkDirection[cell]);
        }
        while (count > 0) {
            plan.append(walkSteps[--count]);
        }
    }

    static final int INITIAL_NODES = 524288;
    static final int INITIAL_HEAP = 65536;
    // Reserve primitive search buffers to avoid garbage from repeated doubling.
    static long[] nodeKeys = new long[INITIAL_NODES];
    static int[] nodeParents = new int[INITIAL_NODES];
    static byte[] nodeMoves = new byte[INITIAL_NODES];
    static int[] nodePushes = new int[INITIAL_NODES];
    static int nodeCount;
    static int[] heapNodes = new int[INITIAL_HEAP];
    static int[] heapWeights = new int[INITIAL_HEAP];
    static int heapSize;
    static final int UNSIGNED_BYTE_MASK = 255;

    static boolean earlier(int weight, int node, int otherWeight, int otherNode) {
        return weight < otherWeight || (weight == otherWeight && node < otherNode);
    }

    // The C++ pair ordering breaks equal weights by insertion index.
    static void pushHeap(int node, int weight) {
        if (heapSize == heapNodes.length) {
            heapNodes = Arrays.copyOf(heapNodes, heapSize * 2);
            heapWeights = Arrays.copyOf(heapWeights, heapSize * 2);
        }
        int child = heapSize++;
        while (child > 0) {
            int parent = (child - 1) / 2;
            if (!earlier(weight, node, heapWeights[parent], heapNodes[parent])) {
                break;
            }
            heapNodes[child] = heapNodes[parent];
            heapWeights[child] = heapWeights[parent];
            child = parent;
        }
        heapNodes[child] = node;
        heapWeights[child] = weight;
    }

    static int popHeap() {
        int result = heapNodes[0];
        int node = heapNodes[--heapSize];
        int weight = heapWeights[heapSize];
        int parent = 0;
        while (parent * 2 + 1 < heapSize) {
            int child = parent * 2 + 1;
            if (child + 1 < heapSize
                    && earlier(
                            heapWeights[child + 1],
                            heapNodes[child + 1],
                            heapWeights[child],
                            heapNodes[child])) {
                child++;
            }
            if (!earlier(heapWeights[child], heapNodes[child], weight, node)) {
                break;
            }
            heapNodes[parent] = heapNodes[child];
            heapWeights[parent] = heapWeights[child];
            parent = child;
        }
        heapNodes[parent] = node;
        heapWeights[parent] = weight;
        return result;
    }

    static void add(long boxes, int player, int parent, int move, int pushes) {
        long area = reach(bit(player), floorCells & ~boxes);
        long key = boxes | (long) lowest(area) << PLAYER_SHIFT;
        if (!insertKey(key)) {
            return;
        }
        boolean alive =
                (frozenBoxes(boxes) & ~goals) == 0 && (stuckBoxes(boxes, area) & ~goals) == 0;
        if (parent >= 0) {
            int moved = move / DIRECTIONS + STEP[move % DIRECTIONS];
            int count = prepareSubsets(boxes, moved);
            for (int size = 2; size <= MAX_SUBSET && alive; size++) {
                if (count + 1 >= size) {
                    alive = subsetsSolvable(size, count, area);
                }
            }
        }
        int estimate = alive ? matching(boxes) : -1;
        if (estimate < 0) {
            return;
        }
        if (nodeCount == nodeKeys.length) {
            int capacity = nodeCount * 2;
            nodeKeys = Arrays.copyOf(nodeKeys, capacity);
            nodeParents = Arrays.copyOf(nodeParents, capacity);
            nodeMoves = Arrays.copyOf(nodeMoves, capacity);
            nodePushes = Arrays.copyOf(nodePushes, capacity);
        }
        nodeKeys[nodeCount] = key;
        nodeParents[nodeCount] = parent;
        nodeMoves[nodeCount] = (byte) move;
        nodePushes[nodeCount] = pushes;
        pushHeap(nodeCount++, pushes + ESTIMATE_WEIGHT * estimate);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader input =
                new BufferedReader(new InputStreamReader(System.in, StandardCharsets.US_ASCII));
        String line;
        int row = 0;
        while ((line = input.readLine()) != null) {
            if (line.isEmpty()) {
                continue;
            }
            for (int column = 0; column < line.length() && column < BOARD_WIDTH; column++) {
                char tile = line.charAt(column);
                int cell = row * BOARD_WIDTH + column;
                if (tile != '#') {
                    floorCells |= bit(cell);
                }
                if (tile == '.' || tile == '*' || tile == '+') {
                    goals |= bit(cell);
                }
                if (tile == '$' || tile == '*') {
                    startBoxes |= bit(cell);
                }
                if (tile == '@' || tile == '+') {
                    startPlayer = cell;
                }
            }
            row++;
        }
        floorCells = reach(bit(startPlayer), floorCells);
        goals &= floorCells;
        startBoxes &= floorCells;
        if (startBoxes == goals) {
            System.out.print('\n');
            return;
        }
        for (long rest = goals; rest != 0; rest &= rest - 1) {
            int goal = goalCount++;
            int offset = goal * CELL_COUNT;
            int head = 0;
            int tail = 0;
            Arrays.fill(pushDistance, offset, offset + CELL_COUNT, UNREACHABLE);
            int goalCell = lowest(rest);
            goalCells[goal] = goalCell;
            pushDistance[offset + goalCell] = 0;
            cellQueue[tail++] = goalCell;
            while (head < tail) {
                int cell = cellQueue[head++];
                for (int direction = 0; direction < DIRECTIONS; direction++) {
                    int from = cell - STEP[direction];
                    int player = from - STEP[direction];
                    if ((floorCells >>> from & 1) != 0
                            && (floorCells >>> player & 1) != 0
                            && pushDistance[offset + from] == UNREACHABLE) {
                        pushDistance[offset + from] = pushDistance[offset + cell] + 1;
                        cellQueue[tail++] = from;
                    }
                }
            }
            for (int cell = 0; cell < CELL_COUNT; cell++) {
                if (pushDistance[offset + cell] < UNREACHABLE) {
                    liveCells |= bit(cell);
                }
            }
        }
        for (int cell = 0; cell < CELL_COUNT; cell++) {
            for (int goal = 0; goal < goalCount; goal++) {
                matchingDistance[cell * MAX_BOXES + goal] = pushDistance[goal * CELL_COUNT + cell];
            }
        }
        for (int cell = 0; cell < CELL_COUNT; cell++) {
            if ((liveCells >>> cell & 1) != 0) {
                liveIndex[cell] = liveCount++;
            }
        }
        for (int count = 0; count <= MAX_BOXES; count++) {
            for (int size = 0; size <= MAX_SUBSET; size++) {
                binomial[count * SUBSET_STRIDE + size] =
                        size == 0
                                ? 1
                                : count == 0
                                        ? 0
                                        : binomial[(count - 1) * SUBSET_STRIDE + size - 1]
                                                + binomial[(count - 1) * SUBSET_STRIDE + size];
            }
        }
        for (int size = 2; size <= MAX_SUBSET; size++) {
            buildTable(size);
        }
        tableBoxes = null;
        tableAreas = null;

        add(startBoxes, startPlayer, -1, 0, 0);
        int solved = -1;
        while (heapSize != 0) {
            int id = popHeap();
            long boxes = nodeKeys[id] & BOX_BITS;
            if (boxes == goals) {
                solved = id;
                break;
            }
            long area = reach(bit((int) (nodeKeys[id] >>> PLAYER_SHIFT)), floorCells & ~boxes);
            long emptyLive = floorCells & ~boxes & liveCells;
            long allowed = corralBoxes(boxes, area);
            for (int direction = 0; direction < DIRECTIONS; direction++) {
                for (long can = allowed & shift(area, direction) & shift(emptyLive, direction ^ 1);
                        can != 0;
                        can &= can - 1) {
                    int box = lowest(can);
                    add(
                            boxes ^ bit(box) ^ bit(box + STEP[direction]),
                            box,
                            id,
                            box * DIRECTIONS + direction,
                            nodePushes[id] + 1);
                }
            }
        }
        int count = 0;
        for (int id = solved; id > 0; id = nodeParents[id]) {
            count++;
        }
        byte[] moves = new byte[count];
        for (int id = solved; id > 0; id = nodeParents[id]) {
            moves[--count] = nodeMoves[id];
        }
        StringBuilder plan = new StringBuilder();
        long boxes = startBoxes;
        int player = startPlayer;
        for (byte packedMove : moves) {
            int move = packedMove & UNSIGNED_BYTE_MASK;
            int box = move / DIRECTIONS;
            int direction = move % DIRECTIONS;
            walk(plan, boxes, player, box - STEP[direction]);
            plan.append((char) (LETTERS.charAt(direction) - LETTER_CASE));
            boxes ^= bit(box) ^ bit(box + STEP[direction]);
            player = box;
        }
        plan.append('\n');
        System.out.print(plan);
    }
}
