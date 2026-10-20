import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int BUFFER_SIZE = 65536;

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length == -1) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        long nextLong() throws IOException {
            int current = read();
            while (current <= ' ') {
                current = read();
            }
            long sign = 1;
            if (current == '-') {
                sign = -1;
                current = read();
            }
            long value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value * sign;
        }
    }

    private static final class Point implements Comparable<Point> {
        final long first;
        final long second;

        Point(long first, long second) {
            this.first = first;
            this.second = second;
        }

        @Override
        public int compareTo(Point other) {
            int order = Long.compare(first, other.first);
            return order == 0 ? Long.compare(second, other.second) : order;
        }
    }

    private static int lowerBound(Point[] points, long first, long second) {
        int left = 0;
        int right = points.length;
        while (left < right) {
            int middle = left + (right - left) / 2;
            Point point = points[middle];
            if (point.first < first || (point.first == first && point.second < second)) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return left;
    }

    private static int count(Point[] points, long fixed, long low, long high) {
        return lowerBound(points, fixed, high + 1) - lowerBound(points, fixed, low);
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int size = (int) input.nextLong();
        Point[] byU = new Point[size];
        Point[] byV = new Point[size];
        for (int index = 0; index < size; index++) {
            long x = input.nextLong();
            long y = input.nextLong();
            byU[index] = new Point(x + y, x - y);
            byV[index] = new Point(x - y, x + y);
        }
        Arrays.sort(byU);
        Arrays.sort(byV);

        int queries = (int) input.nextLong();
        StringBuilder output = new StringBuilder();
        for (int index = 0; index < queries; index++) {
            long x = input.nextLong();
            long y = input.nextLong();
            long distance = input.nextLong();
            long u = x + y;
            long v = x - y;
            int answer;
            if (distance == 0) {
                answer = count(byU, u, v, v);
            } else {
                answer = count(byU, u - distance, v - distance, v + distance);
                answer += count(byU, u + distance, v - distance, v + distance);
                // The vertical sides already include the four corners.
                answer += count(byV, v - distance, u - distance + 1, u + distance - 1);
                answer += count(byV, v + distance, u - distance + 1, u + distance - 1);
            }
            output.append(answer).append('\n');
        }
        System.out.print(output);
    }
}
