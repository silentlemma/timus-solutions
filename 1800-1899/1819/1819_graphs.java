import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.HashMap;

public class Main {
    // splitmix64 with a fixed seed
    static final long SEED = 2010, GAMMA = 0x9e3779b97f4a7c15L;
    static final long MIX1 = 0xbf58476d1ce4e5b9L, MIX2 = 0x94d049bb133111ebL;
    static final int SHIFT1 = 30, SHIFT2 = 27, SHIFT3 = 31, BUFFER = 1 << 16;
    static long state = SEED;

    static long nextRandom() {
        state += GAMMA;
        long z = state;
        z = (z ^ (z >>> SHIFT1)) * MIX1;
        z = (z ^ (z >>> SHIFT2)) * MIX2;
        return z ^ (z >>> SHIFT3);
    }

    static InputStream in = new BufferedInputStream(System.in, BUFFER);

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0') {
            c = in.read();
        }
        int v = 0;
        while (c >= '0') {
            v = v * 10 + c - '0';
            c = in.read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt(), k = readInt();
        // half-edge h runs from ends[h] to ends[h ^ 1], and the half-edges
        // of a vertex are chained through head and nxt
        int[] ends = new int[2 * k], head = new int[n], nxt = new int[2 * k];
        Arrays.fill(head, -1);
        for (int h = 0; h < 2 * k; h++) {
            ends[h] = readInt() - 1;
            nxt[h] = head[ends[h]];
            head[ends[h]] = h;
        }
        int[] comp = new int[n], tin = new int[n], parent = new int[n], upEdge = new int[n];
        Arrays.fill(comp, -1);
        Arrays.fill(parent, -1);
        Arrays.fill(upEdge, -1);
        int[] order = new int[n], stack = new int[n], it = head.clone();
        int seen = 0;
        for (int root = 0; root < n; root++) {
            if (comp[root] >= 0) {
                continue;
            }
            comp[root] = root;
            tin[root] = seen;
            order[seen++] = root;
            int top = 0;
            stack[top++] = root;
            while (top > 0) {
                int v = stack[top - 1], h = it[v];
                if (h < 0) {
                    top--;
                    continue;
                }
                it[v] = nxt[h];
                int w = ends[h ^ 1];
                if (comp[w] < 0) {
                    comp[w] = root;
                    parent[w] = v;
                    upEdge[w] = h >> 1;
                    tin[w] = seen;
                    order[seen++] = w;
                    stack[top++] = w;
                }
            }
        }
        // every non-tree edge joins a vertex and its ancestor; mark it with
        // a random value at both ends, so after summing over subtrees the
        // edge above v carries the xor of the non-tree edges passing over it
        long[] cover = new long[n];
        int[] count = new int[n];
        for (int e = 0; e < k; e++) {
            int a = ends[2 * e], b = ends[2 * e + 1];
            if (upEdge[a] == e || upEdge[b] == e) {
                continue;
            }
            if (tin[a] < tin[b]) {
                int t = a;
                a = b;
                b = t;
            }
            long r = nextRandom();
            cover[a] ^= r;
            cover[b] ^= r;
            count[a]++;
            count[b]--;
        }
        for (int i = n - 1; i >= 0; i--) {
            int v = order[i], p = parent[v];
            if (p >= 0) {
                cover[p] ^= cover[v];
                count[p] += count[v];
            }
        }
        // a pair of edges is a cut exactly when it is a tree edge covered by
        // nothing but that non-tree edge, or two tree edges covered by the
        // same set; values make a path xor to zero iff it crosses no cut
        long[] value = new long[n];
        HashMap<Long, Integer> first = new HashMap<>();
        for (int v : order) {
            if (parent[v] < 0) {
                continue;
            }
            if (count[v] < 2) {
                // a bridge or an edge with one cover: crossing it separates
                value[v] = nextRandom();
                continue;
            }
            // edges with one cover set lie on a chain and cut the tree into
            // pieces closed into a ring; a path inside the ring crosses all
            // of them or none of them, so the class must xor to zero
            Integer rep = first.putIfAbsent(cover[v], v);
            if (rep != null) {
                value[v] = nextRandom();
                value[rep] ^= value[v];
            }
        }
        long[] label = new long[n];
        for (int v : order) {
            if (parent[v] >= 0) {
                label[v] = label[parent[v]] ^ value[v];
            }
        }
        int q = readInt();
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int a = readInt() - 1, b = readInt() - 1;
            out.append(comp[a] == comp[b] && label[a] == label[b] ? "Yes\n" : "No\n");
        }
        System.out.print(out);
    }
}
