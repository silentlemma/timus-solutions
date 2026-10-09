import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        StringBuilder out = new StringBuilder();
        BigInteger a = BigInteger.valueOf(2);
        for (int i = 0; i < n; i++) {
            out.append(a).append('\n');
            // after the shares 1/a(1) .. 1/a(k) the remainder is 1/(a(k+1) - 1), and the
            // largest share that still leaves something is 1/a(k+1)
            a = a.multiply(a.subtract(BigInteger.ONE)).add(BigInteger.ONE);
        }
        System.out.print(out);
    }
}
