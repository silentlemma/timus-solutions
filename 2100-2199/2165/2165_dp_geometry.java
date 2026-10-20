import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final long COORDINATE_LIMIT = 100000000L;
    private static final long AREA_BOUND_FACTOR = 8;
    private static final long INFINITY = AREA_BOUND_FACTOR * COORDINATE_LIMIT * COORDINATE_LIMIT;
    private static final String WHOLE_SUFFIX = ".0";
    private static final String HALF_SUFFIX = ".5";
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static long nextLong() throws IOException {
        int character = INPUT.read();
        while (character <= ' ') {
            character = INPUT.read();
        }
        long sign = 1;
        if (character == '-') {
            sign = -1;
            character = INPUT.read();
        }
        long value = 0;
        while (character >= '0' && character <= '9') {
            value = value * 10 + character - '0';
            character = INPUT.read();
        }
        return value * sign;
    }

    public static void main(String[] args) throws IOException {
        int n = (int) nextLong();
        long[] x = new long[n];
        long[] y = new long[n];
        for (int i = 0; i < n; i++) {
            x[i] = nextLong();
            y[i] = nextLong();
        }

        long[][] dp = new long[n][n];
        for (int i = 0; i + 1 < n; i++) {
            dp[i][i + 1] = INFINITY;
        }
        for (int width = 2; width < n; width++) {
            for (int left = 0; left + width < n; left++) {
                int right = left + width;
                long best = 0;
                long dx = x[right] - x[left];
                long dy = y[right] - y[left];
                for (int middle = left + 1; middle < right; middle++) {
                    long candidate = Math.min(dp[left][middle], dp[middle][right]);
                    if (candidate <= best) {
                        continue;
                    }
                    long area = (x[middle] - x[left]) * dy - (y[middle] - y[left]) * dx;
                    candidate = Math.min(candidate, area);
                    best = Math.max(best, candidate);
                }
                dp[left][right] = best;
            }
        }
        long answer = dp[0][n - 1];
        String suffix = answer % 2 == 0 ? WHOLE_SUFFIX : HALF_SUFFIX;
        System.out.println(answer / 2 + suffix);
    }
}
