import java.util.Scanner;

public class Main {
    static long big, small;

    static long pairs(long k) {
        return k * (k - 1) / 2;
    }

    static long gcd(long x, long y) {
        return y == 0 ? x : gcd(y, x % y);
    }

    // pairs among the first m sleepers on one page of both notebooks: walk the
    // pages of the larger size, each cut by the smaller pages into a head,
    // whole pages and a tail
    static long shared(long m) {
        long total = 0;
        for (long start = 0; start < m; start += big) {
            long end = Math.min(start + big, m);
            long cut = (start / small + 1) * small;
            if (cut >= end) {
                total += pairs(end - start);
            } else {
                long whole = (end - cut) / small, tail = (end - cut) % small;
                total += pairs(cut - start) + whole * pairs(small) + pairs(tail);
            }
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong(), b = in.nextLong(), n = in.nextLong();
        big = Math.max(a, b);
        small = Math.min(a, b);
        // both page breaks repeat every lcm(a, b) sleepers, and so do the pairs
        long period = a / gcd(a, b) * b;
        long both = period <= n ? n / period * shared(period) + shared(n % period) : shared(n);
        long vasily = n / a * pairs(a) + pairs(n % a);
        System.out.println(vasily - both);
    }
}
