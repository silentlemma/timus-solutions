import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static BigInteger m;

    static BigInteger[][] multiply(BigInteger[][] x, BigInteger[][] y) {
        BigInteger[][] r = new BigInteger[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                r[i][j] = x[i][0].multiply(y[0][j]).add(x[i][1].multiply(y[1][j])).mod(m);
            }
        }
        return r;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger n = in.nextBigInteger(), k = in.nextBigInteger();
        m = in.nextBigInteger();
        BigInteger d = k.subtract(BigInteger.ONE).mod(m);
        // (zero, other) -> (other, (zero + other)(K - 1)) is the matrix step,
        // after the first digit the pair is (0, K - 1)
        BigInteger[][] step = {{BigInteger.ZERO, BigInteger.ONE}, {d, d}};
        BigInteger[][] power = {{BigInteger.ONE, BigInteger.ZERO},
                                {BigInteger.ZERO, BigInteger.ONE}};
        BigInteger e = n.subtract(BigInteger.ONE);
        for (int bit = 0; bit < e.bitLength(); bit++) {
            if (e.testBit(bit)) {
                power = multiply(power, step);
            }
            step = multiply(step, step);
        }
        System.out.println(power[0][1].add(power[1][1]).multiply(d).mod(m));
    }
}
