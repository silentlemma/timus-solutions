import java.io.*;
import java.util.Arrays;
public class Main {
    static final int OUTPUT_BUFFER = 8192;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static int width;
    static int[] tree;
    static int segmentMax(int left, int right) {
        int best = 0;
        for (left += width, right += width + 1; left < right; left >>= 1, right >>= 1) {
            if ((left & 1) != 0)
                best = Math.max(best, tree[left++]);
            if ((right & 1) != 0)
                best = Math.max(best, tree[--right]);
        }
        return best;
    }
    public static void main(String[] args) throws Exception {
        int n = nextInt();
        width = n;
        int[] first = new int[n], to = new int[2 * n], link = new int[2 * n - 2];
        Arrays.fill(first, -1);
        for (int i = 0; i < n - 1; i++) {
            int a = nextInt() - 1, b = nextInt() - 1, j = 2 * i;
            to[j] = b;
            link[j] = first[a];
            first[a] = j;
            to[j + 1] = a;
            link[j + 1] = first[b];
            first[b] = j + 1;
        }
        int[] parent = new int[n], depth = new int[n], order = new int[n], size = new int[n];
        Arrays.fill(parent, -1);
        Arrays.fill(size, 1);
        for (int i = 0, end = 1; i < n; i++) {
            int v = order[i];
            for (int e = first[v]; e != -1; e = link[e]) {
                int u = to[e];
                if (u != parent[v]) {
                    parent[u] = v;
                    depth[u] = depth[v] + 1;
                    order[end++] = u;
                }
            }
        }
        // Adjacency heads are dead after the traversal; reuse them for heavy children.
        int[] heavy = first;
        Arrays.fill(heavy, -1);
        for (int i = n - 1; i > 0; i--) {
            int v = order[i], p = parent[v];
            size[p] += size[v];
            if (heavy[p] == -1 || size[v] > size[heavy[p]])
                heavy[p] = v;
        }
        // Subtree sizes and traversal order are dead; chain numbering reuses both.
        int[] index = size, head = order;
        int next = 0;
        for (int v = 0; v < n; v++)
            if (v == 0 || heavy[parent[v]] != v) {
                for (int u = v; u != -1; u = heavy[u]) {
                    head[u] = v;
                    index[u] = next++;
                }
            }
        // Edge destinations are dead after chain construction; reuse their 2*n cells.
        tree = to;
        Arrays.fill(tree, 0);
        StringBuilder out = new StringBuilder(OUTPUT_BUFFER);
        int q = nextInt();
        while (q-- > 0) {
            int kind = read();
            while (kind <= ' ')
                kind = read();
            int u = nextInt() - 1, v = nextInt();
            if (kind == 'I') {
                int at = index[u] + n, value = tree[at] + v;
                tree[at] = value;
                // Monotonic values let an unchanged ancestor end propagation.
                for (at >>= 1; at > 0 && tree[at] < value; at >>= 1)
                    tree[at] = value;
                continue;
            }
            --v;
            int best = 0;
            while (head[u] != head[v]) {
                if (depth[head[u]] < depth[head[v]]) {
                    int swap = u;
                    u = v;
                    v = swap;
                }
                best = Math.max(best, segmentMax(index[head[u]], index[u]));
                u = parent[head[u]];
            }
            best = Math.max(best,
                            segmentMax(Math.min(index[u], index[v]), Math.max(index[u], index[v])));
            out.append(best).append('\n');
            if (out.length() >= OUTPUT_BUFFER) {
                System.out.print(out);
                out.setLength(0);
            }
        }
        System.out.print(out);
    }
}
