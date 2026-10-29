import java.io.IOException;

public class Main {
    // the numbers are parsed by hand from a small buffer, lighter than Scanner
    static final int BUFFER_SIZE = 1024;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return buffer[position++];
    }

    static int nextInt() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

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

    public static void main(String[] args) throws IOException {
        long lo = nextInt(), hi = nextInt();
        // 1 has no proper divisors at all
        if (lo == 1) {
            System.out.println(1);
            return;
        }
        // a prime p has the ratio 1/p, and the largest prime in range beats every
        // composite there (it is above hi / 2 by Bertrand's postulate), so only a
        // range without primes, at most 113 numbers here, needs comparing
        long best = hi, bestSum = 0;
        // the same pass keeps the smallest ratio seen, for a range without primes
        for (long n = hi; n >= lo; n--) {
            long sum = divisorSum(n);
            if (sum == n + 1) {
                System.out.println(n);
                return;
            }
            // sigma(n) / n <= sigma(best) / best, the smaller number winning a tie
            if (bestSum == 0 || sum * best <= bestSum * n) {
                best = n;
                bestSum = sum;
            }
        }
        System.out.println(best);
    }
}
