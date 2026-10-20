import java.io.IOException;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;
    private static final int SPACE = ' ';
    private static final int MINUS = '-';
    private static final int ZERO = '0';

    private static final class FastInput {
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        long nextInt() throws IOException {
            int c = read();
            while (c <= SPACE) {
                c = read();
            }
            int sign = 1;
            if (c == MINUS) {
                sign = -1;
                c = read();
            }
            long value = 0;
            while (c > SPACE) {
                value = value * 10 + c - ZERO;
                c = read();
            }
            return value * sign;
        }
    }

    private static final class Point implements Comparable<Point> {
        final long x;
        final long y;
        final long nx;
        final long ny;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
            boolean flip = y < 0 || y == 0 && x < 0;
            nx = flip ? -x : x;
            ny = flip ? -y : y;
        }

        @Override
        public int compareTo(Point other) {
            long cross = nx * other.ny - ny * other.nx;
            return Long.compare(0, cross);
        }
    }

    private static double distance(Point a, Point b) {
        long area = Math.abs(a.x * b.y - a.y * b.x);
        long dx = a.x - b.x;
        long dy = a.y - b.y;
        return area / Math.sqrt((double) (dx * dx + dy * dy));
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = (int) input.nextInt();
        Point[] points = new Point[n];
        boolean hasOrigin = false;
        for (int i = 0; i < n; i++) {
            long x = input.nextInt();
            long y = input.nextInt();
            points[i] = new Point(x, y);
            hasOrigin |= x == 0 && y == 0;
        }
        double answer = 0;
        if (!hasOrigin) {
            // Opposite rays have the same direction modulo a half turn.
            Arrays.sort(points);
            answer = Double.POSITIVE_INFINITY;
            for (int i = 0; i < n; i++) {
                answer = Math.min(answer, distance(points[i], points[(i + 1) % n]));
            }
        }
        System.out.printf(Locale.ROOT, "%.10f%n", answer);
    }
}
