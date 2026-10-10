import java.util.Scanner;

public class Main {
    // answers above this are reported as 0
    static final int LIMIT = 10000;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt(), n = in.nextInt(), k = in.nextInt();
        // x tiles make one rectangle per divisor pair a * b = x with a <= b,
        // that is half the number of divisors, rounded up
        int[] divisors = new int[LIMIT + 1];
        for (int d = 1; d <= LIMIT; d++) {
            for (int x = d; x <= LIMIT; x += d) {
                divisors[x]++;
            }
        }
        for (int t = k + 1; t <= LIMIT; t++) {
            if ((divisors[t] + 1) / 2 == n && (divisors[t - k] + 1) / 2 == m) {
                System.out.println(t);
                return;
            }
        }
        System.out.println(0);
    }
}
