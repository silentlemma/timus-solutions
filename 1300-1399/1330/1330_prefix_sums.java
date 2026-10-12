import java.io.IOException;

public class Main {
    static final int BUFFER = 1 << 16;
    static byte[] buffer = new byte[BUFFER];
    static int length = 0, position = 0;

    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer, 0, BUFFER);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return buffer[position++];
    }

    static int next() throws IOException {
        int c = read();
        while (c != '-' && (c < '0' || c > '9')) {
            if (c < 0)
                return 0;
            c = read();
        }
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + (c - '0');
            c = read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        // before[i] is the sum of the first i readings
        long[] before = new long[n + 1];
        for (int i = 1; i <= n; i++)
            before[i] = before[i - 1] + next();
        int q = next();
        StringBuilder out = new StringBuilder();
        for (int t = 0; t < q; t++) {
            int i = next(), j = next();
            out.append(before[j] - before[i - 1]).append('\n');
        }
        System.out.print(out);
    }
}
