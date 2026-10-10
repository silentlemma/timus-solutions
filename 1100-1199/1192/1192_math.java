import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double GRAVITY = 10.0, PI = 3.1415926535, HALF_TURN = 180.0;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double v = in.nextDouble(), a = in.nextDouble(), k = in.nextDouble();
        // one flight covers v^2 sin(2a) / g; every bounce keeps the angle and
        // divides v^2 by k, so the flights form a geometric series with
        // ratio 1/k
        double flight = v * v * Math.sin(2 * a * PI / HALF_TURN) / GRAVITY;
        System.out.println(String.format(Locale.US, "%.2f", flight * k / (k - 1)));
    }
}
