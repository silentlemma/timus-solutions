import java.util.Scanner;

public class Main {
    // numbers 1 .. t that are sums of contests: k contests give [kx, ky],
    // once k (y - x) >= x - 1 the next interval touches this one, so from
    // the first such k on everything is covered, and before it they are apart
    static long covered(long t, long x, long y) {
        if (t < x) {
            return 0;
        }
        if (y == x) {
            return t / x;
        }
        long joined = Math.max(1, (x - 1 + (y - x) - 1) / (y - x));
        long full = Math.min(joined - 1, t / y); // the intervals that end by t
        long count = (y - x) * (full * (full + 1) / 2) + full;
        long k = full + 1;
        if (k <= joined - 1 && k <= t / x) {
            count += t - k * x + 1;
        }
        if (joined <= t / x) {
            count += t - joined * x + 1;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long x = in.nextLong();
        long y = in.nextLong();
        long low = in.nextLong();
        long high = in.nextLong();
        System.out.println(covered(high, x, y) - covered(low - 1, x, y));
    }
}
