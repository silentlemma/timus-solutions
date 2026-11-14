import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigInteger;

public class Main {
    private static final int CORNERS = 3;
    private static final int DECIMAL = 10;

    private static long next(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        boolean negative = ch == '-';
        if (negative || ch == '+') {
            ch = input.read();
        }
        long value = 0;
        while (ch >= '0' && ch <= '9') {
            value = DECIMAL * value + (ch - '0');
            ch = input.read();
        }
        return negative ? -value : value;
    }

    private static boolean reachesWall(long reach, long radius, long normSquared) {
        long radiusSquared = radius * radius;
        long absoluteReach = Math.abs(reach);
        // The numerator and the radius budget both need an exact comparison.
        if (absoluteReach <= Long.MAX_VALUE / Math.max(1, absoluteReach) &&
            normSquared <= Long.MAX_VALUE / radiusSquared) {
            return reach * reach <= radiusSquared * normSquared;
        }
        BigInteger numerator = BigInteger.valueOf(reach);
        BigInteger budget =
            BigInteger.valueOf(radiusSquared).multiply(BigInteger.valueOf(normSquared));
        return numerator.multiply(numerator).compareTo(budget) <= 0;
    }

    private static boolean canCollapse(BufferedInputStream input) throws IOException {
        long mana = next(input), height = next(input), top = next(input);
        long radius = mana - height;
        if (radius <= 0) {
            return false;
        }
        if (radius >= height) {
            return true;
        }
        long x = next(input), y = next(input);
        long[] bx = new long[CORNERS];
        long[] by = new long[CORNERS];
        for (int i = 0; i < CORNERS; i++) {
            bx[i] = next(input);
            by[i] = next(input);
        }
        long tx = next(input), ty = next(input);
        for (int i = 0; i < CORNERS; i++) {
            int j = (i + 1) % CORNERS;
            long ux = bx[j] - bx[i], uy = by[j] - by[i];
            long nx = uy * top, ny = -ux * top;
            long nz = ux * (ty - by[i]) - uy * (tx - bx[i]);
            long reach = nx * (x - bx[i]) + ny * (y - by[i]) + nz * height;
            if (reachesWall(reach, radius, nx * nx + ny * ny + nz * nz)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(canCollapse(new BufferedInputStream(System.in)) ? "YES" : "NO");
    }
}
