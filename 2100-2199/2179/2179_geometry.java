import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int TRIANGLE_SIDES = 3;
    private static final int BUFFER_SIZE = 65536;
    private static final int BYTE_MASK = 255;
    private static final int END_OF_FILE = -1;

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length == END_OF_FILE) {
                    return END_OF_FILE;
                }
            }
            return buffer[position++] & BYTE_MASK;
        }

        private long nextLong() throws IOException {
            int c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean negative = c == '-';
            if (negative) {
                c = read();
            }
            long value = 0;
            while (c > ' ') {
                value = value * 10 + c - '0';
                c = read();
            }
            return negative ? -value : value;
        }
    }

    private static final class Point implements Comparable<Point> {
        private final long x;
        private final long y;

        private Point(long x, long y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Point other) {
            return x == other.x ? Long.compare(y, other.y) : Long.compare(x, other.x);
        }
    }

    private static long cross(Point a, Point b, Point c) {
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    }

    private static int chainSize(Point[] points, boolean reverse) {
        Point[] hull = new Point[points.length];
        int size = 0;
        for (int i = 0; i < points.length; i++) {
            Point point = points[reverse ? points.length - 1 - i : i];
            while (size > 1 && cross(hull[size - 2], hull[size - 1], point) < 0) {
                size--;
            }
            hull[size++] = point;
        }
        return size;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = (int) input.nextLong();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            points[i] = new Point(input.nextLong(), input.nextLong());
        }
        Arrays.sort(points);
        int boundary = chainSize(points, false) + chainSize(points, true) - 2;
        // For collinear points the doubled boundary count gives n - 1 roads.
        System.out.println(TRIANGLE_SIDES * n - TRIANGLE_SIDES - boundary);
    }
}
