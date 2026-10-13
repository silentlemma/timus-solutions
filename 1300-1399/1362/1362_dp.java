import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int BUFFER_SIZE = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER_SIZE];
    static int bufLen = 0, bufPos = 0;

    static int readByte() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, buf.length);
            bufPos = 0;
            if (bufLen <= 0)
                return -1;
        }
        return buf[bufPos++];
    }

    static int readInt() throws IOException {
        int c = readByte();
        while (c != -1 && (c < '0' || c > '9'))
            c = readByte();
        int n = 0;
        for (; c >= '0' && c <= '9'; c = readByte())
            n = n * 10 + (c - '0');
        return n;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        // adjacency as linked lists in arrays: head, next and target per edge end
        int[] head = new int[n + 1], next = new int[2 * n], to = new int[2 * n];
        Arrays.fill(head, -1);
        int edges = 0;
        for (int boss = 1; boss <= n; boss++)
            for (int v = readInt(); v != 0; v = readInt()) {
                to[edges] = v;
                next[edges] = head[boss];
                head[boss] = edges++;
                to[edges] = boss;
                next[edges] = head[v];
                head[v] = edges++;
            }
        int root = readInt();
        // calls go both up and down, so the news spreads over the tree rooted
        // at Tanya; order parents before children
        int[] parent = new int[n + 1], order = new int[n];
        parent[root] = -1;
        order[0] = root;
        int size = 1;
        for (int i = 0; i < size; i++) {
            int v = order[i];
            for (int e = head[v]; e >= 0; e = next[e])
                if (to[e] != parent[v]) {
                    parent[to[e]] = v;
                    order[size++] = to[e];
                }
        }
        // the time of v is what it needs to tell its whole subtree; the slowest
        // subtrees are called first, the i-th call starting at minute i
        int[] time = new int[n + 1], kidCount = new int[n + 1];
        for (int v = 1; v <= n; v++)
            if (parent[v] > 0)
                kidCount[parent[v]]++;
        int[][] kids = new int[n + 1][];
        for (int v = 1; v <= n; v++)
            kids[v] = new int[kidCount[v]];
        int[] filled = new int[n + 1];
        for (int i = size - 1; i >= 0; i--) {
            int v = order[i];
            int[] times = kids[v];
            Arrays.sort(times);
            for (int j = 0; j < times.length; j++)
                time[v] = Math.max(time[v], times[times.length - 1 - j] + j + 1);
            if (parent[v] > 0)
                kids[parent[v]][filled[parent[v]]++] = time[v];
        }
        System.out.println(time[root]);
    }
}
