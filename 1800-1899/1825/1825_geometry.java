import java.util.Scanner;

public class Main {
    // area common to discs of radii a and b with centres d apart
    static double lens(long d, long a, long b) {
        if (d >= a + b) {
            return 0.0;
        }
        if (d <= Math.abs(a - b)) {
            long small = Math.min(a, b);
            return Math.PI * small * small;
        }
        // half-angles seen from each centre, by the law of cosines
        double alpha = Math.acos((double) (d * d + a * a - b * b) / (2.0 * d * a));
        double beta = Math.acos((double) (d * d + b * b - a * a) / (2.0 * d * b));
        // the kite between both centres and the two crossing points
        double kite =
                Math.sqrt((double) (-d + a + b) * (d + a - b) * (d - a + b) * (d + a + b)) / 2;
        return (double) a * a * alpha + (double) b * b * beta - kite;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long d = in.nextLong(), r1 = in.nextLong(), big1 = in.nextLong();
        long r2 = in.nextLong(), big2 = in.nextLong();
        double ring1 = Math.PI * (big1 * big1 - r1 * r1);
        double ring2 = Math.PI * (big2 * big2 - r2 * r2);
        // a ring is a disc minus a smaller one, so their overlap follows by
        // inclusion and exclusion over the four pairs of discs
        double common =
                lens(d, big1, big2) - lens(d, r1, big2) - lens(d, big1, r2) + lens(d, r1, r2);
        System.out.printf("%.6f%n", ring1 + ring2 - common);
    }
}
