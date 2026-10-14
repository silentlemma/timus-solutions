import java.io.ByteArrayOutputStream;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class Main {
    static final int SIDES = 4;
    static final int MAXCELLS = 64;
    static final int NONE = -1;
    static final int INF = 1000000;
    static final int MAX_SIDE = 8;
    static final int PLAYER_SHIFT = MAXCELLS - MAX_SIDE - 1;
    static final int INPUT_BUFFER = 4096;
    static final int LONGEST = 10000;
    static final int[] DR = {-1, 1, 0, 0};
    static final int[] DC = {0, 0, -1, 1};
    static final String STEP = "udlr";
    static final int[] OPP = {1, 0, 3, 2};
    static final int UP = 0;
    static final int DOWN = 1;
    static final int LEFT = 2;
    static final int RIGHT = 3;

    // a mask is a set of grid cells, one bit each (grid <= 8 x 8)
    static boolean has(long m, int c) { return ((m >>> c) & 1) != 0; }

    static long bit(int c) { return 1L << c; }

    static int low(long x) { return Long.numberOfTrailingZeros(x); }

    static int rows;
    static int cols;
    static int cells;
    static long floorM;
    static long goalM;
    static long deadM;
    static long deadPullM;
    static int[][] nb = new int[SIDES][MAXCELLS]; // the neighbour in a direction, NONE outside
    static int startPlayer;
    static long startBoxes;
    static int floorCount;
    static int goalCount;
    static int[] floorCell = new int[MAXCELLS];
    static int[] floorIndex = new int[MAXCELLS];

    // Enclosing walls stop horizontal growth before it could wrap into another row.
    static long grow(long r) {
        return r | (r << 1) | (r >>> 1) | (r << cols) | (r >>> cols);
    }

    static long flood(long seed, long within) {
        for (long r = seed;;) {
            long x = grow(r) & within;
            if (x == r) {
                return r;
            }
            r = x;
        }
    }

    static long reach(int p, long boxes) { return flood(bit(p), floorM & ~boxes); }

    // Enclosing walls leave all box bits below the player field.
    static long packKey(long boxes, int player) {
        return boxes | (long)player << PLAYER_SHIFT;
    }

    static long keyBoxes(long key) { return key & floorM; }

    static int keyPlayer(long key) { return (int)(key >>> PLAYER_SHIFT); }

    // A box is frozen when it can move along neither axis: a wall or a frozen box
    // on either side, or dead squares on both sides. Boxes already found frozen
    // count as walls while their neighbours are checked.
    static long frozenAsWall;
    static boolean frozenOffGoal;

    static boolean wallLike(int c) { return c < 0 || !has(floorM, c) || has(frozenAsWall, c); }

    static boolean axisBlocked(int x, int d1, int d2, long boxes) {
        int a = nb[d1][x];
        int b = nb[d2][x];
        if (wallLike(a) || wallLike(b)) {
            return true;
        }
        if (has(deadM, a) && has(deadM, b)) {
            return true;
        }
        return (has(boxes, a) && frozen(a, boxes)) || (has(boxes, b) && frozen(b, boxes));
    }

    static boolean frozen(int x, long boxes) {
        long saved = frozenAsWall;
        frozenAsWall |= bit(x);
        boolean f = axisBlocked(x, LEFT, RIGHT, boxes) && axisBlocked(x, UP, DOWN, boxes);
        frozenAsWall = saved;
        if (f && !has(goalM, x)) {
            frozenOffGoal = true;
        }
        return f;
    }

    // the box just pushed to x froze a box that is not on a goal
    static boolean freezeDeadlock(int x, long boxes) {
        frozenAsWall = 0;
        frozenOffGoal = false;
        return frozen(x, boxes) && frozenOffGoal;
    }

    // h: the sum of each box's push distance to its nearest target; boxes that
    // cannot be matched to distinct reachable targets mean a deadlock
    static long[][] canReach =
        new long[2][MAXCELLS]; // [push or pull search][cell]: reachable targets
    static int[][] nearest = new int[2][MAXCELLS];
    static int[] matchOf = new int[MAXCELLS];
    static long[] boxTargets = new long[MAXCELLS];
    static long visited;

    static boolean augment(int i) {
        for (long m = boxTargets[i] & ~visited; m != 0; m &= m - 1) {
            int j = low(m);
            visited |= bit(j);
            if (matchOf[j] < 0 || augment(matchOf[j])) {
                matchOf[j] = i;
                return true;
            }
        }
        return false;
    }

    static int heuristic(long boxes, int dir) {
        int k = 0;
        int h = 0;
        for (long b = boxes; b != 0; b &= b - 1) {
            h += nearest[dir][low(b)];
            boxTargets[k++] = canReach[dir][low(b)];
        }
        Arrays.fill(matchOf, 0, goalCount, NONE);
        for (int i = 0; i < k; i++) {
            visited = 0;
            if (!augment(i)) {
                return NONE;
            }
        }
        return h;
    }

    // A push is packed as box * SIDES + direction.
    static int[] best = new int[MAXCELLS * SIDES];
    static int[] candidates = new int[MAXCELLS * SIDES];

    // The pushes worth trying, or a deadlock. If every push of the boxes around
    // a region the player cannot reach goes inward and can be made now, one of
    // them is needed first, so only those are tried.
    static int generatePushes(long boxes, long area, int[] out) {
        int count = 0;
        for (long bb = boxes; bb != 0; bb &= bb - 1) {
            int b = low(bb);
            for (int d = 0; d < SIDES; d++) {
                int s = nb[OPP[d]][b];
                int t = nb[d][b];
                if (s >= 0 && t >= 0 && has(area, s) && has(floorM, t) && !has(boxes, t)) {
                    out[count++] = b * SIDES + d;
                }
            }
        }
        long unreached = floorM & ~boxes & ~area;
        int bestCount = count + 1;
        while (unreached != 0) {
            long corral = flood(unreached & -unreached, floorM & ~boxes & ~area);
            unreached &= ~corral;
            long barrier = grow(corral) & boxes;
            if ((corral & goalM) == 0 && (barrier & ~goalM) == 0) {
                continue; // finished corral
            }
            boolean inward = true;
            boolean ready = true;
            int nc = 0;
            for (long bb = barrier; bb != 0 && inward; bb &= bb - 1) {
                int b = low(bb);
                for (int d = 0; d < SIDES; d++) {
                    int s = nb[OPP[d]][b];
                    int t = nb[d][b];
                    // the player stands outside the corral and off the barrier
                    if (s < 0 || !has(floorM, s) || has(corral, s) || has(barrier, s)) {
                        continue;
                    }
                    if (t < 0 || !has(floorM, t) || has(barrier, t)) {
                        continue; // blocked for good
                    }
                    if (!has(corral, t)) {
                        inward = false; // a push away from the corral
                        break;
                    }
                    if (has(area, s)) {
                        candidates[nc++] = b * SIDES + d;
                    } else {
                        ready = false;
                    }
                }
            }
            if (!inward) {
                continue;
            }
            if (ready && nc == 0) {
                return NONE; // unfinished, and no push can ever enter it
            }
            if (ready && nc < bestCount) {
                bestCount = nc;
                System.arraycopy(candidates, 0, best, 0, nc);
            }
        }
        if (bestCount <= count) {
            System.arraycopy(best, 0, out, 0, bestCount);
            count = bestCount;
        }
        return count;
    }

    // One open-addressing table holds the states of both searches; pull-search
    // keys carry PULLED. A slot keeps the key and the move that made it.
    static final long PULLED = 1L << 63;
    static final int TABLE_BITS = 21;
    static final int TABLE = 1 << TABLE_BITS;
    static final int TABLE_MASK = TABLE - 1;
    static final int TABLE_FILL = TABLE / 100 * 88; // the most keys before the table counts as full
    static final int ROOT = 255;
    static final int BYTE_MASK = 0xff;
    static final long GOLDEN = 0x9E3779B97F4A7C15L;
    static final int KEY_BITS = 64;
    static final int PRESENT = -1;
    static final int FULL = -2;
    static long[] tableKey;
    static byte[] tableMove; // floor index of the moved box * 4 + direction
    static int keyCount;

    static int slotOf(long key) { return (int)((key * GOLDEN) >>> (KEY_BITS - TABLE_BITS)); }

    static int insertKey(long key) {
        int h = slotOf(key);
        for (; tableKey[h] != 0; h = (h + 1) & TABLE_MASK) {
            if (tableKey[h] == key) {
                return PRESENT;
            }
        }
        if (keyCount >= TABLE_FILL) {
            return FULL;
        }
        keyCount++;
        tableKey[h] = key;
        return h;
    }

    // the slot of key, or else ~ the empty slot where it would go
    static int probe(long key) {
        int h = slotOf(key);
        for (; tableKey[h] != 0; h = (h + 1) & TABLE_MASK) {
            if (tableKey[h] == key) {
                return h;
            }
        }
        return ~h;
    }

    // put key into the empty slot s that probe found, unless the table is full
    static boolean insertAt(int s, long key) {
        if (keyCount >= TABLE_FILL) {
            return false;
        }
        keyCount++;
        tableKey[s] = key;
        return true;
    }

    static boolean hasKey(long key) {
        for (int h = slotOf(key); tableKey[h] != 0; h = (h + 1) & TABLE_MASK) {
            if (tableKey[h] == key) {
                return true;
            }
        }
        return false;
    }

    static int findKey(long key) {
        int h = slotOf(key);
        while (tableKey[h] != key) {
            h = (h + 1) & TABLE_MASK;
        }
        return h;
    }

    // Open lists: buckets by f = g + WEIGHT * h, each a stack threaded through the
    // table slots (a slot is queued at most once), so the memory stays fixed.
    static final int BUCKETS = 4096;
    static final int G_BITS = 9;
    static final int G_MASK = (1 << G_BITS) - 1;
    static final int WEIGHT = 3;
    static int[] tableNext; // (next slot + 1) << G_BITS | g
    static int popSlot;
    static int popG;

    static class Open {
        int[] head = new int[BUCKETS]; // slot + 1, 0 when empty
        int lowest = BUCKETS;

        void push(int slot, int g, int f) {
            f = Math.min(f, BUCKETS - 1);
            tableNext[slot] = head[f] << G_BITS | Math.min(g, G_MASK);
            head[f] = slot + 1;
            lowest = Math.min(lowest, f);
        }

        boolean pop() {
            while (lowest < BUCKETS && head[lowest] == 0) {
                lowest++;
            }
            if (lowest >= BUCKETS) {
                return false;
            }
            popSlot = head[lowest] - 1;
            head[lowest] = tableNext[popSlot] >>> G_BITS;
            popG = tableNext[popSlot] & G_MASK;
            return true;
        }
    }

    static Open pushOpen = new Open();
    static Open pullOpen = new Open();
    static final int PUSH_ROUNDS = 8; // expansions of each search per round
    static final int PULL_ROUNDS = 1;

    static void walk(int from, int to, long boxes, StringBuilder out) {
        if (from == to) {
            return;
        }
        int[] prev = new int[MAXCELLS];
        int[] queue = new int[MAXCELLS];
        Arrays.fill(prev, -2);
        prev[from] = NONE;
        int head = 0;
        int tail = 0;
        queue[tail++] = from;
        while (head < tail) {
            int x = queue[head++];
            if (x == to) {
                break;
            }
            for (int d = 0; d < SIDES; d++) {
                int y = nb[d][x];
                if (y < 0 || !has(floorM, y) || has(boxes, y) || prev[y] != -2) {
                    continue;
                }
                prev[y] = x * SIDES + d;
                queue[tail++] = y;
            }
        }
        StringBuilder s = new StringBuilder();
        for (int x = to; x != from; x = prev[x] / SIDES) {
            s.append(STEP.charAt(prev[x] % SIDES));
        }
        out.append(s.reverse());
    }

    // the plan through the state key, which both searches reached (or which is solved)
    static String buildAnswer(long key) {
        int[] plan = new int[LONGEST];
        int count = 0;
        for (long k = key;;) { // back from key to the start through the push search
            int move = tableMove[findKey(k)] & BYTE_MASK;
            if (move == ROOT) {
                break;
            }
            int b = floorCell[move / SIDES];
            int d = move % SIDES;
            int t = nb[d][b];
            plan[count++] = b * SIDES + d;
            long boxes = (keyBoxes(k) & ~bit(t)) | bit(b);
            k = packKey(boxes, low(reach(nb[OPP[d]][b], boxes)));
        }
        for (int i = 0; i < count / 2; i++) {
            int move = plan[i];
            plan[i] = plan[count - 1 - i];
            plan[count - 1 - i] = move;
        }
        if (keyBoxes(key) != goalM) {
            for (long k = key;;) { // forward to the goal: each pull, undone, is a push
                int move = tableMove[findKey(k | PULLED)] & BYTE_MASK;
                if (move == ROOT) {
                    break;
                }
                int x = floorCell[move / SIDES];
                int d = move % SIDES;
                int b = nb[d][x];
                plan[count++] = x * SIDES + d;
                long boxes = (keyBoxes(k) & ~bit(x)) | bit(b);
                k = packKey(boxes, low(reach(x, boxes)));
            }
        }
        StringBuilder out = new StringBuilder();
        long boxes = startBoxes;
        int pos = startPlayer;
        for (int i = 0; i < count; i++) {
            int b = plan[i] / SIDES;
            int d = plan[i] % SIDES;
            walk(pos, nb[OPP[d]][b], boxes, out);
            out.append(Character.toUpperCase(STEP.charAt(d)));
            boxes = (boxes & ~bit(b)) | bit(nb[d][b]);
            pos = b;
        }
        return out.toString();
    }

    // For sets of k = 2..MOST cells, the player cells from which these boxes alone
    // can be solved (a pull search from the goals) or reached (a push search from
    // the start); a state with a failing subset is dead.
    static final int MOST = 4;
    static final int TRIO = 3;
    static final int NEAR = 3; // sets of four only with boxes this close to the moved one
    static int[][] binom = new int[MAXCELLS + 1][MOST + 2];
    static long[][][] setTable =
        new long[2][MOST + 1][]; // [solvable or reachable][k][set]: player cells

    static int setIndex(long boxes) { // the combinatorial number system
        int index = 0;
        int i = 1;
        for (long b = boxes; b != 0; b &= b - 1, i++) {
            index += binom[floorIndex[low(b)]][i];
        }
        return index;
    }

    static int enqueueSet(long boxes, long seed, long[] table, long[] queue, int tail) {
        int index = setIndex(boxes);
        if ((table[index] & seed) != 0) {
            return tail;
        }
        long area = flood(seed, floorM & ~boxes);
        table[index] |= area;
        queue[tail++] = boxes;
        queue[tail++] = area;
        return tail;
    }

    static void buildSetTable(int dir, int k) {
        long[] table = new long[binom[floorCount][k]];
        setTable[dir][k] = table;
        long[] queue = tableKey;
        int head = 0;
        int tail = 0;
        int[] at = new int[MAXCELLS];
        int n = 0;
        for (long c = dir == 1 ? startBoxes : goalM; c != 0; c &= c - 1) {
            at[n++] = low(c);
        }
        int[] pick = new int[MOST];
        for (int i = 0; i < k; i++) {
            pick[i] = i;
        }
        while (k <= n) {
            long set = 0;
            for (int i = 0; i < k; i++) {
                set |= bit(at[pick[i]]);
            }
            if (dir == 1) {
                tail = enqueueSet(set, bit(startPlayer), table, queue, tail);
            } else {
                for (long rest = floorM & ~set; rest != 0;) {
                    long area = flood(rest & -rest, rest);
                    tail = enqueueSet(set, area & -area, table, queue, tail);
                    rest &= ~area;
                }
            }
            int i = k - 1;
            while (i >= 0 && pick[i] == n - k + i) {
                i--;
            }
            if (i < 0) {
                break;
            }
            pick[i]++;
            for (int j = i + 1; j < k; j++) {
                pick[j] = pick[j - 1] + 1;
            }
        }
        int[] shifts = {-cols, cols, -1, 1};
        while (head < tail) {
            long boxes = queue[head++];
            long area = queue[head++];
            long free = floorM & ~boxes;
            for (int delta : shifts) {
                long movable;
                if (dir == 1) {
                    movable = boxes & (delta > 0 ? area << delta : area >>> -delta);
                    movable &= delta > 0 ? free >>> delta : free << -delta;
                } else {
                    long ready = area & (delta > 0 ? free << delta : free >>> -delta);
                    movable = boxes & (delta > 0 ? ready << delta : ready >>> -delta);
                }
                while (movable != 0) {
                    long b = movable & -movable;
                    movable ^= b;
                    long dest;
                    long seed;
                    if (dir == 1) {
                        dest = delta > 0 ? b << delta : b >>> -delta;
                        seed = b;
                    } else {
                        dest = delta > 0 ? b >>> delta : b << -delta;
                        seed = delta > 0 ? dest >>> delta : dest << -delta;
                    }
                    tail = enqueueSet(boxes ^ b ^ dest, seed, table, queue, tail);
                }
            }
        }
        Arrays.fill(queue, 0, tail, 0);
    }

    // The set index of floor indexes a < b < ... with x added in its place:
    // binom[v][rank] summed over the sorted values.
    static int index2(int a, int x) {
        return x < a ? binom[x][1] + binom[a][2] : binom[a][1] + binom[x][2];
    }

    static int index3(int a, int b, int x) {
        if (x < a) {
            return binom[x][1] + binom[a][2] + binom[b][TRIO];
        }
        if (x < b) {
            return binom[a][1] + binom[x][2] + binom[b][TRIO];
        }
        return binom[a][1] + binom[b][2] + binom[x][TRIO];
    }

    static int index4(int a, int b, int c, int x) {
        if (x < a) {
            return binom[x][1] + binom[a][2] + binom[b][TRIO] + binom[c][MOST];
        }
        if (x < b) {
            return binom[a][1] + binom[x][2] + binom[b][TRIO] + binom[c][MOST];
        }
        if (x < c) {
            return binom[a][1] + binom[b][2] + binom[x][TRIO] + binom[c][MOST];
        }
        return binom[a][1] + binom[b][2] + binom[c][TRIO] + binom[x][MOST];
    }

    static int[] other = new int[MAXCELLS];
    static int[] close = new int[MAXCELLS];

    // every set of up to MOST boxes with the moved box t is in the table; the
    // other boxes come by floor index in increasing order
    static boolean setsOK(int dir, long boxes, int t, int player) {
        int n = 0;
        int nc = 0;
        for (long b = boxes & ~bit(t); b != 0; b &= b - 1) {
            int c = low(b);
            other[n++] = floorIndex[c];
            if (Math.abs(c / cols - t / cols) <= NEAR && Math.abs(c % cols - t % cols) <= NEAR) {
                close[nc++] = floorIndex[c];
            }
        }
        int ft = floorIndex[t];
        long pb = bit(player);
        long[] pairs = setTable[dir][2];
        long[] trios = setTable[dir][TRIO];
        long[] fours = setTable[dir][MOST];
        for (int i = 0; i < n; i++) {
            if ((pairs[index2(other[i], ft)] & pb) == 0) {
                return false;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((trios[index3(other[i], other[j], ft)] & pb) == 0) {
                    return false;
                }
            }
        }
        for (int i = 0; i < nc; i++) {
            for (int j = i + 1; j < nc; j++) {
                for (int l = j + 1; l < nc; l++) {
                    if ((fours[index4(close[i], close[j], close[l], ft)] & pb) == 0) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    // Both expansions return the key of a state where the searches met (or a
    // solved state), 0 if none yet; tableFull is set when the table is full.
    static boolean tableFull;
    static int[] pushes = new int[MAXCELLS * SIDES];

    static long expandPush(int slot, int g) {
        g++;
        long key = tableKey[slot];
        long boxes = keyBoxes(key);
        long area = reach(keyPlayer(key), boxes);
        int count = generatePushes(boxes, area, pushes);
        for (int i = 0; i < count; i++) {
            int b = pushes[i] / SIDES;
            int d = pushes[i] % SIDES;
            int t = nb[d][b];
            if (has(deadM, t)) {
                continue;
            }
            long moved = (boxes & ~bit(b)) | bit(t);
            if (freezeDeadlock(t, moved)) {
                continue;
            }
            long next = packKey(moved, low(reach(b, moved)));
            int s = ~probe(next);
            if (s < 0 || !setsOK(0, moved, t, b)) {
                continue;
            }
            if (!insertAt(s, next)) {
                tableFull = true;
                return 0;
            }
            tableMove[s] = (byte)(floorIndex[b] * SIDES + d);
            if (moved == goalM || hasKey(next | PULLED)) {
                return next;
            }
            int h = heuristic(moved, 0);
            if (h != NONE) { // a deadlocked state stays in the table as visited
                pushOpen.push(s, g, g + WEIGHT * h);
            }
        }
        return 0;
    }

    static long expandPull(int slot, int g) {
        g++;
        long key = tableKey[slot] & ~PULLED;
        long boxes = keyBoxes(key);
        long area = reach(keyPlayer(key), boxes);
        for (long bb = boxes; bb != 0; bb &= bb - 1) {
            int b = low(bb);
            for (int d = 0; d < SIDES; d++) {
                // the player at x pulls the box from b to x and steps back to y
                int x = nb[OPP[d]][b];
                if (x < 0 || !has(area, x) || has(deadPullM, x)) {
                    continue;
                }
                int y = nb[OPP[d]][x];
                if (y < 0 || !has(floorM, y) || has(boxes, y)) {
                    continue;
                }
                long moved = (boxes & ~bit(b)) | bit(x);
                long next = packKey(moved, low(reach(y, moved)));
                int s = ~probe(next | PULLED);
                if (s < 0 || !setsOK(1, moved, x, y)) {
                    continue;
                }
                if (!insertAt(s, next | PULLED)) {
                    tableFull = true;
                    return 0;
                }
                tableMove[s] = (byte)(floorIndex[x] * SIDES + d);
                if (hasKey(next)) {
                    return next;
                }
                int h = heuristic(moved, 1);
                if (h != NONE) {
                    pullOpen.push(s, g, g + WEIGHT * h);
                }
            }
        }
        return 0;
    }

    // The push search from the start and the pull search from the goal take
    // turns until some state is in both.
    static long solve() {
        long root = packKey(startBoxes, low(reach(startPlayer, startBoxes)));
        tableMove[insertKey(root)] = (byte)ROOT;
        int h0 = heuristic(startBoxes, 0);
        if (h0 != NONE) {
            pushOpen.push(findKey(root), 0, WEIGHT * h0);
        }
        int hg = heuristic(goalM, 1);
        for (long rest = floorM & ~goalM;
             rest != 0;) { // the boxes on the goals, the player anywhere
            long area = reach(low(rest), goalM);
            rest &= ~area;
            long key = packKey(goalM, low(area));
            int s = insertKey(key | PULLED);
            if (s < 0) {
                continue;
            }
            tableMove[s] = (byte)ROOT;
            if (key == root) {
                return key;
            }
            if (hg != NONE) {
                pullOpen.push(s, 0, WEIGHT * hg);
            }
        }
        for (;;) {
            boolean progress = false;
            for (int i = 0; i < PUSH_ROUNDS && pushOpen.pop(); i++) {
                progress = true;
                long k = expandPush(popSlot, popG);
                if (k != 0) {
                    return k;
                }
                if (tableFull) {
                    return 0;
                }
            }
            for (int i = 0; i < PULL_ROUNDS && pullOpen.pop(); i++) {
                progress = true;
                long k = expandPull(popSlot, popG);
                if (k != 0) {
                    return k;
                }
                if (tableFull) {
                    return 0;
                }
            }
            if (!progress) {
                return 0;
            }
        }
    }

    // push distances of a lone box: dist[target][cell] to bring a box from cell
    // to the target (dir 0), or from the target to cell (dir 1)
    static int[][][] dist = new int[2][MAXCELLS][MAXCELLS];

    static long boxDistances(long targets, int dir) {
        long unreachable = floorM;
        int j = 0;
        for (long tg = targets; tg != 0; tg &= tg - 1, j++) {
            int[] dd = dist[dir][j];
            int[] queue = new int[MAXCELLS];
            int head = 0;
            int tail = 0;
            Arrays.fill(dd, INF);
            dd[low(tg)] = 0;
            queue[tail++] = low(tg);
            while (head < tail) {
                int x = queue[head++];
                unreachable &= ~bit(x);
                for (int d = 0; d < SIDES; d++) {
                    // a box pushed from y to x (the player behind y), or from x to y
                    int y = dir == 1 ? nb[d][x] : nb[OPP[d]][x];
                    int p = dir == 1 ? nb[OPP[d]][x] : (y < 0 ? NONE : nb[OPP[d]][y]);
                    if (y < 0 || p < 0 || !has(floorM, y) || !has(floorM, p) || dd[y] != INF) {
                        continue;
                    }
                    dd[y] = dd[x] + 1;
                    queue[tail++] = y;
                }
            }
        }
        return unreachable;
    }

    static String stripRight(String s) {
        int e = s.length();
        while (e > 0 && (s.charAt(e - 1) == ' ' || s.charAt(e - 1) == '\r')) {
            e--;
        }
        return s.substring(0, e);
    }

    public static void main(String[] args) throws Exception {
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        byte[] buffer = new byte[INPUT_BUFFER];
        for (int n; (n = System.in.read(buffer)) >= 0;) {
            bytes.write(buffer, 0, n);
        }
        String input = new String(bytes.toByteArray(), StandardCharsets.US_ASCII);
        String[] lines = input.split("\n");
        int first = 0;
        int last = lines.length;
        for (int i = 0; i < last; i++) {
            lines[i] = stripRight(lines[i]);
        }
        while (first < last && lines[first].isEmpty()) {
            first++;
        }
        while (last > first && lines[last - 1].isEmpty()) {
            last--;
        }
        lines = Arrays.copyOfRange(lines, first, last);
        int lead = MAXCELLS;
        for (String line : lines) {
            if (!line.isEmpty()) {
                int i = 0;
                while (line.charAt(i) == ' ') {
                    i++;
                }
                lead = Math.min(lead, i);
            }
        }
        for (int i = 0; i < lines.length; i++) {
            String line = lines[i];
            lines[i] = line.length() > lead ? line.substring(lead) : "";
        }
        rows = lines.length;
        for (String line : lines) {
            cols = Math.max(cols, line.length());
        }
        cells = rows * cols;
        long wallM = 0;
        for (int r = 0; r < rows; r++) {
            String line = lines[r];
            for (int c = 0; c < cols; c++) {
                char ch = c < line.length() ? line.charAt(c) : ' ';
                int id = r * cols + c;
                if (ch == '#') {
                    wallM |= bit(id);
                }
                if (ch == '.' || ch == '+' || ch == '*') {
                    goalM |= bit(id);
                }
                if (ch == '$' || ch == '*') {
                    startBoxes |= bit(id);
                }
                if (ch == '@' || ch == '+') {
                    startPlayer = id;
                }
            }
        }
        for (int i = 0; i < cells; i++) {
            for (int d = 0; d < SIDES; d++) {
                int r = i / cols + DR[d];
                int c = i % cols + DC[d];
                nb[d][i] = r < 0 || r >= rows || c < 0 || c >= cols ? NONE : r * cols + c;
            }
        }
        // the floor: the cells the player reaches through non-walls; boxes on
        // goals walled off from the player never move and count as walls
        floorM = ~wallM & (cells == MAXCELLS ? ~0L : bit(cells) - 1);
        floorM = reach(startPlayer, 0);
        goalM &= floorM;
        startBoxes &= floorM;
        if (startBoxes == goalM) {
            System.out.write("\n".getBytes(StandardCharsets.US_ASCII));
            return;
        }
        for (long f = floorM; f != 0; f &= f - 1) {
            floorIndex[low(f)] = floorCount;
            floorCell[floorCount++] = low(f);
        }
        goalCount = Long.bitCount(goalM);
        tableKey = new long[TABLE];
        tableMove = new byte[TABLE];
        tableNext = new int[TABLE];
        deadM = boxDistances(goalM, 0);
        deadPullM = boxDistances(startBoxes, 1);
        for (int i = 0; i <= MAXCELLS; i++) {
            for (int j = 0; j <= MOST + 1; j++) {
                binom[i][j] = j == 0 ? 1 : i == 0 ? 0 : binom[i - 1][j - 1] + binom[i - 1][j];
            }
        }
        for (int k = 2; k <= MOST && k <= goalCount; k++) {
            for (int dir = 0; dir < 2; dir++) {
                buildSetTable(dir, k);
            }
        }
        for (int dir = 0; dir < 2; dir++) {
            for (int c = 0; c < cells; c++) {
                nearest[dir][c] = INF;
                for (int j = 0; j < goalCount; j++) {
                    if (dist[dir][j][c] < INF) {
                        canReach[dir][c] |= bit(j);
                    }
                    nearest[dir][c] = Math.min(nearest[dir][c], dist[dir][j][c]);
                }
            }
        }
        String answer = "";
        if (startBoxes != goalM) {
            long meet = solve();
            if (meet != 0) {
                answer = buildAnswer(meet);
            }
        }
        System.out.write((answer + "\n").getBytes(StandardCharsets.US_ASCII));
    }
}
