import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int DIGITS = 10;
    static final double FULL_TURN = 360;
    static final int VERTICES = 3;
    static final int[][] ORDERS = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2},
                                   {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};

    static long cross(long[] o, long[] a, long[] b) {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }

    static long length2(long[] a, long[] b) {
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
    }

    // num / den with exactly ten digits after the point
    static String decimal(long num, long den) {
        return new BigDecimal(num)
            .divide(new BigDecimal(den), DIGITS, RoundingMode.HALF_UP)
            .toPlainString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long[][] target = new long[VERTICES][2], token = new long[VERTICES][2];
        for (long[] p : target) {
            p[0] = in.nextLong();
            p[1] = in.nextLong();
        }
        for (long[] p : token) {
            p[0] = in.nextLong();
            p[1] = in.nextLong();
        }

        // a correspondence works when the sides match and the turn is the same
        // (the token cannot be flipped over)
        List<long[][]> fits = new ArrayList<>();
        for (int[] idx : ORDERS) {
            long[][] order = {target[idx[0]], target[idx[1]], target[idx[2]]};
            if (length2(token[0], token[1]) == length2(order[0], order[1]) &&
                length2(token[0], token[2]) == length2(order[0], order[2]) &&
                length2(token[1], token[2]) == length2(order[1], order[2]) &&
                (cross(token[0], token[1], token[2]) > 0) ==
                    (cross(order[0], order[1], order[2]) > 0))
                fits.add(order);
        }
        if (fits.isEmpty()) {
            System.out.println(0);
            return;
        }
        for (long[][] order : fits) {
            long dx = order[0][0] - token[0][0], dy = order[0][1] - token[0][1];
            boolean shift = true;
            for (int i = 1; i < VERTICES; i++)
                shift = shift && order[i][0] - token[i][0] == dx && order[i][1] - token[i][1] == dy;
            if (shift) {
                System.out.println("1 " + decimal(dx, 1) + " " + decimal(dy, 1));
                return;
            }
        }

        long[][] order = fits.get(0);
        long ux = token[1][0] - token[0][0], uy = token[1][1] - token[0][1];
        long wx = order[1][0] - order[0][0], wy = order[1][1] - order[0][1];
        double angle = Math.toDegrees(Math.atan2(ux * wy - uy * wx, ux * wx + uy * wy));
        if (angle < 0)
            angle += FULL_TURN;

        // the centre is a vertex that stays, or it lies on the perpendicular
        // bisector of every vertex and its image: 2 d . c = |t|^2 - |s|^2
        String cx = null, cy = null;
        for (int i = 0; i < VERTICES; i++)
            if (token[i][0] == order[i][0] && token[i][1] == order[i][1]) {
                cx = decimal(token[i][0], 1);
                cy = decimal(token[i][1], 1);
            }
        if (cx == null) {
            long[] a = new long[VERTICES], b = new long[VERTICES], e = new long[VERTICES];
            for (int i = 0; i < VERTICES; i++) {
                a[i] = 2 * (order[i][0] - token[i][0]);
                b[i] = 2 * (order[i][1] - token[i][1]);
                e[i] = order[i][0] * order[i][0] + order[i][1] * order[i][1] -
                       token[i][0] * token[i][0] - token[i][1] * token[i][1];
            }
            for (int i = 0; i < VERTICES && cx == null; i++)
                for (int j = i + 1; j < VERTICES && cx == null; j++) {
                    long det = a[i] * b[j] - a[j] * b[i];
                    if (det != 0) {
                        cx = decimal(e[i] * b[j] - e[j] * b[i], det);
                        cy = decimal(a[i] * e[j] - a[j] * e[i], det);
                    }
                }
        }
        System.out.println("2 " + cx + " " + cy + " " + String.format(Locale.US, "%.10f", angle));
    }
}
