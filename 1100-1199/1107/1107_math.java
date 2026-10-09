import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static DataInputStream in = new DataInputStream(System.in);
    static final int BUF_SIZE = 1 << 16;
    static byte[] buf = new byte[BUF_SIZE];
    static int len, pos;

    static int read() throws IOException {
        if (pos == len) {
            len = in.read(buf, 0, buf.length);
            pos = 0;
            if (len <= 0) {
                return -1;
            }
        }
        return buf[pos++];
    }

    static int readInt() throws IOException {
        int c = read();
        while (c < '0' || c > '9') {
            c = read();
        }
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + c - '0';
            c = read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt(), k = readInt();
        readInt();
        // removing an item changes the sum by 1..N and replacing one by -N+1..N-1,
        // never by a multiple of N + 1, so similar sets differ modulo N + 1
        StringBuilder out = new StringBuilder("YES\n");
        for (int i = 0; i < k; i++) {
            int count = readInt(), sum = 0;
            for (int j = 0; j < count; j++) {
                sum += readInt();
            }
            out.append(sum % (n + 1) + 1).append('\n');
        }
        System.out.print(out);
    }
}
