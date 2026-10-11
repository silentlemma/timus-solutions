import java.io.*;

public class Main {
    static final int THREE = 3;
    static final int BUFFER = 1 << 15;
    static final InputStream in = System.in;
    static final byte[] buf = new byte[BUFFER];
    static int len = 0, pos = 0;

    // the next byte of input, or -1 at its end
    static int read() throws IOException {
        if (pos == len) {
            len = in.read(buf, 0, BUFFER);
            pos = 0;
            if (len <= 0)
                return -1;
        }
        return buf[pos++];
    }

    static int readInt() throws IOException {
        int c = read();
        while (c < '0' || c > '9')
            c = read();
        int v = 0;
        for (; c >= '0' && c <= '9'; c = read())
            v = v * 10 + (c - '0');
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        // every dark region is a rectangle exactly when no 2 x 2 window holds
        // three dark cells, so two rows are enough, and the image never fits
        // in 4 MB anyway
        int[] prev = new int[m], cur = new int[m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int c = read();
                while (c != '0' && c != '1')
                    c = read();
                cur[j] = c - '0';
                if (i > 0 && j > 0 && prev[j - 1] + prev[j] + cur[j - 1] + cur[j] == THREE) {
                    System.out.println("No");
                    return;
                }
            }
            int[] t = prev;
            prev = cur;
            cur = t;
        }
        System.out.println("Yes");
    }
}
