import java.util.*;

public class Main {
    static final long BASE = 10;
    // more than 10^18 ones are counted below this floor
    static final long TOP = 1000000000000000000L;

    // the number of digits 1 in the numbers from 1 to x: at each place p, every
    // full block of 10 p numbers holds p ones there, and the last part adds p,
    // the rest past the 1, or nothing, as its digit is above, at or below 1
    static long ones(long x) {
        long total = 0;
        // x is at least 1; p stops before p * 10 could pass 10^19
        for (long p = 1;; p *= BASE) {
            long high = x / p / BASE, digit = x / p % BASE, low = x % p;
            total += high * p + (digit > 1 ? p : digit == 1 ? low + 1 : 0);
            if (p > x / BASE)
                break;
        }
        return total;
    }

    public static void main(String[] args) {
        long k = new Scanner(System.in).nextLong();
        // the floor where the k-th one was counted is the first x with ones(x) >= k
        long lo = 1, hi = TOP;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (ones(mid) >= k)
                hi = mid;
            else
                lo = mid + 1;
        }
        System.out.println(ones(lo) == k ? String.valueOf(lo) : "Petr lies");
    }
}
