import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    // inputs are at most this
    static final int LARGEST = 10;

    public static void main(String[] args) throws IOException {
        // a(n) counts weak orders of n objects: the k objects tied for the
        // smallest place are any k of them, followed by a weak order of the rest
        long[][] binom = new long[LARGEST + 1][LARGEST + 1];
        long[] a = new long[LARGEST + 1];
        a[0] = 1;
        for (int n = 0; n <= LARGEST; n++) {
            binom[n][0] = 1;
            binom[n][n] = 1;
            for (int k = 1; k < n; k++) {
                binom[n][k] = binom[n - 1][k - 1] + binom[n - 1][k];
            }
        }
        for (int n = 1; n <= LARGEST; n++) {
            for (int k = 1; k <= n; k++) {
                a[n] += binom[n][k] * a[n - k];
            }
        }
        // tokenization avoids scanner's regular-expression and locale machinery.
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        java.io.PrintWriter out = new java.io.PrintWriter(System.out);
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int n = (int)in.nval;
            if (n < 0) {
                break;
            }
            out.println(a[n]);
        }
        out.flush();
    }
}
