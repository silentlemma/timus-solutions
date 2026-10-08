import java.util.Scanner;

public class Main {
    static final int BASE = 10;

    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        // a zero digit makes the product zero: 10 is the smallest such number
        if (n == 0) {
            System.out.println(BASE);
            return;
        }
        if (n == 1) {
            System.out.println(1);
            return;
        }
        // the largest digits first give the fewest digits; then sort them up
        StringBuilder digits = new StringBuilder();
        for (int d = BASE - 1; d >= 2; d--) {
            while (n % d == 0) {
                digits.insert(0, d);
                n /= d;
            }
        }
        System.out.println(n == 1 ? digits.toString() : "-1");
    }
}
