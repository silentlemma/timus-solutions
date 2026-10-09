import java.util.Locale;
import java.util.Scanner;

public class Main {
    static double[] read(Scanner in) {
        return new double[] {in.nextInt(), in.nextInt(), in.nextInt()};
    }

    static double[] sub(double[] a, double[] b) {
        return new double[] {a[0] - b[0], a[1] - b[1], a[2] - b[2]};
    }

    static double dot(double[] a, double[] b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }

    static double norm(double[] a) { return Math.sqrt(dot(a, a)); }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double[] a = read(in), b = read(in), c = read(in);
        double r = in.nextInt();
        double[] u = sub(a, c), v = sub(b, c);
        double[] cross = {u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2],
                          u[0] * v[1] - u[1] * v[0]};
        double angle = Math.atan2(norm(cross), dot(u, v));
        double da = norm(u), db = norm(v);
        // seen from C, the tangents from A and B cover these angles; when the angle
        // ACB fits in them, the segment AB misses the ball
        double reach = Math.acos(r / da) + Math.acos(r / db);
        double length = norm(sub(a, b));
        if (angle > reach) {
            length = Math.sqrt(da * da - r * r) + Math.sqrt(db * db - r * r) + r * (angle - reach);
        }
        System.out.println(String.format(Locale.US, "%.2f", length));
    }
}
