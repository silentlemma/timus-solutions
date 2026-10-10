import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), m = in.nextLong();
        // from the target backwards: the last m km take one load; before it, a
        // stretch of m / (2k - 1) km is crossed 2k - 1 times to bring k loads
        double stretch = 0;
        long k = 1;
        while (stretch + (double)m / (2 * k - 1) < n) {
            stretch += (double)m / (2 * k - 1);
            k++;
        }
        // fuel = (k-1) m + (2k-1) n - sum over i < k of m (2k-1) / (2i-1); its
        // fractional sum f = sum r_i / (2i-1) is kept exactly as num / den
        long whole = (k - 1) * m + (2 * k - 1) * n;
        BigInteger num = BigInteger.ZERO, den = BigInteger.ONE;
        double approx = 0;
        for (long i = 1; i < k; i++) {
            long d = 2 * i - 1, r = m * (2 * k - 1) % d;
            whole -= m * (2 * k - 1) / d;
            if (r == 0) {
                continue;
            }
            approx += (double)r / d;
            long g = gcd(d, den.mod(BigInteger.valueOf(d)).longValue());
            BigInteger scale = BigInteger.valueOf(d / g);
            // num/den + r/d over the denominator den * (d / g)
            num = num.multiply(scale).add(
                den.divide(BigInteger.valueOf(g)).multiply(BigInteger.valueOf(r)));
            den = den.multiply(scale);
        }
        // floor(f) from its approximation, then corrected exactly
        long t = (long)Math.floor(approx);
        while (t > 0 && den.multiply(BigInteger.valueOf(t)).compareTo(num) > 0) {
            t--;
        }
        while (den.multiply(BigInteger.valueOf(t + 1)).compareTo(num) <= 0) {
            t++;
        }
        System.out.println(whole - t);
    }
}
