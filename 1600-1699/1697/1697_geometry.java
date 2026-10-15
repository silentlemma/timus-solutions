import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    // a building is lx ly rx ry h
    static final int FIELDS = 5;
    static final int RY = 3;
    static final int HEIGHT = 4;

    // corners of a polygon with an inside
    static final int AREA = 3;
    static final int SIDES = 4; // the wall constraints come first

    // a gap is the open interval from LO_N / LO_D to HI_N / HI_D
    static final int LO_N = 0;
    static final int LO_D = 1;
    static final int HI_N = 2;
    static final int HI_D = 3;

    static StreamTokenizer in;

    static long next() throws IOException {
        in.nextToken();
        return (long) in.nval;
    }

    // the open interval of t for which the shot from S to
    // A + t (B - A) passes through the inside of the box, or null: a point of the
    // shot is S + u (A - S) + v (B - A) with v = u t, a convex polygon in (u, v)
    static long[] blockedInterval(long[] s, long[] a, long[] b, long[] box) {
        long ax = a[0] - s[0];
        long ay = a[1] - s[1];
        long dx = b[0] - a[0];
        long dy = b[1] - a[1];
        // closed half-planes p u + q v >= c: two strips, 0 <= u <= 1, -1 <= t <= 2
        List<long[]> cons = new ArrayList<>();
        cons.add(new long[] {ax, dx, box[0] - s[0]});
        cons.add(new long[] {-ax, -dx, s[0] - box[2]});
        cons.add(new long[] {ay, dy, box[1] - s[1]});
        cons.add(new long[] {-ay, -dy, s[1] - box[RY]});
        cons.add(new long[] {1, 0, 0});
        cons.add(new long[] {-1, 0, -1});
        cons.add(new long[] {1, 1, 0});
        cons.add(new long[] {2, -1, 0});
        for (int i = 0; i < SIDES; i++) {
            long[] w = cons.get(i);
            if (w[0] == 0 && w[1] == 0 && w[2] >= 0) {
                return null; // the plane of the shots holds a wall or misses the box
            }
        }
        if (s[2] > 0) {
            cons.add(new long[] {s[2], 0, s[2] - box[HEIGHT]}); // below the roof
        }
        List<long[]> corners = new ArrayList<>();
        for (int i = 0; i < cons.size(); i++) {
            for (int j = i + 1; j < cons.size(); j++) {
                long[] f = cons.get(i);
                long[] g = cons.get(j);
                long den = f[0] * g[1] - g[0] * f[1];
                if (den == 0) {
                    continue;
                }
                long u = f[2] * g[1] - g[2] * f[1];
                long v = f[0] * g[2] - g[0] * f[2];
                if (den < 0) {
                    den = -den;
                    u = -u;
                    v = -v;
                }
                boolean fits = true;
                for (long[] h : cons) {
                    fits &= h[0] * u + h[1] * v >= h[2] * den;
                }
                for (long[] k : corners) {
                    fits &= !(u * k[2] == k[0] * den && v * k[2] == k[1] * den);
                }
                if (fits) {
                    corners.add(new long[] {u, v, den});
                }
            }
        }
        // the polygon has an inside exactly when it has three different corners
        if (corners.size() < AREA) {
            return null;
        }
        // t = v / u, and u > 0 at every corner, as S is outside the box
        long[] first = corners.get(0);
        long[] gap = {first[1], first[0], first[1], first[0]};
        for (long[] k : corners) {
            if (k[1] * gap[LO_D] < gap[LO_N] * k[0]) {
                gap[LO_N] = k[1];
                gap[LO_D] = k[0];
            }
            if (k[1] * gap[HI_D] > gap[HI_N] * k[0]) {
                gap[HI_N] = k[1];
                gap[HI_D] = k[0];
            }
        }
        return gap;
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        long[] s = {next(), next(), next()};
        long[] a = {next(), next()};
        long[] b = {next(), next()};
        int n = (int) next();
        List<long[]> gaps = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            long[] box = new long[FIELDS];
            for (int j = 0; j < FIELDS; j++) {
                box[j] = next();
            }
            long[] gap = blockedInterval(s, a, b, box);
            if (gap != null) {
                gaps.add(gap);
            }
        }
        // the free times form a closed set whose first point is 0 or the right
        // end of some blocked interval
        List<long[]> candidates = new ArrayList<>();
        candidates.add(new long[] {0, 1});
        for (long[] g : gaps) {
            if (0 <= g[HI_N] && g[HI_N] <= g[HI_D]) {
                candidates.add(new long[] {g[HI_N], g[HI_D]});
            }
        }
        candidates.sort((f, g) -> Long.compare(f[0] * g[1], g[0] * f[1]));
        for (long[] c : candidates) {
            boolean free = true;
            for (long[] g : gaps) {
                free &= !(g[LO_N] * c[1] < c[0] * g[LO_D] && c[0] * g[HI_D] < g[HI_N] * c[1]);
            }
            if (free) {
                double t = (double) c[0] / c[1];
                System.out.println(String.format(Locale.US, "%.10f %.10f",
                        a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t));
                return;
            }
        }
        System.out.println("Impossible");
    }
}
