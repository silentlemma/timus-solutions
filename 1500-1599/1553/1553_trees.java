import java.io.*;
import java.util.*;

public class Main {
    static int width;
    static long[] tree;

    // the largest level at the places lo to hi of the chains
    static long segMax(int lo, int hi) {
        long best = 0;
        for (lo += width, hi += width + 1; lo < hi; lo >>= 1, hi >>= 1) {
            if ((lo & 1) == 1)
                best = Math.max(best, tree[lo++]);
            if ((hi & 1) == 1)
                best = Math.max(best, tree[--hi]);
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer st =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();
        int n = (int)st.nval;
        int[] from = new int[n - 1], to = new int[n - 1], degree = new int[n + 2];
        for (int i = 0; i < n - 1; i++) {
            st.nextToken();
            from[i] = (int)st.nval;
            st.nextToken();
            to[i] = (int)st.nval;
            degree[from[i]]++;
            degree[to[i]]++;
        }
        // neighbours of v are adj[start[v]] .. adj[start[v + 1] - 1]
        int[] start = new int[n + 2], adj = new int[2 * (n - 1)], fill = new int[n + 2];
        for (int v = 1; v <= n; v++)
            start[v + 1] = start[v] + degree[v];
        for (int i = 0; i < n - 1; i++) {
            adj[start[from[i]] + fill[from[i]]++] = to[i];
            adj[start[to[i]] + fill[to[i]]++] = from[i];
        }
        // heavy-light decomposition: every cave's heavy child continues its chain,
        // and the chains lie consecutively in one segment tree of maxima
        int[] parent = new int[n + 1], depth = new int[n + 1], order = new int[n];
        parent[1] = -1;
        order[0] = 1;
        for (int i = 0, end = 1; i < n; i++) {
            int v = order[i];
            for (int k = start[v]; k < start[v + 1]; k++) {
                int u = adj[k];
                if (u != parent[v]) {
                    parent[u] = v;
                    depth[u] = depth[v] + 1;
                    order[end++] = u;
                }
            }
        }
        int[] size = new int[n + 1], heavy = new int[n + 1];
        Arrays.fill(size, 1);
        for (int i = n - 1; i > 0; i--) {
            int v = order[i], p = parent[v];
            size[p] += size[v];
            if (heavy[p] == 0 || size[v] > size[heavy[p]])
                heavy[p] = v;
        }
        int[] head = new int[n + 1], index = new int[n + 1];
        int next = 0;
        for (int v : order)
            if (v == 1 || heavy[parent[v]] != v)
                for (int u = v; u != 0; u = heavy[u]) {
                    head[u] = v;
                    index[u] = next++;
                }
        width = 1;
        while (width < n)
            width *= 2;
        tree = new long[2 * width];
        st.nextToken();
        int q = (int)st.nval;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < q; i++) {
            st.nextToken();
            boolean increase = st.sval.equals("I");
            st.nextToken();
            int u = (int)st.nval;
            st.nextToken();
            int v = (int)st.nval;
            if (increase) {
                int at = index[u] + width;
                tree[at] += v;
                for (at >>= 1; at > 0; at >>= 1)
                    tree[at] = Math.max(tree[2 * at], tree[2 * at + 1]);
                continue;
            }
            long best = 0;
            while (head[u] != head[v]) {
                if (depth[head[u]] < depth[head[v]]) {
                    int t = u;
                    u = v;
                    v = t;
                }
                best = Math.max(best, segMax(index[head[u]], index[u]));
                u = parent[head[u]];
            }
            best =
                Math.max(best, segMax(Math.min(index[u], index[v]), Math.max(index[u], index[v])));
            out.append(best).append('\n');
        }
        System.out.print(out);
    }
}
