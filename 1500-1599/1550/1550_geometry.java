import java.util.*;

public class Main {
    static final double THIRD = 1.0 / 3; // a pyramid is a third of its prism

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double h = in.nextDouble(), w = in.nextDouble(), x = in.nextDouble(), y = in.nextDouble();
        double r = in.nextDouble();
        // the hole meets no edge, so it lies over a single face, where the height
        // is linear: the cut-out volume is the hole's area times the height at
        // its centre, and that height falls from H to 0 with max(|x|, |y|)
        double centre = h * (1 - Math.max(Math.abs(x), Math.abs(y)) / (w / 2));
        System.out.println(
            String.format(Locale.US, "%.5f", h * w * w * THIRD - Math.PI * r * r * centre));
    }
}
