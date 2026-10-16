import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    // the best split of a prime p < 31623 never uses a prime above 700
    static final int BOUND = 1000;

    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        long p = n;
        for (long d = 2; d * d <= n; d++) {
            if (n % d == 0) {
                p = d;
                break;
            }
        }
        // the largest gcd is n / p: the pockets hold n/p times parts adding up
        // to p, and the lcm is n/p times the lcm of the parts. Parts that are
        // powers of distinct primes, padded with ones, give the best lcm
        long unit = n / p;
        int limit = (int) p;
        List<int[]> groups = new ArrayList<>();
        boolean[] composite = new boolean[BOUND];
        for (int q = 2; q < BOUND && q < limit; q++) {
            if (composite[q]) continue;
            for (int m = q * q; m < BOUND; m += q) composite[m] = true;
            List<Integer> powers = new ArrayList<>();
            for (long w = q; w < limit; w *= q) powers.add((int) w);
            groups.add(powers.stream().mapToInt(Integer::intValue).toArray());
        }
        // best[s]: the largest log of an lcm of parts with weight at most s
        double[] best = new double[limit + 1];
        byte[][] choices = new byte[groups.size()][];
        for (int g = 0; g < groups.size(); g++) {
            int[] powers = groups.get(g);
            double[] next = best.clone();
            byte[] choice = new byte[limit + 1];
            for (int e = 0; e < powers.length; e++) {
                int w = powers[e];
                double value = Math.log(w);
                for (int s = w; s <= limit; s++) {
                    double candidate = best[s - w] + value;
                    if (candidate > next[s]) {
                        next[s] = candidate;
                        choice[s] = (byte) (e + 1);
                    }
                }
            }
            best = next;
            choices[g] = choice;
        }
        StringBuilder out = new StringBuilder();
        int s = limit, used = 0;
        for (int g = groups.size() - 1; g >= 0; g--) {
            int e = choices[g][s];
            if (e > 0) {
                int w = groups.get(g)[e - 1];
                out.append(w * unit).append(' ');
                s -= w;
                used += w;
            }
        }
        for (; used < limit; used++) out.append(unit).append(' ');
        System.out.println(out.toString().trim());
    }
}
