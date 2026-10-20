import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;
import java.util.Arrays;

public class Main {
    private static final int INPUT_BUFFER = 65536;
    private static final int PROBABILITY_SCALE = 100000;
    private static final int PROBABILITY_DIGITS = 5;
    private static final int OUTPUT_DIGITS = 10;
    private static final double HALF_TURN = 180.0;
    private static final double FULL_TURN = 2 * Math.PI;
    private static final double ANGLE_EPSILON = 1e-12;
    private static final double PROBABILITY_EPSILON = 1e-7;

    private static final class Gun implements Comparable<Gun> {
        final long x;
        final long y;
        final long norm;
        final double angle;

        Gun(int x, int y) {
            this.x = x;
            this.y = y;
            norm = this.x * x + this.y * y;
            angle = Math.atan2(y, x);
        }

        @Override
        public int compareTo(Gun other) {
            int order = Double.compare(angle, other.angle);
            if (order != 0) {
                return order;
            }
            long cross = x * other.y - y * other.x;
            return Long.compare(0, cross);
        }
    }

    private static final class FastInput {
        private final BufferedInputStream stream = new BufferedInputStream(System.in, INPUT_BUFFER);

        String next() throws IOException {
            StringBuilder token = new StringBuilder();
            int value;
            do {
                value = stream.read();
            } while (value >= 0 && value <= ' ');
            while (value > ' ') {
                token.append((char) value);
                value = stream.read();
            }
            return token.toString();
        }

        int nextInt() throws IOException {
            int value;
            do {
                value = stream.read();
            } while (value >= 0 && value <= ' ');
            int sign = 1;
            if (value == '-') {
                sign = -1;
                value = stream.read();
            }
            int result = 0;
            while (value > ' ') {
                result = result * 10 + value - '0';
                value = stream.read();
            }
            return result * sign;
        }
    }

    private static double normalize(double angle) {
        angle %= FULL_TURN;
        return angle < 0 ? angle + FULL_TURN : angle;
    }

    private static boolean fits(Gun first, Gun last, double delta, double width,
                                long distance, long cosineNumerator) {
        if (Math.abs(delta - width) > ANGLE_EPSILON) {
            return delta < width;
        }
        long cross = first.x * last.y - first.y * last.x;
        long dot = first.x * last.x + first.y * last.y;
        if (cross < 0) {
            return false;
        }
        if (cross == 0) {
            return dot > 0;
        }
        if (dot >= 0 && cosineNumerator < 0) {
            return true;
        }
        if (dot < 0 && cosineNumerator >= 0) {
            return false;
        }
        // Compare boundary cosines exactly when angles are almost equal.
        BigInteger left = BigInteger.valueOf(dot).pow(2);
        left = left.multiply(BigInteger.valueOf(distance).pow(2));
        BigInteger right = BigInteger.valueOf(cosineNumerator).pow(2);
        right = right.multiply(BigInteger.valueOf(first.norm));
        right = right.multiply(BigInteger.valueOf(last.norm));
        int order = left.compareTo(right);
        return cosineNumerator >= 0 ? order >= 0 : order <= 0;
    }

    private static int probability(String token) {
        int value = 0;
        int digits = 0;
        boolean fraction = false;
        for (int index = 0; index < token.length(); ++index) {
            char character = token.charAt(index);
            if (character == '.') {
                fraction = true;
            } else {
                value = value * 10 + character - '0';
                if (fraction) {
                    ++digits;
                }
            }
        }
        while (digits < PROBABILITY_DIGITS) {
            value *= 10;
            ++digits;
        }
        return value;
    }

    private static int capacity(int hits, int n, int shots, BigInteger totalPower) {
        if (shots == 1) {
            return (int) ((long) PROBABILITY_SCALE * hits / n);
        }
        double miss = (double) (n - hits) / n;
        double scaled = PROBABILITY_SCALE * (1 - Math.pow(miss, shots));
        int result = (int) Math.floor(scaled);
        if (Math.abs(scaled - Math.rint(scaled)) < PROBABILITY_EPSILON) {
            // Decimal query boundaries require an exact integer comparison.
            BigInteger left = BigInteger.valueOf(n - hits).pow(shots);
            left = left.multiply(BigInteger.valueOf(PROBABILITY_SCALE));
            while (result > 0 && left.compareTo(totalPower.multiply(
                    BigInteger.valueOf(PROBABILITY_SCALE - result))) > 0) {
                --result;
            }
            while (result < PROBABILITY_SCALE && left.compareTo(totalPower.multiply(
                    BigInteger.valueOf(PROBABILITY_SCALE - result - 1))) <= 0) {
                ++result;
            }
        }
        return result;
    }

    private static String format(double angle) {
        double degrees = angle * HALF_TURN / Math.PI;
        return new BigDecimal(degrees).setScale(OUTPUT_DIGITS, RoundingMode.HALF_EVEN)
                .toPlainString();
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int shots = input.nextInt();
        int queries = input.nextInt();
        Gun[] guns = new Gun[n];
        for (int index = 0; index < n; ++index) {
            int x = input.nextInt();
            int y = input.nextInt();
            guns[index] = new Gun(x, y);
        }
        int a = input.nextInt();
        int b = input.nextInt();
        int radius = input.nextInt();
        long distance = (long) a * a + (long) b * b;
        long radiusSquared = (long) radius * radius;
        long cosineNumerator = distance - 2 * radiusSquared;
        double center = Math.atan2(b, a);
        double halfWidth = Math.atan2(radius, Math.sqrt(distance - radiusSquared));
        double width = 2 * halfWidth;
        int active = 0;
        BigInteger radiusPower = BigInteger.valueOf(radiusSquared);
        for (Gun gun : guns) {
            long dot = (long) a * gun.x + (long) b * gun.y;
            if (dot < 0) {
                continue;
            }
            long cross = (long) a * gun.y - (long) b * gun.x;
            BigInteger left = BigInteger.valueOf(cross).pow(2);
            BigInteger right = radiusPower.multiply(BigInteger.valueOf(gun.norm));
            if (left.compareTo(right) <= 0) {
                ++active;
            }
        }
        Arrays.sort(guns);
        double[] earliest = new double[n + 1];
        Arrays.fill(earliest, Double.POSITIVE_INFINITY);
        earliest[0] = 0;
        earliest[active] = 0;
        int end = 0;
        for (int begin = 0; begin < n; ++begin) {
            while (end < begin + n) {
                Gun last = guns[end % n];
                double delta = last.angle - guns[begin].angle;
                if (end >= n) {
                    delta += FULL_TURN;
                }
                if (!fits(guns[begin], last, delta, width, distance, cosineNumerator)) {
                    break;
                }
                ++end;
            }
            int count = end - begin;
            double angle = normalize(center - halfWidth - guns[begin].angle);
            // Resolve which side of zero contains an almost tangent entry.
            if (angle <= ANGLE_EPSILON || FULL_TURN - angle <= ANGLE_EPSILON) {
                long cross = (long) a * guns[begin].y - (long) b * guns[begin].x;
                BigInteger left = BigInteger.valueOf(cross).pow(2);
                BigInteger right = radiusPower.multiply(BigInteger.valueOf(guns[begin].norm));
                angle = left.compareTo(right) < 0 ? FULL_TURN - ANGLE_EPSILON : 0;
            }
            earliest[count] = Math.min(earliest[count], angle);
        }
        for (int count = n; count > 0; --count) {
            earliest[count - 1] = Math.min(earliest[count - 1], earliest[count]);
        }
        BigInteger totalPower = BigInteger.valueOf(n).pow(shots);
        String[] answers = new String[PROBABILITY_SCALE + 1];
        int assigned = 0;
        for (int count = 0; count <= n && Double.isFinite(earliest[count]); ++count) {
            int limit = capacity(count, n, shots, totalPower);
            if (assigned <= limit) {
                String answer = format(earliest[count]);
                while (assigned <= limit) {
                    answers[assigned++] = answer;
                }
            }
        }
        StringBuilder output = new StringBuilder();
        for (int query = 0; query < queries; ++query) {
            String answer = answers[probability(input.next())];
            output.append(answer == null ? "-1" : answer).append('\n');
        }
        System.out.print(output);
    }
}
