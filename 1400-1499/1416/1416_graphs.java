import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final int INF = 1 << 30;
    static final int BASE = 10;

    static InputStream in = new BufferedInputStream(System.in);

    static int nextInt() throws IOException {
        int c = in.read();
        while (c < '0' || c > '9')
            c = in.read();
        int value = 0;
        for (; c >= '0' && c <= '9'; c = in.read())
            value = value * BASE + c - '0';
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt(), m = nextInt();
        int[][] w = new int[n][n];
        for (int[] row : w)
            java.util.Arrays.fill(row, INF);
        int[] ea = new int[m], eb = new int[m], ec = new int[m];
        for (int i = 0; i < m; i++) {
            ea[i] = nextInt() - 1;
            eb[i] = nextInt() - 1;
            ec[i] = nextInt();
            w[ea[i]][eb[i]] = w[eb[i]][ea[i]] = ec[i];
        }
        // Prim on the matrix; heaviest[u][v] is the heaviest tree edge between u and v
        int[][] heaviest = new int[n][n];
        boolean[][] inTree = new boolean[n][n];
        int[] dist = w[0].clone(), parent = new int[n], order = new int[n];
        boolean[] done = new boolean[n];
        done[0] = true;
        int size = 1;
        long total = 0;
        for (int step = 1; step < n; step++) {
            int v = -1;
            for (int u = 0; u < n; u++)
                if (!done[u] && (v < 0 || dist[u] < dist[v]))
                    v = u;
            int p = parent[v], c = dist[v];
            total += c;
            inTree[p][v] = inTree[v][p] = true;
            for (int k = 0; k < size; k++) {
                int u = order[k];
                heaviest[u][v] = heaviest[v][u] = Math.max(heaviest[p][u], c);
            }
            done[v] = true;
            order[size++] = v;
            for (int u = 0; u < n; u++)
                if (!done[u] && w[v][u] < dist[u]) {
                    dist[u] = w[v][u];
                    parent[u] = v;
                }
        }
        // the next tree swaps one outside edge for the heaviest edge on its tree path
        long swap = INF;
        for (int i = 0; i < m; i++)
            if (!inTree[ea[i]][eb[i]])
                swap = Math.min(swap, ec[i] - heaviest[ea[i]][eb[i]]);
        System.out.println("Cost: " + total);
        System.out.println("Cost: " + (swap == INF ? -1 : total + swap));
    }
}
