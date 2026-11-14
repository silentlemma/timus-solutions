import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int DIMENSIONS = 3;
    private static final int DECIMAL = 10;
    private static final long CHUNK_BASE = 65_536L;

    private static long next(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        boolean negative = ch == '-';
        if (negative) {
            ch = input.read();
        }
        long value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * DECIMAL + ch - '0';
            ch = input.read();
        }
        return negative ? -value : value;
    }

    private static long[] subtract(long[] left, long[] right) {
        long[] result = new long[DIMENSIONS];
        for (int i = 0; i < DIMENSIONS; i++) {
            result[i] = left[i] - right[i];
        }
        return result;
    }

    private static long dot(long[] left, long[] right) {
        long total = 0;
        for (int i = 0; i < DIMENSIONS; i++) {
            total += left[i] * right[i];
        }
        return total;
    }

    private static boolean coplanar(long[] ab, long[] cd, long[] ac) {
        long high = 0;
        long low = 0;
        for (int i = 0; i < DIMENSIONS; i++) {
            int j = (i + 1) % DIMENSIONS;
            int k = (i + 2) % DIMENSIONS;
            long normal = ab[j] * cd[k] - ab[k] * cd[j];
            // The mixed product may overflow, but each partial sum fits in long.
            high += normal * (ac[i] / CHUNK_BASE);
            low += normal * (ac[i] % CHUNK_BASE);
        }
        return low % CHUNK_BASE == 0 && high + low / CHUNK_BASE == 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        long[][] points = new long[DIMENSIONS + 1][DIMENSIONS];
        for (long[] point : points) {
            for (int i = 0; i < DIMENSIONS; i++) {
                point[i] = next(input);
            }
        }
        long[] ab = subtract(points[1], points[0]);
        long[] cd = subtract(points[DIMENSIONS], points[2]);
        long[] ac = subtract(points[2], points[0]);
        boolean valid = dot(ab, cd) == 0 && dot(ac, ab) >= dot(ab, ab) && dot(ac, cd) >= 0 &&
                        coplanar(ab, cd, ac);
        System.out.println(valid ? "Valid" : "Invalid");
    }
}
