import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    static final int MOD = 2007;

    public static void main(String[] args) throws IOException {
        StreamTokenizer st =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();
        int n = (int)st.nval;
        long[] f = new long[n + 1], g = new long[n + 1], acc = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            st.nextToken();
            f[i] = (long)st.nval % MOD;
        }
        // (F * G)(n) sums F(n / d) G(d) over the divisors d of n and is 0 for n > 1,
        // so G(n) = -G(1) * (the sum over the proper divisors), with G(1) = 1 / F(1),
        // and a sieve adds G(d) times F to every multiple of d once G(d) is known
        long first = BigInteger.valueOf(f[1]).modInverse(BigInteger.valueOf(MOD)).longValue();
        StringBuilder out = new StringBuilder();
        for (int d = 1; d <= n; d++) {
            g[d] = d == 1 ? first : (MOD - first * acc[d] % MOD) % MOD;
            for (int k = 2; d * k <= n; k++)
                acc[d * k] = (acc[d * k] + f[k] * g[d]) % MOD;
            out.append(d > 1 ? " " : "").append(g[d]);
        }
        System.out.println(out);
    }
}
