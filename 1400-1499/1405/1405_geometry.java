import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Locale;

public class Main {
    static final double SHORTEST = 1.0, LONGEST = 50.0; // the allowed rope lengths
    static final double EPS = 1e-9;

    // the largest a^2 + b^2 with 1 <= a <= topA, 1 <= b <= topB, a + b <= d, or -1
    static double bestPair(double topA, double topB, double d) {
        if (topA < SHORTEST - EPS || topB < SHORTEST - EPS || d < 2 * SHORTEST - EPS)
            return -1;
        // a convex function is largest at a corner of the region
        double[][] corners = {
            {topA, topB},     {topA, SHORTEST},         {SHORTEST, topB},        {topA, d - topA},
            {d - topB, topB}, {d - SHORTEST, SHORTEST}, {SHORTEST, d - SHORTEST}};
        double best = -1;
        for (double[] c : corners) {
            double a = c[0], b = c[1];
            if (a >= SHORTEST - EPS && a <= topA + EPS && b >= SHORTEST - EPS && b <= topB + EPS &&
                a + b <= d + EPS)
                best = Math.max(best, a * a + b * b);
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        double[] x = new double[n], y = new double[n], top = new double[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = in.nval;
            in.nextToken();
            y[i] = in.nval;
            top[i] = LONGEST;
        }
        // the longest rope at each tree: up to the nearest other tree and 50 meters
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (j != i)
                    top[i] = Math.min(top[i], Math.sqrt((x[i] - x[j]) * (x[i] - x[j]) +
                                                        (y[i] - y[j]) * (y[i] - y[j])));
        double best = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                double d = Math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
                best = Math.max(best, bestPair(top[i], top[j], d));
            }
        System.out.println(String.format(Locale.US, "%.4f", Math.PI * best));
    }
}
