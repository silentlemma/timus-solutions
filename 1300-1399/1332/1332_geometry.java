import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final double EPS = 1e-7;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        double[] xs = new double[n], ys = new double[n];
        List<double[]> places = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            xs[i] = in.nextInt();
            ys[i] = in.nextInt();
            places.add(new double[] {xs[i], ys[i]});
        }
        double reach = in.nextInt() - in.nextInt(); // how far a center may be
        if (reach < 0) {
            System.out.println(0);
            return;
        }
        // a best circle can be moved until it passes through two centers or
        // stands on one, so only such places need to be tried
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                double dx = xs[j] - xs[i], dy = ys[j] - ys[i];
                double half = Math.hypot(dx, dy) / 2;
                if (half > 0 && half <= reach) {
                    double rise = Math.sqrt(Math.max(0, reach * reach - half * half)) / (2 * half);
                    double mx = xs[i] + dx / 2, my = ys[i] + dy / 2;
                    places.add(new double[] {mx - dy * rise, my + dx * rise});
                    places.add(new double[] {mx + dy * rise, my - dx * rise});
                }
            }
        }
        double limit = (reach + EPS) * (reach + EPS);
        int best = 0;
        for (double[] p : places) {
            int inside = 0;
            for (int k = 0; k < n; k++) {
                double dx = xs[k] - p[0], dy = ys[k] - p[1];
                if (dx * dx + dy * dy <= limit)
                    inside++;
            }
            best = Math.max(best, inside);
        }
        System.out.println(best);
    }
}
