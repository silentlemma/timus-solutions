import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    static final double EPS = 1e-9;

    static int n;
    static double[] xs, ys;

    // distance from an inner point to the fence, or -1 outside
    static double distanceToFence(double px, double py) {
        boolean inside = false;
        double best = Double.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            double ax = xs[i], ay = ys[i], bx = xs[(i + 1) % n], by = ys[(i + 1) % n];
            if ((ay > py) != (by > py) && px < ax + (py - ay) * (bx - ax) / (by - ay))
                inside = !inside;
            double dx = bx - ax, dy = by - ay;
            double t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy);
            t = Math.max(0, Math.min(1, t));
            best = Math.min(best, Math.hypot(px - ax - t * dx, py - ay - t * dy));
        }
        return inside ? best : -1;
    }

    // points o + t u whose distance to v equals base + slope t
    static void onCircle(double ox, double oy, double ux, double uy, double base, double slope,
                         double vx, double vy, List<double[]> out) {
        // |o + t u - v|^2 = (base + slope t)^2, or qa t^2 + 2 hb t + qc = 0
        double wx = ox - vx, wy = oy - vy;
        double qa = ux * ux + uy * uy - slope * slope;
        double hb = wx * ux + wy * uy - base * slope;
        double qc = wx * wx + wy * wy - base * base;
        double disc = hb * hb - qa * qc;
        if (disc < -EPS * (hb * hb + Math.abs(qa * qc)))
            return;
        // the stable form of the roots, also when qa is next to zero
        double q = -(hb + Math.copySign(Math.sqrt(Math.max(0, disc)), hb));
        if (Math.abs(qa) > EPS)
            out.add(new double[] {ox + q / qa * ux, oy + q / qa * uy});
        if (Math.abs(q) > EPS)
            out.add(new double[] {ox + qc / q * ux, oy + qc / q * uy});
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        xs = new double[n];
        ys = new double[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            xs[i] = in.nval;
            in.nextToken();
            ys[i] = in.nval;
        }
        // each edge as a line a x + b y + c, positive inside
        double[][] lines = new double[n][];
        for (int i = 0; i < n; i++) {
            double ax = xs[i], ay = ys[i], bx = xs[(i + 1) % n], by = ys[(i + 1) % n];
            double length = Math.hypot(bx - ax, by - ay);
            double a = -(by - ay) / length, b = (bx - ax) / length;
            lines[i] = new double[] {a, b, -(a * ax + b * ay)};
        }
        // only reflex vertices can be the nearest point of the fence from inside
        List<double[]> reflex = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int p = (i + n - 1) % n, r = (i + 1) % n;
            if ((xs[i] - xs[p]) * (ys[r] - ys[i]) - (ys[i] - ys[p]) * (xs[r] - xs[i]) < 0)
                reflex.add(new double[] {xs[i], ys[i]});
        }
        int k = reflex.size();
        List<double[]> cand = new ArrayList<>();
        // three lines: a_i x + b_i y + c_i = r for all three, by Cramer's rule
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int l = j + 1; l < n; l++) {
                    double[] p = lines[i], q = lines[j], s = lines[l];
                    double det =
                        p[0] * (q[1] - s[1]) - p[1] * (q[0] - s[0]) + (q[0] * s[1] - s[0] * q[1]);
                    if (Math.abs(det) < EPS)
                        continue;
                    double rx =
                        -p[2] * (q[1] - s[1]) - p[1] * (s[2] - q[2]) + (s[2] * q[1] - q[2] * s[1]);
                    double ry =
                        p[0] * (s[2] - q[2]) + p[2] * (q[0] - s[0]) + (s[0] * q[2] - q[0] * s[2]);
                    cand.add(new double[] {rx / det, ry / det});
                }
        // two lines and a reflex vertex: on the bisector, as far from the vertex
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                double[] p = lines[i], q = lines[j];
                double da = p[0] - q[0], db = p[1] - q[1], dc = p[2] - q[2];
                double norm = da * da + db * db;
                if (norm < EPS)
                    continue;
                double ox = -dc * da / norm, oy = -dc * db / norm, ux = -db, uy = da;
                for (double[] v : reflex)
                    onCircle(ox, oy, ux, uy, p[0] * ox + p[1] * oy + p[2], p[0] * ux + p[1] * uy,
                             v[0], v[1], cand);
            }
        // a line and two reflex vertices: on their perpendicular bisector
        for (int i = 0; i < k; i++)
            for (int j = i + 1; j < k; j++) {
                double[] v = reflex.get(i), w = reflex.get(j);
                double ox = (v[0] + w[0]) / 2, oy = (v[1] + w[1]) / 2;
                double ux = -(w[1] - v[1]), uy = w[0] - v[0];
                for (double[] p : lines)
                    onCircle(ox, oy, ux, uy, p[0] * ox + p[1] * oy + p[2], p[0] * ux + p[1] * uy,
                             v[0], v[1], cand);
            }
        // three reflex vertices: the centre of their circle
        for (int i = 0; i < k; i++)
            for (int j = i + 1; j < k; j++)
                for (int l = j + 1; l < k; l++) {
                    double[] p = reflex.get(i), q = reflex.get(j), r = reflex.get(l);
                    double d =
                        2 * (p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]));
                    if (Math.abs(d) < EPS)
                        continue;
                    double s1 = p[0] * p[0] + p[1] * p[1], s2 = q[0] * q[0] + q[1] * q[1];
                    double s3 = r[0] * r[0] + r[1] * r[1];
                    cand.add(new double[] {
                        (s1 * (q[1] - r[1]) + s2 * (r[1] - p[1]) + s3 * (p[1] - q[1])) / d,
                        (s1 * (r[0] - q[0]) + s2 * (p[0] - r[0]) + s3 * (q[0] - p[0])) / d});
                }
        double best = 0;
        for (double[] c : cand)
            best = Math.max(best, distanceToFence(c[0], c[1]));
        System.out.println(String.format(Locale.US, "%.2f", best));
    }
}
