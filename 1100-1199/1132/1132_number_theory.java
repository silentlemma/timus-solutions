import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // moduli are below this bound
    static final int LIMIT = 32768;

    static long power(long b, long e, long p) {
        long r = 1;
        for (b %= p; e > 0; e /= 2, b = b * b % p) {
            if (e % 2 == 1) {
                r = r * b % p;
            }
        }
        return r;
    }

    // Tonelli-Shanks for an odd prime p = q * 2^s + 1, a quadratic residue a
    // and a non-residue z
    static long sqrtMod(long a, long p, long z) {
        long q = p - 1, s = 0;
        while (q % 2 == 0) {
            q /= 2;
            s++;
        }
        long c = power(z, q, p), t = power(a, q, p), r = power(a, (q + 1) / 2, p);
        while (t != 1) {
            // the order of t is 2^i with i < s; b fixes the top bits
            long i = 0, tt = t;
            while (tt != 1) {
                tt = tt * tt % p;
                i++;
            }
            long b = power(c, 1L << (s - i - 1), p);
            s = i;
            c = b * b % p;
            t = t * c % p;
            r = r * b % p;
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int k = (int)in.nval;
        long[] nonResidue = new long[LIMIT];
        StringBuilder out = new StringBuilder();
        while (k-- > 0) {
            in.nextToken();
            long a = (long)in.nval;
            in.nextToken();
            int p = (int)in.nval;
            a %= p;
            if (p == 2) {
                out.append("1\n");
                continue;
            }
            long half = (p - 1) / 2;
            if (power(a, half, p) != 1) {
                out.append("No root\n");
                continue;
            }
            if (nonResidue[p] == 0) {
                long z = 2;
                while (power(z, half, p) != p - 1) {
                    z++;
                }
                nonResidue[p] = z;
            }
            long r = sqrtMod(a, p, nonResidue[p]);
            out.append(Math.min(r, p - r)).append(' ').append(Math.max(r, p - r)).append('\n');
        }
        System.out.print(out);
    }
}
