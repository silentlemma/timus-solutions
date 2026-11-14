import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.Locale;

public class Main {
    private static final int DIMENSIONS = 3;
    private static final int COMPONENTS = 2 * DIMENSIONS;
    private static final double ROUNDING_MARGIN = 64.0 * Math.ulp(1.0);

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        String next() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c >= 0 && c <= ' ');
            StringBuilder token = new StringBuilder();
            while (c > ' ') {
                token.append((char)c);
                c = stream.read();
            }
            return token.toString();
        }
    }

    private static double exactEntry(BigDecimal[] left, BigDecimal[] right, BigDecimal threshold) {
        BigDecimal speed = BigDecimal.ZERO;
        BigDecimal projection = BigDecimal.ZERO;
        BigDecimal gap = threshold.negate();
        for (int axis = 0; axis < DIMENSIONS; axis++) {
            BigDecimal p = right[axis].subtract(left[axis]);
            BigDecimal v = right[axis + DIMENSIONS].subtract(left[axis + DIMENSIONS]);
            speed = speed.add(v.multiply(v));
            projection = projection.add(p.multiply(v));
            gap = gap.add(p.multiply(p));
        }
        if (projection.signum() >= 0) {
            return Double.POSITIVE_INFINITY;
        }
        BigDecimal discriminant = projection.multiply(projection).subtract(speed.multiply(gap));
        if (discriminant.signum() < 0) {
            return Double.POSITIVE_INFINITY;
        }
        return gap.doubleValue() /
            (Math.sqrt(discriminant.doubleValue()) - projection.doubleValue());
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        String count = input.next();
        if (count.isEmpty()) {
            return;
        }
        int n = Integer.parseInt(count);
        BigDecimal distance = new BigDecimal(input.next());
        BigDecimal exactThreshold = distance.multiply(distance);
        double threshold = exactThreshold.doubleValue();
        double[][] objects = new double[n][COMPONENTS];
        BigDecimal[][] exactObjects = new BigDecimal[n][COMPONENTS];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < COMPONENTS; k++) {
                exactObjects[i][k] = new BigDecimal(input.next());
                objects[i][k] = exactObjects[i][k].doubleValue();
            }
        }

        double best = Double.POSITIVE_INFINITY;
        int first = 0;
        int second = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                double[] p = objects[i];
                double[] q = objects[j];
                double speed = 0;
                double projection = 0;
                double gap = -threshold;
                double positionScale = 0;
                double velocityScale = 0;
                for (int axis = 0; axis < DIMENSIONS; axis++) {
                    double x = q[axis] - p[axis];
                    double v = q[axis + DIMENSIONS] - p[axis + DIMENSIONS];
                    speed += v * v;
                    projection += x * v;
                    gap += x * x;
                    positionScale += Math.abs(p[axis]) + Math.abs(q[axis]);
                    velocityScale +=
                        Math.abs(p[axis + DIMENSIONS]) + Math.abs(q[axis + DIMENSIONS]);
                }

                double xError = ROUNDING_MARGIN * positionScale;
                double vError = ROUNDING_MARGIN * velocityScale;
                if (speed == 0 && sameVelocity(exactObjects[i], exactObjects[j])) {
                    continue;
                }
                double xLength = Math.sqrt(Math.max(0, gap + threshold));
                double vLength = Math.sqrt(speed);
                double dotError = xError * (vLength + vError) + vError * xLength;
                if (projection > dotError || (speed == 0 && velocityScale == 0)) {
                    continue;
                }
                double gapError = xError * (2 * xLength + xError) + ROUNDING_MARGIN * threshold;
                double speedError = vError * (2 * vLength + vError);
                double discriminant = projection * projection - speed * gap;
                double discError = dotError * (2 * Math.abs(projection) + dotError) +
                                   speedError * Math.abs(gap) + (speed + speedError) * gapError;
                double time;
                if (Math.abs(discriminant) <= discError || gap <= gapError ||
                    projection >= -dotError) {
                    time = exactEntry(exactObjects[i], exactObjects[j], exactThreshold);
                } else if (discriminant < 0) {
                    continue;
                } else {
                    time = gap / (Math.sqrt(discriminant) - projection);
                }
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

    private static boolean sameVelocity(BigDecimal[] left, BigDecimal[] right) {
        for (int axis = DIMENSIONS; axis < COMPONENTS; axis++) {
            if (left[axis].compareTo(right[axis]) != 0) {
                return false;
            }
        }
        return true;
    }
}
