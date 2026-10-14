import java.math.BigInteger;
import java.util.*;

public class Main {
    static final int ODD = 3;  // the factor of the power of two for odd n
    static final int LESS = 4; // every count is that power times 1 or ODD, minus LESS

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        if (n == 1) {
            System.out.println(1);
            return;
        }
        // the counts of polygons grow by 4, 4, 8, 8, 16, 16, ... from zone 3 on:
        // 2^(n / 2 + 2) - 4 for even n and 3 * 2^(n / 2 + 1) - 4 for odd n
        BigInteger count = BigInteger.valueOf(n % 2 == 0 ? 1 : ODD).shiftLeft(n / 2 + 2 - n % 2);
        System.out.println(count.subtract(BigInteger.valueOf(LESS)));
    }
}
