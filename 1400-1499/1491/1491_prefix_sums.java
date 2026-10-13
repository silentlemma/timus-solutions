import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int BUFFER = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int bufLen = 0, bufPos = 0;

    static int read() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, BUFFER);
            bufPos = 0;
            if (bufLen <= 0)
                return -1;
        }
        return buf[bufPos++];
    }

    static int readInt() throws IOException {
        int c = read();
        while (c < '0' || c > '9')
            c = read();
        int x = 0;
        for (; c >= '0' && c <= '9'; c = read())
            x = x * 10 + c - '0';
        return x;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        // every gift adds c to the knights a..b: mark it at both ends of the
        // range, then a running sum gives each knight's total
        long[] diff = new long[n + 2];
        for (int k = 0; k <= n; k++) {
            int a = readInt(), b = readInt();
            long c = readInt();
            diff[a] += c;
            diff[b + 1] -= c;
        }
        StringBuilder out = new StringBuilder();
        long total = 0;
        for (int i = 1; i <= n; i++) {
            total += diff[i];
            out.append(total).append(i < n ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
