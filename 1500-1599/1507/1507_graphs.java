import java.io.*;

public class Main {
    static class Input {
        private static final int BUFFER_SIZE = 256, BYTE_MASK = 255;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position, length;
        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length <= 0)
                    return -1;
            }
            return buffer[position++] & BYTE_MASK;
        }
        int number() throws IOException {
            int c = read();
            while (c >= 0 && c <= ' ')
                c = read();
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return sign * value;
        }
    }

    static boolean reachesAll(long[] edges) {
        long seen = 1, pending = 1;
        while (pending != 0) {
            int vertex = Long.numberOfTrailingZeros(pending);
            pending &= pending - 1;
            long fresh = edges[vertex] & ~seen;
            seen |= fresh;
            pending |= fresh;
        }
        return seen == (1L << edges.length) - 1;
    }
    public static void main(String[] args) throws IOException {
        Input in = new Input();
        int n = in.number();
        long[] forward = new long[n], reverse = new long[n];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                if (in.number() != 0) {
                    forward[i] |= 1L << j;
                    reverse[j] |= 1L << i;
                }
            }
        System.out.println(reachesAll(forward) && reachesAll(reverse) ? "Yes" : "No");
    }
}
