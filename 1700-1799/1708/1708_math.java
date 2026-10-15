import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

public class Main {
    static final int LONGEST = 15; // no minimal forbidden multiset is longer for bases up to 36
    static final int SHIFT = 6; // bits per digit in a word code
    static final long DIGIT_MASK = (1 << SHIFT) - 1;
    static final int LOW_BITS = 64; // a word keeps its low 64 bits apart
    static final int LENGTH_AT = 28; // the length sits above the 26 high bits of the word
    static final long HIGH_MASK = (1L << LENGTH_AT) - 1;
    static final int STAR = 15; // a pattern count meaning "any number of this digit"
    static final int FIELD = 4; // bits per count in a packed vector
    static final int FIELDS = 16; // counts per 64-bit word
    static final int WORDS = 3;
    static final long COUNT_MASK = (1 << FIELD) - 1;
    static final long MIX_1 = 0x9e3779b97f4a7c15L;
    static final long MIX_2 = 0xbf58476d1ce4e5b9L;
    static final long MIX_3 = 0x94d049bb133111ebL;
    static final int MIX_SHIFT_1 = 30;
    static final int MIX_SHIFT_2 = 27;
    static final int MIX_SHIFT_3 = 31;
    // the hash table is kept at most three quarters full, to save memory
    static final int LOAD_NUM = 3;
    static final int LOAD_DEN = 4;
    static final int KEY_AT = 32; // a table slot keeps the key above the index
    static final long INDEX_MASK = (1L << KEY_AT) - 1;
    // about 0.43 base^4 least words exist, and the arrays grow if needed
    static final int ESTIMATE_NUM = 43;
    static final int ESTIMATE_DEN = 100;
    static final String DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    static long mix(long x) {
        x += MIX_1;
        x = (x ^ (x >>> MIX_SHIFT_1)) * MIX_2;
        x = (x ^ (x >>> MIX_SHIFT_2)) * MIX_3;
        return x ^ (x >>> MIX_SHIFT_3);
    }

    // open addressing from a pair key to the index of its least word: a slot
    // holds (key + 1) << KEY_AT | index, and 0 marks an empty one
    static long[] slots;
    static int bits = 1;
    static int used = 0;

    static int slot(int key) {
        int mask = slots.length - 1;
        int pos = (int) ((key * MIX_1) >>> (LOW_BITS - bits));
        while (slots[pos] != 0 && (slots[pos] >>> KEY_AT) != key + 1L) {
            pos = (pos + 1) & mask;
        }
        return pos;
    }

    static int get(int key) {
        long s = slots[slot(key)];
        return s == 0 ? -1 : (int) (s & INDEX_MASK);
    }

    static void put(int key, int value) {
        if ((long) (used + 1) * LOAD_DEN > (long) slots.length * LOAD_NUM) {
            long[] old = slots;
            bits++;
            slots = new long[old.length * 2];
            for (long s : old) {
                if (s != 0) {
                    slots[slot((int) (s >>> KEY_AT) - 1)] = s;
                }
            }
        }
        slots[slot(key)] = (key + 1L) << KEY_AT | value;
        used++;
    }

    // the least words: length and sorted digits, SHIFT bits each, split into
    // a high part (with the length on top) and a low part, so that comparing
    // (high, low) compares length first; and the key of the pair
    static int[] highs;
    static long[] lows;
    static int[] keys;
    static int count = 0;

    static void addLeast(int high, long low, int key) {
        if (count == keys.length) {
            highs = Arrays.copyOf(highs, count * 2);
            lows = Arrays.copyOf(lows, count * 2);
            keys = Arrays.copyOf(keys, count * 2);
        }
        highs[count] = high;
        lows[count] = low;
        keys[count] = key;
        count++;
    }

    static boolean less(int h1, long l1, int h2, long l2) {
        int c = Integer.compareUnsigned(h1, h2);
        return c < 0 || c == 0 && Long.compareUnsigned(l1, l2) < 0;
    }

    // counts of the digits 1 .. m, FIELD bits each, with the set of nonzero
    // counts and their total
    static final class Counts {
        long[] w = new long[WORDS];
        long mask;
        int sum;

        Counts copy() {
            Counts c = new Counts();
            c.w = w.clone();
            c.mask = mask;
            c.sum = sum;
            return c;
        }

        int get(int i) {
            return (int) ((w[i / FIELDS] >>> (i % FIELDS * FIELD)) & COUNT_MASK);
        }

        void put(int i, int c) {
            int at = i % FIELDS * FIELD;
            sum += c - get(i);
            w[i / FIELDS] = (w[i / FIELDS] & ~(COUNT_MASK << at)) | (long) c << at;
            mask = c != 0 ? mask | 1L << i : mask & ~(1L << i);
        }

        Counts without(int i) {
            Counts c = copy();
            c.put(i, 0);
            return c;
        }
    }

    // whether every count of g is at most that of f
    static boolean below(Counts g, Counts f) {
        for (long rest = g.mask; rest != 0; rest &= rest - 1) {
            int i = Long.numberOfTrailingZeros(rest);
            if (g.get(i) > f.get(i)) {
                return false;
            }
        }
        return true;
    }

    // vectors sorted by their sets of nonzero counts, to find quickly whether
    // one of them lies below a given vector
    static final class Index {
        final List<Counts> items;
        final long[] supports; // the distinct sets, increasing
        final int[] begin; // items of supports[s] are begin[s] .. begin[s + 1] - 1

        Index(List<Counts> vectors) {
            items = vectors;
            items.sort((a, b) -> Long.compare(a.mask, b.mask));
            int distinct = 0;
            for (int i = 0; i < items.size(); i++) {
                if (i == 0 || items.get(i).mask != items.get(i - 1).mask) {
                    distinct++;
                }
            }
            supports = new long[distinct];
            begin = new int[distinct + 1];
            int s = 0;
            for (int i = 0; i < items.size(); i++) {
                if (i == 0 || items.get(i).mask != items.get(i - 1).mask) {
                    supports[s] = items.get(i).mask;
                    begin[s++] = i;
                }
            }
            begin[distinct] = items.size();
        }

        boolean inGroup(int s, Counts f) {
            for (int j = begin[s]; j < begin[s + 1]; j++) {
                if (below(items.get(j), f)) {
                    return true;
                }
            }
            return false;
        }

        // whether some item lies below f: by the subsets of its support or by
        // a scan of the supports, whichever is shorter
        boolean covers(Counts f) {
            if ((1L << Long.bitCount(f.mask)) < supports.length) {
                for (long sub = f.mask;; sub = (sub - 1) & f.mask) {
                    int s = Arrays.binarySearch(supports, sub);
                    if (s >= 0 && inGroup(s, f)) {
                        return true;
                    }
                    if (sub == 0) {
                        return false;
                    }
                }
            }
            for (int s = 0; s < supports.length; s++) {
                if ((supports[s] & ~f.mask) == 0 && inGroup(s, f)) {
                    return true;
                }
            }
            return false;
        }
    }

    static final Comparator<Counts> BY_TOTAL = (a, b) -> {
        if (a.sum != b.sum) {
            return Integer.compare(a.sum, b.sum);
        }
        for (int k = 0; k < WORDS; k++) {
            if (a.w[k] != b.w[k]) {
                return Long.compareUnsigned(a.w[k], b.w[k]);
            }
        }
        return 0;
    };

    // the minimal vectors: one that lies below another has a smaller total,
    // so the vectors are taken by total, and those of one total are checked
    // against the smaller ones only
    static List<Counts> minimal(List<Counts> vectors) {
        vectors.sort(BY_TOTAL);
        List<Counts> kept = new ArrayList<>();
        Index smaller = new Index(new ArrayList<>());
        for (int i = 0; i < vectors.size();) {
            int j = i;
            boolean grown = false;
            for (; j < vectors.size() && vectors.get(j).sum == vectors.get(i).sum; j++) {
                boolean repeat = j > i && BY_TOTAL.compare(vectors.get(j), vectors.get(j - 1)) == 0;
                if (!repeat && !smaller.covers(vectors.get(j))) {
                    kept.add(vectors.get(j));
                    grown = true;
                }
            }
            if (grown && j < vectors.size()) {
                smaller = new Index(new ArrayList<>(kept));
            }
            i = j;
        }
        return kept;
    }

    // patterns over the first n digits, a trie of (parent, count) nodes with
    // node 0 the empty pattern, where the patterns of one solved set are a few
    // runs of consecutive nodes, each node being (parent << FIELD) | count
    static int[] nodes = new int[1 << FIELDS];
    static int nodeCount = 1;
    static int[] stars;
    static HashMap<Long, Integer> memo = new HashMap<>();
    static int[] runStart = new int[1 << FIELDS];
    static int[] runCount = new int[1 << FIELDS];
    static int runTotal = 0;
    // the runs of result i are firstRun[i] .. firstRun[i + 1] - 1
    static int[] firstRun = new int[1 << FIELDS];
    static int results = 0;

    static int extend(int parent, int count) {
        if (nodeCount == nodes.length) {
            nodes = Arrays.copyOf(nodes, nodeCount * 2);
        }
        nodes[nodeCount] = parent << FIELD | count;
        return nodeCount++;
    }

    static void addRun(int start, int count) {
        if (runTotal == runStart.length) {
            runStart = Arrays.copyOf(runStart, runTotal * 2);
            runCount = Arrays.copyOf(runCount, runTotal * 2);
        }
        runStart[runTotal] = start;
        runCount[runTotal++] = count;
    }

    static Counts decode(int node, int n) {
        Counts p = new Counts();
        for (int i = n - 1; i >= 0; i--) {
            long c = nodes[node] & COUNT_MASK;
            p.w[i / FIELDS] |= c << (i % FIELDS * FIELD);
            if (c != 0) {
                p.mask |= 1L << i;
            }
            node = nodes[node] >>> FIELD;
        }
        return p;
    }

    // the index of the result: patterns covering exactly the count vectors
    // over the first n digits above none of gens (minimal vectors); the last
    // digit takes each fixed count below the largest in gens, then any count
    static int solve(List<Counts> gens, int n) {
        long key = mix(n) + gens.size();
        for (Counts g : gens) {
            key += mix(g.w[0]) ^ mix(g.w[1] + MIX_1) * MIX_3 ^ mix(g.w[2] + MIX_2);
        }
        Integer found = memo.get(key);
        if (found != null) {
            return found;
        }
        List<int[]> result = new ArrayList<>();
        if (gens.isEmpty()) {
            result.add(new int[] {stars[n], 1});
        } else if (gens.get(0).mask != 0) {
            int last = n - 1;
            int top = 0;
            for (Counts g : gens) {
                top = Math.max(top, g.get(last));
            }
            // levels[k]: the minimal gens that apply with k copies of the last
            // digit; as gens are minimal, a newcomer with k copies never lies
            // above an earlier one, and the last level serves any count
            List<List<Counts>> levels = new ArrayList<>();
            for (int k = 0; k <= top; k++) {
                List<Counts> fresh = new ArrayList<>();
                for (Counts g : gens) {
                    if (g.get(last) == k) {
                        fresh.add(g.without(last));
                    }
                }
                List<Counts> level = new ArrayList<>();
                if (k > 0) {
                    Index newcomers = new Index(new ArrayList<>(fresh));
                    for (Counts f : levels.get(k - 1)) {
                        if (!newcomers.covers(f)) {
                            level.add(f);
                        }
                    }
                }
                level.addAll(fresh);
                levels.add(level);
            }
            Index open = new Index(levels.get(top));
            for (int k = 0; k <= top; k++) {
                int sub = solve(k < top ? levels.get(k) : open.items, last);
                int start = nodeCount;
                for (int r = firstRun[sub]; r < firstRun[sub + 1]; r++) {
                    for (int node = runStart[r]; node < runStart[r] + runCount[r]; node++) {
                        // a prefix allowed with any count is already covered below
                        if (k == top || open.covers(decode(node, last))) {
                            extend(node, k < top ? k : STAR);
                        }
                    }
                }
                result.add(new int[] {start, nodeCount - start});
            }
        }
        for (int[] run : result) {
            addRun(run[0], run[1]);
        }
        if (results + 2 > firstRun.length) {
            firstRun = Arrays.copyOf(firstRun, firstRun.length * 2);
        }
        firstRun[++results] = runTotal;
        memo.put(key, results - 1);
        return results - 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int base = Integer.parseInt(in.readLine().trim());
        int m = base - 1;
        // the least number of every pair (sum of digits, sum of squares) with at
        // most LONGEST digits: digits are appended in increasing order, and adding
        // the same digits to two words keeps their order, so the best suffices
        int width = LONGEST * m * m + 1;
        int estimate = base * base * base * base * ESTIMATE_NUM / ESTIMATE_DEN + 1;
        while ((long) (1 << bits) * LOAD_NUM < (long) estimate * LOAD_DEN) {
            bits++;
        }
        slots = new long[1 << bits];
        highs = new int[estimate];
        lows = new long[estimate];
        keys = new int[estimate];
        addLeast(0, 0, 0);
        put(0, 0);
        for (int d = 1; d < base; d++) {
            int step = d * width + d * d;
            int before = count;
            for (int i = 0; i < before; i++) {
                int key = keys[i];
                int length = highs[i] >>> LENGTH_AT;
                long hi = highs[i] & HIGH_MASK;
                long lo = lows[i];
                for (int grown = length + 1; grown <= LONGEST; grown++) {
                    key += step;
                    hi = hi << SHIFT | lo >>> (LOW_BITS - SHIFT);
                    lo = lo << SHIFT | d;
                    int high = grown << LENGTH_AT | (int) hi;
                    int at = get(key);
                    if (at < 0) {
                        put(key, count);
                        addLeast(high, lo, key);
                    } else if (less(high, lo, highs[at], lows[at])) {
                        highs[at] = high;
                        lows[at] = lo;
                    }
                }
            }
        }
        // a minimal forbidden multiset is not the least of its pair, while
        // every multiset with one digit fewer is; without its largest digit it
        // is one of the least words, so each least word is grown at its end
        List<Counts> forbidden = new ArrayList<>();
        int[] digits = new int[LONGEST];
        for (int r = 0; r < count; r++) {
            int length = highs[r] >>> LENGTH_AT;
            if (length == 0 || length >= LONGEST) {
                continue;
            }
            long hi = highs[r] & HIGH_MASK;
            long lo = lows[r];
            for (int i = length - 1; i >= 0; i--) {
                digits[i] = (int) (lo & DIGIT_MASK);
                lo = lo >>> SHIFT | (hi & DIGIT_MASK) << (LOW_BITS - SHIFT);
                hi >>>= SHIFT;
            }
            hi = highs[r] & HIGH_MASK;
            lo = lows[r];
            for (int add = digits[length - 1]; add < base; add++) {
                int key = keys[r] + add * width + add * add;
                int at = get(key);
                long gh = hi << SHIFT | lo >>> (LOW_BITS - SHIFT);
                long gl = lo << SHIFT | add;
                if (highs[at] == ((length + 1) << LENGTH_AT | (int) gh) && lows[at] == gl) {
                    continue;
                }
                boolean isMinimal = true;
                for (int i = 0; i < length && isMinimal; i++) {
                    int drop = digits[i];
                    if (drop == add || i > 0 && digits[i - 1] == drop) {
                        continue;
                    }
                    long rh = 0;
                    long rl = 0;
                    for (int j = 0; j <= length; j++) {
                        if (j != i) {
                            int digit = j < length ? digits[j] : add;
                            rh = rh << SHIFT | rl >>> (LOW_BITS - SHIFT);
                            rl = rl << SHIFT | digit;
                        }
                    }
                    int shorter = get(key - drop * width - drop * drop);
                    isMinimal = highs[shorter] == (length << LENGTH_AT | (int) rh)
                            && lows[shorter] == rl;
                }
                if (isMinimal) {
                    Counts f = new Counts();
                    for (int i = 0; i < length; i++) {
                        f.put(digits[i] - 1, f.get(digits[i] - 1) + 1);
                    }
                    f.put(add - 1, f.get(add - 1) + 1);
                    forbidden.add(f);
                }
            }
        }
        slots = null;
        highs = null;
        lows = null;
        keys = null;
        stars = new int[m + 1];
        for (int i = 1; i <= m; i++) {
            stars[i] = extend(stars[i - 1], STAR);
        }
        int top = solve(minimal(forbidden), m);
        List<String> lines = new ArrayList<>();
        for (int r = firstRun[top]; r < firstRun[top + 1]; r++) {
            for (int node = runStart[r]; node < runStart[r] + runCount[r]; node++) {
                Counts p = decode(node, m);
                StringBuilder line = new StringBuilder();
                for (int i = 0; i < m; i++) {
                    char ch = DIGITS.charAt(i + 1);
                    int c = p.get(i);
                    if (c == STAR) {
                        line.append(ch).append('*');
                    } else {
                        for (int k = 0; k < c; k++) {
                            line.append(ch);
                        }
                    }
                }
                lines.add(line.toString());
            }
        }
        Collections.sort(lines);
        PrintWriter out = new PrintWriter(System.out);
        for (String line : lines) {
            out.println(line);
        }
        out.flush();
    }
}
