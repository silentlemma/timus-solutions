import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int SIDES = 4;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double a = in.nextInt(), r = in.nextInt();
        double half = a / 2, area;
        if (r <= half) {
            area = Math.PI * r * r;
        } else if (r * r >= 2 * half * half) {
            area = a * a;
        } else {
            // the circle minus the four caps cut off by the sides
            double cap = r * r * Math.acos(half / r) - half * Math.sqrt(r * r - half * half);
            area = Math.PI * r * r - SIDES * cap;
        }
        System.out.println(String.format(Locale.US, "%.3f", area));
    }
}
