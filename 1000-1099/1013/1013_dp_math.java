import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    static final BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static BigInteger modulus, coefficient;

    static String next() throws Exception {
        while (tokens == null || !tokens.hasMoreTokens())
            tokens = new StringTokenizer(input.readLine());
        return tokens.nextToken();
    }

    static BigInteger[] multiply(BigInteger[] x, BigInteger[] y) {
        BigInteger product = x[0].multiply(y[0]);
        BigInteger constant = x[1].multiply(y[1]);
        BigInteger cross =
            x[0].add(x[1]).multiply(y[0].add(y[1])).subtract(product).subtract(constant);
        BigInteger shared = product.mod(modulus).multiply(coefficient);
        // x²=cx+c reduces every polynomial to a*x+b. This composition
        // needs four products and no modular inverses, even for even moduli.
        return new BigInteger[] {shared.add(cross).mod(modulus), shared.add(constant).mod(modulus)};
    }

    public static void main(String[] args) throws Exception {
        long n = Long.parseLong(next());
        long base = Long.parseLong(next());
        modulus = new BigInteger(next());
        coefficient = BigInteger.valueOf(base - 1).mod(modulus);
        BigInteger[] power = {BigInteger.ZERO, BigInteger.ONE};
        BigInteger[] step = {BigInteger.ONE, BigInteger.ZERO};
        while (n > 0) {
            if ((n & 1) != 0)
                power = multiply(power, step);
            step = multiply(step, step);
            n >>= 1;
        }
        // A(0)=1 and A(1)=c, so a*x+b represents a*c+b for this sequence.
        System.out.println(power[0].multiply(coefficient).add(power[1]).mod(modulus));
    }
}
