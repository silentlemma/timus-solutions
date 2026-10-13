import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // a number of k digits 1 and 2 divisible by 2^k: put 1 or 2 in front of the
        // one for k - 1, whichever keeps one more factor 2
        BigInteger value = BigInteger.ZERO, power = BigInteger.ONE;
        char[] digits = new char[n];
        for (int k = 0; k < n; k++) {
            BigInteger next = value.add(power);
            char d = '1';
            // divisible by 2^(k+1): the lowest set bit is at k + 1 or higher
            if (next.getLowestSetBit() <= k) {
                next = next.add(power);
                d = '2';
            }
            value = next;
            digits[n - 1 - k] = d;
            power = power.multiply(BigInteger.TEN);
        }
        System.out.println(new String(digits));
    }
}
