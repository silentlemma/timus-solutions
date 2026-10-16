import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final long LIMIT = 1_000_000_000_000_000_000L;
    static final long[] PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};
    static final int MOST = 64;

    static List<long[]> found = new ArrayList<>();

    // the smallest number with a given set of exponents puts the largest
    // exponents on the smallest primes, so only numbers 2^a 3^b 5^c ...
    // with a >= b >= c >= ... can be answers
    static void grow(int index, int cap, long value, long divisors) {
        found.add(new long[] {value, divisors});
        if (index == PRIMES.length) {
            return;
        }
        for (int e = 1; e <= cap; e++) {
            if (value > LIMIT / PRIMES[index]) {
                break;
            }
            value *= PRIMES[index];
            grow(index + 1, e, value, divisors * (e + 1));
        }
    }

    public static void main(String[] args) {
        grow(0, MOST, 1, 1);
        found.sort((a, b) -> Long.compare(a[0], b[0]));
        int size = found.size();
        long[] values = new long[size], bestValue = new long[size], bestCount = new long[size];
        long topValue = 0, topCount = 0;
        for (int i = 0; i < size; i++) {
            long[] f = found.get(i);
            if (f[1] > topCount) {
                topValue = f[0];
                topCount = f[1];
            }
            values[i] = f[0];
            bestValue[i] = topValue;
            bestCount[i] = topCount;
        }
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        StringBuilder out = new StringBuilder();
        for (int q = 0; q < t; q++) {
            long n = in.nextLong();
            int lo = 0, hi = size - 1;
            while (lo < hi) {
                int mid = (lo + hi + 1) / 2;
                if (values[mid] <= n) {
                    lo = mid;
                } else {
                    hi = mid - 1;
                }
            }
            out.append(bestValue[lo]).append(' ').append(bestCount[lo]).append('\n');
        }
        System.out.print(out);
    }
}
