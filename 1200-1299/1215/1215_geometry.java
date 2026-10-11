import java.util.Locale;
import java.util.Scanner;

public class Main {
    static double segmentDistance(double px, double py, double ax, double ay, double bx,
                                  double by) {
        double dx = bx - ax, dy = by - ay;
        double t = (px - ax) * dx + (py - ay) * dy, length2 = dx * dx + dy * dy;
        if (t <= 0) {
            return Math.hypot(px - ax, py - ay);
        }
        if (t >= length2) {
            return Math.hypot(px - bx, py - by);
        }
        return Math.abs((px - ax) * dy - (py - ay) * dx) / Math.sqrt(length2);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long px = in.nextLong(), py = in.nextLong();
        int n = in.nextInt();
        long[] x = new long[n], y = new long[n];
        for (int i = 0; i < n; i++) {
            x[i] = in.nextLong();
            y[i] = in.nextLong();
        }
        boolean inside = true;
        double best = Double.POSITIVE_INFINITY;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            // inside a counterclockwise polygon the point is left of every edge
            if ((x[j] - x[i]) * (py - y[i]) - (y[j] - y[i]) * (px - x[i]) < 0) {
                inside = false;
            }
            best = Math.min(best, segmentDistance(px, py, x[i], y[i], x[j], y[j]));
        }
        System.out.println(String.format(Locale.US, "%.3f", inside ? 0.0 : 2 * best));
    }
}
