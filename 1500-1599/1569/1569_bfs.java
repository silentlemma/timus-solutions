import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static List<List<Integer>> adj = new ArrayList<>();

    // distances from the nearest source; the edges of a tree of shortest paths
    // that grows from the sources go to tree, when it is given
    static int[] bfs(int[] sources, List<int[]> tree) {
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int s : sources) {
            dist[s] = 0;
            queue.add(s);
        }
        while (!queue.isEmpty()) {
            int v = queue.poll();
            for (int u : adj.get(v))
                if (dist[u] < 0) {
                    dist[u] = dist[v] + 1;
                    if (tree != null)
                        tree.add(new int[] {v, u});
                    queue.add(u);
                }
        }
        return dist;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());
        int[][] edges = new int[m][];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            int a = (int)in.nval - 1;
            in.nextToken();
            int b = (int)in.nval - 1;
            edges[i] = new int[] {a, b};
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        int[][] dist = new int[n][];
        for (int v = 0; v < n; v++)
            dist[v] = bfs(new int[] {v}, null);
        // the middle of a tree of least diameter is a node or the middle of an edge, and
        // a tree of shortest paths from there has diameter 2 r or 2 r + 1 for the
        // largest distance r from it, and no tree can do better
        int best = -1;
        int[] centre = null;
        for (int v = 0; v < n; v++) {
            int far = Arrays.stream(dist[v]).max().getAsInt();
            if (best < 0 || 2 * far < best) {
                best = 2 * far;
                centre = new int[] {v};
            }
        }
        for (int[] e : edges) {
            int far = 0;
            for (int w = 0; w < n; w++)
                far = Math.max(far, Math.min(dist[e[0]][w], dist[e[1]][w]));
            if (2 * far + 1 < best) {
                best = 2 * far + 1;
                centre = e;
            }
        }
        List<int[]> tree = new ArrayList<>();
        bfs(centre, tree);
        if (centre.length > 1)
            tree.add(centre);
        StringBuilder out = new StringBuilder();
        for (int[] e : tree)
            out.append(e[0] + 1).append(' ').append(e[1] + 1).append('\n');
        System.out.print(out);
    }
}
