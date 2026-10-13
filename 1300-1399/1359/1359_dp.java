import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double GRAVITY = 10;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        // the speed at depth d is sqrt(2 g d), whatever the way down was
        double[] speed = new double[m + 1];
        for (int d = 0; d <= m; d++)
            speed[d] = Math.sqrt(2 * GRAVITY * d);
        // best holds the least time to reach each depth and distance to the left,
        // where a board with constant acceleration takes 2 L / (v1 + v2)
        double[][] best = new double[m + 1][n + 1];
        for (double[] row : best)
            Arrays.fill(row, Double.POSITIVE_INFINITY);
        best[0][0] = 0;
        for (int d = 1; d <= m; d++)
            for (int e = 0; e < d; e++) {
                double vs = speed[d] + speed[e];
                for (int x = 0; x <= n; x++) {
                    double t = best[e][x];
                    if (Double.isInfinite(t))
                        continue;
                    for (int y = x; y <= n; y++) {
                        int dx = y - x, dd = d - e;
                        double c = t + 2 * Math.sqrt(dx * dx + dd * dd) / vs;
                        if (c < best[d][y])
                            best[d][y] = c;
                    }
                }
            }
        System.out.println(String.format(Locale.US, "%.4f", best[m][n]));
    }
}
