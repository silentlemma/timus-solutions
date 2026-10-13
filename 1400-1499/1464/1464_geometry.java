import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static final int DIGITS = 4; // coordinates are given to four decimals
    static final double SCALE = 1e4;

    static StringTokenizer st;
    static BufferedReader in;

    static String word() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(in.readLine());
        return st.nextToken();
    }

    // a coordinate times 10^4, read exactly
    static long exact(String text) {
        long sign = 1;
        if (text.startsWith("-")) {
            sign = -1;
            text = text.substring(1);
        }
        int dot = text.indexOf('.');
        String whole = dot < 0 ? text : text.substring(0, dot);
        StringBuilder frac = new StringBuilder(dot < 0 ? "" : text.substring(dot + 1));
        while (frac.length() < DIGITS)
            frac.append('0');
        return sign *
            (Long.parseLong("0" + whole) * (long)SCALE + Long.parseLong(frac.substring(0, DIGITS)));
    }

    static double[] num, ex, ey, midX, midY;
    static int[] best, first;
    static int size;

    // how far along the middle ray of gap k the line of edge e lies
    static double distance(int e, int k) { return num[e] / (midX[k] * ey[e] - midY[k] * ex[e]); }

    // each node keeps the nearest edge among those covering all its gaps,
    // and edges never cross, so one gap decides for the whole node
    static void offer(int x, int e) {
        if (best[x] < 0 || distance(e, first[x]) < distance(best[x], first[x]))
            best[x] = e;
    }

    static void cover(int lo, int hi, int e) {
        for (lo += size, hi += size; lo < hi; lo >>= 1, hi >>= 1) {
            if ((lo & 1) == 1)
                offer(lo++, e);
            if ((hi & 1) == 1)
                offer(--hi, e);
        }
    }

    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        long px = exact(word()), py = exact(word());
        int n = Integer.parseInt(word());
        long[] xs = new long[n], ys = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = exact(word()) - px;
            ys[i] = exact(word()) - py;
        }
        // the directions of the corners seen from the lamp, equal ones merged
        Integer[] order = new Integer[n];
        double[] angle = new double[n];
        for (int i = 0; i < n; i++) {
            order[i] = i;
            angle[i] = Math.atan2(ys[i], xs[i]);
        }
        Arrays.sort(order, (a, b) -> Double.compare(angle[a], angle[b]));
        int[] group = new int[n];
        long[] dx = new long[n], dy = new long[n];
        int m = 0;
        for (int i : order) {
            boolean same = m > 0 && xs[i] * dy[m - 1] == ys[i] * dx[m - 1] &&
                           xs[i] * dx[m - 1] + ys[i] * dy[m - 1] > 0;
            if (!same) {
                dx[m] = xs[i];
                dy[m] = ys[i];
                m++;
            }
            group[i] = m - 1;
        }
        // every gap between neighbouring directions is below half a turn; its middle
        midX = new double[m];
        midY = new double[m];
        for (int k = 0; k < m; k++) {
            int l = (k + 1) % m;
            double la = Math.hypot(dx[k], dy[k]), lb = Math.hypot(dx[l], dy[l]);
            midX[k] = dx[k] / la + dx[l] / lb;
            midY[k] = dy[k] / la + dy[l] / lb;
        }
        for (size = 1; size < m; size *= 2)
            ;
        first = new int[2 * size];
        best = new int[2 * size];
        Arrays.fill(best, -1);
        for (int x = 2 * size - 1; x > 0; x--)
            first[x] = x >= size ? x - size : first[2 * x];
        num = new double[n];
        ex = new double[n];
        ey = new double[n];
        int edges = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            long c = xs[i] * ys[j] - ys[i] * xs[j];
            if (c == 0)
                continue; // seen edge-on, it hides nothing
            int a = c > 0 ? i : j, b = c > 0 ? j : i, e = edges++;
            num[e] = xs[a] * (ys[b] - ys[a]) - ys[a] * (xs[b] - xs[a]);
            ex[e] = xs[b] - xs[a];
            ey[e] = ys[b] - ys[a];
            if (group[a] < group[b]) {
                cover(group[a], group[b], e);
            } else {
                cover(group[a], m, e);
                cover(0, group[b], e);
            }
        }
        double area = 0;
        for (int k = 0; k < m; k++) {
            int near = -1;
            for (int x = k + size; x > 0; x >>= 1)
                if (best[x] >= 0 && (near < 0 || distance(best[x], k) < distance(near, k)))
                    near = best[x];
            int l = (k + 1) % m;
            double ta = num[near] / (dx[k] * ey[near] - dy[k] * ex[near]);
            double tb = num[near] / (dx[l] * ey[near] - dy[l] * ex[near]);
            area += ta * tb * ((double)dx[k] * dy[l] - (double)dy[k] * dx[l]) / 2;
        }
        System.out.printf(Locale.US, "%.4f%n", area / SCALE / SCALE);
    }
}
