import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    static final double EPS = 1e-9;

    static BigInteger big(long a) { return BigInteger.valueOf(a); }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[] x = new long[n], y = new long[n], z = new long[n], r = new long[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = (long)in.nval;
            in.nextToken();
            y[i] = (long)in.nval;
            in.nextToken();
            z[i] = (long)in.nval;
            in.nextToken();
            r[i] = (long)in.nval;
        }
        // a ray along d touches ghost i when d.C_i >= L_i |d|, where L_i is the
        // length of a tangent from the gun: L_i^2 = |C_i|^2 - R_i^2
        long[] norm = new long[n], tan2 = new long[n];
        double[] tan = new double[n];
        long[][] dot = new long[n][n];
        for (int i = 0; i < n; i++) {
            norm[i] = x[i] * x[i] + y[i] * y[i] + z[i] * z[i];
            tan2[i] = norm[i] - r[i] * r[i];
            tan[i] = Math.sqrt(tan2[i]);
        }
        for (int i = 0; i < n; i++)
            for (int k = 0; k < n; k++)
                dot[i][k] = x[i] * x[k] + y[i] * y[k] + z[i] * z[k];
        int[] best = new int[0];
        int[] hit = new int[n];
        // the ray through the centre of ghost i, tested exactly in integers
        for (int i = 0; i < n; i++) {
            int m = 0;
            for (int k = 0; k < n; k++)
                if (dot[i][k] * dot[i][k] >= tan2[k] * norm[i])
                    hit[m++] = k;
            if (m > best.length)
                best = Arrays.copyOf(hit, m);
        }
        // rays touching two ghosts i and j: d = (a C_i + b C_j + c C_i x C_j) / det
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                long g = dot[i][j], det = norm[i] * norm[j] - g * g;
                if (det == 0)
                    continue;
                // 1 - |a C_i + b C_j|^2 = Q / det with Q = base + 2 g L_i L_j
                long base = det - tan2[i] * norm[j] - tan2[j] * norm[i], p = tan2[i] * tan2[j];
                BigInteger gap =
                    big(2 * g * 2 * g).multiply(big(p)).subtract(big(base).multiply(big(base)));
                if (base < 0 && gap.signum() < 0)
                    continue; // the two outlines do not meet
                double root = Math.sqrt((double)p), q;
                if (base >= 0)
                    q = base + 2.0 * g * root;
                else
                    q = gap.doubleValue() / (2.0 * g * root - base);
                // a det and b det, rationalised to avoid cancellation
                BigInteger na = big(tan2[i] * norm[j])
                                    .multiply(big(norm[j]))
                                    .subtract(big(tan2[j] * g).multiply(big(g)));
                BigInteger nb = big(tan2[j] * norm[i])
                                    .multiply(big(norm[i]))
                                    .subtract(big(tan2[i] * g).multiply(big(g)));
                double ad = na.doubleValue() / (tan[i] * norm[j] + tan[j] * g);
                double bd = nb.doubleValue() / (tan[j] * norm[i] + tan[i] * g);
                long cx = y[i] * z[j] - z[i] * y[j], cy = z[i] * x[j] - x[i] * z[j];
                long cz = x[i] * y[j] - y[i] * x[j];
                for (int sign = 1; sign >= -1; sign -= 2) {
                    if (sign < 0 && q == 0)
                        break;
                    double s = sign * Math.sqrt(q);
                    int m = 0;
                    for (int k = 0; k < n; k++) {
                        double t = (double)(cx * x[k] + cy * y[k] + cz * z[k]);
                        double v = ad * dot[i][k] + bd * dot[j][k] + s * t;
                        if (k == i || k == j || v >= det * tan[k] * (1 - EPS))
                            hit[m++] = k;
                    }
                    if (m > best.length)
                        best = Arrays.copyOf(hit, m);
                }
            }
        StringBuilder sb = new StringBuilder();
        sb.append(best.length).append('\n');
        for (int i = 0; i < best.length; i++)
            sb.append(i > 0 ? " " : "").append(best[i] + 1);
        System.out.println(sb);
    }
}
