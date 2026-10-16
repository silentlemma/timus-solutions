import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int QUARTERS = 4;
    static final double CLOSE = 1e-9;

    static long isqrt(long v) {
        long r = (long) Math.sqrt((double) v);
        while (r * r > v) r--;
        while ((r + 1) * (r + 1) <= v) r++;
        return r;
    }

    // whether p * q >= r * s for nonnegative values: in doubles when the
    // two sides are clearly apart, exactly otherwise
    static boolean atLeast(long p, long q, long r, long s) {
        double left = (double) p * q, right = (double) r * s;
        if (Math.abs(left - right) > CLOSE * Math.max(left, right)) return left > right;
        BigInteger exactLeft = BigInteger.valueOf(p).multiply(BigInteger.valueOf(q));
        return exactLeft.compareTo(BigInteger.valueOf(r).multiply(BigInteger.valueOf(s))) >= 0;
    }

    static long n;

    static boolean inside(long px, long py) {
        return px >= 0 && px * px + py * py <= n;
    }

    // the sum of isqrt(n - x*x) over x = 0 .. m, where 2*m*m <= n, found by
    // walking from m to the left along the upper hull of the lattice points
    // in the disk; a vector (a, b) moves a columns left and b rows up
    static long columnSum(long m) {
        long x = m, y = isqrt(n - m * m);
        long total = y;
        long[] stackA = {1, 1}, stackB = {0, 1};
        int size = 2;
        while (x > 0) {
            size--;
            long a1 = stackA[size], b1 = stackB[size];
            while (inside(x - a1, y + b1)) {
                // the columns x - a1 .. x - 1 lie under this hull edge
                total += a1 * y + (a1 - 1) * (b1 - 1) / 2 + b1;
                x -= a1;
                y += b1;
            }
            if (x - a1 < 0) break;
            long a2 = a1, b2 = b1;
            while (true) {
                a1 = stackA[size - 1];
                b1 = stackB[size - 1];
                if (inside(x - a1, y + b1)) break;
                a2 = a1;
                b2 = b1;
                size--;
            }
            while (true) {
                long a12 = a1 + a2, b12 = b1 + b2, nx = x - a12;
                if (nx < 0) break;
                if (inside(nx, y + b12)) {
                    if (size == stackA.length) {
                        stackA = Arrays.copyOf(stackA, 2 * size);
                        stackB = Arrays.copyOf(stackB, 2 * size);
                    }
                    stackA[size] = a12;
                    stackB[size++] = b12;
                    a1 = a12;
                    b1 = b12;
                } else {
                    // from the outside point nx, steps of (a1, b1) rise at
                    // least as fast as the circle, so no inside point lies
                    // between
                    if (atLeast(b1 * b1, n - nx * nx, a1 * a1, nx * nx)) break;
                    a2 = a12;
                    b2 = b12;
                }
            }
        }
        for (long column = 0; column < x; column++) total += isqrt(n - column * column);
        return total;
    }

    public static void main(String[] args) {
        long radius = new Scanner(System.in).nextLong();
        // slab (x, y) of the first quarter burns when its nearest corner is
        // strictly inside the circle: x*x + y*y <= radius^2 - 1
        n = radius * radius - 1;
        long m = isqrt(n / 2);
        long total = columnSum(m);
        // points with x < y twice, then the diagonal once
        long quarter = 2 * (total - m * (m + 1) / 2) + m + 1;
        System.out.println(QUARTERS * quarter);
    }
}
