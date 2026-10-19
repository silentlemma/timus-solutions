import java.util.Scanner;
import java.util.Locale;

public class Main {
    static final double FOCAL_SCALE = 3;
    static final double AXIS_SCALE = 6;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long a = input.nextLong(), b = input.nextLong(), c = input.nextLong();
        long x = a * a, y = b * b, z = c * c;
        long discriminant = 2 * ((x - y) * (x - y) + (y - z) * (y - z)
                + (z - x) * (z - x));
        double gap = Math.sqrt(discriminant);
        double focalDistance = Math.sqrt(2 * gap) / FOCAL_SCALE;
        double radius = Math.sqrt(x + y + z + gap) / AXIS_SCALE;
        System.out.printf(Locale.US, "%.12f %.12f%n", focalDistance, radius);
    }
}
