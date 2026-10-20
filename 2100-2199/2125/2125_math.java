import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;

public class Main {
    private static final int MOD = 998244353;
    private static final int ROOT = 3;
    private static final int BUFFER_BITS = 16;
    private static final int BUFFER_SIZE = 1 << BUFFER_BITS;

    private static int power(int base, int exponent) {
        long result = 1;
        long value = base;
        while (exponent > 0) {
            if ((exponent & 1) != 0) {
                result = result * value % MOD;
            }
            value = value * value % MOD;
            exponent >>= 1;
        }
        return (int) result;
    }

    private static void transform(int[] values, boolean inverse) {
        int size = values.length;
        for (int i = 1, j = 0; i < size; ++i) {
            int bit = size >> 1;
            while ((j & bit) != 0) {
                j ^= bit;
                bit >>= 1;
            }
            j ^= bit;
            if (i < j) {
                int temporary = values[i];
                values[i] = values[j];
                values[j] = temporary;
            }
        }
        int primitive = inverse ? power(ROOT, MOD - 2) : ROOT;
        for (int length = 2; length <= size; length <<= 1) {
            int half = length >> 1;
            int step = power(primitive, (MOD - 1) / length);
            for (int start = 0; start < size; start += length) {
                long root = 1;
                for (int j = 0; j < half; ++j) {
                    int left = values[start + j];
                    int right = (int) (values[start + j + half] * root % MOD);
                    int sum = left + right;
                    if (sum >= MOD) {
                        sum -= MOD;
                    }
                    int difference = left - right;
                    if (difference < 0) {
                        difference += MOD;
                    }
                    values[start + j] = sum;
                    values[start + j + half] = difference;
                    root = root * step % MOD;
                }
            }
        }
        if (inverse) {
            long scale = power(size, MOD - 2);
            for (int i = 0; i < size; ++i) {
                values[i] = (int) (values[i] * scale % MOD);
            }
        }
    }

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in, BUFFER_SIZE);

        int nextInt() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c >= 0);
            int value = 0;
            while (c > ' ') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int n = input.nextInt();
        int m = input.nextInt();
        int total = n + m;
        int size = 1;
        while (size < n + total - 1) {
            size <<= 1;
        }
        int[] factorial = new int[total];
        int[] inverseFactorial = new int[total];
        factorial[0] = 1;
        for (int i = 1; i < total; ++i) {
            factorial[i] = (int) ((long) factorial[i - 1] * i % MOD);
        }
        inverseFactorial[total - 1] = power(factorial[total - 1], MOD - 2);
        for (int i = total - 1; i > 0; --i) {
            inverseFactorial[i - 1] = (int) ((long) inverseFactorial[i] * i % MOD);
        }
        int[] weights = new int[size];
        int[] reciprocals = new int[size];
        for (int i = 0; i < n; ++i) {
            long weight = (long) input.nextInt() * inverseFactorial[i] % MOD;
            weight = weight * inverseFactorial[n - 1 - i] % MOD;
            if (((n - 1 - i) & 1) != 0 && weight != 0) {
                weight = MOD - weight;
            }
            weights[i] = (int) weight;
        }
        for (int i = 1; i < total; ++i) {
            reciprocals[i] = (int) ((long) factorial[i - 1] * inverseFactorial[i] % MOD);
        }
        // Lagrange denominators become a convolution on consecutive evaluation points.
        transform(weights, false);
        transform(reciprocals, false);
        for (int i = 0; i < size; ++i) {
            weights[i] = (int) ((long) weights[i] * reciprocals[i] % MOD);
        }
        transform(weights, true);
        BufferedOutputStream output = new BufferedOutputStream(System.out, BUFFER_SIZE);
        byte[] digits = new byte[Integer.toString(MOD).length()];
        for (int i = n; i < total; ++i) {
            long value = (long) weights[i] * factorial[i] % MOD;
            int answer = (int) (value * inverseFactorial[i - n] % MOD);
            int end = digits.length;
            do {
                digits[--end] = (byte) ('0' + answer % 10);
                answer /= 10;
            } while (answer != 0);
            output.write(digits, end, digits.length - end);
            output.write(i + 1 == total ? '\n' : ' ');
        }
        output.flush();
    }
}
