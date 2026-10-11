import java.io.*;
import java.util.*;

public class Main {
    static final int LIMIT = 1 << 16; // N < 65536

    static long power(long b, long e, long m) {
        long r = 1;
        for (b %= m; e > 0; e >>= 1) {
            if ((e & 1) == 1)
                r = r * b % m;
            b = b * b % m;
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        // smallest prime factor of every number below the limit
        int[] spf = new int[LIMIT];
        for (int i = 0; i < LIMIT; i++)
            spf[i] = i;
        for (int i = 2; i * i < LIMIT; i++)
            if (spf[i] == i)
                for (int j = i * i; j < LIMIT; j += i)
                    if (spf[j] == j)
                        spf[j] = i;
        int[] known = new int[LIMIT];
        in.nextToken();
        int t = (int)in.nval;
        StringBuilder out = new StringBuilder();
        while (t-- > 0) {
            in.nextToken();
            int p = (int)in.nval;
            if (known[p] == 0) {
                // g is a primitive root when no g^((p-1)/q) is 1 for a prime q | p-1
                List<Integer> quotients = new ArrayList<>();
                for (int rest = p - 1; rest > 1;) {
                    int q = spf[rest];
                    quotients.add((p - 1) / q);
                    while (rest % q == 0)
                        rest /= q;
                }
                int g = p - 1;
                for (;; g--) {
                    boolean root = true;
                    for (int e : quotients)
                        if (power(g, e, p) == 1) {
                            root = false;
                            break;
                        }
                    if (root)
                        break;
                }
                known[p] = g;
            }
            out.append(known[p]).append("\n");
        }
        System.out.print(out);
    }
}
