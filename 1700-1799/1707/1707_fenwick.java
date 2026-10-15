import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static final long MOD = 200904040963L; // the modulus of the hash printed for long experiments
    static final long BASE = 7;
    static final int SHORT = 20; // experiments up to this length are printed digit by digit
    static final int CORNERS = 4;
    static final int OPPOSITE = 3; // the corner (a - 1, c - 1) among the four of a step
    static final int BUFFER = 1 << 16;

    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buffer = new byte[BUFFER];
    static int filled = 0;
    static int at = 0;

    static int read() throws IOException {
        if (at == filled) {
            filled = in.read(buffer, 0, BUFFER);
            at = 0;
            if (filled <= 0) {
                return -1;
            }
        }
        return buffer[at++];
    }

    static long next() throws IOException {
        int ch = read();
        while (ch != '-' && (ch < '0' || ch > '9')) {
            ch = read();
        }
        boolean negative = ch == '-';
        if (negative) {
            ch = read();
        }
        long v = 0;
        while (ch >= '0' && ch <= '9') {
            v = v * 10 + (ch - '0');
            ch = read();
        }
        return negative ? -v : v;
    }

    static int wrap(long v, int n) {
        int r = (int) (v % n);
        return r < 0 ? r + n : r;
    }

    static int[] grow(int[] a, int size) {
        if (size < a.length) {
            return a;
        }
        int[] b = new int[a.length * 2];
        System.arraycopy(a, 0, b, 0, a.length);
        return b;
    }

    public static void main(String[] args) throws IOException {
        int n = (int) next();
        int m = (int) next();
        // the eyes' states are points (s, t); an experiment step asks whether a
        // rectangle holds one, answered by four prefix counts of a sweep over t
        int[][] xsByY = new int[n][2];
        int[] pointCount = new int[n];
        for (int l = 0; l < m; l++) {
            long s0 = next(), t0 = next(), ds = next(), dt = next();
            int k = (int) next();
            for (int i = 0; i < k; i++) {
                int y = wrap(t0 + i * dt, n);
                xsByY[y] = grow(xsByY[y], pointCount[y]);
                xsByY[y][pointCount[y]++] = wrap(s0 + i * ds, n);
            }
        }
        int p = (int) next();
        // per row t the asked x and the slot of its count, interleaved
        int[][] asksByY = new int[n][2];
        int[] askCount = new int[n];
        // count 0 is a fixed zero for the corners outside the grid
        int count = 1;
        int[] lengths = new int[p];
        int[][] cornerIds = new int[p][];
        for (int e = 0; e < p; e++) {
            long a0 = next(), b0 = next(), c0 = next(), d0 = next();
            long da = next(), db = next(), dc = next(), dd = next();
            int q = (int) next();
            lengths[e] = q;
            cornerIds[e] = new int[q * CORNERS];
            for (int j = 0; j < q; j++) {
                int a = wrap(a0 + j * da, n), b = wrap(b0 + j * db, n);
                int c = wrap(c0 + j * dc, n), d = wrap(d0 + j * dd, n);
                if (a > b) {
                    int swap = a;
                    a = b;
                    b = swap;
                }
                if (c > d) {
                    int swap = c;
                    c = d;
                    d = swap;
                }
                int[] xs = {b, a - 1, b, a - 1};
                int[] ys = {d, d, c - 1, c - 1};
                for (int r = 0; r < CORNERS; r++) {
                    if (xs[r] >= 0 && ys[r] >= 0) {
                        int y = ys[r];
                        asksByY[y] = grow(asksByY[y], askCount[y] + 1);
                        asksByY[y][askCount[y]++] = xs[r];
                        asksByY[y][askCount[y]++] = count;
                        cornerIds[e][j * CORNERS + r] = count++;
                    }
                }
            }
        }
        int[] below = new int[count]; // points with s <= x and t <= y for each asked corner
        int[] tree = new int[n + 1];
        for (int y = 0; y < n; y++) {
            for (int r = 0; r < pointCount[y]; r++) {
                for (int i = xsByY[y][r] + 1; i <= n; i += i & -i) {
                    tree[i]++;
                }
            }
            for (int r = 0; r < askCount[y]; r += 2) {
                int total = 0;
                for (int i = asksByY[y][r] + 1; i > 0; i -= i & -i) {
                    total += tree[i];
                }
                below[asksByY[y][r + 1]] = total;
            }
        }
        StringBuilder out = new StringBuilder();
        for (int e = 0; e < p; e++) {
            int[] c = cornerIds[e];
            char[] bits = new char[lengths[e]];
            for (int j = 0; j < lengths[e]; j++) {
                int r = j * CORNERS;
                int inside = below[c[r]] - below[c[r + 1]] - below[c[r + 2]]
                        + below[c[r + OPPOSITE]];
                bits[j] = inside > 0 ? '1' : '0';
            }
            if (lengths[e] <= SHORT) {
                out.append(bits);
            } else {
                long value = 0;
                for (int j = lengths[e] - 1; j >= 0; j--) {
                    value = (value * BASE + (bits[j] - '0')) % MOD;
                }
                out.append(value);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
