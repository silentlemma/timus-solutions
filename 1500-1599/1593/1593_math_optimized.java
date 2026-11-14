import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    private static final long[] BASES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    private static final int BATCH = 64;
    private static final int MAX_CYCLE = 1 << 16;

    private static strictfp long multiply(long a, long b, long n) {
        // For n <= 10^15 the rounded quotient is off by at most one.
        // The wrapped subtraction still gives the small signed remainder.
        long quotient = (long)((double)a * b / n);
        long remainder = a * b - quotient * n;
        if (remainder < 0)
            return remainder + n;
        if (remainder >= n)
            return remainder - n;
        return remainder;
    }

    private static boolean prime(long n) {
        for (long p : BASES) {
            if (n % p == 0)
                return n == p;
        }
        int twos = Long.numberOfTrailingZeros(n - 1);
        long odd = (n - 1) >> twos;
        for (long a : BASES) {
            long value = 1;
            for (long exponent = odd; exponent > 0; exponent >>= 1) {
                if ((exponent & 1) != 0)
                    value = multiply(value, a, n);
                a = multiply(a, a, n);
            }
            if (value == 1)
                continue;
            for (int i = 1; i < twos && value != n - 1; i++)
                value = multiply(value, value, n);
            if (value != n - 1)
                return false;
        }
        return true;
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long rest = a % b;
            a = b;
            b = rest;
        }
        return a;
    }

    private static long step(long a, long c, long n) { return (multiply(a, a, n) + c) % n; }

    private static long divisor(long n) {
        for (long c = 1;; c++) {
            long x = 0, y = 2, saved = 0, factor = 1;
            for (int size = 1; size <= MAX_CYCLE && factor == 1; size *= 2) {
                x = y;
                for (int i = 0; i < size; i++)
                    y = step(y, c, n);
                for (int start = 0; start < size && factor == 1; start += BATCH) {
                    saved = y;
                    long product = 1;
                    for (int i = 0; i < Math.min(BATCH, size - start); i++) {
                        y = step(y, c, n);
                        product = multiply(product, Math.abs(x - y), n);
                    }
                    factor = gcd(product, n);
                }
            }
            if (factor == n) {
                do {
                    saved = step(saved, c, n);
                    factor = gcd(Math.abs(x - saved), n);
                } while (factor == 1);
            }
            if (factor > 1 && factor < n)
                return factor;
        }
    }

    private static boolean square(long n) {
        long root = (long)Math.sqrt(n);
        return root * root == n || (root + 1) * (root + 1) == n;
    }

    private static final int POWER_OF_FOUR = 4;
    private static final int LEGENDRE_MODULUS = 8;
    private static final int LEGENDRE_RESIDUE = 7;
    private static final int TWO_SQUARE_OBSTRUCTION = 3;
    private static final int THREE_SQUARES = 3;
    private static final int FOUR_SQUARES = 4;

    private static void collect(long n, Set<Long> odd) {
        if (square(n))
            return;
        if (prime(n)) {
            if (n % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION && !odd.remove(n))
                odd.add(n);
            return;
        }
        long part = divisor(n);
        collect(part, odd);
        collect(n / part, odd);
    }

    static int solve(long n) {
        if (square(n))
            return 1;
        while (n % POWER_OF_FOUR == 0)
            n /= POWER_OF_FOUR;
        if (n % LEGENDRE_MODULUS == LEGENDRE_RESIDUE)
            return FOUR_SQUARES;
        if (n % 2 == 0)
            n /= 2;
        if (n % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION)
            return THREE_SQUARES;
        for (long p : BASES) {
            boolean odd = false;
            while (n % p == 0) {
                n /= p;
                odd = !odd;
            }
            if (odd && p % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION)
                return THREE_SQUARES;
        }
        Set<Long> odd = new HashSet<>();
        collect(n, odd);
        return odd.isEmpty() ? 2 : THREE_SQUARES;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(solve(Long.parseLong(input.readLine().trim())));
    }
}
