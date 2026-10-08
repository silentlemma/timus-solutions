import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int BUFFER = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buffer = new byte[BUFFER];
    static int length, pos;

    static int read() throws IOException {
        if (pos == length) {
            length = in.read(buffer, 0, BUFFER);
            pos = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[pos++];
    }

    static long nextLong() throws IOException {
        int c = read();
        while (c != '-' && (c < '0' || c > '9')) {
            c = read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = read();
        }
        long v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = read();
        }
        return negative ? -v : v;
    }

    public static void main(String[] args) throws IOException {
        int n = (int)nextLong();
        long prev = nextLong(), best = -1;
        int a = 1;
        // the slope of a chord is the mean of the slopes of the steps under it,
        // so the steepest valid chord joins two neighbours; take the first one
        for (int x = 2; x <= n; x++) {
            long cur = nextLong();
            if (Math.abs(cur - prev) > best) {
                best = Math.abs(cur - prev);
                a = x - 1;
            }
            prev = cur;
        }
        System.out.println(a + " " + (a + 1));
    }
}
