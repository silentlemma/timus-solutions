import java.util.*;

public class Main {
    static final int INF = 1000000000;
    static int n, k, size;
    static int[][] road;

    // distances between the doors of the outer house when walking through an
    // inner house from door i to door j costs inside[i][j]
    static int[][] outerDistances(int[][] inside) {
        int[][] weight = new int[size][];
        for (int i = 0; i < size; i++)
            weight[i] = road[i].clone();
        for (int h = 1; h <= k; h++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (inside[i][j] < weight[h * n + i][h * n + j])
                        weight[h * n + i][h * n + j] = inside[i][j];
        int[][] result = new int[n][];
        int[] dist = new int[size];
        boolean[] done = new boolean[size];
        for (int s = 0; s < n; s++) {
            // Dijkstra on the dense graph, O(size^2)
            Arrays.fill(dist, INF);
            Arrays.fill(done, false);
            dist[s] = 0;
            for (int step = 0; step < size; step++) {
                int u = -1;
                for (int v = 0; v < size; v++)
                    if (!done[v] && dist[v] < INF && (u < 0 || dist[v] < dist[u]))
                        u = v;
                if (u < 0)
                    break;
                done[u] = true;
                for (int v = 0; v < size; v++)
                    if (weight[u][v] < INF && dist[u] + weight[u][v] < dist[v])
                        dist[v] = dist[u] + weight[u][v];
            }
            result[s] = Arrays.copyOf(dist, n);
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        k = in.nextInt();
        int m = in.nextInt();
        size = (k + 1) * n; // door d of house h is h * n + d
        road = new int[size][size];
        for (int[] row : road)
            Arrays.fill(row, INF);
        for (int i = 0; i < m; i++) {
            String left = in.next();
            in.next();
            String right = in.next();
            int u = index(left), v = index(right);
            road[u][v] = road[v][u] = 1;
        }
        int source = in.nextInt(), sink = in.nextInt();
        // Round t allows paths nested t houses deep; the distances only shrink,
        // and once a round changes nothing, no later round will.
        int[][] opaque = new int[n][n];
        for (int[] row : opaque)
            Arrays.fill(row, INF);
        int[][] inside = outerDistances(opaque);
        while (true) {
            int[][] next = outerDistances(inside);
            if (Arrays.deepEquals(next, inside))
                break;
            inside = next;
        }
        System.out.println(inside[source][sink] >= INF ? "no solution" : "" + inside[source][sink]);
    }

    static int index(String s) {
        int dot = s.indexOf('.');
        return Integer.parseInt(s.substring(0, dot)) * n + Integer.parseInt(s.substring(dot + 1));
    }
}
