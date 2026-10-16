import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int ROUTES = 4, BRIDGES = 6;
    // each bridge lies on exactly two of the four routes, one pair per bridge,
    // in the input order: Nizhny Novgorod, Kotelnich, Perm, Kazan, Vyatskiye
    // Polyany, Sarapul
    static final int[][] PAIRS = {{0, 3}, {0, 2}, {2, 3}, {1, 2}, {1, 3}, {0, 1}};

    // determinant of a small integer matrix, expanded along the first row
    static long det(long[][] rows) {
        int n = rows.length;
        if (n == 1) return rows[0][0];
        long total = 0;
        for (int j = 0; j < n; j++) {
            if (rows[0][j] == 0) continue;
            long[][] minor = new long[n - 1][n - 1];
            for (int r = 1; r < n; r++) {
                for (int c = 0, k = 0; c < n; c++) {
                    if (c != j) minor[r - 1][k++] = rows[r][c];
                }
            }
            total += (j % 2 == 1 ? -1 : 1) * rows[0][j] * det(minor);
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<long[]> rows = new ArrayList<>();
        List<Long> bounds = new ArrayList<>();
        for (int k = 0; k < BRIDGES; k++) {
            long[] a = new long[ROUTES];
            a[PAIRS[k][0]] = 1;
            a[PAIRS[k][1]] = 1;
            rows.add(a);
            bounds.add(in.nextLong());
        }
        for (int i = 0; i < ROUTES; i++) {
            long[] a = new long[ROUTES];
            a[i] = -1;
            rows.add(a);
            bounds.add(0L);
        }
        // the best plan is a corner where four constraints are tight; each
        // corner is solved exactly by Cramer's rule, as numerators over a
        // common positive denominator
        int total = rows.size();
        long bestNum = -1, bestDen = 1;
        long[] best = null;
        for (int mask = 0; mask < 1 << total; mask++) {
            if (Integer.bitCount(mask) != ROUTES) continue;
            int[] chosen = new int[ROUTES];
            for (int k = 0, r = 0; k < total; k++) {
                if ((mask >> k & 1) == 1) chosen[r++] = k;
            }
            long[][] matrix = new long[ROUTES][];
            for (int r = 0; r < ROUTES; r++) matrix[r] = rows.get(chosen[r]);
            long den = det(matrix);
            if (den == 0) continue;
            long[] nums = new long[ROUTES];
            for (int c = 0; c < ROUTES; c++) {
                long[][] swapped = new long[ROUTES][];
                for (int r = 0; r < ROUTES; r++) {
                    swapped[r] = matrix[r].clone();
                    swapped[r][c] = bounds.get(chosen[r]);
                }
                nums[c] = det(swapped);
            }
            if (den < 0) {
                den = -den;
                for (int c = 0; c < ROUTES; c++) nums[c] = -nums[c];
            }
            boolean ok = true;
            for (int k = 0; k < total; k++) {
                long lhs = 0;
                for (int c = 0; c < ROUTES; c++) lhs += rows.get(k)[c] * nums[c];
                if (lhs > bounds.get(k) * den) ok = false;
            }
            long sum = 0;
            for (long v : nums) sum += v;
            if (ok && sum * bestDen > bestNum * den) {
                bestNum = sum;
                bestDen = den;
                best = nums;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int c = 0; c < ROUTES; c++) {
            if (c > 0) sb.append(' ');
            sb.append(String.format(Locale.US, "%.3f", (double) best[c] / bestDen));
        }
        System.out.println(sb);
    }
}
