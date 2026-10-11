import java.util.*;

public class Main {
    static final double KM = 1000; // input distances are in thousands of kilometres

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
        // inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
        long a = in.nextLong(), b = in.nextLong(), c = in.nextLong(), d = in.nextLong();
        long den = a * b - c * d;
        long diff = a * a + b * b - c * c - d * d;
        if (den == 0 || Math.abs(diff) > 2 * Math.abs(den)) {
            System.out.println("Impossible.");
            return;
        }
        long num = a * b * (c * c + d * d) - c * d * (a * a + b * b);
        System.out.println("Distance is " + Math.round(KM * Math.sqrt((double)num / den)) + " km.");
    }
}
