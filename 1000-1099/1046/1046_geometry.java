import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static final double ROUNDING = 0.005;

    // a value that prints as -0.00 is printed as 0.00
    static double clean(double v) { return Math.abs(v) < ROUNDING ? 0 : v; }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(all.toString());
        int n = Integer.parseInt(st.nextToken());
        // complex numbers as separate real and imaginary parts
        double[] mx = new double[n], my = new double[n];
        double[] wx = new double[n], wy = new double[n];
        for (int i = 0; i < n; i++) {
            mx[i] = Double.parseDouble(st.nextToken());
            my[i] = Double.parseDouble(st.nextToken());
        }
        for (int i = 0; i < n; i++) {
            double t = Math.toRadians(Double.parseDouble(st.nextToken()));
            wx[i] = Math.cos(t);
            wy[i] = Math.sin(t);
        }
        // a step turns z around M[i] by its angle, z -> w z + (1 - w) M[i], and going
        // around the polygon composes the steps into z -> a z + b that fixes A[0]
        double ax = 1, ay = 0, bx = 0, by = 0;
        for (int i = 0; i < n; i++) {
            double nax = wx[i] * ax - wy[i] * ay, nay = wx[i] * ay + wy[i] * ax;
            double ux = 1 - wx[i], uy = -wy[i];
            double nbx = wx[i] * bx - wy[i] * by + ux * mx[i] - uy * my[i];
            double nby = wx[i] * by + wy[i] * bx + ux * my[i] + uy * mx[i];
            ax = nax;
            ay = nay;
            bx = nbx;
            by = nby;
        }
        // the angles never add up to a multiple of 360, so a != 1
        double dx = 1 - ax, dy = -ay, d = dx * dx + dy * dy;
        double zx = (bx * dx + by * dy) / d, zy = (by * dx - bx * dy) / d;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            out.append(String.format(Locale.US, "%.2f %.2f%n", clean(zx), clean(zy)));
            double rx = zx - mx[i], ry = zy - my[i];
            zx = mx[i] + wx[i] * rx - wy[i] * ry;
            zy = my[i] + wx[i] * ry + wy[i] * rx;
        }
        System.out.print(out);
    }
}
