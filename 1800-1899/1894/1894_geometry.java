import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int SNAPSHOT_AGE = 60;

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        long number() throws IOException {
            int character;
            do {
                character = stream.read();
            } while (character <= ' ' && character != -1);
            long sign = 1;
            if (character == '-') {
                sign = -1;
                character = stream.read();
            }
            long result = 0;
            while (character > ' ') {
                result = result * 10 + character - '0';
                character = stream.read();
            }
            return sign * result;
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

    private static Point[] rotatePolygon(Point[] points) {
        int start = 0;
        for (int i = 1; i < points.length; ++i) {
            if (points[i].y < points[start].y
                    || (points[i].y == points[start].y && points[i].x < points[start].x)) {
                start = i;
            }
        }
        Point[] result = new Point[points.length + 1];
        for (int i = 0; i < points.length; ++i) {
            result[i] = points[(start + i) % points.length];
        }
        result[points.length] = result[0];
        return result;
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int n = (int) input.number();
        int m = (int) input.number();
        Point[] airport = new Point[n];
        Point[] cloud = new Point[m];
        for (int i = 0; i < n; ++i) {
            airport[i] = new Point(input.number(), input.number());
        }
        for (int i = 0; i < m; ++i) {
            cloud[i] = new Point(-input.number(), -input.number());
        }
        airport = rotatePolygon(airport);
        cloud = rotatePolygon(cloud);
        long x = airport[0].x + cloud[0].x;
        long y = airport[0].y + cloud[0].y;
        int i = 0;
        int j = 0;
        double distance = Double.POSITIVE_INFINITY;
        while (i < n || j < m) {
            long ax = i < n ? airport[i + 1].x - airport[i].x : 0;
            long ay = i < n ? airport[i + 1].y - airport[i].y : 0;
            long bx = j < m ? cloud[j + 1].x - cloud[j].x : 0;
            long by = j < m ? cloud[j + 1].y - cloud[j].y : 0;
            long turn = ax * by - ay * bx;
            boolean takeAirport = i < n && (j == m || turn >= 0);
            boolean takeCloud = j < m && (i == n || turn <= 0);
            long dx = (takeAirport ? ax : 0) + (takeCloud ? bx : 0);
            long dy = (takeAirport ? ay : 0) + (takeCloud ? by : 0);
            double candidate = (x * dy - y * dx) / Math.hypot(dx, dy);
            distance = Math.min(distance, candidate);
            x += dx;
            y += dy;
            if (takeAirport) {
                ++i;
            }
            if (takeCloud) {
                ++j;
            }
        }
        System.out.printf(java.util.Locale.US, "%.10f%n", Math.max(0, distance - SNAPSHOT_AGE));
    }
}
