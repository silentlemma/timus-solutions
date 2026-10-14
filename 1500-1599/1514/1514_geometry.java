import java.io.*;
import java.util.*;

public class Main {
    static final int SMALL = 8; // pieces up to this size are checked triple by triple
    // a better triangle has every side shorter than half its perimeter
    static final double HALF = 0.5;

    static double[] xs, ys;
    static Integer[] order;
    static double best = Double.POSITIVE_INFINITY;
    static int[] answer = {0, 1, 2};

    static double dist(int a, int b) { return Math.hypot(xs[a] - xs[b], ys[a] - ys[b]); }

    // tries every triple of pts, sorted by y, that fits within reach vertically
    static void triples(Integer[] pts, double reach) {
        int size = pts.length;
        for (int i = 0; i < size; i++) {
            int a = pts[i];
            double top = ys[a] + reach;
            for (int j = i + 1; j < size && ys[pts[j]] < top; j++)
                for (int k = j + 1; k < size && ys[pts[k]] < top; k++) {
                    int b = pts[j], c = pts[k];
                    double p = dist(a, b) + dist(b, c) + dist(c, a);
                    if (p < best) {
                        best = p;
                        answer = new int[] {a, b, c};
                        top = ys[a] + best * HALF;
                    }
                }
        }
    }

    static void byY(Integer[] pts) { Arrays.sort(pts, (a, b) -> Double.compare(ys[a], ys[b])); }

    // solves the points order[lo:hi]
    static void solve(int lo, int hi) {
        if (hi - lo <= SMALL) {
            Integer[] pts = Arrays.copyOfRange(order, lo, hi);
            byY(pts);
            triples(pts, Double.POSITIVE_INFINITY);
            return;
        }
        int mid = (lo + hi) / 2;
        double split = xs[order[mid]];
        solve(lo, mid);
        solve(mid, hi);
        // a better triangle across the split lies in a strip around it
        double reach = best * HALF;
        List<Integer> strip = new ArrayList<>();
        for (int i = lo; i < hi; i++)
            if (Math.abs(xs[order[i]] - split) < reach)
                strip.add(order[i]);
        Integer[] pts = strip.toArray(new Integer[0]);
        byY(pts);
        triples(pts, reach);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        xs = new double[n];
        ys = new double[n];
        order = new Integer[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            xs[i] = in.nval;
            in.nextToken();
            ys[i] = in.nval;
            order[i] = i;
        }
        Arrays.sort(
            order,
            (a, b) -> xs[a] != xs[b] ? Double.compare(xs[a], xs[b]) : Double.compare(ys[a], ys[b]));
        solve(0, n);
        System.out.printf(Locale.US, "%.6f%n%d %d %d%n", best, answer[0] + 1, answer[1] + 1,
                          answer[2] + 1);
    }
}
