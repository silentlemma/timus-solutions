import java.math.BigInteger;
import java.util.*;

public class Main {
    static final BigInteger LETTERS = BigInteger.valueOf(26);

    // the k-th password from 1: by length, then alphabetically, which is k
    // written in bijective base 26 with digits a to z
    static String word(BigInteger k) {
        StringBuilder out = new StringBuilder();
        while (k.signum() > 0) {
            BigInteger[] qr = k.subtract(BigInteger.ONE).divideAndRemainder(LETTERS);
            out.append((char)('a' + qr[1].intValue()));
            k = qr[0];
        }
        return out.reverse().toString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        BigInteger total = BigInteger.ZERO, power = BigInteger.ONE;
        for (int i = 0; i < n; i++) {
            power = power.multiply(LETTERS);
            total = total.add(power);
        }
        BigInteger[] qr = total.divideAndRemainder(BigInteger.valueOf(m));
        BigInteger share = qr[0];
        int extra = qr[1].intValue();
        // the first extra processors take one password more
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < m; i++) {
            BigInteger start = share.multiply(BigInteger.valueOf(i))
                                   .add(BigInteger.valueOf(Math.min(i, extra) + 1));
            BigInteger end = share.multiply(BigInteger.valueOf(i + 1))
                                 .add(BigInteger.valueOf(Math.min(i + 1, extra)));
            out.append(word(start)).append('-').append(word(end)).append('\n');
        }
        System.out.print(out);
    }
}
