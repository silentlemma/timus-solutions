import java.util.*;

public class Main {
    static final double AREA = 100; // the cross-section of the bar, 10 by 10 cm
    static final double LENGTH = 100;
    static final double PIECE = 500;   // grams, at one gram per cubic centimetre
    static final long MICRONS = 10000; // in a centimetre
    static final int STEPS = 100;
    static final double CAP = 3; // a cap of height h has volume pi h^2 (3 r - h) / 3
    static final double HALF = 0.5;

    static double[] centre, radius;

    // the weight of the bar from its start to the mark at (in cm): the full volume
    // minus the part of every hole below the mark, a spherical cap of height h
    // with volume pi h^2 (3 r - h) / 3
    static double cheese(double at) {
        double weight = AREA * at;
        for (int i = 0; i < centre.length; i++) {
            double r = radius[i], h = Math.min(Math.max(at - (centre[i] - r), 0), 2 * r);
            weight -= Math.PI * h * h * (CAP * r - h) / CAP;
        }
        return weight;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        int n = in.nextInt();
        centre = new double[n];
        radius = new double[n];
        for (int i = 0; i < n; i++) {
            in.nextDouble();
            centre[i] = in.nextDouble();
            in.nextDouble();
            radius[i] = in.nextDouble();
        }
        List<Long> cuts = new ArrayList<>();
        long start = 0;
        while (cheese(LENGTH) - cheese((double)start / MICRONS) >= PIECE) {
            // the mark where the next piece reaches 500 grams, then rounded to the
            // micrometre grid; the next piece starts at the cut actually made
            double base = cheese((double)start / MICRONS);
            double lo = (double)start / MICRONS, hi = LENGTH;
            for (int i = 0; i < STEPS; i++) {
                double mid = (lo + hi) / 2;
                if (cheese(mid) - base < PIECE)
                    lo = mid;
                else
                    hi = mid;
            }
            start = (long)Math.floor(hi * MICRONS + HALF);
            if (start >= (long)LENGTH * MICRONS)
                break;
            cuts.add(start);
        }
        StringBuilder out = new StringBuilder();
        out.append(cuts.size()).append('\n');
        for (long c : cuts)
            out.append(c).append('\n');
        System.out.print(out);
    }
}
