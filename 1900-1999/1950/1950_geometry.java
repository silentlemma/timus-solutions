import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    private static final long DECIMAL_SCALE = 1000, SIDE = 10 * DECIMAL_SCALE;
    private static final int DECIMAL_PLACES = 3, CUTS = 30;
    private static final long GRID_SCALE = 1L << CUTS;
    private static final double INITIAL_AREA = 50.0;

    static final class Point {
        final long x, y;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    static long parseCoordinate(String text) {
        int dot = text.indexOf('.');
        String whole = dot < 0 ? text : text.substring(0, dot);
        String fractional = dot < 0 ? "" : text.substring(dot + 1);
        fractional = (fractional + "000").substring(0, DECIMAL_PLACES);
        return Long.parseLong(whole.isEmpty() ? "0" : whole) * DECIMAL_SCALE
            + Long.parseLong(fractional);
    }

    static long sign(long value) {
        return Long.compare(value, 0);
    }

    static boolean opposite(long first, long second) {
        return (first < 0 && second > 0) || (second < 0 && first > 0);
    }

    static double areaForSale(long x, long y) {
        Point target = new Point(x * GRID_SCALE, y * GRID_SCALE);
        Point right = new Point(SIDE * GRID_SCALE, 0), first = new Point(0, 0);
        Point second = new Point(SIDE * GRID_SCALE, SIDE * GRID_SCALE);
        double area = INITIAL_AREA, answer = 0;
        for (int cut = 0; cut < CUTS; ++cut) {
            Point middle = new Point((first.x + second.x) / 2, (first.y + second.y) / 2);
            long normalX = sign(middle.y - right.y), normalY = -sign(middle.x - right.x);
            long originSide = -normalX * right.x - normalY * right.y;
            long targetSide = normalX * (target.x - right.x) + normalY * (target.y - right.y);
            long rayRight = x * right.y - y * right.x, rayMiddle = x * middle.y - y * middle.x;
            double half = area / 2;
            if (opposite(rayRight, rayMiddle) &&
                (opposite(originSide, targetSide) || targetSide == 0))
                answer += half;
            if (targetSide == 0)
                break;
            long firstSide = normalX * (first.x - right.x) + normalY * (first.y - right.y);
            if ((targetSide > 0) == (firstSide > 0))
                second = right;
            else
                first = right;
            right = middle;
            area = half;
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder input = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null)
            input.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(input.toString());
        long x = parseCoordinate(words.nextToken()), y = parseCoordinate(words.nextToken());
        System.out.printf(Locale.US, "%.10f%n", areaForSale(x, y));
    }
}
