import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;
    private static final int DECIMAL_PLACES = 6;
    private static final long DECIMAL_SCALE = 1000000;

    private static final class FastInput {
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = stream.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int value = read();
            while (value <= ' ' && value != -1) {
                value = read();
            }
            int sign = 1;
            if (value == '-') {
                sign = -1;
                value = read();
            }
            int number = 0;
            while (value >= '0' && value <= '9') {
                number = number * 10 + value - '0';
                value = read();
            }
            return number * sign;
        }
    }

    private static final class Line {
        final long dx;
        final long dy;
        final long c;

        Line(long x1, long y1, long x2, long y2) {
            long directionX = x2 - x1;
            long directionY = y2 - y1;
            if (directionX < 0 || (directionX == 0 && directionY < 0)) {
                directionX = -directionX;
                directionY = -directionY;
            }
            dx = directionX;
            dy = directionY;
            c = dy * x1 - dx * y1;
        }
    }

    private static String formatAnswer(long numerator, long denominator) {
        long rounded = (numerator * DECIMAL_SCALE + denominator / 2) / denominator;
        String integer = Long.toString(rounded / DECIMAL_SCALE);
        long fraction = rounded % DECIMAL_SCALE;
        if (fraction == 0) {
            return integer;
        }
        String digits = Long.toString(fraction);
        StringBuilder answer = new StringBuilder(integer).append('.');
        for (int i = digits.length(); i < DECIMAL_PLACES; ++i) {
            answer.append('0');
        }
        answer.append(digits);
        while (answer.charAt(answer.length() - 1) == '0') {
            answer.setLength(answer.length() - 1);
        }
        return answer.toString();
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt();
        Line[] lines = new Line[count];
        for (int i = 0; i < count; ++i) {
            lines[i] = new Line(input.nextInt(), input.nextInt(), input.nextInt(), input.nextInt());
        }
        Arrays.sort(lines,
                    (first, second) -> Long.compare(first.dy * second.dx, second.dy * first.dx));
        long bestNumerator = 0;
        long bestDenominator = 1;
        Line first = lines[count - 1];
        // Every directional extreme occurs between cyclic neighboring directions.
        for (Line second : lines) {
            long denominator = Math.abs(first.dx * second.dy - first.dy * second.dx);
            long numerator = Math.abs(first.dx * second.c - first.c * second.dx) +
                             Math.abs(first.dy * second.c - first.c * second.dy);
            if (numerator * bestDenominator > bestNumerator * denominator) {
                bestNumerator = numerator;
                bestDenominator = denominator;
            }
            first = second;
        }
        System.out.println(formatAnswer(bestNumerator, bestDenominator));
    }
}
