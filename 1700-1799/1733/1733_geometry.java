import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final double EPS = 1e-9;
    static final int SIDES = 4;
    static final int POINTS = SIDES + 1;

    // the mouse, then the corners of the book
    static double[] px = new double[POINTS], py = new double[POINTS];
    static double cx, cy, r;

    // positive inside the book (the corners go counterclockwise)
    static double side(int i, double x, double y) {
        int a = 1 + i, b = 1 + (i + 1) % SIDES;
        return (px[b] - px[a]) * (y - py[a]) - (py[b] - py[a]) * (x - px[a]);
    }

    static boolean outside(double x, double y) {
        for (int i = 0; i < SIDES; i++) {
            if (side(i, x, y) < -EPS) {
                return true;
            }
        }
        return false;
    }

    // whether the segment passes through the inside of the book
    static boolean blocks(double ax, double ay, double bx, double by) {
        double lo = 0, hi = 1;
        for (int i = 0; i < SIDES; i++) {
            double f0 = side(i, ax, ay), f1 = side(i, bx, by);
            if (f0 <= EPS && f1 <= EPS) {
                return false;
            }
            if (f0 < f1 && f0 <= EPS) {
                lo = Math.max(lo, (EPS - f0) / (f1 - f0));
            }
            if (f1 < f0 && f1 <= EPS) {
                hi = Math.min(hi, (f0 - EPS) / (f0 - f1));
            }
        }
        return hi - lo > EPS;
    }

    // the closest point of the disk outside the book that (sx, sy) sees
    static double nearest(double sx, double sy) {
        double best = Double.POSITIVE_INFINITY;
        double d = Math.hypot(sx - cx, sy - cy);
        if (d > EPS) {
            double qx = cx + (sx - cx) * r / d, qy = cy + (sy - cy) * r / d;
            if (outside(qx, qy) && !blocks(sx, sy, qx, qy)) {
                best = Math.max(0, d - r);
            }
        }
        for (int i = 0; i < SIDES; i++) {
            if (side(i, sx, sy) > EPS) {
                continue;
            }
            // the part of side i inside the disk, as a parameter range on it
            int a = 1 + i, b = 1 + (i + 1) % SIDES;
            double ex = px[b] - px[a], ey = py[b] - py[a];
            double qa = ex * ex + ey * ey;
            double qb = (px[a] - cx) * ex + (py[a] - cy) * ey;
            double qc = (px[a] - cx) * (px[a] - cx) + (py[a] - cy) * (py[a] - cy) - r * r;
            double disc = qb * qb - qa * qc;
            if (disc <= 0) {
                continue;
            }
            double lo = Math.max(0, (-qb - Math.sqrt(disc)) / qa);
            double hi = Math.min(1, (-qb + Math.sqrt(disc)) / qa);
            if ((hi - lo) * Math.sqrt(qa) <= EPS) {
                continue;
            }
            double t = ((sx - px[a]) * ex + (sy - py[a]) * ey) / qa;
            t = Math.min(Math.max(t, lo), hi);
            best = Math.min(best, Math.hypot(px[a] + t * ex - sx, py[a] + t * ey - sy));
        }
        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for (int i = 1; i < POINTS; i++) {
            px[i] = in.nextInt();
            py[i] = in.nextInt();
        }
        cx = in.nextInt();
        cy = in.nextInt();
        r = in.nextInt();
        px[0] = in.nextInt();
        py[0] = in.nextInt();
        // the mouse goes straight or around corners of the book; Dijkstra
        // over the mouse and the corners gives each its shortest way
        double[] dist = new double[POINTS];
        boolean[] done = new boolean[POINTS];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[0] = 0;
        for (int step = 0; step < POINTS; step++) {
            int u = -1;
            for (int w = 0; w < POINTS; w++) {
                if (!done[w] && (u < 0 || dist[w] < dist[u])) {
                    u = w;
                }
            }
            done[u] = true;
            for (int w = 1; w < POINTS; w++) {
                int gap = (u - w + SIDES) % SIDES;
                boolean joined = u == 0 ? !blocks(px[0], py[0], px[w], py[w])
                        : gap == 1 || gap == SIDES - 1;
                if (w != u && joined) {
                    double edge = Math.hypot(px[w] - px[u], py[w] - py[u]);
                    dist[w] = Math.min(dist[w], dist[u] + edge);
                }
            }
        }
        double answer = Double.POSITIVE_INFINITY;
        for (int k = 0; k < POINTS; k++) {
            answer = Math.min(answer, dist[k] + nearest(px[k], py[k]));
        }
        System.out.printf("%.5f%n", answer);
    }
}
