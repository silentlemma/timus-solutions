import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int MOD = 3, SHIFT = 32;
    static final long LOW = (1L << SHIFT) - 1;

    // vectors over GF(3) are packed as (mask of 1s) << 32 | (mask of 2s)
    static long add(long a, long b) {
        long a1 = a >>> SHIFT, a2 = a & LOW, b1 = b >>> SHIFT, b2 = b & LOW;
        long t = (a1 | b2) ^ (a2 | b1);
        return ((a2 | b2) ^ t) << SHIFT | ((a1 | b1) ^ t);
    }

    static long negate(long a) {
        return (a & LOW) << SHIFT | a >>> SHIFT;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt(), n = in.nextInt();
        int[][] m = new int[n][k];
        int[] target = new int[k];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < n; j++) m[j][i] = in.nextInt();
            target[i] = in.nextInt();
        }
        // vectors w that are orthogonal to the column of every variable span the
        // null space of the transposed matrix, and y is Ax for some x exactly when
        // every such w is orthogonal to y
        List<Integer> pivots = new ArrayList<>();
        boolean[] isPivot = new boolean[k];
        for (int c = 0; c < k; c++) {
            int r = pivots.size(), sel = -1;
            for (int i = r; i < n && sel == -1; i++) {
                if (m[i][c] != 0) sel = i;
            }
            if (sel == -1) continue;
            int[] swap = m[r];
            m[r] = m[sel];
            m[sel] = swap;
            if (m[r][c] == 2) {
                for (int j = 0; j < k; j++) m[r][j] = m[r][j] * 2 % MOD;
            }
            for (int i = 0; i < n; i++) {
                if (i == r || m[i][c] == 0) continue;
                int f = m[i][c];
                for (int j = 0; j < k; j++) m[i][j] = ((m[i][j] - f * m[r][j]) % MOD + MOD) % MOD;
            }
            pivots.add(c);
            isPivot[c] = true;
        }
        int rank = pivots.size();
        List<int[]> basis = new ArrayList<>();
        for (int free = 0; free < k; free++) {
            if (isPivot[free]) continue;
            int[] w = new int[k];
            w[free] = 1;
            for (int i = 0; i < rank; i++) w[pivots.get(i)] = (MOD - m[i][free]) % MOD;
            basis.add(w);
        }
        // the change that y_i = 1 makes to the syndromes w . y over the basis,
        // and y_i = 2 makes the opposite change, the two masks swapped
        long[] unit = new long[k];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < basis.size(); j++) {
                if (basis.get(j)[i] == 1) unit[i] |= 1L << (SHIFT + j);
                if (basis.get(j)[i] == 2) unit[i] |= 1L << j;
            }
        }
        // every y_i has two allowed values: meet in the middle on syndromes
        int half = k / 2;
        long[] left = syndromes(0, half, target, unit);
        Arrays.sort(left);
        long total = 0;
        for (long s : syndromes(half, k, target, unit)) {
            long key = negate(s);
            int lo = lowerBound(left, key), hi = lowerBound(left, key + 1);
            total += hi - lo;
        }
        for (int i = rank; i < n; i++) total *= MOD;
        System.out.println(total);
    }

    static long[] syndromes(int from, int to, int[] target, long[] unit) {
        long[] sums = {0};
        for (int i = from; i < to; i++) {
            long[] next = new long[sums.length * (MOD - 1)];
            int size = 0;
            for (long s : sums) {
                for (int v = 0; v < MOD; v++) {
                    if (v == target[i]) continue;
                    next[size++] = v == 0 ? s : add(s, v == 1 ? unit[i] : negate(unit[i]));
                }
            }
            sums = next;
        }
        return sums;
    }

    static int lowerBound(long[] a, long key) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] < key) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
