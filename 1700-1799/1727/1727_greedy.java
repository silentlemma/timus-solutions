import java.util.Scanner;

public class Main {
    static final int LIMIT = 100000;
    static final int BASE = 10;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int[] digits = new int[LIMIT];
        for (int i = 1; i < LIMIT; i++) {
            digits[i] = digits[i / BASE] + i % BASE;
        }
        // take numbers from the top whenever their digits still fit; the
        // small ones at the end fill any remainder, so the sum always comes out
        StringBuilder numbers = new StringBuilder();
        int count = 0;
        for (int i = LIMIT - 1; i >= 1 && n > 0; i--) {
            if (digits[i] <= n) {
                if (count++ > 0) {
                    numbers.append(' ');
                }
                numbers.append(i);
                n -= digits[i];
            }
        }
        System.out.println(count);
        System.out.println(numbers);
    }
}
