import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int ROOT = 31623;

    // The inverse of a modulo m by the extended Euclidean algorithm.
    static long inverse(long a, long m) {
        long r0 = m, r1 = a % m, s0 = 0, s1 = 1;
        while (r1 != 0) {
            long t = r0 / r1, r = r0 - t * r1, s = s0 - t * s1;
            r0 = r1;
            r1 = r;
            s0 = s1;
            s1 = s;
        }
        return (s0 % m + m) % m;
    }

    public static void main(String[] args) throws IOException {
        boolean[] composite = new boolean[ROOT + 1];
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= ROOT; i++) {
            if (!composite[i]) {
                primes.add(i);
                for (long j = (long)i * i; j <= ROOT; j += i) {
                    composite[(int)j] = true;
                }
            }
        }
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tok = new StringTokenizer("");
        StringBuilder out = new StringBuilder();
        int k = -1;
        while (k != 0) {
            while (!tok.hasMoreTokens()) {
                tok = new StringTokenizer(in.readLine());
            }
            long v = Long.parseLong(tok.nextToken());
            if (k < 0) {
                k = (int)v;
                continue;
            }
            k--;
            long n = v, p = 0;
            for (int d : primes) {
                if (n % d == 0) {
                    p = d;
                    break;
                }
            }
            long q = n / p;
            // x = 1 (mod p) and x = 0 (mod q); the other root is n + 1 - x
            long x = q * inverse(q, p) % n, y = n + 1 - x;
            out.append("0 1 ")
                .append(Math.min(x, y))
                .append(' ')
                .append(Math.max(x, y))
                .append('\n');
        }
        System.out.print(out);
    }
}
