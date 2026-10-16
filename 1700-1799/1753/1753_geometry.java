import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double rim = in.nextInt(), book = in.nextInt();
        // with the foot at distance x from the rim and r = hypot(x, rim), the book
        // leans on the rim top and its middle lies x * (book / 2r - 1) to the left,
        // which is largest where r cubed is book * rim * rim / 2
        double r = Math.cbrt(book * rim * rim / 2);
        double shift = 0;
        if (r > rim) {
            double x = Math.sqrt(r * r - rim * rim);
            shift = x * (book / (2 * r) - 1);
        }
        System.out.printf(java.util.Locale.US, "%.6f%n", shift);
    }
}
