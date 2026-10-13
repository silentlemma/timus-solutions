import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int CORNERS = 3;
    static final double WIDE = 2 * Math.PI / 3; // 120 degrees

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double[] x = new double[CORNERS], y = new double[CORNERS];
        double[] angle = new double[CORNERS], side = new double[CORNERS];
        for (int i = 0; i < CORNERS; i++) {
            x[i] = in.nextDouble();
            y[i] = in.nextDouble();
        }
        for (int i = 0; i < CORNERS; i++) {
            int b = (i + 1) % CORNERS, c = (i + 2) % CORNERS;
            double ux = x[b] - x[i], uy = y[b] - y[i], wx = x[c] - x[i], wy = y[c] - y[i];
            angle[i] = Math.atan2(Math.abs(ux * wy - uy * wx), ux * wx + uy * wy);
            side[i] = Math.hypot(x[c] - x[b], y[c] - y[b]);
        }
        for (int i = 0; i < CORNERS; i++)
            if (angle[i] >= WIDE) {
                // a corner of at least 120 degrees is the best place itself
                System.out.printf(Locale.US, "%.8f %.8f%n", x[i], y[i]);
                return;
            }
        // otherwise the Fermat point: every side is seen at 120 degrees, and its
        // barycentric weights are a / sin(A + 60 degrees) and so on
        double total = 0, fx = 0, fy = 0;
        for (int i = 0; i < CORNERS; i++) {
            double w = side[i] / Math.sin(angle[i] + Math.PI / CORNERS);
            total += w;
            fx += w * x[i];
            fy += w * y[i];
        }
        System.out.printf(Locale.US, "%.8f %.8f%n", fx / total, fy / total);
    }
}
