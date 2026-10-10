import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    // among three vectors no longer than L, some sum or difference of two of
    // them is no longer than L, so they can be merged into one
    static final int KEEP = 3;

    static long[] x, y;
    static int[] parent, rel;
    static int nodes;

    static int join(int a, int b, int s) {
        x[nodes] = x[a] + s * x[b];
        y[nodes] = y[a] + s * y[b];
        parent[a] = nodes;
        parent[b] = nodes;
        rel[b] = s;
        return nodes++;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        long length = (long)in.nval;
        // nodes 0..n-1 are the input vectors, later nodes are merged pairs
        x = new long[2 * n];
        y = new long[2 * n];
        parent = new int[2 * n];
        rel = new int[2 * n];
        Arrays.fill(parent, -1);
        Arrays.fill(rel, 1);
        nodes = n;
        List<Integer> active = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = (long)in.nval;
            in.nextToken();
            y[i] = (long)in.nval;
            active.add(i);
            if (active.size() < KEEP) {
                continue;
            }
        search:
            for (int p = 0; p < KEEP; p++) {
                for (int q = p + 1; q < KEEP; q++) {
                    for (int s = -1; s <= 1; s += 2) {
                        int a = active.get(p), b = active.get(q);
                        long dx = x[a] + s * x[b], dy = y[a] + s * y[b];
                        if (dx * dx + dy * dy > length * length) {
                            continue;
                        }
                        List<Integer> next = new ArrayList<>();
                        for (int r = 0; r < KEEP; r++) {
                            if (r != p && r != q) {
                                next.add(active.get(r));
                            }
                        }
                        next.add(join(a, b, s));
                        active = next;
                        break search;
                    }
                }
            }
        }
        // two vectors no longer than L: a sign making their dot product
        // non-positive keeps the sum within sqrt(2) L
        if (active.size() == 2) {
            int a = active.get(0), b = active.get(1);
            join(a, b, x[a] * x[b] + y[a] * y[b] > 0 ? -1 : 1);
        }
        int[] sign = new int[nodes];
        for (int k = nodes - 1; k >= 0; k--) {
            sign[k] = parent[k] >= 0 ? sign[parent[k]] * rel[k] : 1;
        }
        StringBuilder out = new StringBuilder("YES\n");
        for (int i = 0; i < n; i++) {
            out.append(sign[i] > 0 ? '+' : '-');
        }
        System.out.println(out);
    }
}
