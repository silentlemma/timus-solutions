import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int BUFFER_SIZE = 4096;
    static final long INF = 1L << 60;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;
    static int read() throws IOException {
        if (position >= available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int nextInt() throws IOException {
        int c = read(), value = 0;
        while (c <= ' ')
            c = read();
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }
    static byte nextKind() throws IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        byte kind = (byte)c;
        while (read() > ' ') {
        }
        return kind;
    }
    public static void main(String[] args) throws IOException {
        int n = nextInt(), m = nextInt();
        int[] head = new int[n], to = new int[m], link = new int[m], weight = new int[m];
        byte[] kind = new byte[m];
        Arrays.fill(head, -1);
        for (int i = 0; i < m; i++) {
            int x = nextInt() - 1;
            to[i] = nextInt() - 1;
            weight[i] = nextInt();
            kind[i] = nextKind();
            link[i] = head[x];
            head[x] = i;
        }
        long[] clean = new long[n], dirty = new long[n];
        Arrays.fill(clean, INF);
        Arrays.fill(dirty, INF);
        clean[0] = 0;
        for (int v = 0; v < n; v++) {
            long licensed = clean[v], pirated = dirty[v];
            for (int edge = head[v]; edge != -1; edge = link[edge]) {
                int y = to[edge], cost = weight[edge];
                if (kind[edge] == 'P')
                    dirty[y] = Math.min(dirty[y], Math.min(licensed, pirated) + cost);
                else {
                    clean[y] = Math.min(clean[y], licensed + cost);
                    if (kind[edge] == 'C')
                        dirty[y] = Math.min(dirty[y], pirated + cost);
                }
            }
        }
        long answer = Math.min(clean[n - 1], dirty[n - 1]);
        System.out.println(answer == INF ? "Offline" : "Online\n" + answer);
    }
}
