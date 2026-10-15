import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int DIM = 3;

    static double[] cross(double[] u, double[] v) {
        return new double[] {
            u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]
        };
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong();
        long b = in.nextLong();
        long[] p = new long[DIM];
        long[] d = new long[DIM];
        for (int i = 0; i < DIM; i++) {
            p[i] = in.nextLong();
        }
        for (int i = 0; i < DIM; i++) {
            d[i] = in.nextLong() - p[i];
        }
        // the elbow's axis is parallel to the rail and across both segments, so the
        // shoulder, the elbow and the claw lie in the plane through the shoulder
        // across the rail, and the claw sits at the rail's point h nearest to it
        long[] c = {
            p[1] * d[2] - p[2] * d[1], p[2] * d[0] - p[0] * d[2], p[0] * d[1] - p[1] * d[0]
        };
        long dd = d[0] * d[0] + d[1] * d[1] + d[2] * d[2];
        long num = c[0] * c[0] + c[1] * c[1] + c[2] * c[2]; // |h|^2 = num / dd, exactly

        // the bend (the angle opposite h) is not acute and the triangle closes:
        // a^2 + b^2 <= |h|^2 <= (a + b)^2
        if ((a * a + b * b) * dd > num || num > (a + b) * (a + b) * dd) {
            System.out.println("No solution.");
            return;
        }
        double t = -(double) (p[0] * d[0] + p[1] * d[1] + p[2] * d[2]) / dd;
        double r = Math.sqrt((double) num / dd);
        double[] e1 = new double[DIM];
        double[] unit = new double[DIM];
        for (int i = 0; i < DIM; i++) {
            e1[i] = (p[i] + t * d[i]) / r;
            unit[i] = d[i] / Math.sqrt(dd);
        }
        double[] e2 = cross(unit, e1);
        // the elbow is at distance a from the shoulder and b from h
        double along = (a * a - b * b + r * r) / (2 * r);
        double side = Math.sqrt(Math.max(0, a * a - along * along));
        double bend = Math.acos(Math.max(-1, Math.min(1, (a * a + b * b - r * r) / (2.0 * a * b))));
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < DIM; i++) {
            out.append(String.format(Locale.US, "%.15f ", along * e1[i] + side * e2[i]));
        }
        out.append(String.format(Locale.US, "%.15f", bend));
        System.out.println(out);
    }
}
