import java.io.*;
import java.util.*;

public class Main {
    static final int MOST = 4; // the highest K asked for

    static long power(long b, long e, long mod) {
        long r = 1;
        for (b %= mod; e > 0; e >>= 1, b = b * b % mod)
            if ((e & 1) == 1)
                r = r * b % mod;
        return r;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        long mod = Long.parseLong(st.nextToken());
        long[] values = new long[n + 1];
        // trees[j] is a Fenwick tree of the power sums of a^j for j = 1..4; the
        // sums stay unreduced and are only reduced when a query reads them
        long[][] trees = new long[MOST + 1][n + 1];
        st = new StringTokenizer(in.readLine());
        for (int i = 1; i <= n; i++) {
            while (!st.hasMoreTokens())
                st = new StringTokenizer(in.readLine());
            values[i] = (Long.parseLong(st.nextToken()) % mod + mod) % mod;
            long p = 1;
            for (int j = 1; j <= MOST; j++) {
                p = p * values[i] % mod;
                trees[j][i] += p;
            }
        }
        for (int j = 1; j <= MOST; j++)
            for (int i = 1; i <= n; i++)
                if (i + (i & -i) <= n)
                    trees[j][i + (i & -i)] += trees[j][i];
        long[] inverse = new long[MOST + 1];
        for (int k = 1; k <= MOST; k++)
            inverse[k] = power(k, mod - 2, mod);
        StringBuilder out = new StringBuilder();
        for (int q = 0; q < m; q++) {
            st = new StringTokenizer(in.readLine());
            while (!st.hasMoreTokens())
                st = new StringTokenizer(in.readLine());
            if (st.nextToken().equals("I")) {
                int i = Integer.parseInt(st.nextToken());
                long delta = Long.parseLong(st.nextToken());
                long old = values[i], now = ((old + delta) % mod + mod) % mod;
                values[i] = now;
                long po = 1, pn = 1;
                for (int j = 1; j <= MOST; j++) {
                    po = po * old % mod;
                    pn = pn * now % mod;
                    for (int k = i; k <= n; k += k & -k)
                        trees[j][k] += pn - po;
                }
                continue;
            }
            int left = Integer.parseInt(st.nextToken()), right = Integer.parseInt(st.nextToken());
            int top = Integer.parseInt(st.nextToken());
            long[] sums = new long[MOST + 1], e = new long[MOST + 1];
            for (int j = 1; j <= top; j++) {
                long total = 0;
                for (int k = right; k > 0; k -= k & -k)
                    total += trees[j][k];
                for (int k = left - 1; k > 0; k -= k & -k)
                    total -= trees[j][k];
                sums[j] = (total % mod + mod) % mod;
            }
            // Newton's identities: k e(k) is the alternating sum of e(k - i) p(i)
            e[0] = 1;
            for (int k = 1; k <= top; k++) {
                long acc = 0;
                for (int i = 1; i <= k; i++) {
                    long term = e[k - i] * sums[i] % mod;
                    acc += i % 2 == 1 ? term : mod - term;
                }
                e[k] = acc % mod * inverse[k] % mod;
            }
            for (int k = 0; k <= top; k++)
                out.append(k > 0 ? " " : "").append(e[k]);
            out.append('\n');
        }
        System.out.print(out);
    }
}
