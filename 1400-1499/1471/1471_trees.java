import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static StreamTokenizer input =
        new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static int readInt() throws IOException {
        input.nextToken();
        return (int)input.nval;
    }
    static class Edge {
        int to, weight;
        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }
    static int[] depth;

    static int shallower(int a, int b) { return depth[a] <= depth[b] ? a : b; }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        List<List<Edge>> adjacency = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adjacency.add(new ArrayList<Edge>());
        for (int i = 1; i < n; i++) {
            int u = readInt(), v = readInt(), w = readInt();
            adjacency.get(u).add(new Edge(v, w));
            adjacency.get(v).add(new Edge(u, w));
        }
        // euler tour from vertex 0: a vertex is written on entry and after each child
        int[] parent = new int[n], dist = new int[n], first = new int[n];
        depth = new int[n];
        Arrays.fill(parent, -1);
        int[] tour = new int[2 * n - 1], stack = new int[n];
        int[] pointer = new int[n];
        int len = 1, top = 1;
        while (top > 0) {
            int v = stack[top - 1];
            int p = pointer[v];
            if (p < adjacency.get(v).size()) {
                pointer[v]++;
                Edge edge = adjacency.get(v).get(p);
                int u = edge.to;
                if (u == parent[v])
                    continue;
                parent[u] = v;
                depth[u] = depth[v] + 1;
                dist[u] = dist[v] + edge.weight;
                first[u] = len;
                tour[len++] = u;
                stack[top++] = u;
            } else {
                top--;
                if (top > 0)
                    tour[len++] = stack[top - 1];
            }
        }

        // sparse table: the shallowest vertex of each run of 2^k tour entries
        int levels = Integer.SIZE - Integer.numberOfLeadingZeros(len);
        int[][] table = new int[levels][];
        table[0] = tour;
        for (int k = 1, span = 1; k < levels; k++, span *= 2) {
            int[] prev = table[k - 1];
            int[] level = new int[len - 2 * span + 1];
            for (int i = 0; i < level.length; i++)
                level[i] = shallower(prev[i], prev[i + span]);
            table[k] = level;
        }

        int m = readInt();
        StringBuilder out = new StringBuilder();
        while (m-- > 0) {
            int a = readInt(), b = readInt();
            int lo = Math.min(first[a], first[b]), hi = Math.max(first[a], first[b]);
            int k = Integer.SIZE - 1 - Integer.numberOfLeadingZeros(hi - lo + 1);
            int lca = shallower(table[k][lo], table[k][hi - (1 << k) + 1]);
            out.append(dist[a] + dist[b] - 2 * dist[lca]).append('\n');
        }
        System.out.print(out);
    }
}
