import java.io.*;
import java.util.*;

public class Main {
    static final double EPS = 1e-9;
    // the starting cell is a square of half-side BOX * R around the table, and
    // a piece cuts a cell only within twice its reach, squared 4 times
    static final double BOX = 2, SPAN = 4;

    // the part of the convex polygon (xs, ys) with (p - m) . d <= 0
    static double[][] clip(double[][] poly, double mx, double my, double dx, double dy) {
        int n = poly[0].length;
        double[] xs = new double[n + 1], ys = new double[n + 1];
        int m = 0;
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

    // a point of the table edge where piece i is the nearest, or null: the
    // Voronoi cell of the piece is convex and reaches the edge exactly when
    // its farthest vertex from the centre is at least R away
    static double[] seat(double[] px, double[] py, int i, double r) {
        double cx = px[i], cy = py[i];
        double side = BOX * r, limit = r * r - EPS;
        double[][] poly = {{-side, side, side, -side}, {-side, -side, side, side}};
        int k = px.length;
        double[] dist = new double[k];
        Integer[] order = new Integer[k];
        for (int j = 0; j < k; j++) {
            dist[j] = (px[j] - cx) * (px[j] - cx) + (py[j] - cy) * (py[j] - cy);
            order[j] = j;
        }
        Arrays.sort(order, (a, b) -> Double.compare(dist[a], dist[b]));
        for (int j : order) {
            if (j == i)
                continue;
            double reach = 0;
            for (int v = 0; v < poly[0].length; v++) {
                double vx = poly[0][v] - cx, vy = poly[1][v] - cy;
                reach = Math.max(reach, vx * vx + vy * vy);
            }
            if (dist[j] > SPAN * reach)
                break; // farther than twice the cell's reach: cannot cut it
            poly = clip(poly, (px[j] + cx) / 2, (py[j] + cy) / 2, px[j] - cx, py[j] - cy);
            double far = 0;
            for (int v = 0; v < poly[0].length; v++)
                far = Math.max(far, poly[0][v] * poly[0][v] + poly[1][v] * poly[1][v]);
            if (far < limit)
                return null;
        }
        int best = 0;
        for (int v = 1; v < poly[0].length; v++)
            if (poly[0][v] * poly[0][v] + poly[1][v] * poly[1][v] >
                poly[0][best] * poly[0][best] + poly[1][best] * poly[1][best])
                best = v;
        // the segment from the piece to that vertex lies in the cell and
        // crosses the edge: solve |c + t (v - c)| = R
        double ux = poly[0][best] - cx, uy = poly[1][best] - cy;
        double a = ux * ux + uy * uy, b = cx * ux + cy * uy, c = cx * cx + cy * cy - r * r;
        double t = Math.min(1, (-b + Math.sqrt(Math.max(0, b * b - a * c))) / a);
        double x = cx + t * ux, y = cy + t * uy, len = Math.hypot(x, y);
        return new double[] {x * r / len, y * r / len};
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        double r = in.nval;
        in.nextToken();
        int k = (int)in.nval;
        double[] px = new double[k], py = new double[k];
        int[] weight = new int[k];
        Integer[] order = new Integer[k];
        for (int i = 0; i < k; i++) {
            in.nextToken();
            px[i] = in.nval;
            in.nextToken();
            py[i] = in.nval;
            in.nextToken();
            weight[i] = (int)in.nval;
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> weight[b] - weight[a]);
        for (int i : order) {
            double[] p = seat(px, py, i, r);
            if (p != null) {
                System.out.println(String.format(Locale.US, "%.10f %.10f", p[0], p[1]));
                return;
            }
        }
    }
}
