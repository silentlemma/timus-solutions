import java.util.Scanner;

public class Main {
    static final int DIGITS = 9; // numbers below 10^9 have at most nine digits
    static final int BASE = 10;

    public static void main(String[] args) {
        int target = new Scanner(System.in).nextInt();
        // ways[s]: digit strings of the current length with digit sum s
        long[] ways = {1};
        for (int len = 0; len < DIGITS; len++) {
            long[] next = new long[ways.length + BASE - 1];
            for (int s = 0; s < ways.length; s++)
                for (int d = 0; d < BASE; d++)
                    next[s + d] += ways[s];
            ways = next;
        }
        // 10^9 itself has digit sum 1; zero is not counted since S >= 1
        System.out.println(ways[target] + (target == 1 ? 1 : 0));
    }
}
