import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static final int CUTS = 4; // both ends and at most two roots
    static double asinh(double x) {
        return x < 0 ? -asinh(-x) : Math.log(x + Math.sqrt(x * x + 1));
    }

    // the length of the trace while the source a and the receiver b move
    // along the directions ua and ub for the time span
    static double stretch(double ax, double ay, double bx, double by,
            double uax, double uay, double ubx, double uby, double span) {
        double dx = bx - ax;
        double dy = by - ay;
        double vx = ubx - uax;
        double vy = uby - uay;
        double a = vx * vx + vy * vy;
        double m = dx * vy - dy * vx; // constant cross product of d(t) = b - a and v
        if (a == 0 || m <= 0) {
            return 0;
        }
        // the trace point is a + lam(t) d(t), lam linear; its speed is
        // |r(t)| / sqrt(q(t)) for q(t) = |d(t)|^2 and a quadratic r(t)
        double lam0 = (uax * dy - uay * dx) / m;
        double lam1 = (uax * vy - uay * vx) / m;
        double h = dx * vx + dy * vy;
        double c = dx * dx + dy * dy;
        double b = 2 * h;
        double r2 = 2 * lam1 * a;
        double r1 = uax * vx + uay * vy + lam1 * (b + h) + lam0 * a;
        double r0 = uax * dx + uay * dy + lam1 * c + lam0 * h;
        // r = alpha q + beta q' + gamma, integrated term by term
        double alpha = 2 * lam1;
        double beta = (r1 - alpha * b) / (2 * a);
        double gamma = r0 - alpha * c - beta * b;
        double rootA = Math.sqrt(a);
        double tail = alpha * m * m / (2 * a) + gamma;
        // the speed changes sign at the roots of r: the trace has a cusp there
        double[] cuts = new double[CUTS];
        int count = 0;
        cuts[count++] = 0;
        if (r2 != 0) {
            double half = r1 / 2;
            double disc = half * half - r2 * r0;
            if (disc > 0) {
                double s = Math.sqrt(disc);
                double[] roots = {(-half - s) / r2, (-half + s) / r2};
                Arrays.sort(roots);
                for (double t : roots) {
                    if (t > 0 && t < span) {
                        cuts[count++] = t;
                    }
                }
            }
        } else if (r1 != 0) {
            double t = -r0 / r1;
            if (t > 0 && t < span) {
                cuts[count++] = t;
            }
        }
        cuts[count++] = span;
        double total = 0;
        for (int k = 0; k + 1 < count; k++) {
            double lo = cuts[k];
            double hi = cuts[k + 1];
            double mid = (lo + hi) / 2;
            double part = 0;
            for (int side = 0; side < 2; side++) {
                double t = side == 0 ? hi : lo;
                double q = Math.max(a * t * t + b * t + c, 0);
                double slope = 2 * a * t + b;
                double value = (lam1 * slope / (2 * a) + 2 * beta) * Math.sqrt(q)
                        + tail * asinh(slope / (2 * m)) / rootA;
                part += side == 0 ? value : -value;
            }
            total += r2 * mid * mid + r1 * mid + r0 >= 0 ? part : -part;
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken());
        double[] xs = new double[n];
        double[] ys = new double[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Double.parseDouble(st.nextToken());
            ys[i] = Double.parseDouble(st.nextToken());
        }
        double d = Double.parseDouble(st.nextToken());
        double[] size = new double[n];
        double[] ux = new double[n];
        double[] uy = new double[n];
        for (int i = 0; i < n; i++) {
            int k = (i + 1) % n;
            size[i] = Math.hypot(xs[k] - xs[i], ys[k] - ys[i]);
            ux[i] = (xs[k] - xs[i]) / size[i];
            uy[i] = (ys[k] - ys[i]) / size[i];
        }
        // the source starts at vertex 0; the receiver d further along the
        // border
        int j = 0;
        double left = d;
        while (left >= size[j]) {
            left -= size[j++];
        }
        double bx = xs[j] + ux[j] * left;
        double by = ys[j] + uy[j] * left;
        double ahead = size[j] - left; // what is left of the receiver's edge
        int i = 0;
        double ax = xs[0];
        double ay = ys[0];
        double behind = size[0];
        double total = 0;
        // walk from one corner event to the next, one of the two at a vertex
        while (i < n) {
            total += stretch(ax, ay, bx, by, ux[i], uy[i], ux[j], uy[j], Math.min(behind, ahead));
            if (behind <= ahead) {
                ahead -= behind;
                bx += ux[j] * behind;
                by += uy[j] * behind;
                i++;
                if (i < n) {
                    ax = xs[i];
                    ay = ys[i];
                    behind = size[i];
                }
                if (ahead <= 0) {
                    j = (j + 1) % n;
                    bx = xs[j];
                    by = ys[j];
                    ahead = size[j];
                }
            } else {
                behind -= ahead;
                ax += ux[i] * ahead;
                ay += uy[i] * ahead;
                j = (j + 1) % n;
                bx = xs[j];
                by = ys[j];
                ahead = size[j];
            }
        }
        System.out.println(String.format(Locale.US, "%.10f", total));
    }
}
