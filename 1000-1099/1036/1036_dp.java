import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int DIGITS = 10;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int s = in.nextInt();
        int half = s / 2;
        if (s % 2 != 0 || half > (DIGITS - 1) * n) {
            System.out.println(0);
            return;
        }
        // ways[t]: the number of strings of the digits seen so far with digit sum t
        BigInteger[] ways = new BigInteger[half + 1];
        Arrays.fill(ways, BigInteger.ZERO);
        ways[0] = BigInteger.ONE;
        for (int k = 0; k < n; k++) {
            BigInteger[] next = new BigInteger[half + 1];
            for (int t = 0; t <= half; t++) {
                BigInteger sum = BigInteger.ZERO;
                for (int d = 0; d < DIGITS && d <= t; d++) {
                    sum = sum.add(ways[t - d]);
                }
                next[t] = sum;
            }
            ways = next;
        }
        // the two halves are chosen independently
        System.out.println(ways[half].multiply(ways[half]));
    }
}
