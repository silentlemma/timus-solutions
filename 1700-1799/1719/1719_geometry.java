import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int BOSSES = 4;
    // the three ways to split the four bosses into two shots
    static final int[][][] SPLITS = {{{0, 1}, {2, 3}}, {{0, 2}, {1, 3}}, {{0, 3}, {1, 2}}};
    static double[] x = new double[BOSSES];
    static double[] y = new double[BOSSES];

    // walk from the origin to a point P on the line a1 b1, shoot, then walk
    // straight to the line a2 b2; along the first line P = a1 + t u and the
    // length is sqrt((t - t0)^2 + h^2) + |k t + m|, convex in t
    static double walk(int a1, int b1, int a2, int b2) {
        double length = Math.hypot(x[b1] - x[a1], y[b1] - y[a1]);
        double ux = (x[b1] - x[a1]) / length;
        double uy = (y[b1] - y[a1]) / length;
        double t0 = -(x[a1] * ux + y[a1] * uy);
        double h = Math.abs(x[a1] * uy - y[a1] * ux);
        double norm = Math.hypot(x[b2] - x[a2], y[b2] - y[a2]);
        double nx = -(y[b2] - y[a2]) / norm;
        double ny = (x[b2] - x[a2]) / norm;
        double k = nx * ux + ny * uy;
        double m = nx * (x[a1] - x[a2]) + ny * (y[a1] - y[a2]);
        // the minimum is at the foot of the origin, where the lines cross, or
        // where the slope of the first term cancels the slope k of the second
        double root = k != 0 ? -m / k : t0;
        double shift = Math.abs(k) < 1 ? k * h / Math.sqrt(1 - k * k) : 0;
        double[] candidates = {t0, root, t0 + shift, t0 - shift};
        double best = Double.POSITIVE_INFINITY;
        for (double t : candidates) {
            best = Math.min(best, Math.hypot(t - t0, h) + Math.abs(k * t + m));
        }
        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for (int i = 0; i < BOSSES; i++) {
            x[i] = in.nextInt();
            y[i] = in.nextInt();
        }
        double best = Double.POSITIVE_INFINITY;
        for (int[][] s : SPLITS) {
            int[] p = s[0];
            int[] q = s[1];
            best = Math.min(best, walk(p[0], p[1], q[0], q[1]));
            best = Math.min(best, walk(q[0], q[1], p[0], p[1]));
        }
        System.out.println(String.format(Locale.US, "%.10f", best));
    }
}
