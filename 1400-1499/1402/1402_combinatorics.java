import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // ordered choices of k different drinks: n (n - 1) ... (n - k + 1), for k from 2,
        // the sum for n = 21 needs more than 64 bits
        BigInteger total = BigInteger.ZERO, ways = BigInteger.valueOf(n);
        for (int k = 2; k <= n; k++) {
            ways = ways.multiply(BigInteger.valueOf(n - k + 1));
            total = total.add(ways);
        }
        System.out.println(total);
    }
}
