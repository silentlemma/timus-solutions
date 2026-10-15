import java.util.Scanner;

public class Main {
    static final int BASE = 10;
    static final int FIVE = 5; // the last digit of one endless solution of x^2 = x

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // x^2 ends with x exactly when x^2 = x mod 10^d for its d digits; besides
        // 0 and 1 the solutions are the endings of two 10-adic numbers, ...0625
        // and ...9376, whose digits other than the last add up to 9 place by place

        int[] digits = new int[n];
        digits[0] = FIVE; // the 5-adic one, lowest digit first

        long carry = FIVE * FIVE / BASE; // carry into position d of the square so far
        for (int d = 1; d < n; d++) {
            // digit d of x^2: the products x_i x_j with i + j = d, plus the carry, and
            // a new digit c adds 2 * 5 * c, a multiple of 10: c is forced
            long total = carry;
            for (int i = 1; i < d; i++) {
                total += digits[i] * digits[d - i];
            }
            int c = (int) (total % BASE);
            digits[d] = c;
            carry = (total + 2 * FIVE * c) / BASE;
        }
        int count = 1 + 2; // the numbers 1, 5 and 6

        for (int d = 1; d < n; d++) {
            // a d + 1 digit number needs a nonzero leading digit
            count += (digits[d] != 0 ? 1 : 0) + (digits[d] != BASE - 1 ? 1 : 0);
        }
        System.out.println(count);
    }
}
