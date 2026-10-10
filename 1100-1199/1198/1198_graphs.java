import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    static final int BUFFER = 1 << 16;
    static InputStream in = System.in;
    static byte[] buf = new byte[BUFFER];
    static int bufLen = 0, bufPos = 0;

    static int readChar() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, BUFFER);
            bufPos = 0;
            if (bufLen <= 0) {
                return -1;
            }
        }
        return buf[bufPos++];
    }

    static int readInt() throws IOException {
        int c = readChar();
        while (c != -1 && (c < '0' || c > '9')) {
            c = readChar();
        }
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + c - '0';
            c = readChar();
        }
        return v;
    }

    // Marks everything reachable from root that is not marked yet; returns
    // how many vertices it marked.
    static int search(int root, int[] start, int[] edges, boolean[] seen) {
        int[] queue = new int[seen.length];
        int tail = 0;
        queue[tail++] = root;
        seen[root] = true;
        for (int head = 0; head < tail; head++) {
            int u = queue[head];
            for (int e = start[u]; e < start[u + 1]; e++) {
                if (!seen[edges[e]]) {
                    seen[edges[e]] = true;
                    queue[tail++] = edges[e];
                }
            }
        }
        return tail;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] start = new int[n + 1];
        int[] edges = new int[BUFFER];
        int m = 0;
        for (int i = 0; i < n; i++) {
            for (int v = readInt(); v != 0; v = readInt()) {
                if (m == edges.length) {
                    edges = Arrays.copyOf(edges, 2 * m);
                }
                edges[m++] = v - 1;
            }
            start[i + 1] = m;
        }
        // the reverse graph in the same compact form, built by counting
        int[] rstart = new int[n + 1];
        int[] redges = new int[m];
        for (int e = 0; e < m; e++) {
            rstart[edges[e] + 1]++;
        }
        for (int i = 0; i < n; i++) {
            rstart[i + 1] += rstart[i];
        }
        int[] fill = Arrays.copyOf(rstart, n);
        for (int u = 0; u < n; u++) {
            for (int e = start[u]; e < start[u + 1]; e++) {
                redges[fill[edges[e]]++] = u;
            }
        }

        // nobody outside the marked set can reach the root of the last search,
        // so that root lies in a strongly connected component with no way in
        boolean[] seen = new boolean[n];
        int root = 0;
        for (int u = 0; u < n; u++) {
            if (!seen[u]) {
                root = u;
                search(u, start, edges, seen);
            }
        }
        StringBuilder out = new StringBuilder();
        if (search(root, start, edges, new boolean[n]) == n) {
            boolean[] backward = new boolean[n];
            search(root, rstart, redges, backward);
            for (int u = 0; u < n; u++) {
                if (backward[u]) {
                    out.append(u + 1).append(' ');
                }
            }
        }
        out.append("0\n");
        System.out.print(out);
    }
}
