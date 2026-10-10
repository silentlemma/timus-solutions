import java.util.Scanner;

public class Main {
    static long a1, a2, a3, a4, b1, b2, c;

    // the term after x, y
    static long next(long x, long y) {
        long h = a1 * x * y + a2 * x + a3 * y + a4;
        if (h > b1 && h > b2 && c > 0) {
            h -= (h - b2 + c - 1) / c * c;
        }
        return h;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        a1 = in.nextLong();
        a2 = in.nextLong();
        a3 = in.nextLong();
        a4 = in.nextLong();
        b1 = in.nextLong();
        b2 = in.nextLong();
        c = in.nextLong();
        long x1 = in.nextLong(), x2 = in.nextLong();
        // the next term depends only on the last two, so the pairs of
        // neighbouring terms run into a cycle; Brent's method finds it in
        // O(1) memory: the length first, then where it starts
        long power = 1, length = 1;
        long sx = x1, sy = x2, fx = x2, fy = next(x1, x2);
        while (sx != fx || sy != fy) {
            if (power == length) {
                sx = fx;
                sy = fy;
                power *= 2;
                length = 0;
            }
            long t = next(fx, fy);
            fx = fy;
            fy = t;
            length++;
        }
        sx = fx = x1;
        sy = fy = x2;
        for (long k = 0; k < length; k++) {
            long t = next(fx, fy);
            fx = fy;
            fy = t;
        }
        long start = 1;
        while (sx != fx || sy != fy) {
            long t = next(sx, sy);
            sx = sy;
            sy = t;
            t = next(fx, fy);
            fx = fy;
            fy = t;
            start++;
        }
        System.out.println(start + " " + length);
    }
}
