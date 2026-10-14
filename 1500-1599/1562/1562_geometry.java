import java.util.*;

public class Main {
    static final double QUARTER = 0.25, THIRD = 1.0 / 3;
    static double a, half;

    // the volume of the pineapple between its middle and height z: the cross-section
    // at z is a disc of area pi (a / 2)^2 (1 - (z / half)^2)
    static double below(double z) {
        return Math.PI * a * a * QUARTER * (z - z * z * z * THIRD / (half * half));
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        a = in.nextDouble();
        double b = in.nextDouble();
        int n = in.nextInt();
        half = b / 2;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            double piece = below(-half + b * (i + 1) / n) - below(-half + b * i / n);
            out.append(String.format(Locale.US, "%.6f", piece)).append('\n');
        }
        System.out.print(out);
    }
}
