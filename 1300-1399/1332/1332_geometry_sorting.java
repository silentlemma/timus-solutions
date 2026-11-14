import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final double FULL_TURN = 2 * Math.PI;
    private static final double EPS = 1e-12;
    private static final int DECIMAL = 10;
    private static final int EVENT_END = 1;

    private static int next(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        boolean negative = ch == '-';
        if (negative) {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * DECIMAL + ch - '0';
            ch = input.read();
        }
        return negative ? -value : value;
    }

    private static double normalize(double angle) { return angle < 0 ? angle + FULL_TURN : angle; }

    private static int mostCities(int[] xs, int[] ys, int reach) {
        int n = xs.length;
        if (reach <= 0 || n <= 1) {
            return reach < 0 ? 0 : Math.min(n, 1);
        }
        int diameter = 2 * reach;
        int limit = diameter * diameter;
        long[] events = new long[2 * (n - 1)];
        int best = 1;
        for (int anchor = 0; anchor < n && best < n; anchor++) {
            int size = 0;
            int active = 1;
            for (int city = 0; city < n; city++) {
                int dx = xs[city] - xs[anchor];
                int dy = ys[city] - ys[anchor];
                int squared = dx * dx + dy * dy;
                if (squared == 0 || squared > limit) {
                    continue;
                }
                double direction = Math.atan2(dy, dx);
                double halfWidth = Math.acos(Math.sqrt(squared) / diameter);
                double start = normalize(direction - halfWidth - EPS);
                double end = normalize(direction + halfWidth + EPS);
                if (start > end) {
                    active++;
                }
                // Positive angles sort by their floating-point bits. Use the low bit
                // to place the start of a closed interval before an equal end.
                events[size++] = Double.doubleToLongBits(start == 0 ? 0.0 : start) & ~1L;
                events[size++] = Double.doubleToLongBits(end == 0 ? 0.0 : end) | EVENT_END;
            }
            Arrays.sort(events, 0, size);
            best = Math.max(best, active);
            for (int i = 0; i < size; i++) {
                active += (events[i] & EVENT_END) == 0 ? 1 : -1;
                best = Math.max(best, active);
            }
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = next(input);
        int[] xs = new int[count];
        int[] ys = new int[count];
        for (int i = 0; i < count; i++) {
            xs[i] = next(input);
            ys[i] = next(input);
        }
        int reach = next(input) - next(input);
        System.out.println(mostCities(xs, ys, reach));
    }
}
