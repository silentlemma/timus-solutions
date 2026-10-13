import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int BUFFER = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int bufLen = 0, bufPos = 0;

    static int read() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, BUFFER);
            bufPos = 0;
            if (bufLen <= 0)
                return -1;
        }
        return buf[bufPos++];
    }

    static int readInt() throws IOException {
        int c = read();
        while (c < '0' || c > '9')
            c = read();
        int x = 0;
        for (; c >= '0' && c <= '9'; c = read())
            x = x * 10 + c - '0';
        return x;
    }

    static int[] depth;

    static int shallower(int a, int b) { return depth[a] <= depth[b] ? a : b; }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] us = new int[n - 1], vs = new int[n - 1], ws = new int[n - 1];
        int[] start = new int[n + 1];
        for (int i = 0; i + 1 < n; i++) {
            us[i] = readInt();
            vs[i] = readInt();
            ws[i] = readInt();
            start[us[i] + 1]++;
            start[vs[i] + 1]++;
        }
        // adjacency lists packed into one array (both directions of each edge)
        for (int i = 0; i < n; i++)
            start[i + 1] += start[i];
        int[] fill = Arrays.copyOf(start, n);
        int[] adj = new int[2 * (n - 1)], weight = new int[2 * (n - 1)];
        for (int i = 0; i + 1 < n; i++) {
            adj[fill[us[i]]] = vs[i];
            weight[fill[us[i]]++] = ws[i];
            adj[fill[vs[i]]] = us[i];
            weight[fill[vs[i]]++] = ws[i];
        }

        // Euler tour from vertex 0: a vertex is written on entry and after each child
        int[] parent = new int[n], dist = new int[n], first = new int[n];
        depth = new int[n];
        Arrays.fill(parent, -1);
        int[] tour = new int[2 * n - 1], stack = new int[n];
        int[] pointer = Arrays.copyOf(start, n);
        int len = 1, top = 1;
        while (top > 0) {
            int v = stack[top - 1];
            int p = pointer[v];
            if (p < start[v + 1]) {
                pointer[v]++;
                int u = adj[p];
                if (u == parent[v])
                    continue;
                parent[u] = v;
                depth[u] = depth[v] + 1;
                dist[u] = dist[v] + weight[p];
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
