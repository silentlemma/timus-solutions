import java.util.Scanner;

public class Main {
    static final long SMALLEST = 3;

    public static void main(String[] args) {
        long k = new Scanner(System.in).nextLong();
        // the second player wins exactly when L + 1 divides K: find the smallest
        // divisor of K that is at least 3
        for (long d = SMALLEST; d * d <= k; d++) {
            if (k % d == 0) {
                System.out.println(d - 1);
                return;
            }
        }
        // no such divisor up to sqrt(K): above it the candidates are K / 2 and K
        long d = k % 2 == 0 && k / 2 >= SMALLEST ? k / 2 : k;
        System.out.println(d - 1);
    }
}
