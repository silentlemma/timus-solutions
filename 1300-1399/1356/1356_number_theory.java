import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // these bases make Miller-Rabin exact for every n below 3.2 * 10^9
    static final long[] BASES = {2, 3, 5, 7};
    static final long SMALLEST_SPLIT = 4; // the smallest even number that is a sum of two primes

    static long power(long b, long e, long m) {
        long r = 1;
        b %= m;
        for (; e > 0; e >>= 1) {
            if ((e & 1) == 1)
                r = r * b % m;
            b = b * b % m;
        }
        return r;
    }

    static boolean isPrime(long n) {
        if (n < 2)
            return false;
        for (long b : BASES)
            if (n % b == 0)
                return n == b;
        long d = n - 1;
        int s = 0;
        while (d % 2 == 0) {
            d /= 2;
            s++;
        }
        for (long b : BASES) {
            long x = power(b, d, n);
            if (x == 1 || x == n - 1)
                continue;
            boolean composite = true;
            for (int i = 1; i < s && composite; i++) {
                x = x * x % n;
                composite = x != n - 1;
            }
            if (composite)
                return false;
        }
        return true;
    }

    // an even n >= 4 as the smallest prime p and n - p
    static String twoPrimes(long n) {
        long p = 2;
        while (!(isPrime(p) && isPrime(n - p)))
            p++;
        return p + " " + (n - p);
    }

    static String split(long n) {
        if (isPrime(n))
            return Long.toString(n);
        if (n % 2 == 0)
            return twoPrimes(n);
        if (isPrime(n - 2))
            return "2 " + (n - 2);
        // the largest prime p that leaves an even rest of at least 4
        long p = n - SMALLEST_SPLIT;
        while (!isPrime(p))
            p -= 2;
        return p + " " + twoPrimes(n - p);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextToken() == StreamTokenizer.TT_EOF ? 0 : (int)in.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < t; i++) {
            in.nextToken();
            out.append(split((long)in.nval)).append('\n');
        }
        System.out.print(out);
    }
}
