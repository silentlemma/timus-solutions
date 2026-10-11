import java.io.*;
import java.util.*;

public class Main {
    static final int CORNERS = 3;

    static long cross(long[] o, long[] a, long[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    static long dot(long[] n, long[] p) { return n[0] * p[0] + n[1] * p[1]; }

    // convex hull, counterclockwise, without points on the edges
    static List<long[]> hull(List<long[]> pts) {
        pts.sort((a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1]));
        List<long[]> h = new ArrayList<>();
        for (long[] p : pts) {
            while (h.size() >= 2 && cross(h.get(h.size() - 2), h.get(h.size() - 1), p) <= 0)
                h.remove(h.size() - 1);
            h.add(p);
        }
        for (int i = pts.size() - 2, t = h.size() + 1; i >= 0; i--) {
            while (h.size() >= t &&
                   cross(h.get(h.size() - 2), h.get(h.size() - 1), pts.get(i)) <= 0)
                h.remove(h.size() - 1);
            h.add(pts.get(i));
        }
        h.remove(h.size() - 1);
        return h;
    }

    // an open convex polygon: the places where the tanker hits a ship
    static class Polygon {
        long[][] v;
        long x0, x1, y0, y1;
        long[][] normals, ranges;

        Polygon(List<long[]> vertices) {
            v = vertices.toArray(new long[0][]);
            x0 = x1 = v[0][0];
            y0 = y1 = v[0][1];
            for (long[] p : v) {
                x0 = Math.min(x0, p[0]);
                x1 = Math.max(x1, p[0]);
                y0 = Math.min(y0, p[1]);
                y1 = Math.max(y1, p[1]);
            }
            normals = new long[v.length][];
            ranges = new long[v.length][];
            for (int i = 0; i < v.length; i++) {
                long[] a = v[i], b = v[(i + 1) % v.length];
                normals[i] = new long[] {b[1] - a[1], a[0] - b[0]};
                ranges[i] = project(normals[i]);
            }
        }

        long[] project(long[] n) {
            long lo = dot(n, v[0]), hi = lo;
            for (long[] p : v) {
                lo = Math.min(lo, dot(n, p));
                hi = Math.max(hi, dot(n, p));
            }
            return new long[] {lo, hi};
        }

        // whether p is strictly inside
        boolean holds(long[] p) {
            for (int i = 0; i < v.length; i++)
                if (cross(v[i], v[(i + 1) % v.length], p) <= 0)
                    return false;
            return true;
        }

        // whether the segment pq crosses the inside: no axis separates them,
        // neither an edge normal nor the normal of pq itself
        boolean blocks(long[] p, long[] q) {
            if (Math.max(p[0], q[0]) <= x0 || Math.min(p[0], q[0]) >= x1)
                return false;
            if (Math.max(p[1], q[1]) <= y0 || Math.min(p[1], q[1]) >= y1)
                return false;
            for (int i = 0; i < v.length; i++) {
                long a = dot(normals[i], p), b = dot(normals[i], q);
                if (Math.max(a, b) <= ranges[i][0] || Math.min(a, b) >= ranges[i][1])
                    return false;
            }
            long[] n = {q[1] - p[1], p[0] - q[0]};
            long c = dot(n, p);
            long[] range = project(n);
            return range[0] < c && c < range[1];
        }
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        List<Long> all = new ArrayList<>();
        while (in.nextToken() != StreamTokenizer.TT_EOF)
            all.add((long)in.nval);
        Iterator<Long> it = all.iterator();
        long dx = it.next(), dy = it.next();
        long[][] tanker = new long[CORNERS][];
        for (int i = 0; i < CORNERS; i++)
            tanker[i] = new long[] {it.next(), it.next()};
        long[] goal = {it.next(), it.next()};
        int n = (int)(long)it.next();
        // the tanker is placed by its first corner; offsets of all corners
        long[] start = tanker[0];
        long xlo = 0, xhi = dx, ylo = 0, yhi = dy;
        List<long[]> offsets = new ArrayList<>();
        for (long[] t : tanker) {
            long[] o = {t[0] - start[0], t[1] - start[1]};
            offsets.add(o);
            xlo = Math.max(xlo, -o[0]);
            xhi = Math.min(xhi, dx - o[0]);
            ylo = Math.max(ylo, -o[1]);
            yhi = Math.min(yhi, dy - o[1]);
        }
        List<Polygon> polygons = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            List<long[]> sums = new ArrayList<>();
            long[][] ship = new long[CORNERS][];
            for (int k = 0; k < CORNERS; k++)
                ship[k] = new long[] {it.next(), it.next()};
            for (long[] s : ship)
                for (long[] o : offsets)
                    sums.add(new long[] {s[0] - o[0], s[1] - o[1]});
            polygons.add(new Polygon(hull(sums)));
        }
        final long fxlo = xlo, fxhi = xhi, fylo = ylo, fyhi = yhi;
        java.util.function.Predicate<long[]> free = p -> {
            if (p[0] < fxlo || p[0] > fxhi || p[1] < fylo || p[1] > fyhi)
                return false;
            for (Polygon g : polygons)
                if (g.holds(p))
                    return false;
            return true;
        };
        if (!free.test(goal)) {
            System.out.println(-1);
            return;
        }
        if (goal[0] == start[0] && goal[1] == start[1]) {
            System.out.println("0.000");
            return;
        }
        // shortest paths bend only at corners of the forbidden polygons
        List<long[]> points = new ArrayList<>(Arrays.asList(start, goal));
        Set<String> seen = new HashSet<>();
        for (Polygon g : polygons)
            for (long[] v : g.v)
                if (free.test(v) && seen.add(v[0] + " " + v[1]))
                    points.add(v);
        int m = points.size();
        double[] dist = new double[m];
        boolean[] done = new boolean[m];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[0] = 0;
        while (true) {
            int i = -1;
            for (int j = 0; j < m; j++)
                if (!done[j] && dist[j] < Double.POSITIVE_INFINITY && (i < 0 || dist[j] < dist[i]))
                    i = j;
            if (i < 0 || i == 1)
                break;
            done[i] = true;
            long[] p = points.get(i);
            for (int j = 0; j < m; j++) {
                long[] q = points.get(j);
                if (done[j] || (q[0] == p[0] && q[1] == p[1]))
                    continue;
                double nd = dist[i] + Math.hypot(q[0] - p[0], q[1] - p[1]);
                if (nd >= dist[j])
                    continue;
                boolean clear = true;
                for (Polygon g : polygons)
                    if (g.blocks(p, q)) {
                        clear = false;
                        break;
                    }
                if (clear)
                    dist[j] = nd;
            }
        }
        if (dist[1] < Double.POSITIVE_INFINITY)
            System.out.println(String.format(Locale.ROOT, "%.3f", dist[1]));
        else
            System.out.println(-1);
    }
}
