import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double h = in.nextInt();
        double t = in.nextInt();
        double v = in.nextInt();
        double x = in.nextInt();
        // the least time climbs at x as long as possible and at full speed in
        // the remaining seconds; the most climbs just faster than x, or during
        // all t seconds when that is too slow to reach h
        double least = Math.max(0, h - t * x) / (v - x);
        double most = Math.min(t, h / x);
        System.out.println(String.format(Locale.US, "%.6f %.6f", least, most));
    }
}
