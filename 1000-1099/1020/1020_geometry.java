import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        int n = in.nextInt();
        double r = in.nextDouble();
        double[] x = new double[n], y = new double[n];
        for (int i = 0; i < n; i++) {
            x[i] = in.nextDouble();
            y[i] = in.nextDouble();
        }
        // the straight parts are the sides of the polygon, the arcs around the
        // nails turn by 2*pi in total: one full circle of radius r
        double length = 2 * Math.PI * r;
        for (int i = 0; n > 1 && i < n; i++) {
            length += Math.hypot(x[(i + 1) % n] - x[i], y[(i + 1) % n] - y[i]);
        }
        System.out.println(String.format(Locale.US, "%.2f", length));
    }
}
