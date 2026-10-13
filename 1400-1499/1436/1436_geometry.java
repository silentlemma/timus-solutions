import java.util.Locale;
import java.util.Scanner;

public class Main {
    static double angle(double px, double ax, double ay, double bx, double by) {
        double ux = ax - px, uy = ay, vx = bx - px, vy = by;
        return Math.atan2(Math.abs(ux * vy - uy * vx), ux * vx + uy * vy);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long x1 = in.nextLong(), y1 = in.nextLong(), x2 = in.nextLong(), y2 = in.nextLong();
        double best = 0;
        if (y1 * y2 < 0 || (y1 * y2 == 0 && x1 != x2)) {
            best = Math.PI; // stand on the billboard itself
        } else if (y1 * y2 == 0) {
            best = Math.PI / 2; // a vertical billboard standing on the road
        } else {
            y1 = Math.abs(y1);
            y2 = Math.abs(y2);
            double[] spots;
            if (y1 == y2) {
                spots = new double[] {(x1 + x2) / 2.0};
            } else {
                // the best spot is where a circle through both ends touches the road:
                // its distance from where the billboard's line meets the road is sqrt(QA * QB)
                double qx = x1 - (double)y1 * (x2 - x1) / (y2 - y1);
                double reach = Math.sqrt(Math.hypot(x1 - qx, y1) * Math.hypot(x2 - qx, y2));
                spots = new double[] {qx - reach, qx + reach};
            }
            for (double p : spots)
                best = Math.max(best, angle(p, x1, y1, x2, y2));
        }
        System.out.println(String.format(Locale.US, "%.6f", best));
    }
}
