import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static final double MOST = 4.0; // the longest squared chord, between opposite points
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static double next() throws IOException {
        while (!words.hasMoreTokens())
            words = new StringTokenizer(in.readLine());
        return Double.parseDouble(words.nextToken());
    }

    public static void main(String[] args) throws IOException {
        int n = (int)next(), m = (int)next();
        double r = next();
        // the pads as points on the unit sphere
        double[] px = new double[m], py = new double[m], pz = new double[m];
        for (int i = 0; i < m; i++) {
            double a = Math.toRadians(next()), b = Math.toRadians(next());
            px[i] = Math.cos(a) * Math.cos(b);
            py[i] = Math.cos(a) * Math.sin(b);
            pz[i] = Math.sin(a);
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            double a = Math.toRadians(next()), b = Math.toRadians(next());
            double x = Math.cos(a) * Math.cos(b), y = Math.cos(a) * Math.sin(b), z = Math.sin(a);
            // the nearest pad has the shortest chord through the planet
            double best = MOST;
            for (int k = 0; k < m; k++) {
                double dx = x - px[k], dy = y - py[k], dz = z - pz[k];
                best = Math.min(best, dx * dx + dy * dy + dz * dz);
            }
            double half = Math.min(1.0, Math.sqrt(best) / 2);
            out.append(String.format(Locale.US, "%.2f%n", 2 * r * Math.asin(half)));
        }
        System.out.print(out);
    }
}
