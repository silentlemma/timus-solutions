import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final double HALF_TURN = 180.0;
    static long w, h, bx, by;

    // the mirror images of B that a straight line from A reaches after the
    // given number of bounces: i walls across, j walls up
    static long[] image(int i, int j) {
        long x = i * w + (Math.abs(i) % 2 == 0 ? bx : w - bx);
        long y = j * h + (Math.abs(j) % 2 == 0 ? by : h - by);
        return new long[] {x, y};
    }

    static List<long[]> images(int bounces) {
        List<long[]> found = new ArrayList<>();
        for (int i = -bounces; i <= bounces; i++) {
            int rest = bounces - Math.abs(i);
            found.add(image(i, rest));
            if (rest != 0)
                found.add(image(i, -rest));
        }
        return found;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        w = in.nextLong();
        h = in.nextLong();
        int n = in.nextInt();
        long ax = in.nextLong(), ay = in.nextLong();
        bx = in.nextLong();
        by = in.nextLong();
        boolean found = false;
        long bestLength = 0;
        double bestAngle = 0;
        for (long[] p : images(n)) {
            long dx = p[0] - ax, dy = p[1] - ay, length = dx * dx + dy * dy;
            double angle = Math.toDegrees(Math.atan2(dy, dx));
            if (angle < 0)
                angle += 2 * HALF_TURN;
            if (!found || length < bestLength || (length == bestLength && angle < bestAngle)) {
                found = true;
                bestLength = length;
                bestAngle = angle;
            }
        }
        System.out.println(String.format(Locale.US, "%.2f", bestAngle));
    }
}
