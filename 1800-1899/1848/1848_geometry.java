import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;

public class Main {
    static final int BUFFER_SIZE = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buffer = new byte[BUFFER_SIZE];
    static int length;
    static int index;

    static int read() throws IOException {
        if (index == length) {
            length = in.read(buffer, 0, BUFFER_SIZE);
            index = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[index++];
    }

    static long number() throws IOException {
        int c = read();
        while (c != '-' && (c < '0' || c > '9')) {
            c = read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = read();
        }
        long v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = read();
        }
        return negative ? -v : v;
    }

    // an edge from its left end to its right end, or a fly when both ends meet
    static final class Item {
        final long lx;
        final long ly;
        final long rx;
        final long ry;
        final int polygon;
        final boolean top; // the inside lies below the edge

        Item(long lx, long ly, long rx, long ry, int polygon, boolean top) {
            this.lx = lx;
            this.ly = ly;
            this.rx = rx;
            this.ry = ry;
            this.polygon = polygon;
            this.top = top;
        }

        boolean point() {
            return lx == rx;
        }
    }

    // where s lies against t, both crossing the sweep line just right of its
    // position: -1 below, 1 above, 0 the same edge or a fly on it. The
    // comparison uses the end of one that lies over the other.
    static int side(Item s, Item t) {
        if (t.point() || (!s.point() && s.lx < t.lx)) {
            return -side(t, s);
        }
        long tx = t.rx - t.lx;
        long ty = t.ry - t.ly;
        long c = tx * (s.ly - t.ly) - ty * (s.lx - t.lx);
        if (c == 0 && !s.point()) {
            // two edges of one polygon from a common left end
            c = tx * (s.ry - t.ly) - ty * (s.rx - t.lx);
        }
        return Long.signum(c);
    }

    static long key(long x, long y) {
        return x * (1L << Integer.SIZE) + y;
    }

    public static void main(String[] args) throws IOException {
        int n = (int) number();
        long[] fx = new long[n];
        long[] fy = new long[n];
        for (int i = 0; i < n; i++) {
            fx[i] = number();
            fy[i] = number();
        }
        int m = (int) number();
        Map<Long, Integer> corners = new HashMap<>(); // vertex -> polygon
        // vertical edges by their x: low y, high y and polygon
        Map<Long, List<long[]>> upright = new HashMap<>();
        List<Item> edges = new ArrayList<>();
        for (int p = 0; p < m; p++) {
            int k = (int) number();
            long[] xs = new long[k];
            long[] ys = new long[k];
            for (int i = 0; i < k; i++) {
                xs[i] = number();
                ys[i] = number();
            }
            for (int i = 0; i < k; i++) {
                long ax = xs[(i + k - 1) % k];
                long ay = ys[(i + k - 1) % k];
                long bx = xs[i];
                long by = ys[i];
                corners.put(key(bx, by), p);
                if (ax == bx) {
                    long[] span = {Math.min(ay, by), Math.max(ay, by), p};
                    upright.computeIfAbsent(ax, z -> new ArrayList<>()).add(span);
                    continue;
                }
                // counter-clockwise: the inside is left of the edge, so an
                // edge running right to left has the inside below it
                if (ax > bx) {
                    edges.add(new Item(bx, by, ax, ay, p, true));
                } else {
                    edges.add(new Item(ax, ay, bx, by, p, false));
                }
            }
        }
        for (List<long[]> spans : upright.values()) {
            spans.sort(Comparator.comparingLong(s -> s[0]));
        }
        Item[] starts = edges.toArray(new Item[0]);
        Item[] ends = starts.clone();
        Arrays.sort(starts, Comparator.comparingLong(s -> s.lx));
        Arrays.sort(ends, Comparator.comparingLong(s -> s.rx));
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            order[i] = i;
        }
        Arrays.sort(order, Comparator.comparingLong(i -> fx[i]));
        TreeSet<Item> active = new TreeSet<>(Main::side);
        int[] count = new int[m];
        int e = starts.length;
        int si = 0;
        int ei = 0;
        for (int f : order) {
            long x = fx[f];
            long y = fy[f];
            // sweep every event column up to x; in a column, edges ending
            // there leave before edges starting there come in
            while (true) {
                long column = x + 1;
                if (si < e) {
                    column = Math.min(column, starts[si].lx);
                }
                if (ei < e) {
                    column = Math.min(column, ends[ei].rx);
                }
                if (column > x) {
                    break;
                }
                for (; ei < e && ends[ei].rx == column; ei++) {
                    active.remove(ends[ei]);
                }
                for (; si < e && starts[si].lx == column; si++) {
                    active.add(starts[si]);
                }
            }
            Integer corner = corners.get(key(x, y));
            if (corner != null) {
                count[corner]++;
                continue;
            }
            List<long[]> spans = upright.get(x);
            if (spans != null) {
                int lo = 0;
                int hi = spans.size();
                while (lo < hi) {
                    int mid = (lo + hi) >>> 1;
                    if (spans.get(mid)[0] <= y) {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }
                if (lo > 0 && spans.get(lo - 1)[1] >= y) {
                    count[(int) spans.get(lo - 1)[2]]++;
                    continue;
                }
            }
            Item fly = new Item(x, y, x, y, -1, false);
            Item edge = active.ceiling(fly);
            if (edge != null && (edge.top || side(fly, edge) == 0)) {
                count[edge.polygon]++;
            }
        }
        StringBuilder out = new StringBuilder();
        for (int c : count) {
            out.append(c).append('\n');
        }
        System.out.print(out);
    }
}
