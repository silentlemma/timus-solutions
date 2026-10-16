import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        long[] xs = new long[n], ys = new long[n], across = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = in.nextLong();
            ys[i] = in.nextLong();
        }
        // a ball of diameter D hits the pins whose centres lie in a strip of width
        // D + 1 along its path, so the narrowest strip holding k centres decides, and
        // one side of that strip runs along two centres, so only those directions
        double best = k > 1 ? Double.POSITIVE_INFINITY : 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long dx = xs[j] - xs[i], dy = ys[j] - ys[i];
                for (int t = 0; t < n; t++) across[t] = dx * ys[t] - dy * xs[t];
                Arrays.sort(across);
                long gap = across[k - 1] - across[0];
                for (int t = 1; t + k <= n; t++) gap = Math.min(gap, across[t + k - 1] - across[t]);
                best = Math.min(best, gap / Math.hypot(dx, dy));
            }
        }
        // a ball of any size will do when the strip is no wider than a pin
        System.out.println(best > 1 ? String.format(Locale.US, "%.10f", best - 1) : "0.000000");
    }
}
