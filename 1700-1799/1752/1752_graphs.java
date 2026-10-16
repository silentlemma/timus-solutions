import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;

public class Main {
    static int n, q;
    static int[] head, nxt, to, askHead, askNext, askDist, answer, depth, path, stack;

    // walk the tree from root in preorder: when a vertex is reached, path holds
    // its ancestors by depth, so a query at it with d <= depth is answered at
    // once; returns the deepest vertex
    static int walk(int root) {
        Arrays.fill(depth, -1);
        depth[root] = 0;
        int deepest = root, top = 0;
        stack[top++] = root;
        while (top > 0) {
            int v = stack[--top];
            path[depth[v]] = v;
            if (depth[v] > depth[deepest]) deepest = v;
            for (int i = askHead[v]; i >= 0; i = askNext[i]) {
                if (answer[i] == 0 && askDist[i] <= depth[v]) {
                    answer[i] = path[depth[v] - askDist[i]];
                }
            }
            for (int e = head[v]; e >= 0; e = nxt[e]) {
                if (depth[to[e]] < 0) {
                    depth[to[e]] = depth[v] + 1;
                    stack[top++] = to[e];
                }
            }
        }
        return deepest;
    }

    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        n = in.nextInt();
        q = in.nextInt();
        head = new int[n + 1];
        Arrays.fill(head, -1);
        nxt = new int[2 * n];
        to = new int[2 * n];
        int edges = 0;
        for (int i = 0; i < n - 1; i++) {
            int a = in.nextInt(), b = in.nextInt();
            to[edges] = b;
            nxt[edges] = head[a];
            head[a] = edges++;
            to[edges] = a;
            nxt[edges] = head[b];
            head[b] = edges++;
        }
        askHead = new int[n + 1];
        Arrays.fill(askHead, -1);
        askNext = new int[q];
        askDist = new int[q];
        answer = new int[q];
        for (int i = 0; i < q; i++) {
            int v = in.nextInt();
            askDist[i] = in.nextInt();
            askNext[i] = askHead[v];
            askHead[v] = i;
        }
        depth = new int[n + 1];
        path = new int[n + 1];
        stack = new int[n + 1];
        // the farthest vertex from any vertex is an end of a diameter, and the
        // walk from vertex 1 ends at one end, the walk from there at the other
        int a = walk(1);
        int b = walk(a);
        walk(b);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) sb.append(answer[i]).append('\n');
        PrintWriter out = new PrintWriter(System.out);
        out.print(sb);
        out.flush();
    }

    static class Reader {
        private static final int SIZE = 1 << 16;
        private final DataInputStream stream = new DataInputStream(System.in);
        private final byte[] buffer = new byte[SIZE];
        private int length, pointer;

        private int read() throws IOException {
            if (pointer == length) {
                length = stream.read(buffer, 0, SIZE);
                pointer = 0;
                if (length <= 0) return -1;
            }
            return buffer[pointer++];
        }

        int nextInt() throws IOException {
            int c = read();
            while (c != -1 && (c < '0' || c > '9')) c = read();
            int x = 0;
            while (c >= '0' && c <= '9') {
                x = x * 10 + (c - '0');
                c = read();
            }
            return x;
        }
    }
}
