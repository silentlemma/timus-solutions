import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    // squared distances carry these denominators: a point scaled by 2, a square
    // by its projections
    static final long POINT_DEN = 4, SQUARE_DEN = 8;

    // squared distance from P to the square with diagonal (x1, y1)-(x2, y2),
    // as a numerator and a denominator
    static BigInteger[] distance(long x1, long y1, long x2, long y2, BigInteger px, BigInteger py) {
        // doubled coordinates of P relative to the centre, and the diagonal
        BigInteger qx = px.multiply(BigInteger.valueOf(2)).subtract(BigInteger.valueOf(x1 + x2));
        BigInteger qy = py.multiply(BigInteger.valueOf(2)).subtract(BigInteger.valueOf(y1 + y2));
        long dx = x2 - x1, dy = y2 - y1, h = dx * dx + dy * dy;
        if (h == 0) {
            return new BigInteger[] {qx.multiply(qx).add(qy.multiply(qy)),
                                     BigInteger.valueOf(POINT_DEN)};
        }
        // projections on the two side directions, the diagonal turned by +-45
        // degrees; inside the square both stay within h
        BigInteger s1 = qx.multiply(BigInteger.valueOf(dx - dy))
                            .add(qy.multiply(BigInteger.valueOf(dy + dx))).abs();
        BigInteger s2 = qx.multiply(BigInteger.valueOf(dx + dy))
                            .add(qy.multiply(BigInteger.valueOf(dy - dx))).abs();
        BigInteger a = s1.subtract(BigInteger.valueOf(h)).max(BigInteger.ZERO);
        BigInteger b = s2.subtract(BigInteger.valueOf(h)).max(BigInteger.ZERO);
        return new BigInteger[] {a.multiply(a).add(b.multiply(b)),
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
        BigInteger px = new BigInteger(in.next()), py = new BigInteger(in.next());
        BigInteger[][] dist = new BigInteger[n][];
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            dist[i] = distance(x1[i], y1[i], x2[i], y2[i], px, py);
            order[i] = i;
        }
        // exact cross products, with the input index breaking ties
        Arrays.sort(
            order,
            (i, j) -> {
                int c = dist[i][0].multiply(dist[j][1]).compareTo(dist[j][0].multiply(dist[i][1]));
                return c != 0 ? c : Integer.compare(i, j);
            });
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            out.append(i > 0 ? " " : "").append(order[i] + 1);
        }
        System.out.println(out);
    }
}
