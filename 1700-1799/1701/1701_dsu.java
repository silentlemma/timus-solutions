import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final long MOST = 1000000000L; // nobody but Vasily earns more; nobody earns less than 0
    static int[] parent;
    static int[] sizes;
    static long[] offset;

    static int find(int x) {
        int root = x;
        while (parent[root] != root) {
            root = parent[root];
        }
        // compress: the offsets of the path, summed from the far end
        long total = 0;
        for (int v = x; v != root; v = parent[v]) {
            total += offset[v];
        }
        for (int v = x; v != root;) {
            int next = parent[v];
            long own = offset[v];
            offset[v] = total;
            parent[v] = root;
            total -= own;
            v = next;
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        int m = (int) in.nval;
        // a weighted union-find: salary[x] = salary[root] + offset[x], and every
        // root keeps the range its own salary may take so that all salaries of
        // its set stay in [0, MOST]; Vasily (0) is pinned to 0
        parent = new int[n];
        sizes = new int[n];
        offset = new long[n];
        long[] low = new long[n];
        long[] high = new long[n];
        for (int x = 0; x < n; x++) {
            parent[x] = x;
            sizes[x] = 1;
            high[x] = MOST;
        }
        high[0] = 0;
        for (int k = 1; k <= m; k++) {
            in.nextToken();
            int i = (int) in.nval;
            in.nextToken();
            int j = (int) in.nval;
            in.nextToken();
            long d = (long) in.nval;
            int ri = find(i);
            int rj = find(j);
            // salary[i] - salary[j] = d means salary[rj] = salary[ri] + shift
            long shift = offset[i] - offset[j] - d;
            boolean ok = shift == 0;
            if (ri != rj) {
                if (sizes[ri] < sizes[rj]) {
                    int t = ri;
                    ri = rj;
                    rj = t;
                    shift = -shift;
                }
                // salary[rj] lies in [low[rj], high[rj]], so salary[ri] in that minus shift
                low[ri] = Math.max(low[ri], low[rj] - shift);
                high[ri] = Math.min(high[ri], high[rj] - shift);
                ok = low[ri] <= high[ri];
                parent[rj] = ri;
                offset[rj] = shift;
                sizes[ri] += sizes[rj];
            }
            if (!ok) {
                System.out.println("Impossible after " + k + " statements");
                return;
            }
        }
        StringBuilder out = new StringBuilder("Possible\n");
        for (int x = 0; x < n; x++) {
            int r = find(x);
            out.append(low[r] + offset[x]).append('\n');
        }
        System.out.print(out);
    }
}
