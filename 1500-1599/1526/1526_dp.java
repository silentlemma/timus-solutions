import java.io.*;
import java.util.*;

public class Main {
    static StreamTokenizer in;

    static int next() throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int p = next(), t = next(), n = next(), m = next();
        int half = t / 2, full = (1 << n) - 1;
        // after[x]: the dishes that may still be brought over a plate of dish x
        int[] after = new int[n];
        Arrays.fill(after, full);
        for (int k = 0; k < m; k++) {
            int i = next(), j = next();
            after[i - 1] &= ~(1 << (j - 1));
        }
        // the count of time-tables depends only on the set of dishes that may be
        // brought; plates above a plate of x shrink that set to its part in after[x]
        boolean[] seen = new boolean[full + 1];
        seen[full] = true;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(full);
        List<Integer> order = new ArrayList<>();
        while (!stack.isEmpty()) {
            int allowed = stack.pop();
            order.add(allowed);
            for (int x = 0; x < n; x++) {
                int inner = allowed & after[x];
                if ((allowed >> x & 1) == 1 && !seen[inner]) {
                    seen[inner] = true;
                    stack.push(inner);
                }
            }
        }
        order.sort(Comparator.comparingInt(Integer::bitCount));
        // ways[s][q]: time-tables of q dishes with the set s allowed
        int[][] ways = new int[full + 1][];
        for (int allowed : order) {
            int[] f = new int[half + 1],
                  tree = new int[half]; // tree[q]: one plate with q dishes over it
            f[0] = 1;
            for (int q = 1; q <= half; q++) {
                long sum = 0;
                for (int x = 0; x < n; x++)
                    if ((allowed >> x & 1) == 1) {
                        int inner = allowed & after[x];
                        sum += inner == allowed ? f[q - 1] : ways[inner][q - 1];
                    }
                tree[q - 1] = (int)(sum % p);
                // the first plate holds a dishes over it, the rest follow it
                long total = 0;
                for (int a = 0; a < q; a++)
                    total = (total + (long)tree[a] * f[q - 1 - a]) % p;
                f[q] = (int)total;
            }
            ways[allowed] = f;
        }
        System.out.println(ways[full][half] % p);
    }
}
