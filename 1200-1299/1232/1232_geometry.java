import java.io.*;
import java.util.*;

public class Main {
    static final double EPS = 1e-9;
    static double h, d, tg, sn, cs;

    // the smallest drop of one move from a point on the cone wall at depth t
    // below the station: the move goes across to the opposite wall, or is
    // almost level once the cone there is at least d wide
    static double minDrop(double t) {
        double w = 2 * t * tg;
        if (w >= d)
            return 0;
        return (Math.sqrt(d * d * (1 + tg * tg) - w * w) - w * tg) / (1 + tg * tg);
    }

    // n moves in the plane y = 0 as x, z pairs: first slides moves down the
    // wall, then crossings at full tilt, and as soon as one move can drop
    // exactly the extra height, that move and then straight down
    static double[] path(int n, int slides) {
        double[] pts = new double[2 * n];
        int m = 0;
        double t = 0, x = 0, side = 1;
        for (int left = n; left >= 1; left--) {
            double extra = h - t - (left - 1) * d;
            double drop = minDrop(t);
            if (extra >= drop - EPS) {
                x += side * Math.sqrt(Math.max(0, d * d - extra * extra));
                t += extra;
                pts[m++] = x;
                pts[m++] = h - t;
                for (int k = left - 1; k >= 1; k--) {
                    pts[m++] = x;
                    pts[m++] = (k - 1) * d;
                }
                pts[m - 1] = 0;
                return pts;
            }
            if (left == 1)
                return null;
            if (n - left < slides) {
                x -= side * d * sn;
                t += d * cs;
            } else {
                t += drop;
                x = side * t * tg;
                side = -side;
            }
            pts[m++] = x;
            pts[m++] = h - t;
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new BufferedInputStream(System.in)).useLocale(Locale.ROOT);
        h = in.nextDouble();
        d = in.nextDouble();
        double alpha = in.nextDouble();
        tg = Math.tan(alpha / 2);
        sn = Math.sin(alpha / 2);
        cs = Math.cos(alpha / 2);
        int n = (int)Math.ceil(h / d - EPS);
        for (int slides = 0; slides <= n; slides++) {
            double[] pts = path(n, slides);
            if (pts != null) {
                StringBuilder sb = new StringBuilder();
                sb.append(n).append('\n');
                for (int i = 0; i < n; i++)
                    sb.append(
                        String.format(Locale.ROOT, "%.6f 0 %.6f\n", pts[2 * i], pts[2 * i + 1]));
                System.out.print(sb);
                return;
            }
        }
        System.out.println(-1);
    }
}
