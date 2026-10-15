import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static DataInputStream in = new DataInputStream(new BufferedInputStream(System.in));

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0') {
            c = in.read();
        }
        int value = 0;
        while (c >= '0') {
            value = value * 10 + c - '0';
            c = in.read();
        }
        return value;
    }

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
        int n = readInt();
        long[] x = new long[n], y = new long[n];
        for (int i = 0; i < n; i++) {
            x[i] = readInt();
            y[i] = readInt();
        }
        // walking along the streets, a visit covers |dx| + |dy|
        long pairs = (long) n * (n - 1) / 2;
        System.out.println((pairSum(x) + pairSum(y)) / pairs);
    }
}
