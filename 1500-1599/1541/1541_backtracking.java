import java.util.*;

public class Main {
    static final int FASTEST = 100000; // no speed above this
    static final int MOST = 19;        // K < 20 leagues
    static final double SLACK = 1e-9;  // floating point margin for the pruning bound
    static final long BIG = 1L << 61;

    static double[] harmonic = new double[FASTEST + 2];
    static List<Long> path = new ArrayList<>();

    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }

    // the largest sum of count unit fractions with denominators from start
    static double most(long start, int count) {
        long end = Math.min(start + count - 1, FASTEST);
        return start <= end ? harmonic[(int)end] - harmonic[(int)start - 1] : 0;
    }

    // writes p / q as left or fewer unit fractions above 1 / last
    static boolean search(long p, long q, long last, int left) {
        if (p == 0)
            return true;
        if (left == 0)
            return false;
        long start = Math.max(last + 1, (q + p - 1) / p); // 1 / d must fit into p / q
        // left fractions of 1 / d at most
        long stop = q > BIG / left ? FASTEST : Math.min(FASTEST, left * q / p);
        if (start > stop || most(start, left) + SLACK < (double)p / q)
            return false;
        for (long d = start; d <= stop; d++) {
            if ((double)p / q - 1.0 / d > most(d + 1, left - 1) + SLACK)
                continue;
            // keep every fraction within 64 bits
            if (q > BIG / d || p > BIG / d)
                continue;
            long np = p * d - q, nq = q * d, g = gcd(np, nq);
            path.add(d);
            if (search(np / g, nq / g, d, left - 1))
                return true;
            path.remove(path.size() - 1);
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long m = in.nextLong(), n = in.nextLong();
        // M / N hours over legs of one league each: M / N = 1 / V1 + ... + 1 / VK
        // with distinct whole speeds, a sum of distinct unit fractions
        for (int d = 1; d <= FASTEST; d++)
            harmonic[d] = harmonic[d - 1] + 1.0 / d;
        // the fewest fractions first keeps the search small
        for (int k = 1; k <= MOST; k++)
            if (search(m, n, 0, k)) {
                StringBuilder out = new StringBuilder().append(path.size()).append('\n');
                for (int i = path.size() - 1; i >= 0; i--)
                    out.append(path.get(i)).append(i > 0 ? " " : "\n");
                System.out.print(out);
                return;
            }
        System.out.println(-1);
    }
}
