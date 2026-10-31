import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    // the sum of |a_i - a_j| over all pairs: in sorted order the i-th value
    // is larger than the i values before it
    static long pairSum(long[] a) {
        Arrays.sort(a);
        long total = 0, before = 0;
        for (int i = 0; i < a.length; i++) {
            total += a[i] * i - before;
            before += a[i];
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[] x = new long[n], y = new long[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            x[i] = (long)in.nval;
            in.nextToken();
            y[i] = (long)in.nval;
        }
        // walking along the streets, a visit covers |dx| + |dy|
        long pairs = (long)n * (n - 1) / 2;
        System.out.println((pairSum(x) + pairSum(y)) / pairs);
    }
}
