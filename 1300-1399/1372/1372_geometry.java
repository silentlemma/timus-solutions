import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double TINY = 1e-9; // a torque this small is no torque at all
    static final double TURN = 360.0;
    static final double HALF_UNIT = 5e-9; // half of the last printed digit
    static final int DIM = 3;

    static double[] unit(double lon, double lat) {
        lon = Math.toRadians(lon);
        lat = Math.toRadians(lat);
        return new double[] {Math.cos(lat) * Math.cos(lon), Math.cos(lat) * Math.sin(lon),
                             Math.sin(lat)};
    }

    static double[] cross(double[] a, double[] b) {
        return new double[] {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
                             a[0] * b[1] - a[1] * b[0]};
    }

    static double dot(double[] a, double[] b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }

    static double[] angles(double[] v) {
        double length = Math.sqrt(dot(v, v));
        double lat = Math.toDegrees(Math.asin(Math.max(-1, Math.min(1, v[2] / length))));
        double lon = (Math.toDegrees(Math.atan2(v[1], v[0])) + TURN) % TURN;
        if (lon >= TURN - HALF_UNIT)
            lon = 0; // it would print as 360
        // adding 0.0 turns a negative zero into a plain one
        return new double[] {lon + 0.0, lat + 0.0};
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double radius = in.nextDouble();
        in.nextDouble(); // the mass does not matter
        double mast = in.nextDouble(), thrust = in.nextDouble();
        int count = (int)in.nextDouble();
        double arm = radius + mast; // the engines sit on masts above the surface
        double[] torque = new double[DIM];
        for (int i = 0; i < count; i++) {
            double lon = in.nextDouble(), lat = in.nextDouble();
            double dlon = in.nextDouble(), dlat = in.nextDouble();
            double[] t = cross(unit(lon, lat), unit(dlon, dlat));
            for (int k = 0; k < torque.length; k++)
                torque[k] += arm * thrust * t[k];
        }
        double size = Math.sqrt(dot(torque, torque));
        if (size < TINY) {
            System.out.println(
                String.format(Locale.US, "%.8f %.8f %.8f %.8f %.8f", 0.0, 0.0, 0.0, 0.0, 0.0));
            return;
        }
        // a force f at p turns the station by p x f, at most |p| |f|; so the
        // least thrust |T| / |p| needs p across the torque T and f = p x T / |p|^2
        double[] axis = {torque[0] / size, torque[1] / size, torque[2] / size};
        double[][] axes = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        double[] pick = axes[0];
        for (double[] e : axes)
            if (Math.abs(dot(e, axis)) < Math.abs(dot(pick, axis)))
                pick = e;
        double d = dot(pick, axis);
        double[] place = {pick[0] - d * axis[0], pick[1] - d * axis[1], pick[2] - d * axis[2]};
        double[] push = cross(place, torque);
        double[] at = angles(place), to = angles(push);
        System.out.println(String.format(Locale.US, "%.8f %.8f %.8f %.8f %.8f", at[0], at[1], to[0],
                                         to[1], size / arm));
    }
}
