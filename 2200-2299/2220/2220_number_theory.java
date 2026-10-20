import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final long MOD = 1_000_000_007L;
    private static final int SIEVE_LIMIT = 100_000;

    private static long power(long base, long exponent) {
        long result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exponent /= 2;
        }
        return result;
    }

    private static class Totients {
        private final int n;
        private final int limit;
        private final long[] small;
        private final long[] large;

        Totients(int size) {
            n = size;
            limit = Math.min(n, SIEVE_LIMIT);
            small = new long[limit + 1];
            for (int i = 0; i <= limit; ++i) {
                small[i] = i;
            }
            for (int prime = 2; prime <= limit; ++prime) {
                if (small[prime] == prime) {
                    for (int multiple = prime; multiple <= limit; multiple += prime) {
                        small[multiple] -= small[multiple] / prime;
                    }
                }
            }
            for (int i = 1; i <= limit; ++i) {
                small[i] += small[i - 1];
            }
            int count = n / (limit + 1);
            large = new long[count + 1];
            // Smaller quotient arguments have already been computed.
            for (int index = count; index >= 1; --index) {
                long x = n / index;
                long total = x * (x + 1) / 2;
                for (long left = 2; left <= x; ) {
                    long quotient = x / left;
                    long right = x / quotient;
                    total -= (right - left + 1) * get((int) quotient);
                    left = right + 1;
                }
                large[index] = total;
            }
        }

        long get(int x) {
            return x <= limit ? small[x] : large[n / x];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int digit;
        do {
            digit = in.read();
        } while (digit <= ' ' && digit != -1);
        int n = 0;
        while (digit > ' ') {
            n = n * 10 + digit - '0';
            digit = in.read();
        }
        Totients totients = new Totients(n);
        long factorial = 1;
        long weighted = 0;
        long previous = 0;
        long total = 0;
        for (int left = 1; left <= n; ) {
            int quotient = n / left;
            int right = n / quotient;
            // weighted is factorial times the current harmonic sum.
            for (long i = left; i <= right; ++i) {
                weighted = (weighted * i + factorial) % MOD;
                factorial = factorial * i % MOD;
            }
            long harmonic = weighted * power(factorial, MOD - 2) % MOD;
            long difference = (harmonic - previous + MOD) % MOD;
            total = (total + difference * (totients.get(quotient) % MOD)) % MOD;
            previous = harmonic;
            left = right + 1;
        }
        long pairs = (long) n * (n + 1) / 2 % MOD;
        System.out.println(total * power(pairs, MOD - 2) % MOD);
    }
}
