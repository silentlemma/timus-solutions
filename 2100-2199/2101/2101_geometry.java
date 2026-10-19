import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigInteger;

public class Main {
    private static final int VERTEX_COUNT = 3;
    private static final int DECIMAL_PLACES = 10;
    private static final long SCALE = 10000000000L;

    private static final class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        long nextLong() throws IOException {
            int symbol;
            do {
                symbol = input.read();
            } while (symbol <= ' ' && symbol != -1);
            boolean negative = symbol == '-';
            if (negative) {
                symbol = input.read();
            }
            long value = 0;
            while (symbol > ' ') {
                value = value * 10 + symbol - '0';
                symbol = input.read();
            }
            return negative ? -value : value;
        }
    }

    private static final class Point {
        final long x;
        final long y;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    private static Point subtract(Point a, Point b) {
        return new Point(a.x - b.x, a.y - b.y);
    }

    private static long dot(Point a, Point b) {
        return a.x * b.x + a.y * b.y;
    }

    private static long cross(Point a, Point b) {
        return a.x * b.y - a.y * b.x;
    }

    private static BigInteger product(long... factors) {
        BigInteger result = BigInteger.ONE;
        for (long factor : factors) {
            result = result.multiply(BigInteger.valueOf(factor));
        }
        return result;
    }

    private static long roundedArea(BigInteger numerator, BigInteger denominator) {
        BigInteger half = denominator.divide(BigInteger.valueOf(2));
        return numerator.multiply(BigInteger.valueOf(SCALE)).add(half)
                .divide(denominator).longValueExact();
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        Point[] points = new Point[VERTEX_COUNT + 1];
        for (int i = 0; i < points.length; i++) {
            points[i] = new Point(input.nextLong(), input.nextLong());
        }
        long best = 0;
        int count = 0;
        for (int i = 0; i < VERTEX_COUNT; i++) {
            Point a = points[i];
            Point d = subtract(points[(i + 1) % VERTEX_COUNT], a);
            Point v = subtract(points[(i + 2) % VERTEX_COUNT], a);
            Point w = subtract(points[VERTEX_COUNT], a);
            long s = dot(d, d);
            long p = dot(d, v);
            long x = dot(d, w);
            long height = Math.abs(cross(d, v));
            long q = Math.abs(cross(d, w));
            // A right triangle's two legs describe the same rectangles.
            if (p < 0 || p >= s) {
                continue;
            }
            long area = roundedArea(product(q, height - q), BigInteger.valueOf(height));
            best = Math.max(best, area);
            count++;
            if (x < p) {
                area = roundedArea(product(height, x, p - x), product(p, p));
            } else if (x > p) {
                area = roundedArea(product(height, s - x, x - p), product(s - p, s - p));
            } else {
                continue;
            }
            best = Math.max(best, area);
            count++;
        }
        String fraction = Long.toString(best % SCALE);
        StringBuilder output = new StringBuilder();
        output.append(best / SCALE).append('.');
        for (int i = fraction.length(); i < DECIMAL_PLACES; i++) {
            output.append('0');
        }
        output.append(fraction).append('\n').append(count).append('\n');
        System.out.print(output);
    }
}
