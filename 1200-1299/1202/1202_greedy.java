import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int BUFFER = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int bufLen = 0, bufPos = 0;

    static int readByte() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, BUFFER);
            bufPos = 0;
            if (bufLen <= 0) {
                return -1;
            }
        }
        return buf[bufPos++];
    }

    static long readLong() throws IOException {
        int c = readByte();
        while (c != '-' && (c < '0' || c > '9')) {
            c = readByte();
        }
        long sign = 1, v = 0;
        if (c == '-') {
            sign = -1;
            c = readByte();
        }
        while (c >= '0' && c <= '9') {
            v = v * 10 + c - '0';
            c = readByte();
        }
        return sign * v;
    }

    public static void main(String[] args) throws IOException {
        int n = (int)readLong();
        long y = 1, vertical = 0, low = 0, high = 0, right = 0;
        boolean blocked = false;
        for (int i = 0; i < n; i++) {
            readLong();
            long y1 = readLong(), x2 = readLong(), y2 = readLong();
            if (i > 0 && !blocked) {
                // the rectangles form a chain from left to right, so the
                // horizontal part is fixed; only the height at each border varies
                long lo = Math.max(low, y1) + 1, hi = Math.min(high, y2) - 1;
                if (lo > hi) {
                    blocked = true;
                } else {
                    // moving only when forced is optimal: clamp into the crossing
                    long target = Math.min(Math.max(y, lo), hi);
                    vertical += Math.abs(target - y);
                    y = target;
                }
            }
            low = y1;
            high = y2;
            right = x2;
        }
        System.out.println(blocked ? -1 : right - 2 + vertical + Math.abs(high - 1 - y));
    }
}
