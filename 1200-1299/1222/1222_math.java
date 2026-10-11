import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static final int THREE = 3, FOUR = 4;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // threes are best: a 4 or more splits into parts with a larger product, and
        // three 2s lose to two 3s; a leftover 1 joins a 3 to make 2 + 2
        if (n < FOUR) {
            System.out.println(n);
            return;
        }
        int threes = n / THREE, rest = n % THREE;
        if (rest == 1) {
            threes--;
            rest = FOUR;
        }
        BigInteger product = BigInteger.valueOf(THREE).pow(threes);
        System.out.println(product.multiply(BigInteger.valueOf(Math.max(rest, 1))));
    }
}
