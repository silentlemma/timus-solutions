import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int BUFFER = 1 << 16, BASE = 10;

    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int len = 0, pos = 0;

    // the next byte of the input, or -1 at its end; the input is a few megabytes
    static int nextByte() throws IOException {
        if (pos == len) {
            len = in.read(buf, 0, BUFFER);
            pos = 0;
            if (len <= 0) {
                return -1;
            }
        }
        return buf[pos++];
    }

    static boolean isDigit(int c) { return c >= '0' && c <= '9'; }

    // the next digit, skipping spaces and line breaks
    static int nextDigit() throws IOException {
        int c = nextByte();
        while (c != -1 && !isDigit(c)) {
            c = nextByte();
        }
        return c - '0';
    }

    public static void main(String[] args) throws IOException {
        int n = 0, c = nextByte();
        while (!isDigit(c)) {
            c = nextByte();
        }
        for (; isDigit(c); c = nextByte()) {
            n = n * BASE + (c - '0');
        }
        // column sums from 0 to 18, then the carries from the last column up
        byte[] out = new byte[n + 1];
        out[n] = '\n';
        for (int i = 0; i < n; i++) {
            int a = nextDigit();
            out[i] = (byte)(a + nextDigit());
        }
        int carry = 0;
        for (int i = n - 1; i >= 0; i--) {
            int t = out[i] + carry;
            carry = t / BASE;
            out[i] = (byte)('0' + t % BASE);
        }
        System.out.write(out, 0, out.length);
        System.out.flush();
    }
}
