import java.io.*;

public class Main {
    static final int MAX_CLIQUE = 4; // four points pairwise 1 apart fit in space, five do not
    static int[] parent;

    static int find(int v) {
        while (parent[v] != v)
            v = parent[v] = parent[parent[v]];
        return v;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        parent = new int[n];
        for (int v = 0; v < n; v++)
            parent[v] = v;
        int[] degree = new int[n], ends = new int[m];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            int u = (int)in.nval - 1;
            in.nextToken();
            int v = (int)in.nval - 1;
            degree[u]++;
            degree[v]++;
            ends[i] = u;
            parent[find(u)] = find(v);
        }
        int[] size = new int[n], edges = new int[n], widest = new int[n];
        for (int v = 0; v < n; v++) {
            int root = find(v);
            size[root]++;
            widest[root] = Math.max(widest[root], degree[v]);
        }
        for (int u : ends)
            edges[find(u)]++;
        // every component must be a path or a clique of at most four vertices
        for (int root = 0; root < n; root++) {
            int k = size[root];
            if (k == 0)
                continue;
            boolean path = edges[root] == k - 1 && widest[root] <= 2;
            boolean clique = edges[root] == k * (k - 1) / 2 && k <= MAX_CLIQUE;
            if (!path && !clique) {
                System.out.println("Unlucky Petr");
                return;
            }
        }
        System.out.println("Luck is possible");
    }
}
