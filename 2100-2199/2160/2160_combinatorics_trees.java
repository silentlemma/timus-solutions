import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final long MOD = 1_000_000_007L;
    private static final int SPACE = ' ';
    private static final int ZERO = '0';

    private static final class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int current;
            do {
                current = input.read();
            } while (current <= SPACE && current != -1);
            int value = 0;
            while (current > SPACE) {
                value = value * 10 + current - ZERO;
                current = input.read();
            }
            return value;
        }
    }

    private static long power(long base, long exponent) {
        long result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exponent /= 2;
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int[] values = new int[n];
        int[] sizes = new int[n];
        int height = 0;
        long factorial = 1;
        long denominator = 1;

        for (int i = 1; i <= n; ++i) {
            int value = input.nextInt();
            factorial = factorial * i % MOD;
            int total = 0;
            // Each popped node is complete once its right subtree has been added.
            while (height > 0 && values[height - 1] > value) {
                --height;
                total += sizes[height];
                denominator = denominator * total % MOD;
            }
            values[height] = value;
            sizes[height] = total + 1;
            ++height;
        }

        int total = 0;
        while (height > 0) {
            total += sizes[--height];
            denominator = denominator * total % MOD;
        }

        System.out.println(factorial * power(denominator, MOD - 2) % MOD);
    }
}
