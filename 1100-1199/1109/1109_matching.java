import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {
    static final int BUF_SIZE = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUF_SIZE];
    static int len, pos;

    static int read() throws IOException {
        if (pos == len) {
            len = in.read(buf, 0, BUF_SIZE);
            pos = 0;
            if (len <= 0) {
                return -1;
            }
        }
        return buf[pos++];
    }

    static int readInt() throws IOException {
        int c = read();
        while (c < '0' || c > '9') {
            c = read();
        }
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + c - '0';
            c = read();
        }
        return v;
    }

    static int[][] adj;
    static int[] matchL, matchR, dist, it;

    // Hopcroft-Karp: BFS layers from the free left vertices, then
    // vertex-disjoint shortest augmenting paths along the layers
    static boolean layer() {
        Arrays.fill(dist, -1);
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int v = 0; v < adj.length; v++) {
            if (matchL[v] < 0) {
                dist[v] = 0;
                queue.add(v);
            }
        }
        boolean found = false;
        while (!queue.isEmpty()) {
            int v = queue.poll();
            for (int u : adj[v]) {
                int w = matchR[u];
                if (w < 0) {
                    found = true;
                } else if (dist[w] < 0) {
                    dist[w] = dist[v] + 1;
                    queue.add(w);
                }
            }
        }
        return found;
    }

    static boolean augment(int v) {
        for (; it[v] < adj[v].length; it[v]++) {
            int u = adj[v][it[v]], w = matchR[u];
            if (w < 0 || (dist[w] == dist[v] + 1 && augment(w))) {
                matchL[v] = u;
                matchR[u] = v;
                return true;
            }
        }
        dist[v] = -1;
        return false;
    }

    public static void main(String[] args) throws IOException {
        int m = readInt(), n = readInt(), k = readInt();
        int[] from = new int[k], to = new int[k], degree = new int[m];
        for (int i = 0; i < k; i++) {
            from[i] = readInt() - 1;
            to[i] = readInt() - 1;
            degree[from[i]]++;
        }
        adj = new int[m][];
        for (int v = 0; v < m; v++) {
            adj[v] = new int[degree[v]];
        }
        for (int i = 0; i < k; i++) {
            adj[from[i]][--degree[from[i]]] = to[i];
        }
        matchL = new int[m];
        matchR = new int[n];
        dist = new int[m];
        it = new int[m];
        Arrays.fill(matchL, -1);
        Arrays.fill(matchR, -1);
        int size = 0;
        while (layer()) {
            Arrays.fill(it, 0);
            for (int v = 0; v < m; v++) {
                if (matchL[v] < 0 && augment(v)) {
                    size++;
                }
            }
        }
        // a minimum edge cover takes a maximum matching and one more edge for
        // every vertex the matching leaves uncovered
        System.out.println(m + n - size);
    }
}
