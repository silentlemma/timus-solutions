import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final long CENTS = 100;

    static StringTokenizer st;
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(in.readLine());
        }
        return st.nextToken();
    }

    // the input numbers in hundredths
    static long readCents() throws IOException {
        return Math.round(Double.parseDouble(next()) * CENTS);
    }

    public static void main(String[] args) throws IOException {
        long n = Long.parseLong(next());
        long first = readCents(), last = readCents();
        // with d[i] = a[i] - a[i-1] the relation reads d[i+1] = d[i] + 2 c[i], so
        // a[N+1] - a[0] = (N + 1) d[1] + 2 sum (N + 1 - i) c[i]
        long weighted = 0;
        for (long i = 1; i <= n; i++) {
            weighted += (n + 1 - i) * readCents();
        }
        long num = n * first + last - 2 * weighted, den = n + 1;
        // the answer has two decimals; rounding only guards against bad input
        long q = (2 * Math.abs(num) + den) / (2 * den);
        String sign = num < 0 && q > 0 ? "-" : "";
        System.out.println(sign + q / CENTS + "." + String.format("%02d", q % CENTS));
    }
}
