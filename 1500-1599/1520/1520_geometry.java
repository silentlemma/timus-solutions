import java.io.*;
import java.util.*;

public class Main {
    // the starting cell is a square of half-side BOX * R around the disk, and
    // a site cuts a cell only within twice its reach, squared 4 times
    static final double BOX = 2, SPAN = 4;
    static final double EPS = 1e-9;

    // the part of the convex polygon (as x and y lists) with (p - m) . d <= 0
    static double[][] clip(double[][] poly, double mx, double my, double dx, double dy) {
        int n = poly[0].length, m = 0;
        double[] xs = new double[n + 1], ys = new double[n + 1];
        for (int k = 0; k < n; k++) {
            double px = poly[0][k], py = poly[1][k];
            double qx = poly[0][(k + 1) % n], qy = poly[1][(k + 1) % n];
            double sp = (px - mx) * dx + (py - my) * dy;
            double sq = (qx - mx) * dx + (qy - my) * dy;
            if (sp <= 0) {
                xs[m] = px;
                ys[m++] = py;
            }
            if ((sp < 0 && sq > 0) || (sq < 0 && sp > 0)) {
                double t = sp / (sp - sq);
                xs[m] = px + t * (qx - px);
                ys[m++] = py + t * (qy - py);
            }
        }
        return new double[][] {Arrays.copyOf(xs, m), Arrays.copyOf(ys, m)};
    }

    // whether the point lies in the convex polygon, counterclockwise
    static boolean inside(double[][] poly, double ax, double ay) {
        int n = poly[0].length;
        for (int k = 0; k < n; k++) {
            double px = poly[0][k], py = poly[1][k];
            double qx = poly[0][(k + 1) % n], qy = poly[1][(k + 1) % n];
            if ((qx - px) * (ay - py) - (qy - py) * (ax - px) < -EPS)
                return false;
        }
        return true;
    }

    // the largest distance from c to a point of the polygon inside the disk
    // of radius r around the origin
    static double farthest(double[][] poly, double cx, double cy, double r) {
        double best = 0;
        int n = poly[0].length;
        for (int k = 0; k < n; k++) {
            double px = poly[0][k], py = poly[1][k];
            double qx = poly[0][(k + 1) % n], qy = poly[1][(k + 1) % n];
            if (px * px + py * py <= r * r)
                best = Math.max(best, Math.hypot(px - cx, py - cy));
            // where the edge crosses the circle: |p + t (q - p)| = r
            double ux = qx - px, uy = qy - py;
            double a = ux * ux + uy * uy, b = px * ux + py * uy, c = px * px + py * py - r * r;
            double disc = b * b - a * c;
            if (a > 0 && disc >= 0)
                for (double t :
                     new double[] {(-b - Math.sqrt(disc)) / a, (-b + Math.sqrt(disc)) / a})
                    if (t >= 0 && t <= 1)
                        best = Math.max(best, Math.hypot(px + t * ux - cx, py + t * uy - cy));
        }
        // on an arc inside the cell the distance peaks at the circle point
        // opposite the site, if that point is in the cell
        double norm = Math.hypot(cx, cy);
        double ox = norm > 0 ? -r * cx / norm : r, oy = norm > 0 ? -r * cy / norm : 0;
        if (inside(poly, ox, oy))
            best = Math.max(best, Math.hypot(ox - cx, oy - cy));
        return best;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        double r = in.nval;
        double[] xs = new double[n], ys = new double[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            xs[i] = in.nval;
            in.nextToken();
            ys[i] = in.nval;
        }
        double side = BOX * r, answer = 0;
        for (int i = 0; i < n; i++) {
            double cx = xs[i], cy = ys[i];
            double[][] poly = {{-side, side, side, -side}, {-side, -side, side, side}};
            double[] dist = new double[n];
            Integer[] order = new Integer[n];
            for (int j = 0; j < n; j++) {
                dist[j] = (xs[j] - cx) * (xs[j] - cx) + (ys[j] - cy) * (ys[j] - cy);
                order[j] = j;
            }
            Arrays.sort(order, (a, b) -> Double.compare(dist[a], dist[b]));
            for (int j : order) {
                if (dist[j] == 0)
                    continue; // the site itself, or another one at the same point
                double reach = 0;
                for (int v = 0; v < poly[0].length; v++)
                    reach = Math.max(reach,
                                     Math.pow(poly[0][v] - cx, 2) + Math.pow(poly[1][v] - cy, 2));
                if (dist[j] > SPAN * reach)
                    break;
                poly = clip(poly, (xs[j] + cx) / 2, (ys[j] + cy) / 2, xs[j] - cx, ys[j] - cy);
            }
            answer = Math.max(answer, farthest(poly, cx, cy, r));
        }
        System.out.println(String.format(Locale.US, "%.8f", answer));
    }
}
