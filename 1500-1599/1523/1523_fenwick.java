import java.io.*;

public class Main {
    static final long MOD = 1000000000;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        // count values from the top, so that "larger" becomes a prefix
        int[] flipped = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            flipped[i] = n + 1 - (int)in.nval;
        }
        // ends[i]: decreasing runs of the current length that end at position i
        long[] ends = new long[n];
        java.util.Arrays.fill(ends, 1);
        for (int len = 2; len <= k; len++) {
            long[] tree = new long[n + 1], next = new long[n];
            for (int i = 0; i < n; i++) {
                // the runs one shorter that end earlier at a larger value
                long s = 0;
                for (int j = flipped[i] - 1; j > 0; j &= j - 1)
                    s += tree[j];
                next[i] = s % MOD;
                for (int j = flipped[i]; j <= n; j += j & -j)
                    tree[j] = (tree[j] + ends[i]) % MOD;
            }
            ends = next;
        }
        long total = 0;
        for (long e : ends)
            total = (total + e) % MOD;
        System.out.println(total);
    }
}
