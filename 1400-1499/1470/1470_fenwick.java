import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final int ADD = 1, ASK = 2; // record kinds; any other kind ends the input
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
        while (c != '-' && (c < '0' || c > '9'))
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        int x = 0;
        for (; c >= '0' && c <= '9'; c = read())
            x = x * 10 + c - '0';
        return negative ? -x : x;
    }

    static int n, side;
    static long[] tree; // a 3D Fenwick tree, indices from 1

    static void add(int x, int y, int z, long k) {
        for (int i = x; i <= n; i += i & -i)
            for (int j = y; j <= n; j += j & -j) {
                int row = (i * side + j) * side;
                for (int w = z; w <= n; w += w & -w)
                    tree[row + w] += k;
            }
    }

    static long prefix(int x, int y, int z) {
        long total = 0;
        for (int i = x; i > 0; i -= i & -i)
            for (int j = y; j > 0; j -= j & -j) {
                int row = (i * side + j) * side;
                for (int w = z; w > 0; w -= w & -w)
                    total += tree[row + w];
            }
        return total;
    }

    public static void main(String[] args) throws IOException {
        n = readInt();
        side = n + 1;
        tree = new long[side * side * side];
        StringBuilder out = new StringBuilder();
        while (true) {
            int kind = readInt();
            if (kind == ADD) {
                int x = readInt(), y = readInt(), z = readInt();
                add(x + 1, y + 1, z + 1, readInt());
            } else if (kind == ASK) {
                int x1 = readInt(), y1 = readInt(), z1 = readInt();
                int x2 = readInt() + 1, y2 = readInt() + 1, z2 = readInt() + 1;
                // inclusion and exclusion over the eight corners of the box
                long total = prefix(x2, y2, z2) - prefix(x1, y2, z2) - prefix(x2, y1, z2) -
                             prefix(x2, y2, z1) + prefix(x1, y1, z2) + prefix(x1, y2, z1) +
                             prefix(x2, y1, z1) - prefix(x1, y1, z1);
                out.append(total).append('\n');
            } else {
                break;
            }
        }
        System.out.print(out);
    }
}
