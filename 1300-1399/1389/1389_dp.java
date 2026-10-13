import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[] a = new int[m], b = new int[m], degree = new int[n + 1];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            a[i] = (int)in.nval;
            in.nextToken();
            b[i] = (int)in.nval;
            degree[a[i]]++;
            degree[b[i]]++;
        }
        // roads of each city in one array: start[v] .. start[v + 1]
        int[] start = new int[n + 2], fill = new int[n + 2], adj = new int[2 * m];
        for (int v = 1; v <= n; v++)
            start[v + 1] = start[v] + degree[v];
        System.arraycopy(start, 0, fill, 0, n + 2);
        for (int i = 0; i < m; i++) {
            adj[fill[a[i]]++] = i;
            adj[fill[b[i]]++] = i;
        }
        // breadth-first order from city 1 with the road to each parent
        int[] parent = new int[n + 1], up = new int[n + 1], order = new int[n];
        java.util.Arrays.fill(up, -1);
        parent[1] = -1;
        order[0] = 1;
        int size = 1;
        for (int k = 0; k < size; k++) {
            int v = order[k];
            for (int j = start[v]; j < start[v + 1]; j++) {
                int e = adj[j], u = a[e] + b[e] - v;
                if (u != parent[v]) {
                    parent[u] = v;
                    up[u] = e;
                    order[size++] = u;
                }
            }
        }
        // leaves first: close the road to the parent while both ends are free
        boolean[] used = new boolean[n + 1], chosen = new boolean[m];
        int count = 0;
        for (int k = size - 1; k >= 0; k--) {
            int v = order[k];
            if (up[v] >= 0 && !used[v] && !used[parent[v]]) {
                used[v] = used[parent[v]] = true;
                chosen[up[v]] = true;
                count++;
            }
        }
        StringBuilder out = new StringBuilder();
        out.append(count).append('\n');
        for (int i = 0; i < m; i++)
            if (chosen[i])
                out.append(a[i]).append(' ').append(b[i]).append('\n');
        System.out.print(out);
    }
}
