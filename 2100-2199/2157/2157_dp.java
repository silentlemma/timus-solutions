import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    private static final int MAX_COORDINATE = 10000;
    private static final int COLUMN_COUNT = 2 * MAX_COORDINATE + 1;
    private static final int GRAVITY = 10;
    private static final int HALF_GRAVITY = GRAVITY / 2;
    private static final int OUTPUT_PRECISION = 9;

    private static final class FastInput {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int ch = stream.read();
            while (ch <= ' ') {
                ch = stream.read();
            }
            int sign = 1;
            if (ch == '-') {
                sign = -1;
                ch = stream.read();
            }
            int value = 0;
            while (ch > ' ') {
                value = value * 10 + ch - '0';
                ch = stream.read();
            }
            return value * sign;
        }
    }

    private static final class Point {
        final int x;
        final int y;
        final int wait;
        double best;

        Point(int x, int y, int wait) {
            this.x = x;
            this.y = y;
            this.wait = wait;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput in = new FastInput();
        int n = in.nextInt();
        int startX = in.nextInt();
        int startY = in.nextInt();
        Point[] points = new Point[n + 1];
        for (int i = 0; i < n; i++) {
            points[i] = new Point(in.nextInt(), in.nextInt(), in.nextInt());
        }
        points[n] = new Point(startX, startY, 0);
        Arrays.sort(points, Comparator.comparingInt(p -> p.y));
        int[] counts = new int[COLUMN_COUNT];
        for (int i = 0; i < n; i++) {
            counts[points[i].x + MAX_COORDINATE]++;
        }
        int[][] columns = new int[COLUMN_COUNT][];
        for (int x = 0; x < COLUMN_COUNT; x++) {
            columns[x] = new int[counts[x]];
        }
        Arrays.fill(counts, 0);
        for (int i = 0; i < n; i++) {
            int column = points[i].x + MAX_COORDINATE;
            columns[column][counts[column]++] = i;
        }
        double[] fall = new double[startY + 1];
        for (int drop = 0; drop <= startY; drop++) {
            fall[drop] = Math.sqrt((double) drop / HALF_GRAVITY);
        }
        for (Point p : points) {
            double best = fall[p.y];
            int radius = (int) Math.sqrt((p.y - 1) / HALF_GRAVITY);
            int left = Math.max(-MAX_COORDINATE, p.x - radius);
            int right = Math.min(MAX_COORDINATE, p.x + radius);
            for (int x = left; x <= right; x++) {
                int dx = x - p.x;
                int drop = Math.max(1, HALF_GRAVITY * dx * dx);
                int height = p.y - drop;
                int[] column = columns[x + MAX_COORDINATE];
                int lo = 0;
                int hi = column.length;
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (points[column[mid]].y <= height) {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }
                // A higher reachable cloud dominates all lower clouds in its column.
                if (lo > 0) {
                    Point target = points[column[lo - 1]];
                    double candidate = fall[p.y - target.y] + target.best;
                    best = Math.max(best, candidate);
                }
            }
            p.best = p.wait + best;
        }
        // Round the exact double value consistently with the other languages.
        BigDecimal answer = new BigDecimal(points[n].best);
        String rounded = answer.setScale(OUTPUT_PRECISION, RoundingMode.HALF_EVEN).toPlainString();
        System.out.println(rounded);
    }
}
