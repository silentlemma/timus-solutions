import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    // x' = SHEAR x + y keeps all points apart and no segment vertical
    static final long SHEAR = 20001;
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

    static long[] fx, fy, tx, ty, ax, ay, bx, by; // original ends, sheared ends sorted by x

    static int sign(long v) { return Long.signum(v); }

    static int orient(long px, long py, long qx, long qy, long rx, long ry) {
        return sign((qx - px) * (ry - py) - (qy - py) * (rx - px));
    }

    static boolean onBox(long px, long py, long qx, long qy, long rx, long ry) {
        return Math.min(px, qx) <= rx && rx <= Math.max(px, qx) && Math.min(py, qy) <= ry &&
            ry <= Math.max(py, qy);
    }

    // closed segments i and j share a point
    static boolean touch(int i, int j) {
        int o1 = orient(fx[i], fy[i], tx[i], ty[i], fx[j], fy[j]);
        int o2 = orient(fx[i], fy[i], tx[i], ty[i], tx[j], ty[j]);
        int o3 = orient(fx[j], fy[j], tx[j], ty[j], fx[i], fy[i]);
        int o4 = orient(fx[j], fy[j], tx[j], ty[j], tx[i], ty[i]);
        if (o1 * o2 < 0 && o3 * o4 < 0)
            return true;
        return (o1 == 0 && onBox(fx[i], fy[i], tx[i], ty[i], fx[j], fy[j])) ||
            (o2 == 0 && onBox(fx[i], fy[i], tx[i], ty[i], tx[j], ty[j])) ||
            (o3 == 0 && onBox(fx[j], fy[j], tx[j], ty[j], fx[i], fy[i])) ||
            (o4 == 0 && onBox(fx[j], fy[j], tx[j], ty[j], tx[i], ty[i]));
    }

    // the sign of the height of segment i above point (px, py), at px
    static int side(int i, long px, long py) {
        return sign(ay[i] * (bx[i] - ax[i]) + (by[i] - ay[i]) * (px - ax[i]) -
                    py * (bx[i] - ax[i]));
    }

    static boolean slopeLess(int i, int j) {
        return (by[i] - ay[i]) * (bx[j] - ax[j]) < (by[j] - ay[j]) * (bx[i] - ax[i]);
    }

    static void meet(int i, int j) {
        if (touch(i, j)) {
            System.out.println("YES\n" + (i + 1) + " " + (j + 1));
            System.exit(0);
        }
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        fx = new long[n];
        fy = new long[n];
        tx = new long[n];
        ty = new long[n];
        ax = new long[n];
        ay = new long[n];
        bx = new long[n];
        by = new long[n];
        long[] events = new long[2 * n]; // x, then 0 for a start or 1 for an end, then the segment
        for (int i = 0; i < n; i++) {
            fx[i] = readInt();
            fy[i] = readInt();
            tx[i] = readInt();
            ty[i] = readInt();
            long x1 = SHEAR * fx[i] + fy[i], x2 = SHEAR * tx[i] + ty[i];
            boolean swap = x2 < x1;
            ax[i] = swap ? x2 : x1;
            ay[i] = swap ? ty[i] : fy[i];
            bx[i] = swap ? x1 : x2;
            by[i] = swap ? fy[i] : ty[i];
            events[2 * i] = pack(ax[i], 0, i);
            events[2 * i + 1] = pack(bx[i], 1, i);
        }
        // Shamos-Hoey: sweep a vertical line over the sheared plane, keep the
        // segments it crosses ordered by height, and test only neighbours
        Arrays.sort(events);
        int[] line = new int[n];
        int size = 0;
        for (long ev : events) {
            int i = (int)(ev & ITEM), kind = (int)(ev >> KIND_SHIFT & 1);
            if (kind == 0) {
                int l = 0, h = size;
                while (l < h) {
                    int mid = (l + h) / 2, c = side(line[mid], ax[i], ay[i]);
                    if (c < 0 || (c == 0 && slopeLess(line[mid], i)))
                        l = mid + 1;
                    else
                        h = mid;
                }
                System.arraycopy(line, l, line, l + 1, size - l);
                line[l] = i;
                size++;
                if (l > 0)
                    meet(i, line[l - 1]);
                if (l + 1 < size)
                    meet(i, line[l + 1]);
            } else {
                int l = 0, h = size;
                while (l < h) {
                    int mid = (l + h) / 2;
                    if (side(line[mid], bx[i], by[i]) < 0)
                        l = mid + 1;
                    else
                        h = mid;
                }
                int k = l;
                while (k < size && line[k] != i)
                    k++;
                if (k == size)
                    for (k = 0; line[k] != i; k++)
                        ;
                System.arraycopy(line, k + 1, line, k, size - k - 1);
                size--;
                if (k > 0 && k < size)
                    meet(line[k - 1], line[k]);
            }
        }
        System.out.println("NO");
    }

    // events sort by x, then starts before ends; x' fits in 40 bits after an offset
    static final int KIND_SHIFT = 20;
    static final long ITEM = (1 << KIND_SHIFT) - 1;
    static final long OFFSET = 1L << 32;

    static long pack(long x, int kind, int item) {
        return (x + OFFSET) << (KIND_SHIFT + 1) | (long)kind << KIND_SHIFT | item;
    }
}
