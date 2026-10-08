import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        // numbers of valid prefixes ending with a zero and with another digit,
        // where the first digit is not zero
        BigInteger digits = BigInteger.valueOf(k - 1);
        BigInteger zero = BigInteger.ZERO, other = digits;
        for (int i = 1; i < n; i++) {
            BigInteger next = zero.add(other).multiply(digits);
            zero = other;
            other = next;
        }
        System.out.println(zero.add(other));
    }
}
