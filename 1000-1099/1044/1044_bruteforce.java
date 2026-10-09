import java.util.Scanner;

public class Main {
    static final int DIGITS = 10;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int half = n / 2, limit = 1;
        for (int i = 0; i < half; i++) {
            limit *= DIGITS;
        }
        // ways[s]: how many halves (numbers below 10^half) have digit sum s
        long[] ways = new long[(DIGITS - 1) * half + 1];
        for (int x = 0; x < limit; x++) {
            int s = 0;
            for (int y = x; y > 0; y /= DIGITS) {
                s += y % DIGITS;
            }
            ways[s]++;
        }
        // the two halves are chosen independently with the same sum
        long total = 0;
        for (long w : ways) {
            total += w * w;
        }
        System.out.println(total);
    }
}
