import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {
    static final long SCALE = 100; // coordinates have at most two decimals
    static final int DIGITS = 2;
    static final long VOLUME_CENT = SCALE * SCALE; // a hundredth of a volume unit, in 1 / SCALE^3

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static String next() throws IOException {
        while (!words.hasMoreTokens())
            words = new StringTokenizer(in.readLine());
        return words.nextToken();
    }

    static long scaled(String token) {
        int dot = token.indexOf('.');
        String whole = dot < 0 ? token : token.substring(0, dot);
        String frac = (dot < 0 ? "" : token.substring(dot + 1)) + "00";
        long w = whole.isEmpty() ? 0 : Long.parseLong(whole);
        return w * SCALE + Long.parseLong(frac.substring(0, DIGITS));
    }

    public static void main(String[] args) throws IOException {
        long u = scaled(next()), v = scaled(next()), w = scaled(next());
        int n = Integer.parseInt(next());
        long[] px = new long[n], py = new long[n], pz = new long[n];
        TreeSet<Long> xSet = new TreeSet<>(Arrays.asList(0L, u));
        int kept = 0;
        for (int i = 0; i < n; i++) {
            long x = scaled(next()), y = scaled(next()), z = scaled(next());
            // a point outside A can never be inside G
            if (x <= u && y <= v && z <= w) {
                px[kept] = x;
                py[kept] = y;
                pz[kept++] = z;
                xSet.add(x);
            }
        }
        n = kept;
        Long[] xs = xSet.toArray(new Long[0]);
        long best = 0;
        for (int i = 0; i < xs.length; i++) {
            for (int j = xs.length - 1; j > i; j--) {
                long x1 = xs[i], x2 = xs[j], width = x2 - x1;
                if (width * v * w <= best)
                    break; // the remaining x2 are closer still
                List<long[]> list = new ArrayList<>();
                for (int p = 0; p < n; p++) {
                    if (x1 < px[p] && px[p] < x2)
                        list.add(new long[] {py[p], pz[p]});
                }
                long[][] inside = list.toArray(new long[0][]);
                Arrays.sort(inside, (a, b) -> Long.compare(a[0], b[0]));
                int m = inside.length;
                // the lower y face lies on the floor or on a point; the upper
                // face sweeps down from the top, and every point it passes
                // leaves the slab, so neighbouring z gaps merge into one
                for (int k = -1; k < m; k++) {
                    long y1 = k < 0 ? 0 : inside[k][0];
                    if (width * (v - y1) * w <= best)
                        break;
                    List<Long> zList = new ArrayList<>(Arrays.asList(0L, w));
                    for (int q = k + 1; q < m; q++) {
                        // a point on the floor or the ceiling never splits a gap
                        if (0 < inside[q][1] && inside[q][1] < w)
                            zList.add(inside[q][1]);
                    }
                    long[] zs = new long[zList.size()];
                    for (int t = 0; t < zs.length; t++)
                        zs[t] = zList.get(t);
                    Arrays.sort(zs);
                    int[] prev = new int[zs.length], nxt = new int[zs.length];
                    long gap = 0;
                    for (int t = 0; t < zs.length; t++) {
                        prev[t] = t - 1;
                        nxt[t] = t + 1;
                        if (t > 0)
                            gap = Math.max(gap, zs[t] - zs[t - 1]);
                    }
                    long y2 = v;
                    for (int q = m - 1; q > k; q--) {
                        best = Math.max(best, width * (y2 - y1) * gap);
                        y2 = inside[q][0];
                        long z = inside[q][1];
                        if (z <= 0 || z >= w)
                            continue;
                        int t = Arrays.binarySearch(zs, z);
                        int lo = prev[t], hi = nxt[t];
                        nxt[lo] = hi;
                        prev[hi] = lo;
                        gap = Math.max(gap, zs[hi] - zs[lo]);
                    }
                    best = Math.max(best, width * (y2 - y1) * gap);
                }
            }
        }
        long cents = (best + VOLUME_CENT / 2) / VOLUME_CENT;
        System.out.printf("%d.%02d%n", cents / SCALE, cents % SCALE);
    }
}
