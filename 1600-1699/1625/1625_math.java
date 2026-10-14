import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        StringBuilder out = new StringBuilder();
        // The Catalan numbers: every leading square of their Hankel matrix has
        // determinant 1. C(k + 1) = C(k) * 2 (2k + 1) / (k + 2), always exact.
        BigInteger c = BigInteger.ONE;
        for (int k = 0; k < 2 * n - 1; k++) {
            out.append(c).append('\n');
            c = c.multiply(BigInteger.valueOf(2 * (2 * k + 1))).divide(BigInteger.valueOf(k + 2));
        }
        System.out.print(out);
    }
}
