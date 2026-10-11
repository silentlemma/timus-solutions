import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final double EPS = 1e-9;
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static double next() throws IOException {
        while (!words.hasMoreTokens())
            words = new StringTokenizer(in.readLine());
        return Double.parseDouble(words.nextToken());
    }

    public static void main(String[] args) throws IOException {
        int n = (int)next();
        double h = next();
        double[] xs = new double[n], ys = new double[n];
        for (int i = 0; i < n; i++) {
            xs[i] = next();
            ys[i] = next();
        }
        double d = next(), lx = next(), ly = next();
        double area = 0;
        for (int i = 0; i < n; i++)
            area += xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i];
        if (area < 0) {
            for (int i = 0, j = n - 1; i < j; i++, j--) {
                double t = xs[i];
                xs[i] = xs[j];
                xs[j] = t;
                t = ys[i];
                ys[i] = ys[j];
                ys[j] = t;
            }
        }
        // each side as an outward normal and an offset: inside the lot
        // nx x + ny y <= c on every side
        double[] nxs = new double[n], nys = new double[n], cs = new double[n];
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            nxs[i] = ys[j] - ys[i];
            nys[i] = xs[i] - xs[j];
            cs[i] = nxs[i] * xs[i] + nys[i] * ys[i];
        }
        int k = (int)next(), shot = 0;
        for (int s = 0; s < k; s++) {
            double px = next(), py = next();
            double r = Math.hypot(px - lx, py - ly);
            boolean inside = true;
            for (int i = 0; i < n; i++) {
                if (nxs[i] * px + nys[i] * py >
                    cs[i] + EPS * Math.hypot(nxs[i], nys[i]) * (r + 1)) {
                    inside = false;
                }
            }
            if (inside) {
                shot++; // over the lot the laser always reaches it in time
                continue;
            }
            // the beam leaves the lot at horizontal distance a and must clear
            // the fence there, so it meets the stone no lower than h r / a
            double ux = (px - lx) / r, uy = (py - ly) / r, a = Double.POSITIVE_INFINITY;
            for (int i = 0; i < n; i++) {
                double toward = nxs[i] * ux + nys[i] * uy;
                if (toward > 0)
                    a = Math.min(a, (cs[i] - nxs[i] * lx - nys[i] * ly) / toward);
            }
            if (r * r * (a * a + h * h) <= d * d * a * a * (1 + EPS))
                shot++;
        }
        System.out.println(shot);
    }
}
