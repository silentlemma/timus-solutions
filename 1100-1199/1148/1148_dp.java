import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    // counts are kept only for every STRIDE-th height, so that the table fits
    // in the memory limit; the heights between are recomputed by recursion
    static final int STRIDE = 4;

    static int[][] offset; // -1 where nothing is stored
    static long[] memo;

    // a tower with h levels whose lowest has m bricks uses at most this many
    static int most(int h, int m) { return m * h + h * (h - 1) / 2; }

    // towers of h levels starting with m bricks that use at most n bricks
    static long count(int n, int h, int m) {
        if (m == 0 || n < m) {
            return 0;
        }
        if (h == 1) {
            return 1;
        }
        n = Math.min(n, most(h, m));
        int key = h < offset.length && m < offset[h].length ? offset[h][m] : -1;
        if (key >= 0 && memo[key + n] >= 0) {
            return memo[key + n];
        }
        long ways = count(n - m, h - 1, m - 1) + count(n - m, h - 1, m + 1);
        if (key >= 0) {
            memo[key + n] = ways;
        }
        return ways;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer tok = new StringTokenizer(all.toString());
        int total = Integer.parseInt(tok.nextToken());
        int height = Integer.parseInt(tok.nextToken());
        int base = Integer.parseInt(tok.nextToken());
        // offset[h][m] starts the stored counts for h levels and m bricks below,
        // kept only for the widths that a tower can reach at that height
        offset = new int[height + 1][base + height + 2];
        int size = 0;
        for (int h = 0; h <= height; h++) {
            Arrays.fill(offset[h], -1);
            if (h == 0 || h % STRIDE != 0) {
                continue;
            }
            int depth = height - h, low = base - depth;
            while (low < 1) {
                low += 2;
            }
            for (int m = low; m <= base + depth; m += 2) {
                offset[h][m] = size;
                size += most(h, m) + 1;
            }
        }
        memo = new long[size];
        Arrays.fill(memo, -1);
        StringBuilder out = new StringBuilder().append(count(total, height, base)).append('\n');
        while (tok.hasMoreTokens()) {
            long k = Long.parseLong(tok.nextToken());
            if (k < 0) {
                break;
            }
            // lexicographic order: the narrower next level comes first
            int n = total, m = base;
            out.append(m);
            for (int h = height; h > 1; h--) {
                long fewer = count(n - m, h - 1, m - 1);
                n -= m;
                if (k <= fewer) {
                    m--;
                } else {
                    k -= fewer;
                    m++;
                }
                out.append(' ').append(m);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
