import java.util.Scanner;

public class Main {
    // the sum of all divisors of n by trial division
    static long divisorSum(long n) {
        long total = 0;
        for (long d = 1; d * d <= n; d++) {
            if (n % d == 0) {
                total += d * d == n ? d : d + n / d;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long lo = in.nextLong(), hi = in.nextLong();
        // 1 has no proper divisors at all
        if (lo == 1) {
            System.out.println(1);
            return;
        }
        // a prime p has the ratio 1/p, and the largest prime in range beats every
        // composite there (it is above hi / 2 by Bertrand's postulate), so only a
        // range without primes, at most 113 numbers here, needs comparing
        for (long n = hi; n >= lo; n--) {
            if (divisorSum(n) == n + 1) {
                System.out.println(n);
                return;
            }
        }
        long best = lo;
        for (long n = lo + 1; n <= hi; n++) {
            // sigma(n) / n < sigma(best) / best, the smaller number winning a tie
            if (divisorSum(n) * best < divisorSum(best) * n) {
                best = n;
            }
        }
        System.out.println(best);
    }
}
