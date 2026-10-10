import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int TIME = 30000, BUFFER = 1 << 16;
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

    static int readInt() throws IOException {
        int c = readByte();
        while (c < '0' || c > '9') {
            c = readByte();
        }
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + c - '0';
            c = readByte();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        // the latest start among the talks that end at each minute
        int[] latest = new int[TIME + 1];
        for (int i = 0; i < n; i++) {
            int s = readInt(), e = readInt();
            latest[e] = Math.max(latest[e], s);
        }
        // take the talk that ends first among those starting after the last one
        int count = 0, last = 0;
        for (int e = 1; e <= TIME; e++) {
            if (latest[e] > last) {
                count++;
                last = e;
            }
        }
        System.out.println(count);
    }
}
