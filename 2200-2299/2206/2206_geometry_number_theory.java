import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final long SCALE = 1000;
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static long next() throws IOException {
        int digit;
        do {
            digit = INPUT.read();
        } while (digit <= ' ' && digit >= 0);
        long value = 0;
        while (digit > ' ') {
            if (digit != '.') {
                value = value * 10 + digit - '0';
            }
            digit = INPUT.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = (int) next();
        long[] x = new long[n];
        long[] y = new long[n];
        long minimum = 0;
        long maximum = 0;
        for (int i = 0; i < n; ++i) {
            x[i] = next();
            y[i] = next();
            if (i == 0 || x[i] < minimum) {
                minimum = x[i];
            }
            maximum = Math.max(maximum, x[i]);
        }
        int left = (int) ((minimum + SCALE - 1) / SCALE);
        int right = (int) (maximum / SCALE);
        if (left > right) {
            System.out.println(0);
            return;
        }
        int[] lower = new int[right + 1];
        int[] upper = new int[right + 1];
        for (int i = 0; i < n; ++i) {
            int j = (i + 1) % n;
            if (x[i] == x[j]) {
                continue;
            }
            boolean bottom = x[i] < x[j];
            int a = bottom ? i : j;
            int b = bottom ? j : i;
            int begin = (int) ((x[a] + SCALE - 1) / SCALE);
            int end = (int) (x[b] / SCALE);
            long dx = x[b] - x[a];
            long dy = y[b] - y[a];
            long denominator = dx * SCALE;
            long numerator = y[a] * dx + (begin * SCALE - x[a]) * dy;
            if (bottom) {
                --numerator;
            }
            int[] target = bottom ? lower : upper;
            for (int column = begin; column <= end; ++column) {
                target[column] = (int) (numerator / denominator);
                numerator += dy * SCALE;
            }
        }
        int limit = 0;
        for (int value : upper) {
            limit = Math.max(limit, value);
        }
        limit = Math.min(limit, right);
        int[] mu = new int[limit + 1];
        Arrays.fill(mu, 1);
        boolean[] composite = new boolean[limit + 1];
        for (int prime = 2; prime <= limit; ++prime) {
            if (composite[prime]) {
                continue;
            }
            for (int multiple = prime; multiple <= limit; multiple += prime) {
                composite[multiple] = true;
                mu[multiple] = -mu[multiple];
            }
            long square = (long) prime * prime;
            for (long multiple = square; multiple <= limit; multiple += square) {
                mu[(int) multiple] = 0;
            }
        }
        long answer = 0;
        for (int divisor = 1; divisor <= limit; ++divisor) {
            if (mu[divisor] == 0) {
                continue;
            }
            long subtotal = 0;
            int begin = ((left + divisor - 1) / divisor) * divisor;
            for (int column = begin; column <= right; column += divisor) {
                subtotal += upper[column] / divisor - lower[column] / divisor;
            }
            answer += mu[divisor] * subtotal;
        }
        System.out.println(answer);
    }
}
