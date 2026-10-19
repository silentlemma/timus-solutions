import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long pRe;
    static long pIm;

    // x / y rounded to the nearest Gaussian integer in both parts
    static long[] quotient(long xRe, long xIm, long yRe, long yIm) {
        long n = yRe * yRe + yIm * yIm;
        long re = xRe * yRe + xIm * yIm;
        long im = xIm * yRe - xRe * yIm;
        return new long[] {Math.floorDiv(2 * re + n, 2 * n), Math.floorDiv(2 * im + n, 2 * n)};
    }

    // what is left of x after taking away the nearest multiple of p, stored
    // back into x: its norm is at most half the norm of p
    static void reduce(long[] x) {
        long[] q = quotient(x[0], x[1], pRe, pIm);
        x[0] -= pRe * q[0] - pIm * q[1];
        x[1] -= pRe * q[1] + pIm * q[0];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken());
        long[][][] a = new long[n][n][2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j][0] = Long.parseLong(st.nextToken());
                a[i][j][1] = Long.parseLong(st.nextToken());
            }
        }
        pRe = Long.parseLong(st.nextToken());
        pIm = Long.parseLong(st.nextToken());
        for (long[][] row : a) {
            for (long[] x : row) {
                reduce(x);
            }
        }
        // elimination modulo p: the Euclidean algorithm on the Gaussian
        // integers clears each column below the diagonal with row operations,
        // which keep the determinant; the entries of the column only shrink
        long[] det = {1, 0};
        for (int k = 0; k < n; k++) {
            for (int i = k + 1; i < n; i++) {
                while (a[i][k][0] != 0 || a[i][k][1] != 0) {
                    long[] q = quotient(a[k][k][0], a[k][k][1], a[i][k][0], a[i][k][1]);
                    for (int j = k; j < n; j++) {
                        long[] x = a[k][j];
                        long[] y = a[i][j];
                        x[0] -= q[0] * y[0] - q[1] * y[1];
                        x[1] -= q[0] * y[1] + q[1] * y[0];
                        if (j > k) {
                            reduce(x);
                        }
                    }
                    long[][] row = a[k];
                    a[k] = a[i];
                    a[i] = row;
                    det[0] = -det[0];
                    det[1] = -det[1];
                }
            }
            long[] d = a[k][k];
            long[] product = {det[0] * d[0] - det[1] * d[1], det[0] * d[1] + det[1] * d[0]};
            reduce(product);
            det = product;
        }
        System.out.println(det[0] + " " + det[1]);
    }
}
