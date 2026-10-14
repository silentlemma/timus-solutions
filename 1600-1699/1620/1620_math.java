import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), m = in.nextLong();
        int k = in.nextInt();
        // each flip moves the expectation to E (1 - 2/n) + 1, so after k flips
        // E = n/2 + (m - n/2) ((n - 2)/n)^k = (n^(k+1) + (2m - n)(n - 2)^k) / (2 n^k)
        BigInteger bn = BigInteger.valueOf(n);
        BigInteger tail = BigInteger.valueOf(n - 2).pow(k).multiply(BigInteger.valueOf(2 * m - n));
        BigInteger num = bn.pow(k + 1).add(tail);
        if (num.signum() == 0) {
            System.out.println("0/1");
            return;
        }
        // the denominator 2 n^k by primes: only they can divide num, and
        // dividing by small primes is much faster than a gcd of huge numbers
        BigInteger den = BigInteger.ONE;
        long rest = 2 * n;
        for (long p = 2; p <= rest; p++) {
            if (p * p > rest)
                p = rest;
            if (rest % p != 0)
                continue;
            int e = 0;
            while (rest % p == 0) {
                rest /= p;
                e++;
            }
            int two = p == 2 ? 1 : 0;
            long power = (long)(e - two) * k + two; // the exponent in 2 n^k
            BigInteger bp = BigInteger.valueOf(p);
            while (power > 0) {
                BigInteger[] qr = num.divideAndRemainder(bp);
                if (qr[1].signum() != 0)
                    break;
                num = qr[0];
                power--;
            }
            den = den.multiply(bp.pow((int)power));
        }
        System.out.println(num + "/" + den);
    }
}
