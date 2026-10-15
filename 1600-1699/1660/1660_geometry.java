import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double SLACK = 1e-9; // lets a chain that closes exactly keep its last circle

    static double centre;
    static double mid;
    static double half;
    static double span;

    // the image under inversion in the unit circle around the origin: x, y and r
    static double[] invert(double x, double y, double r) {
        double den = x * x + y * y - r * r;
        return new double[] {x / den, y / den, r / Math.abs(den)};
    }

    static double gap(double theta) {
        double[] a = invert(centre + mid * Math.cos(theta), mid * Math.sin(theta), half);
        double t = theta + span;
        double[] z = invert(centre + mid * Math.cos(t), mid * Math.sin(t), half);
        return Math.hypot(a[0] - z[0], a[1] - z[1]) - a[2] - z[2];
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double big = in.nextInt();
        double small = in.nextInt();
        double d = in.nextInt();
        // the limit point inside the small circle (the common centre if d = 0):
        // inverting there makes both circles concentric
        double b = big * big + d * d - small * small;
        double twice = 2 * d * big;
        double p = twice * big / (b + Math.sqrt(Math.max(0, b * b - twice * twice)));
        double[] outer = invert(-p, 0, big);
        double[] inner = invert(d - p, 0, small);
        centre = (outer[0] + inner[0]) / 2;
        mid = (outer[2] + inner[2]) / 2;
        half = Math.abs(outer[2] - inner[2]) / 2;
        // there every chain circle has radius half and turns by step around the
        // centre; the chain stops once one more would overlap the first
        double step = 2 * Math.asin(half / mid);
        double count = Math.floor(2 * Math.PI / step + SLACK);
        span = (count - 1) * step;
        // the best chain is symmetric about the line through the centres
        double best = Math.min(gap(-span / 2), gap(Math.PI - span / 2));
        System.out.println(String.format(Locale.US, "%.10f", Math.max(0, best)));
    }
}
