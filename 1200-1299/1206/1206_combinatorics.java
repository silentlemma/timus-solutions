import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static final int FIRST = 36, OTHER = 55;

    public static void main(String[] args) {
        int k = new Scanner(System.in).nextInt();
        // no position may carry: 36 pairs of leading digits with a sum of at
        // most 9, and 55 pairs of digits from 0 in every other position
        BigInteger count = BigInteger.valueOf(OTHER).pow(k - 1).multiply(BigInteger.valueOf(FIRST));
        System.out.println(count);
    }
}
