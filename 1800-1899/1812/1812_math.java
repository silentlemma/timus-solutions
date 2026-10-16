import java.util.Scanner;

public class Main {
    static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    static long isqrt(long v) {
        long r = (long) Math.sqrt((double) v);
        while (r * r > v) r--;
        while ((r + 1) * (r + 1) <= v) r++;
        return r;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long r1 = in.nextLong(), r2 = in.nextLong(), n = in.nextLong(), i = in.nextLong();
        long pos = i - 1;
        if (pos == 0) {
            System.out.println(r1 + "/1");
            return;
        }
        if (pos == 1L << n) {
            System.out.println(r2 + "/1");
            return;
        }
        // between touching neighbours 1/sqrt(r) adds up, so circle pos has
        // 1/sqrt(r) = a/sqrt(r1) + b/sqrt(r2), with a and b from Stern's sequence
        // found as alpha f(x) + beta f(x + 1) while x is halved level by level
        long alpha = 1, beta = 0, x = pos;
        for (int level = 0; level < n; level++) {
            if (x % 2 == 0) {
                alpha += beta;
            } else {
                beta += alpha;
            }
            x /= 2;
        }
        // with both a and b positive the radius is rational exactly when
        // r1 = g p^2 and r2 = g q^2 for g = gcd(r1, r2)
        long g = gcd(r1, r2), p = isqrt(r1 / g), q = isqrt(r2 / g);
        if (p * p * g != r1 || q * q * g != r2) {
            System.out.println("Irrational");
            return;
        }
        // r = 1 / ((a q + b p) / (p q sqrt(g)))^2
        long d = alpha * q + beta * p, num = g * p * p * q * q, den = d * d;
        long common = gcd(num, den);
        System.out.println(num / common + "/" + den / common);
    }
}
