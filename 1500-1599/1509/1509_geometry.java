import java.io.*;
import java.util.*;

public class Main {
    static final int MOST = 6; // dots in one square
    static final int FULL = 4; // from four dots on, all corners of the inner square are used
    static final double QUARTER = 0.25; // the inner square's corners are L / 4 from the centre

    static final double SMALLEST = 1, LARGEST = 100;
    static final double EPS = 2e-3; // coordinates come to 1e-4, and a fit spreads that error

    // the dots, as pairs of coordinates, of a square with k dots around
    // the point (cx, 0), for L = 1, with the domino along the x axis
    static List<double[]> square(int k, double cx) {
        double q = QUARTER;
        List<double[]> dots = new ArrayList<>();
        if (k >= 2) {
            dots.add(new double[] {cx - q, -q});
            dots.add(new double[] {cx + q, q});
        }
        if (k >= FULL) {
            dots.add(new double[] {cx + q, -q});
            dots.add(new double[] {cx - q, q});
        }
        if (k == MOST) {
            dots.add(new double[] {cx, -q}); // beside the long sides
            dots.add(new double[] {cx, q});
        }
        if (k % 2 == 1)
            dots.add(new double[] {cx, 0});
        return dots;
    }

    // whether a similarity, maybe mirrored, with scale in the allowed range
    // takes the template onto the given dots
    static boolean fits(List<double[]> template, double[][] given) {
        int n = given.length, far = 0;
        double[] g0 = given[0];
        for (int i = 0; i < n; i++)
            if (Math.hypot(given[i][0] - g0[0], given[i][1] - g0[1]) >
                Math.hypot(given[far][0] - g0[0], given[far][1] - g0[1]))
                far = i;
        double gx = given[far][0] - g0[0], gy = given[far][1] - g0[1];
        for (int mirror = 0; mirror < 2; mirror++) {
            double sign = mirror == 0 ? 1 : -1;
            for (double[] a : template)
                for (double[] b : template) {
                    if (a == b)
                        continue;
                    // turn = (g1 - g0) / (b - a) as complex numbers
                    double bx = b[0] - a[0], by = sign * (b[1] - a[1]);
                    double den = bx * bx + by * by;
                    double tx = (gx * bx + gy * by) / den, ty = (gy * bx - gx * by) / den;
                    double scale = Math.hypot(tx, ty);
                    if (scale < SMALLEST - EPS || scale > LARGEST + EPS)
                        continue;
                    Set<Integer> hit = new HashSet<>();
                    boolean ok = true;
                    for (double[] t : template) {
                        double dx = t[0] - a[0], dy = sign * (t[1] - a[1]);
                        double ix = g0[0] + dx * tx - dy * ty, iy = g0[1] + dx * ty + dy * tx;
                        int near = 0;
                        for (int i = 1; i < n; i++)
                            if (Math.hypot(given[i][0] - ix, given[i][1] - iy) <
                                Math.hypot(given[near][0] - ix, given[near][1] - iy))
                                near = i;
                        if (Math.hypot(given[near][0] - ix, given[near][1] - iy) > EPS) {
                            ok = false;
                            break;
                        }
                        hit.add(near);
                    }
                    if (ok && hit.size() == n)
                        return true;
                }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        double[][] given = new double[n][2];
        for (int i = 0; i < n; i++)
            for (int c = 0; c < 2; c++) {
                in.nextToken();
                given[i][c] = in.nval;
            }
        StringBuilder sb = new StringBuilder();
        for (int a = 0; a <= MOST; a++) {
            int b = n - a;
            if (a > b || b > MOST)
                continue;
            List<double[]> template = square(a, 0);
            template.addAll(square(b, 1));
            if (n == 1 || fits(template, given))
                sb.append(a).append(' ').append(b).append('\n');
        }
        System.out.print(sb);
    }
}
