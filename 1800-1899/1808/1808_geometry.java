import java.util.Scanner;

public class Main {
    static final double EPS = 1e-9;

    static double cross(double ax, double ay, double bx, double by) {
        return ax * by - ay * bx;
    }

    // where the refracted line of sight enters the planet and where it would
    // leave it again: the entry x and y, then the exit x and y
    static double[] chord(double r, double eta, double x, double y, double dx, double dy) {
        // the first crossing of the line of sight with the circle
        double a = dx * dx + dy * dy, halfB = x * dx + y * dy, c = x * x + y * y - r * r;
        double t = (-halfB - Math.sqrt(Math.max(0, halfB * halfB - a * c))) / a;
        double ex = x + dx * t, ey = y + dy * t;
        double length = Math.hypot(dx, dy), ux = dx / length, uy = dy / length;
        // split the direction into the inward normal and the tangent; Snell's
        // law shrinks the tangent part by eta
        double nx = -ex / r, ny = -ey / r, along = ux * nx + uy * ny;
        double tx = (ux - along * nx) / eta, ty = (uy - along * ny) / eta;
        double inward = Math.sqrt(Math.max(0, 1 - tx * tx - ty * ty));
        double vx = inward * nx + tx, vy = inward * ny + ty;
        // the chord from the entry point along v has length -2 (e . v)
        double span = -2 * (ex * vx + ey * vy);
        return new double[] {ex, ey, ex + vx * span, ey + vy * span};
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double r = in.nextDouble(), eta = in.nextDouble();
        double[] one = chord(r, eta, in.nextDouble(), in.nextDouble(), in.nextDouble(),
            in.nextDouble());
        double[] two = chord(r, eta, in.nextDouble(), in.nextDouble(), in.nextDouble(),
            in.nextDouble());
        int x = 0, y = 1, exitX = 2, exitY = exitX + 1;
        double d1x = one[exitX] - one[x], d1y = one[exitY] - one[y];
        double d2x = two[exitX] - two[x], d2y = two[exitY] - two[y];
        double wx = two[x] - one[x], wy = two[y] - one[y];
        double den = cross(d1x, d1y, d2x, d2y);
        boolean seen;
        if (Math.abs(den) < EPS) {
            // parallel chords meet only if they lie on one line
            seen = Math.abs(cross(wx, wy, d1x, d1y)) < EPS * Math.max(1, Math.hypot(d1x, d1y));
        } else {
            double s = cross(wx, wy, d2x, d2y) / den, t = cross(wx, wy, d1x, d1y) / den;
            seen = EPS < s && s < 1 - EPS && EPS < t && t < 1 - EPS;
        }
        System.out.println(seen ? "Yes" : "No");
    }
}
