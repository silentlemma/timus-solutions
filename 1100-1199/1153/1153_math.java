import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    // 8 S + 1 = (2 N + 1)^2 for S = N (N + 1) / 2
    static final BigInteger EIGHT = BigInteger.valueOf(8);

    // the integer square root by Newton's method, starting above the root
    static BigInteger isqrt(BigInteger d) {
        BigInteger x = BigInteger.ONE.shiftLeft(d.bitLength() / 2 + 1);
        while (true) {
            BigInteger y = x.add(d.divide(x)).shiftRight(1);
            if (y.compareTo(x) >= 0) {
                return x;
            }
            x = y;
        }
    }

    public static void main(String[] args) {
        BigInteger total = new BigInteger(new Scanner(System.in).next());
        BigInteger root = isqrt(total.multiply(EIGHT).add(BigInteger.ONE));
        System.out.println(root.subtract(BigInteger.ONE).shiftRight(1));
    }
}
