import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final double EPS = 1e-6;
    private static final int SKY = 1000000;
    private static final int DECIMAL = 10;

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        private int first() throws IOException {
            int c = stream.read();
            while (c >= 0 && c <= ' ') {
                c = stream.read();
            }
            return c;
        }

        int integer() throws IOException {
            int value = 0;
            for (int c = first(); c >= '0' && c <= '9'; c = stream.read()) {
                value = value * DECIMAL + c - '0';
            }
            return value;
        }

        double radius(StringBuilder token) throws IOException {
            token.setLength(0);
            for (int c = first(); c > ' '; c = stream.read()) {
                token.append((char)c);
            }
            return Double.parseDouble(token.toString());
        }
    }

    private static final class Station {
        final int row, col, height;
        final long reach;

        Station(int row, int col, int height, long reach) {
            this.row = row;
            this.col = col;
            this.height = height;
            this.reach = reach;
        }
    }

    private static long square(long x) { return x * x; }

    private static long roundedUpRoot(long x) {
        long root = (long)Math.sqrt(x);
        return root * root < x ? root + 1 : root;
    }

    private static int retainConstraints(Station[] stations) {
        if (stations.length == 0) {
            return 0;
        }
        int smallest = 0;
        for (int i = 1; i < stations.length; i++) {
            if (stations[i].reach < stations[smallest].reach) {
                smallest = i;
            }
        }
        Station inner = stations[smallest];
        stations[smallest] = stations[0];
        stations[0] = inner;
        long radius = roundedUpRoot(inner.reach);
        int count = 1;
        for (int i = 1; i < stations.length; i++) {
            Station s = stations[i];
            long separation = square(s.row - inner.row) + square(s.col - inner.col) +
                              square(s.height - inner.height);
            // Rounded-up distances make this a sufficient containment test.
            if (square(radius + roundedUpRoot(separation)) > s.reach) {
                stations[count++] = s;
            }
        }
        return count;
    }

    private static long placements(int rows, int cols, short[] heights, boolean[] occupied,
                                   Station[] stations) {
        int count = retainConstraints(stations);
        long[] bands = new long[count];
        long total = 0;
        for (int row = 0; row < rows; row++) {
            for (int t = 0; t < count; t++) {
                bands[t] = stations[t].reach - square(row - stations[t].row);
            }
            for (int col = 0; col < cols; col++) {
                int cell = row * cols + col;
                if (occupied[cell]) {
                    continue;
                }
                long low = heights[cell], high = SKY;
                for (int t = 0; t < count && low <= high; t++) {
                    Station s = stations[t];
                    long reach = bands[t] - square(col - s.col);
                    if (reach < 0) {
                        high = -1;
                        break;
                    }
                    if (square(low - s.height) <= reach && square(high - s.height) <= reach) {
                        continue;
                    }
                    long extent = (long)Math.sqrt(reach);
                    if (extent * extent > reach) {
                        extent--;
                    }
                    low = Math.max(low, s.height - extent);
                    high = Math.min(high, s.height + extent);
                }
                if (low <= high) {
                    total += high - low + 1;
                }
            }
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int rows = input.integer(), cols = input.integer(), count = input.integer();
        short[] heights = new short[rows * cols];
        for (int i = 0; i < heights.length; i++) {
            heights[i] = (short)input.integer();
        }
        boolean[] occupied = new boolean[heights.length];
        Station[] stations = new Station[count];
        StringBuilder token = new StringBuilder();
        for (int i = 0; i < count; i++) {
            int row = input.integer() - 1, col = input.integer() - 1;
            double radius = input.radius(token);
            int cell = row * cols + col;
            occupied[cell] = true;
            stations[i] = new Station(row, col, heights[cell], (long)(radius * radius + EPS));
        }
        System.out.println(placements(rows, cols, heights, occupied, stations));
    }
}
