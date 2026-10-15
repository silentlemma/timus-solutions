import java.util.*;

public class Main {
    // keeps an exact integer whole; no expectation lies that close below one
    static final double EPS = 1e-9;

    static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // dp[s][l]: the chance that a random permutation of s elements has only
        // cycles of the lengths seen so far, and that their lcm is l
        List<Map<Long, Double>> dp = new ArrayList<>();
        for (int s = 0; s <= n; s++)
            dp.add(new HashMap<>());
        dp.get(0).put(1L, 1.0);
        for (int k = 1; k <= n; k++) {
            List<Map<Long, Double>> next = new ArrayList<>();
            for (Map<Long, Double> cell : dp)
                next.add(new HashMap<>(cell));
            for (int s = 0; s < n; s++)
                for (Map.Entry<Long, Double> e : dp.get(s).entrySet()) {
                    long lcm = e.getKey();
                    long joined = lcm / gcd(lcm, k) * k;
                    double weight = e.getValue();
                    for (int m = 1; s + m * k <= n; m++) {
                        weight /= (double)k * m; // m cycles of length k: 1 / (k^m m!)
                        next.get(s + m * k).merge(joined, weight, Double::sum);
                    }
                }
            dp = next;
        }
        double expected = 0;
        for (Map.Entry<Long, Double> e : dp.get(n).entrySet())
            expected += e.getKey() * e.getValue();
        System.out.println((long)(expected + EPS));
    }
}
