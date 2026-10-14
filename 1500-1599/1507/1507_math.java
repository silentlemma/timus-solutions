import java.io.*;

public class Main {
    // the boolean product of two matrices kept as row bitmasks
    static long[] multiply(long[] x, long[] y) {
        long[] out = new long[x.length];
        for (int i = 0; i < x.length; i++)
            for (int j = 0; j < y.length; j++)
                if ((x[i] >> j & 1) != 0)
                    out[i] |= y[j];
        return out;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // only whether an entry is zero matters: all entries are non-negative
        long[] a = new long[n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                in.nextToken();
                if (in.nval != 0)
                    a[i] |= 1L << j;
            }
        int low = n * (n - 1), high = n * (n + 1);
        // A^low by repeated squaring
        long[] cur = new long[n], base = a;
        for (int i = 0; i < n; i++)
            cur[i] = 1L << i;
        for (int e = low; e > 0; e >>= 1) {
            if ((e & 1) != 0)
                cur = multiply(cur, base);
            base = multiply(base, base);
        }
        long[] seen = new long[n];
        for (int k = low; k <= high; k++) {
            for (int i = 0; i < n; i++)
                seen[i] |= cur[i];
            cur = multiply(cur, a);
        }
        long full = (1L << n) - 1;
        boolean positive = true;
        for (long s : seen)
            positive &= s == full;
        System.out.println(positive ? "Yes" : "No");
    }
}
