import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // adjacency as linked lists in arrays: head, next, target and cost per edge end
        int[] head = new int[n + 1], next = new int[2 * n], to = new int[2 * n], w = new int[2 * n];
        Arrays.fill(head, -1);
        for (int i = 0; i < 2 * (n - 1); i += 2) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            in.nextToken();
            int c = (int)in.nval;
            to[i] = b;
            w[i] = c;
            next[i] = head[a];
            head[a] = i;
            to[i + 1] = a;
            w[i + 1] = c;
            next[i + 1] = head[b];
            head[b] = i + 1;
        }
        // an edge with s branches on one side carries the s (n - s) pairs that
        // it separates; sizes come from a parents-first order read backwards
        int[] parent = new int[n + 1], cost = new int[n + 1], order = new int[n];
        parent[1] = -1;
        order[0] = 1;
        int len = 1;
        for (int i = 0; i < len; i++) {
            int v = order[i];
            for (int e = head[v]; e >= 0; e = next[e])
                if (to[e] != parent[v]) {
                    parent[to[e]] = v;
                    cost[to[e]] = w[e];
                    order[len++] = to[e];
                }
        }
        long[] size = new long[n + 1];
        Arrays.fill(size, 1);
        long total = 0;
        for (int i = len - 1; i > 0; i--) {
            int v = order[i];
            size[parent[v]] += size[v];
            total += cost[v] * size[v] * (n - size[v]);
        }
        // every pair is counted in both directions
        System.out.println(String.format(Locale.US, "%.4f", 2.0 * total / ((double)n * (n - 1))));
    }
}
