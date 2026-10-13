import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    static final long SPEED = 4; // bounces k come at 4 h sin(a) k (k + 1) down the slope
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens = new StringTokenizer("");

    static String next() throws IOException {
        while (!tokens.hasMoreTokens())
            tokens = new StringTokenizer(in.readLine());
        return tokens.nextToken();
    }

    // the integer square root by Newton's method, starting above the root
    static BigInteger isqrt(BigInteger n) {
        if (n.compareTo(BigInteger.ONE) <= 0)
            return n;
        BigInteger x = BigInteger.ONE.shiftLeft(n.bitLength() / 2 + 1);
        while (true) {
            BigInteger y = x.add(n.divide(x)).shiftRight(1);
            if (y.compareTo(x) >= 0)
                return x;
            x = y;
        }
    }

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(next());
        StringBuilder out = new StringBuilder();
        while (t-- > 0) {
            BigInteger height = new BigInteger(next());
            BigInteger run = new BigInteger(next());
            long drop = Long.parseLong(next());
            // the largest k with SPEED * drop * height * k (k + 1) <= run^2 + height^2
            BigInteger x = run.multiply(run).add(height.multiply(height));
            BigInteger q = x.divide(height.multiply(BigInteger.valueOf(SPEED * drop)));
            BigInteger s = isqrt(q.shiftLeft(2).add(BigInteger.ONE));
            BigInteger k = s.subtract(BigInteger.ONE).shiftRight(1);
            out.append(k.add(BigInteger.ONE)).append('\n');
        }
        System.out.print(out);
    }
}
