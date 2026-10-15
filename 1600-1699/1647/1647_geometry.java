import java.util.*;

public class Main {
    static final int CORNERS = 3;
    static final int ROUNDS = 200; // bisection steps, far beyond double precision
    static double[][] pts = new double[CORNERS][];
    static double[] sides = new double[CORNERS];
    static double perimeter;
    static List<double[]> marks = new ArrayList<>(); // arc, x, y of corners, twice round

    static double shoelace(List<double[]> poly) {
        double twice = 0;
        for (int i = 0; i < poly.size(); i++) {
            double[] a = poly.get((i + poly.size() - 1) % poly.size()), b = poly.get(i);
            twice += a[0] * b[1] - b[0] * a[1];
        }
        return Math.abs(twice) / 2;
    }

    // the coast point at arc length s from the first corner
    static double[] point(double s) {
        s %= perimeter;
        for (int i = 0; i < CORNERS; i++) {
            if (s <= sides[i] || i == CORNERS - 1) {
                double t = Math.min(s / sides[i], 1);
                double[] a = pts[i], b = pts[(i + 1) % CORNERS];
                return new double[] {a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t};
            }
            s -= sides[i];
        }
        return pts[0];
    }

    // area cut off by the coast from s to t (s < t) and the chord
    static double area(double s, double t) {
        List<double[]> poly = new ArrayList<>();
        poly.add(point(s));
        for (double[] m : marks)
            if (s < m[0] && m[0] < t)
                poly.add(new double[] {m[1], m[2]});
        poly.add(point(t));
        return shoelace(poly);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for (int i = 0; i < CORNERS; i++)
            pts[i] = new double[] {in.nextInt(), in.nextInt()};
        for (int i = 0; i < CORNERS; i++) {
            double[] a = pts[i], b = pts[(i + 1) % CORNERS];
            sides[i] = Math.hypot(b[0] - a[0], b[1] - a[1]);
            perimeter += sides[i];
        }
        double pos = 0;
        for (int lap = 0; lap < 2; lap++)
            for (int i = 0; i < CORNERS; i++) {
                marks.add(new double[] {pos, pts[i][0], pts[i][1]});
                pos += sides[i];
            }
        double half = perimeter / 2, total = shoelace(Arrays.asList(pts));
        // the excess changes sign over half a turn, as the other part is the
        // complement, so a chord splitting both evenly always exists
        double lo = 0, hi = half;
        boolean low = area(lo, lo + half) - total / 2 > 0;
        for (int r = 0; r < ROUNDS; r++) {
            double mid = (lo + hi) / 2;
            if ((area(mid, mid + half) - total / 2 > 0) == low)
                lo = mid;
            else
                hi = mid;
        }
        double s = (lo + hi) / 2;
        double[] a = point(s), b = point(s + half);
        System.out.println("YES");
        for (double[] p : new double[][] {a, b})
            System.out.println(String.format(Locale.US, "%.12f %.12f", p[0], p[1]));
    }
}
