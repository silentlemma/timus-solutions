import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextLong(), b = in.nextLong(), n = in.nextLong();
        boolean swapped = a < b;
        if (swapped) {
            long t = a;
            a = b;
            b = t;
        }
        // b items of price a can always become a items of price b, so x below b is enough,
        // with a >= b either b or n / a is at most sqrt(n)
        long spent = -1, bx = 0, by = 0;
        for (long x = 0; x <= Math.min(n / a, b - 1) && spent != n; x++) {
            long y = (n - x * a) / b;
            if (x * a + y * b > spent) {
                spent = x * a + y * b;
                bx = x;
                by = y;
            }
        }
        System.out.println(swapped ? by + " " + bx : bx + " " + by);
    }
}
