import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // derangements: d(1) = 0 and d(k) = k d(k - 1) + (-1)^k
        BigInteger count = BigInteger.ZERO;
        for (int k = 2; k <= n; k++) {
            count = count.multiply(BigInteger.valueOf(k));
            count = k % 2 == 0 ? count.add(BigInteger.ONE) : count.subtract(BigInteger.ONE);
        }
        System.out.println(count);
    }
}
