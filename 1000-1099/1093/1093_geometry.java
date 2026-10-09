import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double HALF_G = 5.0;
    // coefficients this small count as zero
    static final double TINY = 1e-12;
    // tolerance for times and for being strictly inside the rim
    static final double EPS = 1e-9;

    static double dx, dy, dz, vx, vy, vz, r;

    // the dart at time t, if that time has come, is strictly inside the rim
    static boolean inside(double t) {
        if (t < -EPS) {
            return false;
        }
        t = Math.max(t, 0.0);
        double px = dx + vx * t, py = dy + vy * t, pz = dz + vz * t - HALF_G * t * t;
        return px * px + py * py + pz * pz < r * r - EPS;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double cx = in.nextDouble(), cy = in.nextDouble(), cz = in.nextDouble();
        double nx = in.nextDouble(), ny = in.nextDouble(), nz = in.nextDouble();
        r = in.nextDouble();
        double sx = in.nextDouble(), sy = in.nextDouble(), sz = in.nextDouble();
        vx = in.nextDouble();
        vy = in.nextDouble();
        vz = in.nextDouble();
        dx = sx - cx;
        dy = sy - cy;
        dz = sz - cz;
        // the distance to the plane, times |N|, is a t^2 + 2 h t + c; a flight
        // that never crosses the plane, even one lying in it, misses
        double a = -HALF_G * nz, h = (nx * vx + ny * vy + nz * vz) / 2;
        double c = nx * dx + ny * dy + nz * dz;
        boolean hit = false;
        if (Math.abs(a) < TINY) {
            hit = Math.abs(h) >= TINY && inside(-c / (2 * h));
        } else {
            double d = h * h - a * c;
            if (d >= -TINY) {
                double root = Math.sqrt(Math.max(d, 0.0));
                hit = inside((-h - root) / a) || inside((-h + root) / a);
            }
        }
        System.out.println(hit ? "HIT" : "MISSED");
    }
}
