import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    static final long PRIME = 1000000007; // independence is decided exactly, modulo this prime
    static final double ZERO_BAND = 5e-6; // values that print as 0.00000, kept without a minus

    static long power(long base, long exp) {
        long result = 1;
        base %= PRIME;
        for (; exp > 0; exp >>= 1) {
            if ((exp & 1) == 1) {
                result = result * base % PRIME;
            }
            base = base * base % PRIME;
        }
        return result;
    }

    // indices of a maximal linearly independent subset, found by Gaussian
    // elimination modulo PRIME, so no rounding decides the rank
    static List<Integer> independent(long[][] vectors) {
        List<long[]> basis = new ArrayList<>();
        List<Integer> pivots = new ArrayList<>();
        List<Integer> chosen = new ArrayList<>();
        for (int k = 0; k < vectors.length; k++) {
            long[] row = new long[vectors[k].length];
            for (int i = 0; i < row.length; i++) {
                row[i] = (vectors[k][i] % PRIME + PRIME) % PRIME;
            }
            for (int b = 0; b < basis.size(); b++) {
                long f = row[pivots.get(b)];
                if (f != 0) {
                    long[] base = basis.get(b);
                    for (int i = 0; i < row.length; i++) {
                        row[i] = ((row[i] - f * base[i]) % PRIME + PRIME) % PRIME;
                    }
                }
            }
            int pivot = -1;
            for (int i = 0; i < row.length && pivot < 0; i++) {
                if (row[i] != 0) {
                    pivot = i;
                }
            }
            if (pivot < 0) {
                continue;
            }
            long inv = power(row[pivot], PRIME - 2);
            for (int i = 0; i < row.length; i++) {
                row[i] = row[i] * inv % PRIME;
            }
            basis.add(row);
            pivots.add(pivot);
            chosen.add(k);
        }
        return chosen;
    }

    static double dot(double[] u, double[] v) {
        double s = 0;
        for (int i = 0; i < u.length; i++) {
            s += u[i] * v[i];
        }
        return s;
    }

    // Q and R (by columns) of independent columns: Gram-Schmidt with every
    // projection done twice, which keeps Q orthonormal to rounding error
    static void qr(List<double[]> columns, List<double[]> q, List<double[]> r) {
        for (double[] col : columns) {
            double[] v = col.clone();
            double[] coef = new double[q.size() + 1];
            for (int pass = 0; pass < 2; pass++) {
                for (int k = 0; k < q.size(); k++) {
                    double[] u = q.get(k);
                    double c = dot(u, v);
                    coef[k] += c;
                    for (int i = 0; i < v.length; i++) {
                        v[i] -= c * u[i];
                    }
                }
            }
            double norm = Math.sqrt(dot(v, v));
            for (int i = 0; i < v.length; i++) {
                v[i] /= norm;
            }
            coef[q.size()] = norm;
            q.add(v);
            r.add(coef);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        int m = (int) in.nval;
        // engine i pushes along row i; the thrust is the sum of X_i times row i.
        // The shortest best X lies in the span of the columns c_j = (row i at j)_i
        long[][] cols = new long[n][m];
        double[][] real = new double[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                in.nextToken();
                cols[j][i] = (long) in.nval;
                real[j][i] = in.nval;
            }
        }
        double[] b = new double[n];
        for (int j = 0; j < n; j++) {
            in.nextToken();
            b[j] = in.nval;
        }
        List<double[]> picked = new ArrayList<>();
        for (int j : independent(cols)) {
            picked.add(real[j]);
        }
        List<double[]> basis = new ArrayList<>();
        qr(picked, basis, new ArrayList<>());
        // with X = sum of w_k basis[k], the thrust is K w for K[j][k] = c_j . q_k,
        // and K has full column rank: least squares by QR of K
        int size = basis.size();
        List<double[]> kCols = new ArrayList<>();
        for (double[] u : basis) {
            double[] col = new double[n];
            for (int j = 0; j < n; j++) {
                col[j] = dot(real[j], u);
            }
            kCols.add(col);
        }
        List<double[]> q2 = new ArrayList<>();
        List<double[]> upper = new ArrayList<>();
        qr(kCols, q2, upper);
        double[] w = new double[size];
        for (int i = size - 1; i >= 0; i--) {
            double s = dot(q2.get(i), b);
            for (int k = i + 1; k < size; k++) {
                s -= upper.get(k)[i] * w[k];
            }
            w[i] = s / upper.get(i)[i];
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < m; i++) {
            double x = 0;
            for (int k = 0; k < size; k++) {
                x += w[k] * basis.get(k)[i];
            }
            if (Math.abs(x) < ZERO_BAND) {
                x = 0;
            }
            out.append(String.format(Locale.US, "%.5f", x)).append(i + 1 < m ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
