import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final double TOP = 10.0; // the speed limit; accelerations are limited by 1
    static final double EPS = 1e-12;

    // fastest run over a piece entered at v0 and left at v1: speed up,
    // perhaps cruise at the cap, slow down
    static double pieceTime(double length, double cap, double v0, double v1) {
        if (length <= EPS) {
            return 0;
        }
        double up = (cap * cap - v0 * v0) / 2, down = (cap * cap - v1 * v1) / 2;
        if (up + down <= length) {
            return (cap - v0) + (cap - v1) + (length - up - down) / cap;
        }
        double peak = Math.sqrt(length + (v0 * v0 + v1 * v1) / 2);
        return (peak - v0) + (peak - v1);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int) in.nval;
        double[] ax = new double[n], ay = new double[n], bx = new double[n], by = new double[n];
        double[] ux = new double[n], uy = new double[n], len = new double[n];
        double[] extra = new double[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            ax[i] = in.nval;
            in.nextToken();
            ay[i] = in.nval;
            in.nextToken();
            bx[i] = in.nval;
            in.nextToken();
            by[i] = in.nval;
            len[i] = Math.hypot(bx[i] - ax[i], by[i] - ay[i]);
            ux[i] = (bx[i] - ax[i]) / len[i];
            uy[i] = (by[i] - ay[i]) / len[i];
        }
        int m = 2 * n - 1;
        double[] length = new double[m], cap = new double[m];
        for (int i = 0; i + 1 < n; i++) {
            double dx = ax[i + 1] - bx[i], dy = ay[i + 1] - by[i];
            double sin = ux[i] * uy[i + 1] - uy[i] * ux[i + 1];
            double cos = ux[i] * ux[i + 1] + uy[i] * uy[i + 1];
            double radius, angle;
            if (Math.abs(sin) > EPS) {
                // the lines meet t past the end of this segment and back
                // before the start of the next one; the arc touches both
                // lines at the same distance from that point, as far as it can
                double t = (dx * uy[i + 1] - dy * ux[i + 1]) / sin;
                double back = -(dx * uy[i] - dy * ux[i]) / sin;
                double nearest = Math.min(t, back);
                extra[i] += t - nearest;
                extra[i + 1] += back - nearest;
                if (Math.abs(nearest) <= EPS) {
                    continue;
                }
                radius = Math.abs(nearest) * (1 + cos) / Math.abs(sin);
                double turn = Math.atan2(Math.abs(sin), cos);
                // a meeting point behind forces the long way around the circle
                angle = nearest > 0 ? turn : 2 * Math.PI - turn;
            } else {
                // opposite directions: a half circle across the gap
                double along = dx * ux[i] + dy * uy[i], across = -dx * uy[i] + dy * ux[i];
                if (along > 0) {
                    extra[i] += along;
                } else {
                    extra[i + 1] -= along;
                }
                radius = Math.abs(across) / 2;
                angle = Math.PI;
            }
            length[2 * i + 1] = radius * angle;
            cap[2 * i + 1] = Math.min(TOP, Math.sqrt(radius));
        }
        for (int i = 0; i < n; i++) {
            length[2 * i] = len[i] + extra[i];
            cap[2 * i] = TOP;
        }
        // the speed where pieces meet: what acceleration from the start and
        // braking before the end allow, within the caps on both sides
        double[] reach = new double[m + 1], stop = new double[m + 1];
        for (int i = 0; i < m; i++) {
            reach[i + 1] = Math.min(cap[i], Math.sqrt(reach[i] * reach[i] + 2 * length[i]));
        }
        for (int i = m - 1; i >= 0; i--) {
            stop[i] = Math.min(cap[i], Math.sqrt(stop[i + 1] * stop[i + 1] + 2 * length[i]));
        }
        double total = 0;
        for (int i = 0; i < m; i++) {
            double v0 = Math.min(reach[i], stop[i]), v1 = Math.min(reach[i + 1], stop[i + 1]);
            total += pieceTime(length[i], cap[i], v0, v1);
        }
        System.out.printf("%.10f%n", total);
    }
}
