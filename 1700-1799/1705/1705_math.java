import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final long SMALL = 100; // below this the first candidates are simply tried in turn

    static long isqrt(long v) {
        long root = (long) Math.sqrt((double) v);
        while (root * root > v) {
            root--;
        }
        while ((root + 1) * (root + 1) <= v) {
            root++;
        }
        return root;
    }

    static long ceilSqrt(long v) {
        long root = isqrt(v);
        return root * root == v ? root : root + 1;
    }

    static boolean fits(long n, long k) {
        return n / k == n / (k + 1);
    }

    static long least(long n) {
        // the shares agree exactly when n mod k >= n div k, which needs k > s,
        // s = isqrt(n); with k = s + x and e = n - s^2 the quotient is s - x or
        // s - x + 1, and each case gives the least x in closed form
        if (n < SMALL) {
            long k = 1;
            while (!fits(n, k)) {
                k++;
            }
            return k;
        }
        long s = isqrt(n);
        long e = n - s * s;
        long[] xs = new long[2];
        int count = 0;
        long gap = s - e;
        if (gap >= 1) {
            // quotient s - x: the least x with x^2 + x >= gap (then x^2 - x < gap)
            long x = isqrt(gap);
            while (x * x + x < gap) {
                x++;
            }
            while (x > 1 && (x - 1) * (x - 1) + (x - 1) >= gap) {
                x--;
            }
            xs[count++] = x;
        }
        // quotient s - x + 1: x^2 >= 2s - e + 1 > (x - 1)^2
        xs[count++] = ceilSqrt(2 * s - e + 1);
        long best = -1;
        for (int i = 0; i < count; i++) {
            for (long d = -1; d <= 1; d++) {
                long k = s + xs[i] + d;
                if (xs[i] + d >= 1 && fits(n, k) && (best < 0 || k < best)) {
                    best = k;
                }
            }
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        int t = -1;
        int done = 0;
        String line;
        while (done != t && (line = in.readLine()) != null) {
            StringTokenizer tokens = new StringTokenizer(line);
            while (tokens.hasMoreTokens() && done != t) {
                long value = Long.parseLong(tokens.nextToken());
                if (t < 0) {
                    t = (int) value;
                } else {
                    out.append(least(value)).append('\n');
                    done++;
                }
            }
        }
        System.out.print(out);
    }
}
