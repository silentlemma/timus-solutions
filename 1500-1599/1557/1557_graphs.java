import java.io.*;
import java.util.*;

public class Main {
    static final long GOLDEN = 0x9E3779B97F4A7C15L;
    static final long MIX1 = 0xBF58476D1CE4E5B9L, MIX2 = 0x94D049BB133111EBL;
    static final int SHIFT1 = 30, SHIFT2 = 27, SHIFT3 = 31;

    // a splitmix64 step: well-spread 64-bit labels from a counter
    static long mix(long x) {
        x += GOLDEN;
        x = (x ^ (x >>> SHIFT1)) * MIX1;
        x = (x ^ (x >>> SHIFT2)) * MIX2;
        return x ^ (x >>> SHIFT3);
    }

    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(new BufferedInputStream(System.in));
        int n = readInt(in), m = readInt(in);
        int[] from = new int[m], to = new int[m], degree = new int[n + 1];
        for (int e = 0; e < m; e++) {
            from[e] = readInt(in) - 1;
            to[e] = readInt(in) - 1;
            degree[from[e]]++;
            degree[to[e]]++;
        }
        // the arcs of server v are arcs[start[v]] .. arcs[start[v + 1] - 1]
        int[] start = new int[n + 1], fill = new int[n], arcTo = new int[2 * m],
              arcEdge = new int[2 * m];
        for (int v = 0; v < n; v++)
            start[v + 1] = start[v] + degree[v];
        for (int e = 0; e < m; e++) {
            int a = start[from[e]] + fill[from[e]]++, b = start[to[e]] + fill[to[e]]++;
            arcTo[a] = to[e];
            arcEdge[a] = e;
            arcTo[b] = from[e];
            arcEdge[b] = e;
        }
        // a spanning tree in breadth-first order
        int[] parent = new int[n], parentEdge = new int[n], order = new int[n];
        boolean[] seen = new boolean[n], inTree = new boolean[m];
        int size = 1;
        seen[0] = true;
        for (int i = 0; i < size; i++) {
            int v = order[i];
            for (int a = start[v]; a < start[v + 1]; a++) {
                int u = arcTo[a];
                if (!seen[u]) {
                    seen[u] = true;
                    parent[u] = v;
                    parentEdge[u] = arcEdge[a];
                    inTree[arcEdge[a]] = true;
                    order[size++] = u;
                }
            }
        }
        // every other channel gets a random label; a tree channel gets the XOR
        // of the labels of the channels whose cycles pass through it, which is
        // the XOR over the subtree below it
        long[] label = new long[m], below = new long[n];
        for (int e = 0; e < m; e++)
            if (!inTree[e]) {
                label[e] = mix(e);
                below[from[e]] ^= label[e];
                below[to[e]] ^= label[e];
            }
        for (int i = n - 1; i > 0; i--) {
            int v = order[i];
            label[parentEdge[v]] = below[v];
            below[parent[v]] ^= below[v];
        }
        // a bridge (label 0) cuts with any other channel; two other channels cut
        // together exactly when no cycle passes through just one of them
        long bridges = 0;
        for (long x : label)
            if (x == 0)
                bridges++;
        long rest = m - bridges;
        long total = (long)m * (m - 1) / 2 - rest * (rest - 1) / 2;
        Arrays.sort(label);
        for (int i = 0, j = 0; i < m; i = j) {
            while (j < m && label[j] == label[i])
                j++;
            if (label[i] != 0)
                total += (long)(j - i) * (j - i - 1) / 2;
        }
        System.out.println(total);
    }

    static int readInt(DataInputStream in) throws IOException {
        int c = in.read();
        while (c < '0')
            c = in.read();
        int x = 0;
        while (c >= '0') {
            x = x * 10 + c - '0';
            c = in.read();
        }
        return x;
    }
}
