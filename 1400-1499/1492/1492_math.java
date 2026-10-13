import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    static int n;
    static long[] xs, ys;

    // the segment of f that holds x, or the one to its right
    static int segment(long x) {
        int lo = 0, hi = n; // the first index with xs[i] > x
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (xs[mid] > x)
                hi = mid;
            else
                lo = mid + 1;
        }
        return Math.min(lo - 1, n - 2);
    }

    static double value(long x) {
        int j = segment(x);
        return ys[j] + (double)(ys[j + 1] - ys[j]) * (x - xs[j]) / (xs[j + 1] - xs[j]);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        xs = new long[n];
        ys = new long[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            xs[i] = (long)in.nval;
            in.nextToken();
            ys[i] = (long)in.nval;
        }

        // f(x) = E(x) + O(x) with E(x) = (f(x) + f(-x)) / 2 and
        // O(x) = (f(x) - f(-x)) / 2; both are linear between the points of f
        // and their mirror images
        long[] all = new long[2 * n];
        for (int i = 0; i < n; i++) {
            all[2 * i] = xs[i];
            all[2 * i + 1] = -xs[i];
        }
        long[] points = Arrays.stream(all).sorted().distinct().toArray();

        StringBuilder out = new StringBuilder("Yes\n");
        for (long sign : new long[] {1, -1}) { // the even part, then the odd one
            // the slope of a part between neighbouring points: (a/b -+ c/d) / 2 with
            // the slopes a/b of f at x and c/d of f at -x, all below 2 * 10^9
            int m = points.length;
            long[] num = new long[m - 1], den = new long[m - 1];
            for (int k = 0; k + 1 < m; k++) {
                int j = segment(points[k]), i = segment(-points[k + 1]);
                long a = ys[j + 1] - ys[j], b = xs[j + 1] - xs[j];
                long c = ys[i + 1] - ys[i], d = xs[i + 1] - xs[i];
                num[k] = a * d - sign * c * b;
                den[k] = 2 * b * d;
            }
            for (int k = 0; k < m; k++) {
                boolean bend = k == 0 || k + 1 == m || num[k - 1] * den[k] != num[k] * den[k - 1];
                if (bend) // only real bends stay
                    out.append(String.format(Locale.US, "%.6f %.6f\n", (double)points[k],
                                             (value(points[k]) + sign * value(-points[k])) / 2));
            }
        }
        System.out.print(out);
    }
}
