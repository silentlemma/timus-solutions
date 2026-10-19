import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final long FIRST_ODD_PRIME = 3; // n is odd

    // the integer square root, corrected after the floating-point guess
    static long isqrt(long n) {
        long r = (long) Math.sqrt((double) n);
        while (r * r > n) {
            r--;
        }
        while ((r + 1) * (r + 1) <= n) {
            r++;
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(in.readLine().trim());
        // the gods number a square divisor of n: a number has an odd count
        // of divisors exactly when it is a square
        long best = 1;
        for (long p = FIRST_ODD_PRIME; p * p * p <= n; p += 2) {
            int power = 0;
            while (n % p == 0) {
                n /= p;
                power++;
            }
            for (int k = 0; k < power / 2; k++) {
                best *= p * p;
            }
        }
        // what is left has no prime factor up to its cube root, so at most
        // two prime factors: it is a square only as the square of one prime
        long r = isqrt(n);
        if (r * r == n) {
            best *= n;
        }
        System.out.println(best);
    }
}
