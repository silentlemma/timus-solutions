import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int STAGES = 3;

    static BigInteger big(long v) { return BigInteger.valueOf(v); }

    // -1, 0 or 1: where the corner of lines p and q lies against line l, all
    // of them shifted by a tiny eps (a*x + b*y + c + eps < 0 is kept); the
    // values reach 3 * 10^37, past 64 bits
    static int side(long[] p, long[] q, long[] l) {
        BigInteger det = big(p[0]).multiply(big(q[1])).subtract(big(q[0]).multiply(big(p[1])));
        BigInteger x0 = big(q[2]).multiply(big(p[1])).subtract(big(p[2]).multiply(big(q[1])));
        BigInteger y0 = big(p[2]).multiply(big(q[0])).subtract(big(q[2]).multiply(big(p[0])));
        BigInteger t0 =
            big(l[0]).multiply(x0).add(big(l[1]).multiply(y0)).add(big(l[2]).multiply(det));
        BigInteger t1 =
            big(l[0]).multiply(big(p[1] - q[1])).add(big(l[1]).multiply(big(q[0] - p[0]))).add(det);
        int sign = t0.signum() != 0 ? t0.signum() : t1.signum();
        return det.signum() < 0 ? -sign : sign;
    }

    // cut the polygon, given by its lines in boundary order, by the line
    static List<long[]> clip(List<long[]> edges, long[] l) {
        int m = edges.size();
        int[] sides = new int[m];
        for (int k = 0; k < m; k++) {
            sides[k] = side(edges.get((k + m - 1) % m), edges.get(k), l);
        }
        // edge k runs from corner k to corner k + 1; it stays if part of it is inside
        boolean[] keep = new boolean[m];
        int start = -1;
        for (int k = 0; k < m; k++) {
            keep[k] = sides[k] < 0 || sides[(k + 1) % m] < 0;
            if (keep[k] && start < 0) {
                start = k;
            }
        }
        List<long[]> out = new ArrayList<>();
        if (start < 0) {
            return out;
        }
        for (int step = 0; step < m; step++) {
            int k = (start + step) % m, next = (k + 1) % m;
            if (!keep[k]) {
                continue;
            }
            out.add(edges.get(k));
            // the boundary leaves the half-plane before the next kept edge
            if (!keep[next] || sides[next] > 0) {
                out.add(l);
            }
        }
        if (out.size() < STAGES) {
            out.clear();
        }
        return out;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[][] s = new long[n][STAGES];
        for (long[] row : s) {
            for (int k = 0; k < STAGES; k++) {
                in.nextToken();
                row[k] = (long)in.nval;
            }
        }
        // the sides of the triangle x > 0, y > 0, x + y < 1, in boundary order
        List<long[]> triangle =
            Arrays.asList(new long[] {0, -1, 0}, new long[] {1, 1, -1}, new long[] {-1, 0, 0});
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            List<long[]> edges = new ArrayList<>(triangle);
            for (int j = 0; j < n && !edges.isEmpty(); j++) {
                if (j == i) {
                    continue;
                }
                // with u_k = length_k / s_ik > 0, i beats j when
                // sum (s_jk - s_ik) / s_jk * u_k < 0; times s_j1 s_j2 s_j3 the
                // coefficients are integers below 10^12
                long[] g = new long[STAGES];
                for (int k = 0; k < STAGES; k++) {
                    long others = s[j][(k + 1) % STAGES] * s[j][(k + 2) % STAGES];
                    g[k] = (s[j][k] - s[i][k]) * others;
                }
                // u_3 = 1 - x - y on the triangle
                long[] l = {g[0] - g[2], g[1] - g[2], g[2]};
                if (l[0] == 0 && l[1] == 0) {
                    if (l[2] >= 0) {
                        edges.clear();
                    }
                    continue;
                }
                edges = clip(edges, l);
            }
            out.append(edges.isEmpty() ? "No\n" : "Yes\n");
        }
        System.out.print(out);
    }
}
