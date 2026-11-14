import java.io.BufferedInputStream;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    private static final int DIMENSIONS = 3;
    private static final int COMPONENTS = 2 * DIMENSIONS;

    private static double ratio(BigInteger numerator, BigInteger denominator) {
        double a = numerator.doubleValue();
        double b = denominator.doubleValue();
        if (Double.isFinite(a) && Double.isFinite(b)) {
            return a / b;
        }
        return new BigDecimal(numerator)
            .divide(new BigDecimal(denominator), MathContext.DECIMAL128)
            .doubleValue();
    }

    private static double entry(BigInteger[] first, BigInteger[] second,
                                BigInteger distanceSquared) {
        BigInteger speedSquared = BigInteger.ZERO;
        BigInteger projection = BigInteger.ZERO;
        BigInteger gap = distanceSquared.negate();
        for (int axis = 0; axis < DIMENSIONS; axis++) {
            BigInteger position = second[axis].subtract(first[axis]);
            BigInteger velocity = second[axis + DIMENSIONS].subtract(first[axis + DIMENSIONS]);
            projection = projection.add(position.multiply(velocity));
            speedSquared = speedSquared.add(velocity.multiply(velocity));
            gap = gap.add(position.multiply(position));
        }
        if (projection.signum() >= 0) {
            return Double.POSITIVE_INFINITY;
        }

        BigInteger projectionSquared = projection.multiply(projection);
        BigInteger discriminant = projectionSquared.subtract(speedSquared.multiply(gap));
        if (discriminant.signum() < 0) {
            return Double.POSITIVE_INFINITY;
        }
        // Take the square root only after the exact comparison and normalization.
        double root = Math.sqrt(ratio(discriminant, projectionSquared));
        return ratio(gap, projection.negate()) / (1 + root);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(new BufferedInputStream(System.in));
        int count = input.nextInt();
        BigDecimal distance = new BigDecimal(input.next());
        BigDecimal[][] decimal = new BigDecimal[count][COMPONENTS];
        int scale = distance.scale();
        for (BigDecimal[] object : decimal) {
            for (int axis = 0; axis < COMPONENTS; axis++) {
                object[axis] = new BigDecimal(input.next()).stripTrailingZeros();
                scale = Math.max(scale, object[axis].scale());
            }
        }

        BigInteger[][] objects = new BigInteger[count][COMPONENTS];
        for (int i = 0; i < count; i++) {
            for (int axis = 0; axis < COMPONENTS; axis++) {
                objects[i][axis] = decimal[i][axis].setScale(scale).unscaledValue();
            }
        }
        BigInteger limit = distance.setScale(scale).unscaledValue();
        BigInteger distanceSquared = limit.multiply(limit);
        double best = Double.POSITIVE_INFINITY;
        int first = 0, second = 0;
        for (int i = 0; i < count; i++) {
            for (int j = i + 1; j < count; j++) {
                double time = entry(objects[i], objects[j], distanceSquared);
                if (time < best) {
                    best = time;
                    first = i + 1;
                    second = j + 1;
                }
            }
        }
        if (first == 0) {
            System.out.println("OK");
        } else {
            System.out.printf(Locale.US, "ALARM!%n%.3f %d %d%n", best, first, second);
        }
    }
}
