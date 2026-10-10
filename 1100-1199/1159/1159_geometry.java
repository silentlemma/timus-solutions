import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    // halvings of the radius interval; far more than double precision needs
    static final int STEPS = 200;

    static int[] sides, rest;
    static int longest;
    static boolean inside;

    // the largest area belongs to the polygon inscribed in a circle; a side
    // of length l sees the centre at the angle 2 asin(l / 2R)
    static double angle(double length, double r) {
        return 2 * Math.asin(Math.min(1.0, length / (2 * r)));
    }

    static double sum(int[] v, double r) {
        double total = 0;
        for (int s : v) {
            total += angle(s, r);
        }
        return total;
    }

    // with the centre inside, the angles fill the full turn; otherwise the
    // longest side's angle equals the sum of the others
    static double surplus(double r) {
        return inside ? sum(sides, r) - 2 * Math.PI : angle(longest, r) - sum(rest, r);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        sides = new int[n];
        for (int i = 0; i < n; i++) {
            sides[i] = in.nextInt();
        }
        Arrays.sort(sides);
        longest = sides[n - 1];
        rest = Arrays.copyOf(sides, n - 1);
        if (longest >= Arrays.stream(rest).sum()) {
            System.out.println("0.00");
            return;
        }
        double low = longest / 2.0;
        inside = sum(sides, low) >= 2 * Math.PI;
        double high = low;
        while (surplus(high) > 0) {
            high *= 2;
        }
        for (int k = 0; k < STEPS; k++) {
            double mid = (low + high) / 2;
            if (surplus(mid) > 0) {
                low = mid;
            } else {
                high = mid;
            }
        }
        double r = (low + high) / 2, area = 0;
        for (int s : rest) {
            area += Math.sin(angle(s, r));
        }
        area += (inside ? 1 : -1) * Math.sin(angle(longest, r));
        // rounded from the exact binary value, half to even, as printf in C
        System.out.println(
            new BigDecimal(r * r * area / 2).setScale(2, RoundingMode.HALF_EVEN).toPlainString());
    }
}
