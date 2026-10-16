import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final long FAR = 1L << 40;
    static int n, s, size;
    static int[] latest;
    static long[] leftPart, rightPart;

    // the cost of a lane comes from the latest obstacle covering it, as
    // min(left[t] + x, right[t] - x), or from the start as |x - s| if none
    static long cost(int x) {
        int t = 0;
        for (int node = x + size; node > 0; node >>= 1) t = Math.max(t, latest[node]);
        if (t == 0) return Math.abs(x - s);
        return Math.min(leftPart[t] + x, rightPart[t] - x);
    }

    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        n = in.nextInt();
        s = in.nextInt();
        int k = in.nextInt();
        size = 1;
        while (size <= n) size *= 2;
        // latest[node]: the last obstacle whose lanes cover the node's whole range
        latest = new int[2 * size];
        leftPart = new long[k + 1];
        rightPart = new long[k + 1];
        for (int t = 1; t <= k; t++) {
            int lo = in.nextInt(), hi = in.nextInt();
            // the cost stays one per lane apart, so going round the obstacle
            // only needs the lanes just beside it
            long below = lo > 1 ? cost(lo - 1) : FAR, above = hi < n ? cost(hi + 1) : FAR;
            leftPart[t] = below - (lo - 1);
            rightPart[t] = above + hi + 1;
            for (int a = lo + size, b = hi + size + 1; a < b; a >>= 1, b >>= 1) {
                if ((a & 1) == 1) latest[a++] = t;
                if ((b & 1) == 1) latest[--b] = t;
            }
        }
        long best = FAR;
        for (int x = 1; x <= n; x++) best = Math.min(best, cost(x));
        System.out.println(best);
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
