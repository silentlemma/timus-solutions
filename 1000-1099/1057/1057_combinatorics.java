import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int POSITIONS = 32;
    static long[][] binom = new long[POSITIONS + 1][POSITIONS + 1];

    // how many numbers in [0, n] are sums of exactly k different powers of b,
    // that is, have only digits 0 and 1 in base b with k ones
    static long countUpto(long n, int k, int b) {
        List<Integer> digits = new ArrayList<>();
        for (; n > 0; n /= b) {
            digits.add((int)(n % b));
        }
        // a digit above 1 lets every smaller number with 0/1 digits through: it
        // and all digits after it may as well be 1
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits.get(i) > 1) {
                for (int j = i; j >= 0; j--) {
                    digits.set(j, 1);
                }
                break;
            }
        }
        // count 0/1 strings with k ones not above the digits, from the top
        long total = 0;
        int ones = 0;
        for (int i = digits.size() - 1; i >= 0 && ones <= k; i--) {
            if (digits.get(i) == 1) {
                if (k - ones <= i) {
                    total += binom[i][k - ones];
                }
                ones++;
            }
        }
        return total + (ones == k ? 1 : 0);
    }

    public static void main(String[] args) {
        for (int i = 0; i <= POSITIONS; i++) {
            binom[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                binom[i][j] = binom[i - 1][j - 1] + (j < i ? binom[i - 1][j] : 0);
            }
        }
        Scanner in = new Scanner(System.in);
        long x = in.nextLong(), y = in.nextLong();
        int k = in.nextInt(), b = in.nextInt();
        System.out.println(countUpto(y, k, b) - countUpto(x - 1, k, b));
    }
}
