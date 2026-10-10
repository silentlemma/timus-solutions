import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static double[] x, y;

    static double dist(int a, int b) { return Math.hypot(x[a] - x[b], y[a] - y[b]); }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer tok = new StringTokenizer(all.toString());
        int n = Integer.parseInt(tok.nextToken());
        x = new double[n];
        y = new double[n];
        for (int k = 0; k < n; k++) {
            x[k] = Double.parseDouble(tok.nextToken());
            y[k] = Double.parseDouble(tok.nextToken());
        }
        // a shortest path never crosses itself, so on a convex polygon the
        // visited camps form an arc and the path ends at one of its ends; at[i]
        // and atEnd[i] are the best paths over the arc from camp i, at either end
        double[] at = new double[n], atEnd = new double[n];
        for (int length = 1; length < n; length++) {
            double[] grow = new double[n], growEnd = new double[n];
            Arrays.fill(grow, Double.POSITIVE_INFINITY);
            Arrays.fill(growEnd, Double.POSITIVE_INFINITY);
            for (int i = 0; i < n; i++) {
                int j = (i + length - 1) % n, before = (i + n - 1) % n, after = (i + length) % n;
                grow[before] = Math.min(
                    grow[before], Math.min(at[i] + dist(i, before), atEnd[i] + dist(j, before)));
                growEnd[i] = Math.min(growEnd[i],
                                      Math.min(at[i] + dist(i, after), atEnd[i] + dist(j, after)));
            }
            at = grow;
            atEnd = growEnd;
        }
        double best = Double.POSITIVE_INFINITY;
        for (int i = 0; i < n; i++) {
            best = Math.min(best, Math.min(at[i], atEnd[i]));
        }
        System.out.println(String.format(Locale.US, "%.3f", best));
    }
}
