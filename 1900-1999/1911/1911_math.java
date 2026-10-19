import java.math.BigInteger;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    private static final class Parameters {
        final long speed;
        final long length;
        final long fireSpeed;
        final long fireWidth;
        final long gap;
        final long natural;
        final long shield;
        final long braking;

        Parameters(Scanner in) {
            speed = in.nextLong();
            length = in.nextLong();
            fireSpeed = in.nextLong();
            fireWidth = in.nextLong();
            gap = in.nextLong();
            natural = in.nextLong();
            shield = in.nextLong();
            braking = in.nextLong();
        }
    }

    private static double minimumEnergy(Parameters p, long[][] branches) {
        long difference = p.fireSpeed - p.speed;
        double best = Double.POSITIVE_INFINITY;
        for (long[] branch : branches) {
            long entry = branch[0] + p.length;
            long distance = branch[1] - entry;
            long held = entry * difference - p.gap * p.speed;
            long shieldNumerator = Math.max(0, held) * p.shield;
            long shieldDenominator = p.speed * difference;
            long delayNumerator = p.speed * (branch[1] - branch[0] + p.fireWidth)
                    + Math.max(0, -held);
            BigInteger brakeNumerator;
            BigInteger brakeDenominator;
            if (delayNumerator >= 2 * distance * p.fireSpeed) {
                brakeNumerator = BigInteger.valueOf(p.speed * p.speed);
                brakeDenominator = BigInteger.valueOf(2 * distance);
            } else if (delayNumerator <= distance * p.fireSpeed) {
                brakeNumerator = BigInteger.ZERO;
                brakeDenominator = BigInteger.ONE;
            } else {
                brakeNumerator = BigInteger.valueOf(2 * p.speed * p.speed * p.fireSpeed)
                        .multiply(BigInteger.valueOf(delayNumerator - distance * p.fireSpeed));
                brakeDenominator = BigInteger.valueOf(delayNumerator)
                        .multiply(BigInteger.valueOf(delayNumerator));
            }
            BigInteger extra = brakeNumerator.subtract(
                    BigInteger.valueOf(p.natural).multiply(brakeDenominator)).max(BigInteger.ZERO);
            double additional = BigInteger.valueOf(p.braking).multiply(extra).doubleValue()
                    / brakeDenominator.doubleValue();
            double cost = (double) shieldNumerator / shieldDenominator + additional;
            best = Math.min(best, cost);
        }
        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Parameters parameters = new Parameters(in);
        int count = in.nextInt();
        long[][] branches = new long[count][2];
        for (int index = 0; index < count; index++) {
            branches[index][0] = in.nextLong();
            branches[index][1] = in.nextLong();
        }
        System.out.printf(Locale.US, "%.12f%n", minimumEnergy(parameters, branches));
    }
}
