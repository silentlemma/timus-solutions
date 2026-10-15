import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final long NEG = -(1L << 62);
    static final int KINDS = 3; // a count of teams: none, one, two or more
    static final int BUFFER = 1 << 16;

    // every node of the tree over f keeps its total, its count of teams
    // (capped at 2), its best prefix and suffix with exactly 0, 1 or 2+
    // teams, and its best range with at least two teams
    static int size;
    static long[] total;
    static long[] best;
    static int[] kind;
    static long[][] pre = new long[KINDS][];
    static long[][] suf = new long[KINDS][];

    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buffer = new byte[BUFFER];
    static int filled = 0;
    static int at = 0;

    static int read() throws IOException {
        if (at == filled) {
            filled = in.read(buffer, 0, BUFFER);
            at = 0;
            if (filled <= 0) {
                return -1;
            }
        }
        return buffer[at++];
    }

    static long next() throws IOException {
        int ch = read();
        while (ch != '-' && (ch < '0' || ch > '9')) {
            ch = read();
        }
        boolean negative = ch == '-';
        if (negative) {
            ch = read();
        }
        long v = 0;
        while (ch >= '0' && ch <= '9') {
            v = v * 10 + (ch - '0');
            ch = read();
        }
        return negative ? -v : v;
    }

    static void reset() {
        Arrays.fill(total, 0);
        Arrays.fill(kind, 0);
        Arrays.fill(best, NEG);
        for (int k = 0; k < KINDS; k++) {
            Arrays.fill(pre[k], k == 0 ? 0 : NEG);
            Arrays.fill(suf[k], k == 0 ? 0 : NEG);
        }
    }

    static void pull(int v) {
        int a = 2 * v;
        int b = a + 1;
        total[v] = total[a] + total[b];
        kind[v] = Math.min(kind[a] + kind[b], 2);
        for (int k = 0; k < KINDS; k++) {
            pre[k][v] = pre[k][a];
            suf[k][v] = suf[k][b];
        }
        for (int j = 0; j < KINDS; j++) {
            // prefixes: inside the left child, or all of it and more
            if (pre[j][b] != NEG) {
                int k = Math.min(kind[a] + j, 2);
                pre[k][v] = Math.max(pre[k][v], total[a] + pre[j][b]);
            }
            if (suf[j][a] != NEG) {
                int k = Math.min(kind[b] + j, 2);
                suf[k][v] = Math.max(suf[k][v], suf[j][a] + total[b]);
            }
        }
        // ranges: inside a child, or across with two or more teams
        long top = Math.max(best[a], best[b]);
        for (int i = 0; i < KINDS; i++) {
            for (int j = Math.max(0, 2 - i); j < KINDS; j++) {
                if (suf[i][a] != NEG && pre[j][b] != NEG) {
                    top = Math.max(top, suf[i][a] + pre[j][b]);
                }
            }
        }
        best[v] = top;
    }

    static void add(int fi, long s) {
        int v = size + fi;
        total[v] += s;
        kind[v] = Math.min(kind[v] + 1, 2);
        for (int k = 0; k < KINDS; k++) {
            pre[k][v] = k == kind[v] ? total[v] : NEG;
            suf[k][v] = pre[k][v];
        }
        best[v] = kind[v] == 2 ? total[v] : NEG;
        for (v /= 2; v > 0; v /= 2) {
            pull(v);
        }
    }

    static long[] distinct(long[] values) {
        long[] sorted = values.clone();
        Arrays.sort(sorted);
        int k = 0;
        for (int i = 0; i < sorted.length; i++) {
            if (i == 0 || sorted[i] != sorted[k - 1]) {
                sorted[k++] = sorted[i];
            }
        }
        return Arrays.copyOf(sorted, k);
    }

    public static void main(String[] args) throws IOException {
        int n = (int) next();
        long[] a = new long[n];
        long[] f = new long[n];
        long[] s = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = next();
            f[i] = next();
            s[i] = next();
        }
        long[] ages = distinct(a);
        long[] fs = distinct(f);
        List<List<long[]>> byAge = new ArrayList<>();
        for (int i = 0; i < ages.length; i++) {
            byAge.add(new ArrayList<>());
        }
        for (int i = 0; i < n; i++) {
            int ai = Arrays.binarySearch(ages, a[i]);
            byAge.get(ai).add(new long[] {Arrays.binarySearch(fs, f[i]), s[i]});
        }
        size = 1;
        while (size < fs.length) {
            size *= 2;
        }
        total = new long[2 * size];
        best = new long[2 * size];
        kind = new int[2 * size];
        for (int k = 0; k < KINDS; k++) {
            pre[k] = new long[2 * size];
            suf[k] = new long[2 * size];
        }
        long answer = NEG;
        int bestLeft = 0;
        int bestRight = 0;
        for (int left = 0; left < ages.length; left++) {
            reset();
            for (int right = left; right < ages.length; right++) {
                for (long[] team : byAge.get(right)) {
                    add((int) team[0], team[1]);
                }
                if (best[1] > answer) {
                    answer = best[1];
                    bestLeft = left;
                    bestRight = right;
                }
            }
        }
        // the range of f values with the largest total holding at least two
        // teams: for each right end the best left end has the least prefix
        // sum among those leaving at least two teams inside
        int nf = fs.length;
        long[] prefix = new long[nf + 1];
        int[] inside = new int[nf + 1];
        for (int r = bestLeft; r <= bestRight; r++) {
            for (long[] team : byAge.get(r)) {
                prefix[(int) team[0] + 1] += team[1];
                inside[(int) team[0] + 1]++;
            }
        }
        for (int i = 0; i < nf; i++) {
            prefix[i + 1] += prefix[i];
            inside[i + 1] += inside[i];
        }
        long top = NEG;
        long low = NEG;
        int lo = 0;
        int hi = 0;
        int lowAt = 0;
        for (int r = 1, t = 0; r <= nf; r++) {
            for (; t < r && inside[t] <= inside[r] - 2; t++) {
                if (low == NEG || prefix[t] < low) {
                    low = prefix[t];
                    lowAt = t;
                }
            }
            if (low != NEG && prefix[r] - low > top) {
                top = prefix[r] - low;
                lo = lowAt;
                hi = r - 1;
            }
        }
        System.out.println(ages[bestLeft] + " " + ages[bestRight]);
        System.out.println(fs[lo] + " " + fs[hi]);
    }
}
