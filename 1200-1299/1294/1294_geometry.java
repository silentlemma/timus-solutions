import java.util.*;

public class Main {
    static final long KM = 1000; // input distances are in thousands of kilometres

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
        // inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
        long a = in.nextLong(), b = in.nextLong(), c = in.nextLong(), d = in.nextLong();
        long den = a * b - c * d;
        long diff = a * a + b * b - c * c - d * d;
        if (den == 0 || Math.abs(diff) >= 2 * Math.abs(den) || b * c <= a * d) {
            System.out.println("Impossible.");
            return;
        }
        long num = a * b * (c * c + d * d) - c * d * (a * a + b * b);
        if (den < 0) {
            num = -num;
            den = -den;
        }
        long km = (long)(KM * Math.sqrt((double)num / den));
        // Compare the half-kilometre boundary exactly, dividing before scaling.
        long scale = 4 * KM * KM;
        long bound = scale * (num / den) + scale * (num % den) / den;
        if ((2 * km + 1) * (2 * km + 1) <= bound)
            ++km;
        System.out.println("Distance is " + km + " km.");
    }
}
