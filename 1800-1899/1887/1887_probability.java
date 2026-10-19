import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int PRIME = 11;
    static final int DIGITS = 10;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // the coefficients a, b and c, one row each
        int[][] rows = new int["abc".length()][n];
        for (int[] row : rows) {
            for (int i = 0; i < n; i++) {
                row[i] = in.nextInt();
            }
        }
        // chance[r]: probability that the product so far is r modulo 11
        double[] chance = new double[PRIME];
        chance[1] = 1;
        for (int i = 0; i < n; i++) {
            double[] next = new double[PRIME];
            for (int x = 0; x < DIGITS; x++) {
                int factor = (rows[0][i] * x * x + rows[1][i] * x + rows[2][i]) % PRIME;
                for (int r = 0; r < PRIME; r++) {
                    next[r * factor % PRIME] += chance[r] / DIGITS;
                }
            }
            chance = next;
        }
        double[] p = new double[DIGITS];
        for (int r = 0; r < PRIME; r++) {
            p[r % DIGITS] += chance[r];
        }
        for (double q : p) {
            // only positive terms are ever added, so an impossible digit stays 0
            if (q == 0) {
                System.out.println(-1);
                return;
            }
        }
        // expected draws from the set of digits seen to all ten: a draw of a
        // missing digit moves on, others repeat; the chance to move on is summed
        // directly so that small probabilities keep their precision
        int full = (1 << DIGITS) - 1;
        double[] expect = new double[full + 1];
        for (int mask = full - 1; mask >= 0; mask--) {
            double move = 0;
            double sum = 1;
            for (int d = 0; d < DIGITS; d++) {
                if ((mask >> d & 1) == 1) {
                    continue;
                }
                move += p[d];
                sum += p[d] * expect[mask | 1 << d];
            }
            expect[mask] = sum / move;
        }
        System.out.println(String.format(Locale.US, "%.10f", expect[0]));
    }
}
