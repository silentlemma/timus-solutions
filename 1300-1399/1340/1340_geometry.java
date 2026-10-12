import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double TURN = 2 * Math.PI;
    static final double EPS = 1e-9;

    // an arc angle in [0, 2 pi), with angles a hair below a full turn taken
    // as no turn at all
    static double ahead(double angle) {
        angle %= TURN;
        if (angle < 0)
            angle += TURN;
        return angle > TURN - EPS ? 0 : angle;
    }

    // the points where the circles around a and b of radii ra and rb meet
    static double[][] circleCross(double ax, double ay, double ra, double bx, double by,
                                  double rb) {
        double d = Math.hypot(bx - ax, by - ay);
        if (d == 0 || d > ra + rb + EPS || d < Math.abs(ra - rb) - EPS)
            return new double[0][];
        double along = (ra * ra - rb * rb + d * d) / (2 * d);
        double side = Math.sqrt(Math.max(0, ra * ra - along * along));
        double ux = (bx - ax) / d, uy = (by - ay) / d, mx = ax + ux * along, my = ay + uy * along;
        return new double[][] {{mx - uy * side, my + ux * side}, {mx + uy * side, my - ux * side}};
    }

    static double shortest(double x, double y, double heading, double r, double kx, double ky) {
        if (r == 0)
            return Math.hypot(kx - x, ky - y);
        double best = Double.POSITIVE_INFINITY;
        // sign 1 turns left (counter-clockwise), sign -1 turns right
        for (int sign : new int[] {1, -1}) {
            double cx = x - sign * r * Math.sin(heading), cy = y + sign * r * Math.cos(heading);
            double start = Math.atan2(y - cy, x - cx); // where the cockroach is on the circle
            // an arc, then straight along the tangent to the crumb
            double d = Math.hypot(kx - cx, ky - cy);
            if (d >= r - EPS) {
                double run = Math.sqrt(Math.max(0, d * d - r * r));
                double leave = Math.atan2(ky - cy, kx - cx) - sign * Math.acos(Math.min(1, r / d));
                best = Math.min(best, r * ahead(sign * (leave - start)) + run);
            }
            // an arc, then an arc the other way around a circle 2r further out
            // that passes through the crumb
            for (double[] o : circleCross(cx, cy, 2 * r, kx, ky, r)) {
                double sw = Math.atan2(o[1] - cy, o[0] - cx);
                double first = ahead(sign * (sw - start));
                double back = sw + Math.PI; // the switch point seen from the new center
                double end = Math.atan2(ky - o[1], kx - o[0]);
                best = Math.min(best, r * (first + ahead(-sign * (end - back))));
            }
        }
        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double x = in.nextDouble(), y = in.nextDouble(), a = in.nextDouble(), r = in.nextDouble();
        double kx = in.nextDouble(), ky = in.nextDouble();
        double length = shortest(x, y, Math.toRadians(a), Math.abs(r), kx, ky);
        System.out.println(String.format(Locale.US, "%.4f", length));
    }
}
