import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    static final BigInteger TWO = BigInteger.valueOf(2);

    // the sum of (a * i + b) / m over i = 0 .. n - 1
    static BigInteger floorSum(BigInteger n, BigInteger m, BigInteger a, BigInteger b) {
        BigInteger total = BigInteger.ZERO;
        while (true) {
            if (a.compareTo(m) >= 0) {
                BigInteger pairs = n.multiply(n.subtract(BigInteger.ONE)).divide(TWO);
                total = total.add(pairs.multiply(a.divide(m)));
                a = a.mod(m);
            }
            if (b.compareTo(m) >= 0) {
                total = total.add(n.multiply(b.divide(m)));
                b = b.mod(m);
            }
            BigInteger top = a.multiply(n).add(b);
            if (top.compareTo(m) < 0) return total;
            BigInteger[] qr = top.divideAndRemainder(m);
            n = qr[0];
            b = qr[1];
            BigInteger swap = m;
            m = a;
            a = swap;
        }
    }

    // how many numbers from 1 to limit are a * x + b * y with a, b >= 0
    static BigInteger countUpTo(long limit, long x, long y) {
        long g = BigInteger.valueOf(x).gcd(BigInteger.valueOf(y)).longValue();
        limit /= g;
        x /= g;
        y /= g;
        // with x and y coprime every such number has exactly one form with
        // b < x; for each b the values of a run from 0 to (limit - b*y) / x
        long last = Math.min(limit / y, x - 1);
        BigInteger forms = floorSum(BigInteger.valueOf(last + 1), BigInteger.valueOf(x),
                BigInteger.valueOf(y), BigInteger.valueOf(limit - y * last));
        // zero is not a volume size
        return forms.add(BigInteger.valueOf(last));
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens = new StringTokenizer("");

    static long next() throws IOException {
        while (!tokens.hasMoreTokens()) tokens = new StringTokenizer(in.readLine());
        return Long.parseLong(tokens.nextToken());
    }

    public static void main(String[] args) throws IOException {
        long tests = next();
        StringBuilder out = new StringBuilder();
        for (long t = 0; t < tests; t++) {
            long x = next(), y = next(), l = next(), r = next();
            out.append(countUpTo(r, x, y).subtract(countUpTo(l - 1, x, y))).append('\n');
        }
        System.out.print(out);
    }
}
