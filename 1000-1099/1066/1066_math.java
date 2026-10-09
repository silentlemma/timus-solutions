import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        int n = in.nextInt();
        double a = in.nextDouble();
        // with the second height x, lamp i hangs at a + (i-1)(x - a) + (i-1)(i-2)
        // and the last height grows with x, so x is the smallest value keeping every
        // lamp at height 0 or above
        double x = 0;
        for (int k = 1; k < n; k++) {
            x = Math.max(x, a - a / k - (k - 1));
        }
        double b = a + (n - 1) * (x - a) + (double)(n - 1) * (n - 2);
        System.out.println(String.format(Locale.US, "%.2f", b));
    }
}
