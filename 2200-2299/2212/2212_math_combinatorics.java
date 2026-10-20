import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final long MOD = 998244353;
    private static final long ROOT = 3;

    private static long power(long base, long exponent) {
        long result = 1;
        while (exponent > 0) {
            if ((exponent & 1) != 0) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exponent >>= 1;
        }
        return result;
    }

    private static void transform(long[] a, boolean inverse) {
        int size = a.length;
        for (int i = 1, j = 0; i < size; ++i) {
            int bit = size >> 1;
            while ((j & bit) != 0) {
                j ^= bit;
                bit >>= 1;
            }
            j ^= bit;
            if (i < j) {
                long temporary = a[i];
                a[i] = a[j];
                a[j] = temporary;
            }
        }
        for (int length = 2; length <= size; length <<= 1) {
            long step = power(ROOT, (MOD - 1) / length);
            if (inverse) {
                step = power(step, MOD - 2);
            }
            int half = length / 2;
            for (int start = 0; start < size; start += length) {
                long weight = 1;
                for (int j = 0; j < half; ++j) {
                    long left = a[start + j];
                    long right = weight * a[start + j + half] % MOD;
                    long sum = left + right;
                    long difference = left - right;
                    if (sum >= MOD) {
                        sum -= MOD;
                    }
                    if (difference < 0) {
                        difference += MOD;
                    }
                    a[start + j] = sum;
                    a[start + j + half] = difference;
                    weight = weight * step % MOD;
                }
            }
        }
        if (inverse) {
            long scale = power(size, MOD - 2);
            for (int i = 0; i < size; ++i) {
                a[i] = a[i] * scale % MOD;
            }
        }
    }

    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static int nextInt() throws IOException {
        int digit;
        do {
            digit = INPUT.read();
        } while (digit <= ' ' && digit != -1);
        int value = 0;
        while (digit >= '0' && digit <= '9') {
            value = value * 10 + digit - '0';
            digit = INPUT.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt();
        int days = nextInt();
        int size = 1;
        while (size < 2 * n - 1) {
            size <<= 1;
        }
        long[] values = new long[size];
        long[] kernel = new long[size];
        long[] inverses = new long[n];
        for (int i = 0; i < n; ++i) {
            values[i] = nextInt();
        }
        inverses[1] = 1;
        kernel[0] = 1;
        // Repeated prefix sums have coefficients C(days + i - 1, i).
        for (int i = 1; i < n; ++i) {
            if (i > 1) {
                inverses[i] = MOD - (MOD / i) * inverses[(int) (MOD % i)] % MOD;
            }
            kernel[i] = kernel[i - 1] * (days + i - 1) % MOD * inverses[i] % MOD;
        }
        transform(values, false);
        transform(kernel, false);
        for (int i = 0; i < size; ++i) {
            values[i] = values[i] * kernel[i] % MOD;
        }
        transform(values, true);
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < n; ++i) {
            if (i > 0) {
                answer.append(' ');
            }
            answer.append(values[i]);
        }
        System.out.println(answer);
    }
}
