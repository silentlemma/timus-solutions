import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    // samples per smooth piece and golden-section steps around the best samples
    static final int SAMPLES = 64, STEPS = 60;
    static final double EPS = 1e-12;
    // the step of the golden-section search
    static final double GOLDEN = (Math.sqrt(5) - 1) / 2;

    static int n;
    static double[] vx, vy, pre;
    static double half;

    // the point at boundary position u (a vertex index plus a fraction of the edge)
    static double[] at(double u) {
        int i = (int)u;
        double t = u - i;
        return new double[] {vx[i] + t * (vx[i + 1] - vx[i]), vy[i] + t * (vy[i + 1] - vy[i])};
    }

    // twice the area of P, V[i+1], ..., V[j]
    static double fan(double px, double py, int i, int j) {
        return px * vy[i + 1] - vx[i + 1] * py + pre[j] - pre[i + 1] + vx[j] * py - px * vy[j];
    }

    // the position w in (u, u + n) of the other end of the halving cut from u
    static double partner(double u) {
        double[] p = at(u);
        int i = (int)u;
        int lo = i + 1, hi = i + n;
        while (hi - lo > 1) {
            int mid = (lo + hi) / 2;
            if (fan(p[0], p[1], i, mid) <= half) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        int j = lo;
        // on the edge V[j] -> V[j+1] the area grows linearly with the position
        double ex = vx[j + 1] - vx[j], ey = vy[j + 1] - vy[j];
        double slope = vx[j] * ey - ex * vy[j] + ex * p[1] - p[0] * ey;
        double s = slope > 0 ? (half - fan(p[0], p[1], i, j)) / slope : 0;
        return j + Math.min(Math.max(s, 0), 1);
    }

    static double length(double u) {
        double[] p = at(u), q = at(partner(u));
        return Math.hypot(q[0] - p[0], q[1] - p[1]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(all.toString());
        n = Integer.parseInt(st.nextToken());
        // vertices repeated twice so that a walk along the boundary never wraps
        vx = new double[2 * n + 1];
        vy = new double[2 * n + 1];
        for (int i = 0; i < n; i++) {
            vx[i] = Double.parseDouble(st.nextToken());
            vy[i] = Double.parseDouble(st.nextToken());
        }
        // the walk below needs counterclockwise order, whatever order is given
        double twice = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + n - 1) % n;
            twice += vx[j] * vy[i] - vx[i] * vy[j];
        }
        if (twice < 0) {
            for (int i = 0, j = n - 1; i < j; i++, j--) {
                double tx = vx[i], ty = vy[i];
                vx[i] = vx[j];
                vy[i] = vy[j];
                vx[j] = tx;
                vy[j] = ty;
            }
        }
        for (int k = n; k <= 2 * n; k++) {
            vx[k] = vx[k - n];
            vy[k] = vy[k - n];
        }
        // pre[k]: twice the signed area swept by the edges 0 .. k-1 from the origin
        pre = new double[2 * n + 1];
        for (int k = 0; k < 2 * n; k++) {
            pre[k + 1] = pre[k] + vx[k] * vy[k + 1] - vx[k + 1] * vy[k];
        }
        half = pre[n] / 2;
        // the cut length is smooth between the vertices and the partners of the
        // vertices; sample every piece and refine around its local minima
        double[] breaks = new double[2 * n + 1];
        for (int k = 0; k <= n; k++) {
            breaks[k] = k;
            if (k < n) {
                breaks[n + 1 + k] = partner(k) % n;
            }
        }
        Arrays.sort(breaks);
        double best = length(0);
        for (int b = 0; b + 1 < breaks.length; b++) {
            double from = breaks[b], to = breaks[b + 1];
            if (to - from < EPS) {
                continue;
            }
            double[] us = new double[SAMPLES + 1], vals = new double[SAMPLES + 1];
            for (int k = 0; k <= SAMPLES; k++) {
                us[k] = from + (to - from) * k / SAMPLES;
                vals[k] = length(us[k]);
                best = Math.min(best, vals[k]);
            }
            for (int k = 0; k <= SAMPLES; k++) {
                // a local minimum among the samples, the piece ends included
                int left = Math.max(k - 1, 0), right = Math.min(k + 1, SAMPLES);
                if (vals[k] > vals[left] || vals[k] > vals[right]) {
                    continue;
                }
                double lo = us[left], hi = us[right];
                for (int step = 0; step < STEPS; step++) {
                    double m1 = hi - GOLDEN * (hi - lo), m2 = lo + GOLDEN * (hi - lo);
                    if (length(m1) < length(m2)) {
                        hi = m2;
                    } else {
                        lo = m1;
                    }
                }
                best = Math.min(best, length((lo + hi) / 2));
            }
        }
        System.out.println(String.format(Locale.US, "%.6f", best));
    }
}
