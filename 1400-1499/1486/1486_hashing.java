import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    // two hashes modulo two primes, packed into one 64-bit key
    static final long MOD1 = 1000000007L, MOD2 = 998244353L;
    static final long ROW1 = 131, ROW2 = 137, COL1 = 1009, COL2 = 1013;
    static final int HALF = 32;
    static final long LOW = (1L << HALF) - 1;
    static int n, m;
    static String[] grid;

    static long power(long b, int e, long mod) {
        long r = 1;
        for (; e > 0; e--)
            r = r * b % mod;
        return r;
    }

    static boolean same(int r1, int c1, int r2, int c2, int k) {
        for (int t = 0; t < k; t++)
            if (!grid[r1 + t].regionMatches(c1, grid[r2 + t], c2, k))
                return false;
        return true;
    }

    // two different equal k x k squares as top-left corners, or null
    static int[][] find(int k) {
        int width = m - k + 1;
        long[][] rows = new long[n][width];
        long p1 = power(ROW1, k, MOD1), p2 = power(ROW2, k, MOD2);
        for (int i = 0; i < n; i++) {
            long h1 = 0, h2 = 0;
            for (int j = 0; j < m; j++) {
                long c = grid[i].charAt(j);
                h1 = (h1 * ROW1 + c) % MOD1;
                h2 = (h2 * ROW2 + c) % MOD2;
                if (j >= k) {
                    long old = grid[i].charAt(j - k);
                    h1 = (h1 + MOD1 - old * p1 % MOD1) % MOD1;
                    h2 = (h2 + MOD2 - old * p2 % MOD2) % MOD2;
                }
                if (j >= k - 1)
                    rows[i][j - k + 1] = h1 << HALF | h2;
            }
        }
        p1 = power(COL1, k, MOD1);
        p2 = power(COL2, k, MOD2);
        long[] c1 = new long[width], c2 = new long[width];
        int count = (n - k + 1) * width;
        long[] keys = new long[count];
        int[] pos = new int[count];
        int at = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < width; j++) {
                c1[j] = (c1[j] * COL1 + (rows[i][j] >>> HALF)) % MOD1;
                c2[j] = (c2[j] * COL2 + (rows[i][j] & LOW)) % MOD2;
                if (i >= k) {
                    c1[j] = (c1[j] + MOD1 - (rows[i - k][j] >>> HALF) * p1 % MOD1) % MOD1;
                    c2[j] = (c2[j] + MOD2 - (rows[i - k][j] & LOW) * p2 % MOD2) % MOD2;
                }
                if (i >= k - 1) {
                    keys[at] = c1[j] << HALF | c2[j];
                    pos[at++] = (i - k + 1) * width + j;
                }
            }
        // a primitive sort finds the repeated keys; their positions come
        // from one more pass (the keys fit in 62 bits)
        long[] sorted = keys.clone();
        Arrays.sort(sorted);
        for (int t = 1; t < count; t++) {
            if (sorted[t] != sorted[t - 1] || (t > 1 && sorted[t - 2] == sorted[t]))
                continue;
            int a = -1;
            for (int u = 0; u < count; u++)
                if (keys[u] == sorted[t]) {
                    if (a < 0) {
                        a = u;
                        continue;
                    }
                    int[][] pair = {{pos[a] / width, pos[a] % width},
                                    {pos[u] / width, pos[u] % width}};
                    if (same(pair[0][0], pair[0][1], pair[1][0], pair[1][1], k))
                        return pair;
                }
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer first = new StringTokenizer(in.readLine());
        n = Integer.parseInt(first.nextToken());
        m = Integer.parseInt(first.nextToken());
        grid = new String[n];
        for (int i = 0; i < n; i++)
            grid[i] = in.readLine().trim();
        // equal k x k squares contain equal (k - 1) x (k - 1) ones, so the
        // largest size can be found by binary search
        int lo = 1, hi = Math.min(n, m), best = 0;
        int[][] where = null;
        while (lo <= hi) {
            int k = (lo + hi) / 2;
            int[][] pair = find(k);
            if (pair != null) {
                best = k;
                where = pair;
                lo = k + 1;
            } else
                hi = k - 1;
        }
        if (best == 0) {
            System.out.println(0);
            return;
        }
        System.out.println(best + "\n" + (where[0][0] + 1) + " " + (where[0][1] + 1) + "\n" +
                           (where[1][0] + 1) + " " + (where[1][1] + 1));
    }
}
