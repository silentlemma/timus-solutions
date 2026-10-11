import java.util.*;

public class Main {
    static final double EPS = 1e-9; // relative to the size of the tray
    static final int PLATES = 3;
    static double h, w, tol;
    static double[] radii = new double[PLATES];
    static int[] order = new int[PLATES];
    static double[][] pos = new double[PLATES][];

    static boolean fits(double[] p, double r) {
        return p[0] >= r - tol && p[0] <= h - r + tol && p[1] >= r - tol && p[1] <= w - r + tol;
    }

    // centres of a circle touching circles (a, ra) and (b, rb) from outside,
    // with ra and rb already increased by its radius
    static void touching(double[] a, double ra, double[] b, double rb, List<double[]> out) {
        double dx = b[0] - a[0], dy = b[1] - a[1], d2 = dx * dx + dy * dy;
        if (d2 == 0)
            return;
        double d = Math.sqrt(d2), x = (d2 + ra * ra - rb * rb) / (2 * d), h2 = (ra - x) * (ra + x);
        if (h2 < 0)
            return;
        double hh = Math.sqrt(h2), mx = a[0] + dx * x / d, my = a[1] + dy * x / d;
        out.add(new double[] {mx - dy * hh / d, my + dx * hh / d});
        out.add(new double[] {mx + dy * hh / d, my - dx * hh / d});
    }

    static boolean place(int k) {
        if (k == PLATES)
            return true;
        double r = radii[order[k]];
        double[] xs = {r, h - r}, ys = {r, w - r};
        List<double[]> cand = new ArrayList<>();
        for (double x : xs) {
            for (double y : ys)
                cand.add(new double[] {x, y}); // the four corners
        }
        for (int i = 0; i < k; i++) {
            double[] q = pos[order[i]];
            double s = radii[order[i]] + r;
            for (double x : xs) { // against a side wall and a placed plate
                double t = s * s - (x - q[0]) * (x - q[0]);
                if (t >= 0) {
                    cand.add(new double[] {x, q[1] - Math.sqrt(t)});
                    cand.add(new double[] {x, q[1] + Math.sqrt(t)});
                }
            }
            for (double y : ys) {
                double t = s * s - (y - q[1]) * (y - q[1]);
                if (t >= 0) {
                    cand.add(new double[] {q[0] - Math.sqrt(t), y});
                    cand.add(new double[] {q[0] + Math.sqrt(t), y});
                }
            }
            for (int j = 0; j < i; j++) { // against two placed plates
                touching(q, s, pos[order[j]], radii[order[j]] + r, cand);
            }
        }
        for (double[] p : cand) {
            if (!fits(p, r))
                continue;
            boolean ok = true;
            for (int i = 0; i < k && ok; i++) {
                double[] q = pos[order[i]];
                ok = Math.hypot(p[0] - q[0], p[1] - q[1]) >= r + radii[order[i]] - tol;
            }
            if (!ok)
                continue;
            pos[order[k]] = p;
            if (place(k + 1))
                return true;
        }
        return false;
    }

    static boolean permute(int n) {
        if (n == 1)
            return place(0);
        for (int i = 0; i < n; i++) { // Heap's algorithm over the orders
            if (permute(n - 1))
                return true;
            int a = n % 2 == 0 ? i : 0;
            int t = order[a];
            order[a] = order[n - 1];
            order[n - 1] = t;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        h = in.nextDouble();
        w = in.nextDouble();
        for (int i = 0; i < PLATES; i++)
            radii[i] = in.nextDouble();
        tol = EPS * (h + w);
        // pushing every plate down and to the left as far as it goes leaves each
        // one held by two walls or plates placed before it, so some order of the
        // plates and some choice of two such supports finds a placement
        for (int i = 0; i < PLATES; i++)
            order[i] = i;
        if (!permute(PLATES)) {
            System.out.println(0);
            return;
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < PLATES; i++) {
            out.append(i > 0 ? " " : "")
                .append(String.format(Locale.US, "%.4f %.4f", pos[i][0], pos[i][1]));
        }
        System.out.println(out);
    }
}
