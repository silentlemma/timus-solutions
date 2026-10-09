import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final long CAPACITY = 10000;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt(), s = in.nextInt();
        long[][] binom = new long[s + 1][s + 1];
        for (int n = 0; n <= s; n++) {
            binom[n][0] = 1;
            for (int r = 1; r <= n; r++) {
                binom[n][r] = binom[n - 1][r - 1] + binom[n - 1][r];
            }
        }
        // Moebius function by a sieve: -1 per prime factor, 0 with a square factor
        long[] mu = new long[s + 1];
        boolean[] prime = new boolean[s + 1];
        Arrays.fill(mu, 1);
        Arrays.fill(prime, true);
        for (int p = 2; p <= s; p++) {
            if (!prime[p]) {
                continue;
            }
            for (int m = p; m <= s; m += p) {
                prime[m] = m == p;
                mu[m] = -mu[m];
            }
            for (int m = p * p; m <= s; m += p * p) {
                mu[m] = 0;
            }
        }
        // inclusion-exclusion: sets of multiples of d count with the sign -mu(d)
        long total = 0;
        for (int d = 2; d <= s; d++) {
            if (s / d >= k) {
                total -= mu[d] * binom[s / d][k];
            }
        }
        System.out.println(Math.min(total, CAPACITY));
    }
}
