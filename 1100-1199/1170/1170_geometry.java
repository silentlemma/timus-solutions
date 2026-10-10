import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
    // directions (y, x) through corners, compared by slope y/x so that equal
    // slopes share one entry; each holds the change of p and q there
    static TreeMap<long[], long[]> events =
        new TreeMap<>((a, b) -> Long.compare(a[0] * b[1], b[0] * a[1]));

    static void add(long y, long x, long dp, long dq) {
        long[] e = events.computeIfAbsent(new long[] {y, x}, k -> new long[2]);
        e[0] += dp;
        e[1] += dq;
    }

    static void term(long y1, long x1, long y2, long x2, long dp, long dq) {
        add(y1, x1, dp, dq);
        add(y2, x2, -dp, -dq);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = br.readLine(); line != null; line = br.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = Integer.parseInt(in.nextToken());
        long[][] rects = new long[n][];
        for (int i = 0; i < n; i++) {
            rects[i] = new long[] {Long.parseLong(in.nextToken()), Long.parseLong(in.nextToken()),
                                   Long.parseLong(in.nextToken()), Long.parseLong(in.nextToken()),
                                   Long.parseLong(in.nextToken())};
        }
        long c0 = Long.parseLong(in.nextToken()), length = Long.parseLong(in.nextToken());
        // walking at angle t, a vertical line x = a is crossed after a/cos t
        // and a horizontal one y = b after b/sin t; a rectangle adds (c - c0)
        // times (exit - entry), a sum of terms valid between two corners
        for (long[] r : rects) {
            int k = 0;
            long x1 = r[k++], y1 = r[k++], x2 = r[k++], y2 = r[k++], w = r[k++] - c0;
            // out through the right side or the top, in through the left or bottom
            term(y1, x2, y2, x2, w * x2, 0);
            term(y2, x2, y2, x1, 0, w * y2);
            term(y1, x1, y2, x1, -w * x1, 0);
            term(y1, x2, y1, x1, 0, -w * y1);
        }
        // below the lowest corner no rectangle is met at all
        long[] lowest = events.firstKey();
        double bestCost = c0 * length, bestT = Math.atan2(lowest[0], lowest[1]) / 2;
        // between corners the time is c0*L + p/cos t + q/sin t: with p, q > 0
        // it is above c0*L, otherwise monotone or concave, so corners suffice
        long p = 0, q = 0;
        for (Map.Entry<long[], long[]> e : events.entrySet()) {
            double t = Math.atan2(e.getKey()[0], e.getKey()[1]);
            double cost = c0 * length + p / Math.cos(t) + q / Math.sin(t);
            if (cost < bestCost) {
                bestCost = cost;
                bestT = t;
            }
            p += e.getValue()[0];
            q += e.getValue()[1];
        }
        System.out.printf("%.6f%n%.6f %.6f%n", bestCost, length * Math.cos(bestT),
                          length * Math.sin(bestT));
    }
}
