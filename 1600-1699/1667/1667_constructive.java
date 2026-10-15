import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main {
    static final long ROOT_LIMIT = 316227766; // the largest integer whose square is at most 10^17
    static final int LEGS = 40; // Pythagorean pairs from m^2 - n^2 and 2mn with n < m < LEGS

    static final int STARTS = 30; // first terms of the arithmetic sequences
    static final int STEPS = 6; // their differences
    static final int OFFSETS = 30; // where the runs of consecutive primes start
    static final int PRIMES = 80;
    static final int HALF = 32; // a reduced fraction x / y is stored as x << HALF | y

    static class Row {
        long[] nums;
        long[] ratios; // sorted reduced fractions x / y < 1
        long top;

        Row(long[] nums) {
            this.nums = nums;
            List<Long> found = new ArrayList<>();
            for (long x : nums) {
                top = Math.max(top, x);
                for (long y : nums) {
                    if (x < y) {
                        long g = gcd(x, y);
                        found.add((x / g) << HALF | (y / g));
                    }
                }
            }
            ratios = new long[found.size()];
            for (int i = 0; i < ratios.length; i++) {
                ratios[i] = found.get(i);
            }
            Arrays.sort(ratios);
        }
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    // with S the sum of u^2 over u_1..u_k, the numbers 2u_1, ..., 2u_k and S - 1
    // have squares adding up to (S + 1)^2; null if they repeat
    static long[] fromUs(long[] us) {
        long total = 0;
        long[] nums = new long[us.length + 1];
        Set<Long> seen = new HashSet<>();
        for (int i = 0; i < us.length; i++) {
            total += us[i] * us[i];
            nums[i] = 2 * us[i];
            seen.add(nums[i]);
        }
        nums[us.length] = total - 1;
        seen.add(total - 1);
        return seen.size() == nums.length ? nums : null;
    }

    // lists of distinct positive integers whose squares add up to a square,
    // smallest maximum first
    static List<Row> lists(int size, long[] primes) {
        List<long[]> found = new ArrayList<>();
        if (size == 1) {
            found.add(new long[] {1});
        } else if (size == 2) {
            for (long m = 2; m < LEGS; m++) {
                for (long n = 1; n < m; n++) {
                    if (gcd(m, n) == 1 && (m - n) % 2 == 1) {
                        found.add(new long[] {m * m - n * n, 2 * m * n});
                    }
                }
            }
        } else {
            int k = size - 1;
            for (long s = 1; s < STARTS; s++) {
                for (long d = 1; d <= STEPS; d++) {
                    long[] us = new long[k];
                    for (int i = 0; i < k; i++) {
                        us[i] = s + d * i;
                    }
                    found.add(fromUs(us));
                }
            }
            for (int off = 0; off < OFFSETS; off++) {
                found.add(fromUs(Arrays.copyOfRange(primes, off, off + k)));
            }
        }
        List<Row> out = new ArrayList<>();
        for (long[] nums : found) {
            if (nums != null) {
                out.add(new Row(nums));
            }
        }
        out.sort((x, y) -> Long.compare(x.top, y.top));
        return out;
    }

    static boolean disjoint(long[] x, long[] y) {
        int i = 0;
        int j = 0;
        while (i < x.length && j < y.length) {
            if (x[i] == y[j]) {
                return false;
            }
            if (x[i] < y[j]) {
                i++;
            } else {
                j++;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        long[] primes = new long[PRIMES];
        int count = 0;
        for (long n = 2; count < PRIMES; n++) {
            boolean prime = true;
            for (int i = 0; i < count && primes[i] * primes[i] <= n; i++) {
                if (n % primes[i] == 0) {
                    prime = false;
                    break;
                }
            }
            if (prime) {
                primes[count++] = n;
            }
        }
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int t = (int) in.nval;
        Map<Integer, List<Row>> pool = new HashMap<>();
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < t; k++) {
            in.nextToken();
            int rows = (int) in.nval;
            in.nextToken();
            int cols = (int) in.nval;
            for (int size : new int[] {rows, cols}) {
                if (!pool.containsKey(size)) {
                    pool.put(size, lists(size, primes));
                }
            }
            // entry (i, j) is (a_i b_j)^2; two products a_i b_j and a_k b_l are
            // equal exactly when a_i / a_k = b_l / b_j, so no ratio may be shared
            Row found = null;
            Row other = null;
            long smallest = pool.get(cols).get(0).top;
            for (Row a : pool.get(rows)) {
                if (a.top * smallest > ROOT_LIMIT || found != null) {
                    break;
                }
                for (Row b : pool.get(cols)) {
                    if (a.top * b.top > ROOT_LIMIT) {
                        break;
                    }
                    if (disjoint(a.ratios, b.ratios)) {
                        found = a;
                        other = b;
                        break;
                    }
                }
            }
            if (k > 0) {
                out.append('\n');
            }
            if (found == null) {
                out.append("-1\n");
                continue;
            }
            for (long x : found.nums) {
                for (int j = 0; j < other.nums.length; j++) {
                    long v = x * other.nums[j];
                    out.append(v * v).append(j + 1 < other.nums.length ? ' ' : '\n');
                }
            }
        }
        System.out.print(out);
    }
}
