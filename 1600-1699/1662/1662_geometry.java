import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    static final double EPS = 1e-7;

    static int n;
    static double[] px;
    static double[] py;
    // per edge: start, direction, outward unit normal and its offset
    static double[] ax;
    static double[] ay;
    static double[] ex;
    static double[] ey;
    static double[] nx;
    static double[] ny;
    static double[] offset;
    static double reach;
    static double keep;

    // the common points of two circles
    static void circles(double x1, double y1, double ra, double x2, double y2, double rb,
            List<double[]> out) {
        double dx = x2 - x1;
        double dy = y2 - y1;
        double d2 = dx * dx + dy * dy;
        if (d2 == 0) {
            return;
        }
        double along = (d2 + ra * ra - rb * rb) / (2 * d2);
        double h2 = ra * ra / d2 - along * along;
        if (h2 < -EPS) {
            return;
        }
        double h = Math.sqrt(Math.max(0, h2));
        double x = x1 + dx * along;
        double y = y1 + dy * along;
        out.add(new double[] {x - dy * h, y + dx * h});
        out.add(new double[] {x + dy * h, y - dx * h});
    }

    // the common points of the line lx * x + ly * y = c (unit normal) and a circle
    static void lineCircle(double lx, double ly, double c, double cx, double cy, double radius,
            List<double[]> out) {
        double off = lx * cx + ly * cy - c;
        double h2 = radius * radius - off * off;
        if (h2 < -EPS) {
            return;
        }
        double h = Math.sqrt(Math.max(0, h2));
        double x = cx - lx * off;
        double y = cy - ly * off;
        out.add(new double[] {x - ly * h, y + lx * h});
        out.add(new double[] {x + ly * h, y - lx * h});
    }

    static boolean fits(double x, double y) {
        for (int i = 0; i < n; i++) {
            if ((x - px[i]) * (x - px[i]) + (y - py[i]) * (y - py[i]) > reach) {
                return false;
            }
        }
        boolean outside = false;
        for (int i = 0; i < n; i++) {
            if (nx[i] * x + ny[i] * y > offset[i]) {
                outside = true;
            }
            double t = (x - ax[i]) * ex[i] + (y - ay[i]) * ey[i];
            t /= ex[i] * ex[i] + ey[i] * ey[i];
            t = Math.min(1, Math.max(0, t));
            double dx = x - ax[i] - t * ex[i];
            double dy = y - ay[i] - t * ey[i];
            if (dx * dx + dy * dy < keep) {
                return false;
            }
        }
        return outside;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        n = (int) in.nval;
        px = new double[n];
        py = new double[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            px[i] = in.nval;
            in.nextToken();
            py[i] = in.nval;
        }
        in.nextToken();
        double small = in.nval;
        in.nextToken();
        double big = in.nval;
        double turn = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + n - 1) % n;
            turn += px[j] * py[i] - px[i] * py[j];
        }
        int side = turn > 0 ? 1 : -1;
        ax = new double[n];
        ay = new double[n];
        ex = new double[n];
        ey = new double[n];
        nx = new double[n];
        ny = new double[n];
        offset = new double[n];
        for (int i = 0; i < n; i++) {
            int j = (i + n - 1) % n;
            ax[i] = px[j];
            ay[i] = py[j];
            ex[i] = px[i] - px[j];
            ey[i] = py[i] - py[j];
            double length = Math.hypot(ex[i], ey[i]);
            nx[i] = side * ey[i] / length;
            ny[i] = -side * ex[i] / length;
            offset[i] = nx[i] * ax[i] + ny[i] * ay[i];
        }
        reach = (big + EPS) * (big + EPS);
        keep = (small - EPS) * (small - EPS);
        // the goat's area is where the discs of radius R around the vertices meet,
        // and when any of it is far enough from the bed, so is one of its corners
        // or a crossing of its boundary with the boundary of the bed grown by r
        List<double[]> found = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                found.clear();
                if (i < j) {
                    circles(px[i], py[i], big, px[j], py[j], big, found);
                }
                circles(px[i], py[i], big, px[j], py[j], small, found);
                lineCircle(nx[j], ny[j], offset[j] + small, px[i], py[i], big, found);
                for (double[] p : found) {
                    if (fits(p[0], p[1])) {
                        System.out.println(String.format(Locale.US, "%.6f %.6f", p[0], p[1]));
                        return;
                    }
                }
            }
        }
        System.out.println("No solution");
    }
}
