import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int CORNERS = 3, PINS = 4;
    static final double WIDE = 2 * Math.PI / 3; // 120 degrees
    static final double EPS = 1e-12;
    static final double ROOT3 = Math.sqrt(3) / 2; // the height of a unit equilateral triangle
    // the pairs that share an extra point, each way round
    static final int[][][] PAIRINGS = {{{0, 1}, {2, 3}}, {{0, 2}, {1, 3}}, {{0, 3}, {1, 2}},
                                       {{2, 3}, {0, 1}}, {{1, 3}, {0, 2}}, {{1, 2}, {0, 3}}};

    static double dist(double[] p, double[] q) { return Math.hypot(p[0] - q[0], p[1] - q[1]); }

    // the point with the least total distance to three points (see 1451)
    static double[] fermat(double[]... p) {
        for (int i = 0; i < CORNERS; i++)
            for (int j = i + 1; j < CORNERS; j++)
                if (dist(p[i], p[j]) < EPS)
                    return p[i];
        double[] angle = new double[CORNERS], side = new double[CORNERS];
        for (int i = 0; i < CORNERS; i++) {
            double[] a = p[i], b = p[(i + 1) % CORNERS], c = p[(i + 2) % CORNERS];
            double ux = b[0] - a[0], uy = b[1] - a[1], wx = c[0] - a[0], wy = c[1] - a[1];
            angle[i] = Math.atan2(Math.abs(ux * wy - uy * wx), ux * wx + uy * wy);
            side[i] = dist(b, c);
        }
        for (int i = 0; i < CORNERS; i++)
            if (angle[i] >= WIDE)
                return p[i];
        double total = 0, x = 0, y = 0;
        for (int i = 0; i < CORNERS; i++) {
            double w = side[i] / Math.sin(angle[i] + Math.PI / CORNERS);
            total += w;
            x += w * p[i][0];
            y += w * p[i][1];
        }
        return new double[] {x / total, y / total};
    }

    static double shortest(double[][] p) {
        // trees without extra points: the best spanning tree
        List<double[]> edges = new ArrayList<>();
        for (int i = 0; i < PINS; i++)
            for (int j = i + 1; j < PINS; j++)
                edges.add(new double[] {dist(p[i], p[j]), i, j});
        edges.sort((u, v) -> Double.compare(u[0], v[0]));
        int[] group = new int[PINS];
        for (int i = 0; i < PINS; i++)
            group[i] = i;
        double best = 0;
        for (double[] e : edges) {
            int a = (int)e[1], b = (int)e[2];
            while (group[a] != a)
                a = group[a];
            while (group[b] != b)
                b = group[b];
            if (a != b) {
                group[a] = b;
                best += e[0];
            }
        }
        // one extra point joining three pins, the fourth wired to one of the four
        for (int rest = 0; rest < PINS; rest++) {
            double[][] trio = new double[CORNERS][];
            int k = 0;
            for (int i = 0; i < PINS; i++)
                if (i != rest)
                    trio[k++] = p[i];
            double[] s = fermat(trio);
            double star = 0, link = dist(p[rest], s);
            for (double[] q : trio) {
                star += dist(s, q);
                link = Math.min(link, dist(p[rest], q));
            }
            best = Math.min(best, star + link);
        }
        // two extra points, {a, b} on one and {c, d} on the other: the Melzak
        // construction gives both, and the real length of that tree is a candidate
        for (int[][] pr : PAIRINGS) {
            double[] a = p[pr[0][0]], b = p[pr[0][1]], c = p[pr[1][0]], d = p[pr[1][1]];
            double mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
            double dx = b[0] - a[0], dy = b[1] - a[1];
            for (int side = 1; side >= -1; side -= 2) {
                double[] e = {mx - side * dy * ROOT3, my + side * dx * ROOT3};
                double[] s2 = fermat(e, c, d);
                double[] s1 = fermat(a, b, s2);
                double tree = dist(s1, a) + dist(s1, b) + dist(s1, s2) + dist(s2, c) + dist(s2, d);
                best = Math.min(best, tree);
            }
        }
        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int tests = in.nextInt();
        StringBuilder out = new StringBuilder();
        for (int t = 0; t < tests; t++) {
            double[][] p = new double[PINS][];
            for (int i = 0; i < PINS; i++)
                p[i] = new double[] {in.nextInt(), in.nextInt()};
            out.append(String.format(Locale.US, "%.6f%n", shortest(p)));
        }
        System.out.print(out);
    }
}
