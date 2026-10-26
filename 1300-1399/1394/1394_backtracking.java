import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

// Three exact searches with growing time slices and perturbed orders, tried in
// turns until one places all ships: B (rows one at a time), C (B over the
// rare lengths only), D (C with residues modulo K checked exactly).
public class Main {
    static final int MAX_SHIPS = 100;
    static final int MAX_ROWS = 10;
    static final int MAX_LEN = 100;
    static final int MAX_SUM = 10001; // fewer than 100 ships of at most 100
    // milliseconds: past the judge's limit, since a half-done placement is worthless
    static final long TIME_LIMIT = 10000;
    static final int CLOCK_EVERY = 256; // nodes between looks at the clock
    static final int WORD = 64;
    static final int WORDS = (MAX_SUM + WORD - 1) / WORD;
    static final int WORD_SHIFT = 6; // 2^6 = WORD
    static final int WORD_MASK = WORD - 1;
    static final int XS_A = 13; // xorshift32 shifts
    static final int XS_B = 17;
    static final int XS_C = 5;
    static final long GOLDEN = 0x9E3779B97F4A7C15L; // splitmix64 finalizer
    static final long MIX1 = 0xBF58476D1CE4E5B9L;
    static final long MIX2 = 0x94D049BB133111EBL;
    static final int MIX_S1 = 30;
    static final int MIX_S2 = 27;
    static final int MIX_S3 = 31;
    static final long UNSIGNED_INT = 0xffffffffL;

    static int n;
    static int m;
    static int[] ships = new int[MAX_SHIPS];
    static int[] rowLen = new int[MAX_ROWS];
    // the current ship order: lengths and input positions
    static int[] v = new int[MAX_SHIPS];
    static int[] shipId = new int[MAX_SHIPS];

    static int[] rowId = new int[MAX_ROWS];   // the input row of search row b
    static int[] placed = new int[MAX_SHIPS]; // the search row of ship i
    static long nodes;
    static long attemptEnd; // the time when the current attempt stops
    static boolean aborted;
    static long started;
    static final long SEED = 2463534242L;
    static int rngState = (int)SEED;

    static int rnd() {
        rngState ^= rngState << XS_A;
        rngState ^= rngState >>> XS_B;
        rngState ^= rngState << XS_C;
        return rngState;
    }

    static long rnd64() {
        long high = rnd() & UNSIGNED_INT;
        return high << (WORD / 2) | (rnd() & UNSIGNED_INT);
    }

    static long mix(long x) {
        x += GOLDEN;
        x = (x ^ (x >>> MIX_S1)) * MIX1;
        x = (x ^ (x >>> MIX_S2)) * MIX2;
        return x ^ (x >>> MIX_S3);
    }

    static long elapsed() { return System.currentTimeMillis() - started; }

    static boolean tick() {
        ++nodes;
        if ((nodes & (CLOCK_EVERY - 1)) == 0 && elapsed() > attemptEnd) {
            aborted = true;
            return false;
        }
        return true;
    }

    static boolean get(long[] b, int x) {
        return ((b[x >>> WORD_SHIFT] >>> (x & WORD_MASK)) & 1) != 0;
    }

    static void one(long[] b, int words) {
        Arrays.fill(b, 0, words, 0);
        b[0] = 1;
    }

    // dst = src | src << sh over the given width; src may be dst
    static void shiftOr(long[] dst, long[] src, int sh, int words) {
        int ws = sh >>> WORD_SHIFT;
        int bs = sh & WORD_MASK;
        for (int i = words - 1; i >= 0; i--) {
            long x = src[i];
            int j = i - ws;
            if (j >= 0) {
                x |= src[j] << bs;
                if (bs != 0 && j > 0) {
                    x |= src[j - 1] >>> (WORD - bs);
                }
            }
            dst[i] = x;
        }
    }

    // Failed states of the row searches, by a hash of the unused ships and the
    // open rows; they do not depend on the order, so they survive restarts.
    static final int MEMO_BITS = 20;
    static final int MEMO_SIZE = 1 << MEMO_BITS;
    static final int PROBES = 8;
    static long[] zobrist = new long[MAX_LEN + 1]; // a random key per ship length
    static long[] memo = new long[MEMO_SIZE];

    static boolean known(long k) {
        int p = (int)(k >>> (WORD - MEMO_BITS));
        for (int t = 0; t < PROBES; t++) {
            long e = memo[(p + t) & (MEMO_SIZE - 1)];
            if (e == k) {
                return true;
            }
            if (e == 0) {
                return false;
            }
        }
        return false;
    }

    static void remember(long k) {
        int p = (int)(k >>> (WORD - MEMO_BITS));
        for (int t = 0; t < PROBES; t++) {
            int at = (p + t) & (MEMO_SIZE - 1);
            if (memo[at] == 0 || memo[at] == k) {
                memo[at] = k;
                return;
            }
        }
        memo[(p + (int)(k & (PROBES - 1))) & (MEMO_SIZE - 1)] = k;
    }

    // For strategy D: ships not divisible by mod fall into classes by residue.
    // Rows b.. can only be completed if the remaining class counts split among
    // them so that each row gets its length modulo mod: a DP over (row, counts).
    static final int CHECK_BITS = 21;
    static final int CHECK_SIZE = 1 << CHECK_BITS;
    static final int CHECK_PROBES = 4;
    static final double MAX_CODES = 1e17; // the count vectors must fit in 64 bits
    static final long QUERY_BUDGET = 100000;
    static final int MAX_OVER = 5;   // queries over budget before the check gives up
    static final int ROW_RADIX = 16; // more than the rows
    static final int SLOT_SHIFT = 8;
    static final long SALT = 0x1234567L;
    static long[] checked = new long[CHECK_SIZE]; // (key with the low bit cleared) | feasible
    // Residue queries are sequential; recursive calls advance to the next row.
    static int[][] residueRest = new int[MAX_ROWS][MAX_LEN];
    static long[][] residueReach = new long[MAX_ROWS][MAX_LEN + 1];

    static class Residues {
        int mod;
        int classes;
        int[] residue = new int[MAX_LEN]; // classes by count, the largest last
        int[] count = new int[MAX_LEN];
        long[] radix = new long[MAX_LEN];
        int[] target = new int[MAX_ROWS]; // row lengths modulo mod
        long orderSalt;
        long full;
        long ops;
        long budget;
        boolean broken; // the current query is over budget: "feasible"
        int overCount;  // queries over budget in this attempt

        long rotate(long x, int s) { return s == 0 ? x : ((x << s) | (x >>> (mod - s))) & full; }

        boolean overBudget() {
            if (++ops > budget) {
                broken = true;
            }
            return broken;
        }

        // Row b takes c of class j and of the classes after it (rest: the
        // counts left, r: the residue so far, reach[j]: residues of j..).
        boolean split(int b, int[] rest, long[] reach, long code, int j, int r, long taken) {
            if (overBudget()) {
                return true;
            }
            int need = (target[b] - r + mod) % mod;
            if (((reach[j] >>> need) & 1) == 0) {
                return false;
            }
            if (j == classes) {
                return feasible(b + 1, code - taken);
            }
            if (j == classes - 1) { // the last class: its count is fixed modulo mod
                for (int c = 0; c <= rest[j] && c < mod; c++) {
                    if (c * residue[j] % mod != need) {
                        continue;
                    }
                    for (int cc = c; cc <= rest[j]; cc += mod) {
                        if (overBudget() || feasible(b + 1, code - taken - cc * radix[j]) ||
                            broken) {
                            return true;
                        }
                    }
                }
                return false;
            }
            for (int c = 0; c <= rest[j]; c++) {
                if (split(b, rest, reach, code, j + 1, (r + c * residue[j]) % mod,
                          taken + c * radix[j]) ||
                    broken) {
                    return true;
                }
            }
            return false;
        }

        boolean feasible(int b, long code) {
            if (broken) {
                return true;
            }
            int[] rest = residueRest[b];
            long c = code;
            for (int j = 0; j < classes; j++) {
                // MAX_CODES keeps every mixed-radix code within a positive long.
                rest[j] = (int)(c % (count[j] + 1));
                c /= count[j] + 1;
            }
            if (b == m - 1) {
                int r = 0;
                for (int j = 0; j < classes; j++) {
                    r = (r + rest[j] * residue[j]) % mod;
                }
                return r == target[b];
            }
            long key = mix(orderSalt ^ mix(code * ROW_RADIX + b)) & ~1L;
            int p = (int)(key >>> (WORD - CHECK_BITS));
            for (int t = 0; t < CHECK_PROBES; t++) {
                long e = checked[(p + t) & (CHECK_SIZE - 1)];
                if ((e & ~1L) == key) {
                    return (e & 1) != 0;
                }
            }
            long[] reach = residueReach[b];
            Arrays.fill(reach, 0, classes, 0);
            reach[classes] = 1;
            for (int j = classes - 1; j >= 0; j--) {
                for (int t = 0; t <= rest[j] && t < mod; t++) {
                    reach[j] |= rotate(reach[j + 1], t * residue[j] % mod);
                }
                ops += Math.min(rest[j], mod) + 1;
            }
            if (ops > budget) {
                broken = true;
                return true;
            }
            boolean ok = split(b, rest, reach, code, 0, 0, 0);
            if (broken) {
                return true;
            }
            int q = (int)((p + ((key >>> SLOT_SHIFT) & (CHECK_PROBES - 1))) & (CHECK_SIZE - 1));
            for (int t = 0; t < CHECK_PROBES; t++) {
                if (checked[(p + t) & (CHECK_SIZE - 1)] == 0) {
                    q = (p + t) & (CHECK_SIZE - 1);
                    break;
                }
            }
            checked[q] = key | (ok ? 1 : 0);
            return ok;
        }

        // the classes for modulus k; false if the count vectors do not fit in 64 bits
        boolean init(int k) {
            int[] perResidue = new int[MAX_LEN];
            for (int i = 0; i < n; i++) {
                if (ships[i] % k != 0) {
                    perResidue[ships[i] % k]++;
                }
            }
            mod = k;
            classes = 0;
            full = (1L << k) - 1;
            int[] order = new int[MAX_LEN];
            long[] key = new long[MAX_LEN];
            int classCount = 0;
            for (int r = 1; r < k; r++) {
                if (perResidue[r] > 0) {
                    order[classCount++] = r;
                    key[r] = perResidue[r];
                }
            }
            sortByKey(order, classCount, key);
            double total = 1;
            long scale = 1;
            for (int j = 0; j < classCount; j++) {
                int value = order[j];
                residue[classes] = value;
                count[classes] = perResidue[value];
                radix[classes++] = scale;
                total *= perResidue[value] + 1;
                if (total > MAX_CODES) {
                    return false;
                }
                scale *= perResidue[value] + 1;
            }
            return true;
        }

        long fullCode() {
            long c = 0;
            for (int j = 0; j < classes; j++) {
                c += count[j] * radix[j];
            }
            return c;
        }

        // a query from a search: limited effort, "feasible" when it runs out
        boolean query(int b, long code) {
            if (overCount > MAX_OVER || elapsed() > attemptEnd) {
                return true;
            }
            ops = 0;
            broken = false;
            boolean ok = feasible(b, code);
            if (broken) {
                overCount++;
            }
            return ok;
        }

        // a new attempt with these row lengths, in search order
        void setRows(int[] len) {
            orderSalt = mix(SALT + mod);
            for (int b = 0; b < m; b++) {
                target[b] = len[b] % mod;
                orderSalt = mix(orderSalt ^ len[b]);
            }
            overCount = 0;
            budget = QUERY_BUDGET;
        }
    }

    // Strategies B, C, D: rows are filled one at a time; inside a row each ship
    // is taken or skipped (equal ships skipped together). Ships kept..n-1 are
    // deferred: a row only needs a remainder they make, and sub places them last.
    static final int MAX_CHECKS = 13;
    static final long ROW_SALT = 0x51ED27L;
    static final long REMAINDER_SALT = 0xC0FFEEL;
    static final long TAG_SALT = 0x7A6L;

    static class RowSearch {
        int n;
        int m;
        int kept;
        int[] v = new int[MAX_SHIPS];
        int[] len = new int[MAX_ROWS];
        int[] where = new int[MAX_SHIPS];
        int[] remainder = new int[MAX_ROWS];
        boolean[] used = new boolean[MAX_SHIPS];
        long tag; // which lengths are deferred (0: none)
        long shipsHash;
        long remainderHash;
        int words;
        long[][][] sums =
            new long[MAX_ROWS][MAX_SHIPS + 1][]; // per row: sums of unused ships pos..
        long[] deferredSums = new long[WORDS];
        RowSearch sub;
        int checks; // residue checks: valid since closed rows are complete modulo each
        Residues[] check = new Residues[MAX_CHECKS];
        int[][] cls =
            new int[MAX_CHECKS][MAX_SHIPS]; // the class of ship i in check t, -1 if divisible
        long[] code = new long[MAX_CHECKS]; // mixed-radix codes of the unused class counts

        void take(int pos, int sign) {
            for (int t = 0; t < checks; t++) {
                if (cls[t][pos] >= 0) {
                    code[t] += sign * check[t].radix[cls[t][pos]];
                }
            }
        }

        boolean placeDeferred() {
            RowSearch s = sub;
            s.n = n - kept;
            s.kept = s.n;
            s.m = m;
            s.checks = 0;
            System.arraycopy(v, kept, s.v, 0, s.n);
            System.arraycopy(remainder, 0, s.len, 0, m);
            if (!s.run(0)) {
                return false;
            }
            System.arraycopy(s.where, 0, where, kept, s.n);
            return true;
        }

        boolean fill(int b, int pos, int r) {
            long[][] s = sums[b];
            for (;;) { // each turn takes ship pos, or skips it and its copies
                if (!tick()) {
                    return false;
                }
                while (pos < kept && used[pos]) {
                    pos++;
                }
                if (r == 0 || pos >= kept) { // row b is done; the rest comes from deferred ships
                    if (r > 0 && (kept == n || !get(deferredSums, r))) {
                        return false;
                    }
                    remainder[b] = r;
                    long add = kept < n ? mix(r) : 0;
                    remainderHash += add;
                    boolean ok = open(b + 1);
                    remainderHash -= add;
                    return ok;
                }
                int x = v[pos];
                if (x <= r && get(s[pos + 1], r - x)) {
                    used[pos] = true;
                    where[pos] = b;
                    shipsHash -= zobrist[x];
                    take(pos, -1);
                    if (fill(b, pos + 1, r - x)) {
                        return true;
                    }
                    used[pos] = false;
                    shipsHash += zobrist[x];
                    take(pos, 1);
                    if (aborted) {
                        return false;
                    }
                }
                int q = pos + 1;
                while (q < kept && v[q] == x) {
                    q++;
                }
                if (!get(s[q], r)) {
                    return false;
                }
                pos = q;
            }
        }

        boolean open(int b) {
            if (b == m) {
                return placeDeferred();
            }
            if (b == m - 1) { // the last row takes all the ships left
                int s = 0;
                for (int i = 0; i < kept; i++) {
                    if (!used[i]) {
                        s += v[i];
                        where[i] = b;
                    }
                }
                if (kept == n) {
                    return true;
                }
                int r = len[b] - s;
                if (r < 0 || !get(deferredSums, r)) {
                    return false;
                }
                remainder[b] = r;
                return placeDeferred();
            }
            long rowsHash = tag;
            for (int c = b; c < m; c++) {
                rowsHash += mix(len[c] + ROW_SALT);
            }
            long key = (mix(shipsHash ^ mix(rowsHash)) + mix(remainderHash ^ REMAINDER_SALT)) | 1;
            if (known(key)) {
                return false;
            }
            for (int t = 0; t < checks; t++) {
                if (!check[t].query(b, code[t])) {
                    remember(key);
                    return false;
                }
            }
            long[][] s = sums[b];
            if (kept == n) {
                one(s[kept], words);
            } else {
                System.arraycopy(deferredSums, 0, s[kept], 0, words);
            }
            for (int i = kept - 1; i >= 0; i--) {
                if (used[i]) {
                    System.arraycopy(s[i + 1], 0, s[i], 0, words);
                } else {
                    shiftOr(s[i], s[i + 1], v[i], words);
                }
            }
            for (int c = b; c < m; c++) {
                if (!get(s[0], len[c])) {
                    remember(key);
                    return false;
                }
            }
            boolean ok = fill(b, 0, len[b]);
            if (!ok && !aborted) {
                remember(key);
            }
            return ok;
        }

        boolean run(long t) {
            tag = t;
            int longest = 0;
            for (int b = 0; b < m; b++) {
                longest = Math.max(longest, len[b]);
            }
            words = longest / WORD + 1;
            for (long[][] row : sums) {
                for (int i = 0; i < row.length; i++) {
                    if (row[i] == null || row[i].length < words) {
                        row[i] = new long[words];
                    }
                }
            }
            shipsHash = 0;
            remainderHash = 0;
            for (int i = 0; i < checks; i++) {
                code[i] = check[i].fullCode();
            }
            Arrays.fill(used, 0, n, false);
            for (int i = 0; i < kept; i++) {
                shipsHash += zobrist[v[i]];
            }
            if (kept < n) {
                one(deferredSums, words);
                for (int i = kept; i < n; i++) {
                    shiftOr(deferredSums, deferredSums, v[i], words);
                }
            }
            return open(0);
        }
    }

    static RowSearch mainSearch = new RowSearch();
    static RowSearch subSearch = new RowSearch();
    static Residues[] residuePool = new Residues[MAX_CHECKS];

    static boolean runRows(int kept, Residues[] checks, int checkCount) {
        RowSearch s = mainSearch;
        s.n = n;
        s.m = m;
        s.kept = kept;
        s.sub = subSearch;
        s.checks = checkCount;
        System.arraycopy(v, 0, s.v, 0, n);
        for (int b = 0; b < m; b++) {
            s.len[b] = rowLen[rowId[b]];
        }
        for (int t = 0; t < checkCount; t++) {
            Residues r = checks[t];
            s.check[t] = r;
            int[] classOf = new int[MAX_LEN];
            classOf[0] = -1;
            for (int j = 0; j < r.classes; j++) {
                classOf[r.residue[j]] = j;
            }
            for (int i = 0; i < n; i++) {
                s.cls[t][i] = classOf[v[i] % r.mod];
            }
            r.setRows(s.len);
        }
        long tag = 0;
        if (kept < n) {
            boolean[] rare = new boolean[MAX_LEN + 1];
            for (int i = 0; i < kept; i++) {
                rare[v[i]] = true;
            }
            tag = TAG_SALT;
            for (int x = 1; x <= MAX_LEN; x++) {
                if (rare[x]) {
                    tag = mix(tag ^ x);
                }
            }
        }
        if (!s.run(tag)) {
            return false;
        }
        System.arraycopy(s.where, 0, placed, 0, n);
        return true;
    }

    static final int MOD_MIN = 2; // moduli for D
    static final int MOD_MAX = 50;
    static final int SMALL_MOD_MAX = 6; // B also checks moduli up to this
    static final int TOP_MODS = 4;
    static final int SCORE_SCALE = 100;
    static final int SLOTS = 5; // B, B with rows ascending, C, D, B again
    static final int SHARE = 4; // a modulus must divide a quarter of the ships
    static final int STRATEGY_B = 0;
    static final int STRATEGY_C = 1;
    static final int STRATEGY_D = 2;
    // B gets three slots: the hardest inputs need its row-by-row search.
    static final int[] SLOT_STRATEGY = {STRATEGY_B, STRATEGY_B, STRATEGY_C, STRATEGY_D, STRATEGY_B};
    static final int RARE_LEVELS = 3;  // C: "rare" means at most 1..3 copies
    static final int KEY_SCALE = 1000; // ship order keys
    static final int MAX_NOISE = 30;
    static final long RARE_FIRST = 1000000000L;
    static final double FIRST_SLICE = 3; // milliseconds
    static final double SLICE_GROWTH = 1.6;
    static final int MAX_GROWTH = 20;

    static boolean contains(int[] values, int size, int value) {
        for (int i = 0; i < size; i++) {
            if (values[i] == value) {
                return true;
            }
        }
        return false;
    }

    static void sortByKey(int[] order, int size, long[] key) {
        for (int i = 1; i < size; i++) {
            int value = order[i];
            int j = i;
            while (j > 0 && key[order[j - 1]] > key[value]) {
                order[j] = order[j - 1];
                j--;
            }
            order[j] = value;
        }
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        in.nextToken();
        m = (int)in.nval;
        for (int i = 0; i < n; i++) {
            in.nextToken();
            ships[i] = (int)in.nval;
        }
        for (int j = 0; j < m; j++) {
            in.nextToken();
            rowLen[j] = (int)in.nval;
        }
        started = System.currentTimeMillis();
        int[] copies = new int[MAX_LEN + 1];
        for (int i = 0; i < n; i++) {
            copies[ships[i]]++;
        }
        for (int x = 0; x <= MAX_LEN; x++) {
            zobrist[x] = rnd64();
        }
        boolean sane = true;
        for (int j = 0; j < m; j++) {
            sane &= rowLen[j] > 0 && rowLen[j] < MAX_SUM;
        }

        // moduli for D from two rankings: many multiples of a large k, and the
        // fewest non-multiples (say all ships even but one odd ship per row)
        int[] byScore = new int[MOD_MAX];
        int[] byFew = new int[MOD_MAX];
        long[] scoreKey = new long[MOD_MAX + 1];
        long[] fewKey = new long[MOD_MAX + 1];
        int rankedCount = 0;
        for (int k = MOD_MIN; k <= MOD_MAX; k++) {
            int divisible = 0;
            for (int i = 0; i < n; i++) {
                if (ships[i] % k == 0) {
                    divisible++;
                }
            }
            if (divisible < n && divisible >= Math.max(MOD_MIN, n / SHARE)) {
                byScore[rankedCount] = k;
                byFew[rankedCount++] = k;
                scoreKey[k] = -(long)divisible * k;
                fewKey[k] = (long)(n - divisible) * SCORE_SCALE - k;
            }
        }
        sortByKey(byScore, rankedCount, scoreKey);
        sortByKey(byFew, rankedCount, fewKey);
        int[] mods = new int[MAX_CHECKS];
        int dCount = 0;
        for (int c = 0; c < TOP_MODS && c < rankedCount; c++) {
            if (!contains(mods, dCount, byScore[c])) {
                mods[dCount++] = byScore[c];
            }
            if (!contains(mods, dCount, byFew[c])) {
                mods[dCount++] = byFew[c];
            }
        }
        // D's moduli, plus small ones that B checks with them.
        Residues[] dChecks = new Residues[dCount];
        Residues[] bChecks = new Residues[MAX_CHECKS];
        int bCount = 0;
        int modCount = dCount;
        for (int k = MOD_MIN; k <= SMALL_MOD_MAX; k++) {
            if (!contains(mods, modCount, k)) {
                mods[modCount++] = k;
            }
        }
        for (int c = 0; c < modCount; c++) {
            Residues r = new Residues();
            boolean ok = r.init(mods[c]) && r.classes > 0;
            if (c < dCount) {
                dChecks[c] = ok ? r : null;
            }
            if (ok) {
                residuePool[bCount] = r;
                bChecks[bCount++] = r;
            }
        }

        long[] key = new long[n];
        int[] order = new int[n];
        long[] rowKey = new long[m];
        boolean solved = false;
        for (int attempt = 0; sane && !solved; attempt++) {
            int slot = attempt % SLOTS;
            int round = attempt / SLOTS;
            int strategy = SLOT_STRATEGY[slot];
            boolean rowsUp = slot == 1;
            int rareLevel = 1 + round % RARE_LEVELS;
            int ci = dCount == 0 ? -1 : round % dCount;
            int bigK = ci < 0 ? 0 : mods[ci];
            boolean[] rare = new boolean[MAX_LEN + 1];
            for (int x = 1; x <= MAX_LEN; x++) {
                rare[x] = strategy == STRATEGY_C
                              ? copies[x] <= rareLevel
                              : strategy == STRATEGY_D && bigK != 0 && x % bigK != 0;
            }
            if (strategy == STRATEGY_D && bigK == 0) {
                strategy = STRATEGY_B;
            }
            int kept = 0;
            for (int i = 0; i < n; i++) {
                if (rare[ships[i]]) {
                    kept++;
                }
            }
            if ((strategy == STRATEGY_C || strategy == STRATEGY_D) && (kept == 0 || kept == n)) {
                strategy = STRATEGY_B;
            }

            // ship order: B longest first, C and D rare lengths first,
            // later rounds add noise, equal lengths stay together
            long[] lengthKey = new long[MAX_LEN + 1];
            for (int x = 1; x <= MAX_LEN; x++) {
                lengthKey[x] = (long)x * KEY_SCALE;
                if (round > 0) {
                    lengthKey[x] += Long.remainderUnsigned(
                        rnd() & UNSIGNED_INT, KEY_SCALE * Math.min(MAX_NOISE, round + 1));
                }
                if ((strategy == STRATEGY_C || strategy == STRATEGY_D) && rare[x]) {
                    lengthKey[x] += RARE_FIRST;
                }
            }
            for (int i = 0; i < n; i++) {
                order[i] = i;
                key[i] = -lengthKey[ships[i]] * (MAX_LEN + 1) - ships[i];
            }
            sortByKey(order, n, key);
            for (int i = 0; i < n; i++) {
                shipId[i] = order[i];
                v[i] = ships[order[i]];
            }
            // rows: longest first in round 0, then random; shortest first for the
            // second B slot and for D in even rounds (the last row absorbs the rest)
            boolean ascending = rowsUp || (strategy == STRATEGY_D && round % 2 == 0);
            for (int j = 0; j < m; j++) {
                rowId[j] = j;
                rowKey[j] = ascending ? rowLen[j] : -rowLen[j];
            }
            if (ascending || round == 0) {
                sortByKey(rowId, m, rowKey);
            } else {
                for (int j = m - 1; j > 0; j--) {
                    int k = (int)Long.remainderUnsigned(rnd() & UNSIGNED_INT, j + 1);
                    int temporary = rowId[j];
                    rowId[j] = rowId[k];
                    rowId[k] = temporary;
                }
            }

            nodes = 0;
            aborted = false;
            attemptEnd =
                Math.min(TIME_LIMIT,
                         elapsed() + (long)(FIRST_SLICE *
                                            Math.pow(SLICE_GROWTH, Math.min(round, MAX_GROWTH))));
            if (strategy == STRATEGY_B) {
                solved = runRows(n, bChecks, (round + slot) % 2 == 0 ? bCount : 0);
            } else if (strategy == STRATEGY_C) {
                solved = runRows(kept, null, 0);
            } else {
                solved = runRows(kept, new Residues[] {dChecks[ci]}, dChecks[ci] != null ? 1 : 0);
            }
            if (!solved && elapsed() > TIME_LIMIT) {
                break;
            }
        }

        int[][] rows = new int[m][n];
        int[] rowCount = new int[m];
        for (int i = 0; i < n; i++) {
            int row = rowId[placed[i]];
            rows[row][rowCount[row]++] = ships[shipId[i]];
        }
        StringBuilder out = new StringBuilder();
        for (int row = 0; row < m; row++) {
            out.append(rowCount[row]).append('\n');
            for (int k = 0; k < rowCount[row]; k++) {
                out.append(k > 0 ? " " : "").append(rows[row][k]);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
