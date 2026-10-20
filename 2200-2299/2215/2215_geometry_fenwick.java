import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    static final int FULL_TURN = 4;
    static final int THREE_QUARTERS = FULL_TURN - 1;

    static class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        String next() throws IOException {
            StringBuilder token = new StringBuilder();
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c != -1);
            while (c > ' ') {
                token.append((char) c);
                c = stream.read();
            }
            return token.toString();
        }

        long number() throws IOException {
            return Long.parseLong(next());
        }
    }

    static class Point {
        long x, y;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Event {
        long x, low, high;
        int index, sign;

        Event(long x, long low, long high, int index, int sign) {
            this.x = x;
            this.low = low;
            this.high = high;
            this.index = index;
            this.sign = sign;
        }
    }

    static int bound(long[] values, int size, long value, boolean inclusive) {
        int low = 0, high = size;
        while (low < high) {
            int middle = low + (high - low) / 2;
            if (values[middle] < value || (inclusive && values[middle] == value)) {
                low = middle + 1;
            } else {
                high = middle;
            }
        }
        return low;
    }

    static int prefix(int[] tree, int index) {
        int sum = 0;
        for (; index > 0; index -= index & -index) {
            sum += tree[index];
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        Input in = new Input();
        int n = (int) in.number();
        Point[] points = new Point[n];
        long[] ys = new long[n];
        for (int i = 0; i < n; ++i) {
            points[i] = new Point(in.number(), in.number());
            ys[i] = points[i].y;
        }
        Arrays.sort(points, Comparator.comparingLong(p -> p.x));
        Arrays.sort(ys);
        int size = 0;
        for (long y : ys) {
            if (size == 0 || ys[size - 1] != y) {
                ys[size++] = y;
            }
        }
        int q = (int) in.number();
        int orientation = 0;
        long tx = 0, ty = 0;
        ArrayList<Event> events = new ArrayList<>();
        int[] answers = new int[q];
        int answerCount = 0;
        for (int i = 0; i < q; ++i) {
            String command = in.next();
            long x = in.number(), y = in.number();
            if (!command.equals("ask")) {
                int turns = command.equals("r90") ? 1
                    : command.equals("r180") ? 2 : THREE_QUARTERS;
                long dx = tx - x, dy = ty - y;
                for (int step = 0; step < turns; ++step) {
                    long next = -dy;
                    dy = dx;
                    dx = next;
                }
                tx = x + dx;
                ty = y + dy;
                orientation = (orientation + turns) % FULL_TURN;
            } else {
                long xx = in.number(), yy = in.number();
                x -= tx;
                y -= ty;
                xx -= tx;
                yy -= ty;
                // Undo the global transform on two opposite corners.
                for (int step = 0; step < orientation; ++step) {
                    long next = y;
                    y = -x;
                    x = next;
                    next = yy;
                    yy = -xx;
                    xx = next;
                }
                if (x > xx) {
                    long next = x;
                    x = xx;
                    xx = next;
                }
                if (y > yy) {
                    long next = y;
                    y = yy;
                    yy = next;
                }
                events.add(new Event(xx, y, yy, answerCount, 1));
                events.add(new Event(x - 1, y, yy, answerCount, -1));
                ++answerCount;
            }
        }
        events.sort(Comparator.comparingLong(e -> e.x));
        int[] tree = new int[size + 1];
        int inserted = 0;
        for (Event event : events) {
            while (inserted < n && points[inserted].x <= event.x) {
                int index = bound(ys, size, points[inserted].y, false) + 1;
                for (; index <= size; index += index & -index) {
                    ++tree[index];
                }
                ++inserted;
            }
            int low = bound(ys, size, event.low, false);
            int high = bound(ys, size, event.high, true);
            answers[event.index] += event.sign * (prefix(tree, high) - prefix(tree, low));
        }
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < answerCount; ++i) {
            output.append(answers[i]).append('\n');
        }
        System.out.print(output);
    }
}
