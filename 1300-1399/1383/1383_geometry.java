import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    // a pair of frame coordinates, each below 2^24 in size, packed into one
    // long whose order is the order of the pairs
    static final long HALF = 1L << 24;
    static final long SPAN = 1L << 25;
    // a point packed the same way, for sorting the input points
    static final int SHIFT_POINT = 1 << 11;
    static final int POINT_SPAN = 1 << 12;
    static final int KIND_SAME = 0, KIND_LINE = 1, KIND_PLANE = 2;

    static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    static int compare(long[] a, long[] b) {
        for (int i = 0; i < a.length && i < b.length; i++)
            if (a[i] != b[i])
                return Long.compare(a[i], b[i]);
        return Integer.compare(a.length, b.length);
    }

    static long cross(long ox, long oy, long ax, long ay, long bx, long by) {
        return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox);
    }

    static int hullSize;
    static long[] hx = new long[0], hy = new long[0];

    // strict convex hull, counterclockwise, of sorted distinct points
    static void hull(long[] px, long[] py, int n) {
        if (hx.length < 2 * n + 1) {
            hx = new long[2 * n + 1];
            hy = new long[2 * n + 1];
        }
        int k = 0;
        for (int i = 0; i < n; i++) {
            while (k >= 2 && cross(hx[k - 2], hy[k - 2], hx[k - 1], hy[k - 1], px[i], py[i]) <= 0)
                k--;
            hx[k] = px[i];
            hy[k++] = py[i];
        }
        int low = k + 1;
        for (int i = n - 2; i >= 0; i--) {
            while (k >= low && cross(hx[k - 2], hy[k - 2], hx[k - 1], hy[k - 1], px[i], py[i]) <= 0)
                k--;
            hx[k] = px[i];
            hy[k++] = py[i];
        }
        hullSize = k - 1;
    }

    // the points in the frame at hull vertex i (it to 0, the next vertex to
    // (1, 0), the previous to (0, 1)) over their common denominator: the
    // denominator, then the packed pairs of the hull from i or of all points
    static long[] frameKey(int i, long[] px, long[] py, int n, boolean all) {
        int k = hullSize;
        long ox = hx[i], oy = hy[i];
        long ax = hx[(i + 1) % k] - ox, ay = hy[(i + 1) % k] - oy;
        long bx = hx[(i + k - 1) % k] - ox, by = hy[(i + k - 1) % k] - oy;
        long d = ax * by - ay * bx, g = d;
        int count = all ? n : k;
        long[] s = new long[count], t = new long[count];
        for (int j = 0; j < count; j++) {
            long qx = all ? px[j] - ox : hx[(i + j) % k] - ox;
            long qy = all ? py[j] - oy : hy[(i + j) % k] - oy;
            s[j] = qx * by - qy * bx;
            t[j] = ax * qy - ay * qx;
            g = gcd(g, gcd(s[j], t[j]));
        }
        long[] key = new long[1 + count];
        key[0] = d / g;
        for (int j = 0; j < count; j++)
            key[1 + j] = (s[j] / g + HALF) * SPAN + (t[j] / g + HALF);
        if (all)
            Arrays.sort(key, 1, key.length);
        return key;
    }

    // the same for two point lists exactly when an affine map of positive
    // determinant takes one onto the other
    static long[] canonical(int[] xs, int[] ys, int m) {
        long[] packed = new long[m];
        for (int i = 0; i < m; i++)
            packed[i] = (long)(xs[i] + SHIFT_POINT) * POINT_SPAN + (ys[i] + SHIFT_POINT);
        Arrays.sort(packed);
        long[] px = new long[m], py = new long[m];
        int n = 0;
        for (int i = 0; i < m; i++)
            if (i == 0 || packed[i] != packed[i - 1]) {
                px[n] = packed[i] / POINT_SPAN - SHIFT_POINT;
                py[n++] = packed[i] % POINT_SPAN - SHIFT_POINT;
            }
        if (n == 1)
            return new long[] {KIND_SAME, m};
        hull(px, py, n);
        int k = hullSize;
        long[] ax = new long[m], ay = new long[m];
        for (int i = 0; i < m; i++) {
            ax[i] = xs[i];
            ay[i] = ys[i];
        }
        if (k == 2) {
            // on one line: positions from 0 to 1 between the ends, read either way
            long dx = hx[1] - hx[0], dy = hy[1] - hy[0];
            long length = dx * dx + dy * dy, g = length;
            long[] forward = new long[m], backward = new long[m];
            for (int i = 0; i < m; i++) {
                forward[i] = (ax[i] - hx[0]) * dx + (ay[i] - hy[0]) * dy;
                g = gcd(g, forward[i]);
            }
            long den = length / g;
            for (int i = 0; i < m; i++) {
                forward[i] /= g;
                backward[i] = den - forward[i];
            }
            Arrays.sort(forward);
            Arrays.sort(backward);
            long[] pick = compare(backward, forward) < 0 ? backward : forward;
            long[] key = new long[2 + m];
            key[0] = KIND_LINE;
            key[1] = den;
            System.arraycopy(pick, 0, key, 2, m);
            return key;
        }
        // first the hull alone in every frame, then all points in the frames
        // where the hull looks smallest: symmetric hulls tie
        long[] best = null;
        long[][] shapes = new long[k][];
        for (int i = 0; i < k; i++) {
            shapes[i] = frameKey(i, px, py, n, false);
            if (best == null || compare(shapes[i], best) < 0)
                best = shapes[i];
        }
        long[] chosen = null;
        for (int i = 0; i < k; i++)
            if (compare(shapes[i], best) == 0) {
                long[] candidate = frameKey(i, ax, ay, m, true);
                if (chosen == null || compare(candidate, chosen) < 0)
                    chosen = candidate;
            }
        long[] key = new long[2 + chosen.length];
        key[0] = KIND_PLANE;
        key[1] = k;
        System.arraycopy(chosen, 0, key, 2, chosen.length);
        return key;
    }

    static class Key {
        final long[] a;
        final int hash;

        Key(long[] a) {
            this.a = a;
            hash = Arrays.hashCode(a);
        }

        @Override
        public int hashCode() {
            return hash;
        }

        @Override
        public boolean equals(Object o) {
            return o instanceof Key && Arrays.equals(a, ((Key)o).a);
        }
    }

    static DataInputStream in = new DataInputStream(System.in);
    static final int BUFFER = 1 << 16;
    static byte[] buf = new byte[BUFFER];
    static int len, pos;

    static int readByte() throws IOException {
        if (pos == len) {
            len = in.read(buf, 0, buf.length);
            pos = 0;
            if (len <= 0)
                return -1;
        }
        return buf[pos++];
    }

    static int readInt() throws IOException {
        int c = readByte();
        while (c != '-' && (c < '0' || c > '9'))
            c = readByte();
        boolean negative = c == '-';
        if (negative)
            c = readByte();
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = readByte();
        }
        return negative ? -v : v;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        Map<Key, List<Integer>> classes = new HashMap<>();
        Map<Key, Integer> sizes = new HashMap<>();
        List<Key> keys = new ArrayList<>();
        for (int project = 1; project <= n; project++) {
            int m = readInt();
            int[] xs = new int[m], ys = new int[m];
            for (int i = 0; i < m; i++) {
                xs[i] = readInt();
                ys[i] = readInt();
            }
            Key key = new Key(canonical(xs, ys, m));
            List<Integer> members = classes.get(key);
            if (members == null) {
                members = new ArrayList<>();
                classes.put(key, members);
                sizes.put(key, m);
                keys.add(key);
            }
            members.add(project);
        }
        // smaller projects first, then by the first project of the class
        keys.sort((a, b)
                      -> sizes.get(a).equals(sizes.get(b))
                             ? Integer.compare(classes.get(a).get(0), classes.get(b).get(0))
                             : Integer.compare(sizes.get(a), sizes.get(b)));
        StringBuilder out = new StringBuilder();
        out.append(keys.size()).append('\n');
        for (Key key : keys) {
            for (int project : classes.get(key))
                out.append(project).append(' ');
            out.append("0\n");
        }
        System.out.print(out);
    }
}
