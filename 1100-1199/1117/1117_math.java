import java.util.Scanner;

public class Main {
    // sum over even e <= n of tz(e) - 1, that is sum over y <= n/2 of tz(y)
    static long evens(long n) {
        long m = n / 2;
        return m - Long.bitCount(m);
    }

    // tz(x) - 1 for an even x, 0 for an odd one
    static long extra(long x) { return x % 2 == 0 ? Long.numberOfTrailingZeros(x) - 1 : 0; }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong(), b = in.nextLong();
        long i = Math.min(a, b), j = Math.max(a, b);
        // numbers run through the tree in order, so a node's height is the count of
        // trailing zeros; between k and k + 1 the even one is an ancestor of the
        // odd leaf, and the message waits one day per node in between
        long days = i == j ? 0 : 2 * (evens(j) - evens(i - 1)) - extra(i) - extra(j);
        System.out.println(days);
    }
}
