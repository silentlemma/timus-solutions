import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    static long cross(long[] o, long[] a, long[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        long[][] towers = new long[n][2], monuments = new long[m][2];
        for (long[][] list : new long[][][] {towers, monuments}) {
            for (long[] p : list) {
                in.nextToken();
                p[0] = (long)in.nval;
                in.nextToken();
                p[1] = (long)in.nval;
            }
        }
        double[][] dist = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = Math.hypot(towers[i][0] - towers[j][0], towers[i][1] - towers[j][1]);
            }
        }
        double best = Double.POSITIVE_INFINITY;
        if (m == 0) {
            // any convex border contains a triangle of its towers that is not
            // longer, so the best border is the shortest triangle with an area
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    for (int k = j + 1; k < n; k++) {
                        if (cross(towers[i], towers[j], towers[k]) != 0) {
                            best = Math.min(best, dist[i][j] + dist[j][k] + dist[k][i]);
                        }
                    }
                }
            }
        } else {
            // the border goes clockwise, so the inside is on the right of every
            // side: a side i -> j may be used when all monuments are strictly right
            boolean[][] ok = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (i == j) {
                        continue;
                    }
                    boolean all = true;
                    for (long[] p : monuments) {
                        if (cross(towers[i], towers[j], p) >= 0) {
                            all = false;
                            break;
                        }
                    }
                    ok[i][j] = all;
                }
            }
            // a monument inside rules out degenerate borders; from every first
            // tower, the shortest way around through towers in their order
            for (int s = 0; s < n; s++) {
                double[] way = new double[n];
                Arrays.fill(way, Double.POSITIVE_INFINITY);
                way[s] = 0;
                for (int step = 1; step < n; step++) {
                    int k = (s + step) % n;
                    for (int back = 0; back < step; back++) {
                        int j = (s + back) % n;
                        if (ok[j][k]) {
                            way[k] = Math.min(way[k], way[j] + dist[j][k]);
                        }
                    }
                    if (ok[k][s]) {
                        best = Math.min(best, way[k] + dist[k][s]);
                    }
                }
            }
        }
        System.out.println(String.format(Locale.US, "%.2f", best));
    }
}
