import java.io.*;
import java.util.*;

public class Main {
    // two eggs already cover 10^18 floors with this many drops
    static final long MOST_DROPS = 2000000000L;

    // floors that t drops with k eggs can settle, the sum of C(t, i) over
    // i = 1..k, or n + 1 if that is more
    static long covered(long t, long k, long n) {
        long total = 0, term = 1;
        for (long i = 1; i <= k && i <= t; i++) {
            // term * (t - i + 1) / i without overflow: split term by i
            long q = term / i, r = term % i, f = t - i + 1;
            if (q > n / f)
                return n + 1;
            term = q * f + r * f / i;
            total += term;
            if (total > n)
                return n + 1;
        }
        return total;
    }

    static long drops(long k, long n) {
        if (k == 1)
            return n;
        long lo = 1, hi = MOST_DROPS;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (covered(mid, k, n) >= n)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(line);
            if (!st.hasMoreTokens())
                continue;
            long k = Long.parseLong(st.nextToken()), n = Long.parseLong(st.nextToken());
            if (k == 0 && n == 0)
                break;
            out.append(drops(k, n)).append('\n');
        }
        System.out.print(out);
    }
}
