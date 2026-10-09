import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    // squared distances carry these denominators: a point scaled by 2, a square
    // by its projections
    static final long POINT_DEN = 4, SQUARE_DEN = 8;

    // squared distance from P to the square with diagonal (x1, y1)-(x2, y2),
    // as a numerator and a denominator
    static BigInteger[] distance(long x1, long y1, long x2, long y2, long px, long py) {
        // doubled coordinates of P relative to the centre, and the diagonal
        long qx = 2 * px - x1 - x2, qy = 2 * py - y1 - y2;
        long dx = x2 - x1, dy = y2 - y1, h = dx * dx + dy * dy;
        if (h == 0) {
            return new BigInteger[] {BigInteger.valueOf(qx * qx + qy * qy),
                                     BigInteger.valueOf(POINT_DEN)};
        }
        // projections on the two side directions, the diagonal turned by +-45
        // degrees; inside the square both stay within h
        long s1 = Math.abs(qx * (dx - dy) + qy * (dy + dx));
        long s2 = Math.abs(qx * (dx + dy) + qy * (dy - dx));
        long a = Math.max(0, s1 - h), b = Math.max(0, s2 - h);
        return new BigInteger[] {BigInteger.valueOf(a * a + b * b),
                                 BigInteger.valueOf(SQUARE_DEN * h)};
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long[] x1 = new long[n], y1 = new long[n], x2 = new long[n], y2 = new long[n];
        for (int i = 0; i < n; i++) {
            x1[i] = in.nextLong();
            y1[i] = in.nextLong();
            x2[i] = in.nextLong();
            y2[i] = in.nextLong();
        }
        long px = in.nextLong(), py = in.nextLong();
        BigInteger[][] dist = new BigInteger[n][];
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            dist[i] = distance(x1[i], y1[i], x2[i], y2[i], px, py);
            order[i] = i;
        }
        // the cross products reach about 10^28, past 64 bits; the sort is stable
        Arrays.sort(
            order,
            (i, j) -> dist[i][0].multiply(dist[j][1]).compareTo(dist[j][0].multiply(dist[i][1])));
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            out.append(i > 0 ? " " : "").append(order[i] + 1);
        }
        System.out.println(out);
    }
}
