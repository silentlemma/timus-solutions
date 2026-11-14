import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int FIRST_ODD_PRIME = 3;
    private static final int LIMIT = 1 << 16;
    private static final int MAX_FACTORS = 6;
    private static final int DECIMAL = 10;
    private static final int BYTE_MASK = 255;

    private static int number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * DECIMAL + ch - '0';
            ch = input.read();
        }
        return value;
    }

    private static long power(long base, int exponent, int modulus) {
        long result = 1;
        while (exponent != 0) {
            if ((exponent & 1) != 0) {
                result = result * base % modulus;
            }
            base = base * base % modulus;
            exponent >>= 1;
        }
        return result;
    }

    private static char largestRoot(int prime, byte[] factors, int[] powers) {
        int order = prime - 1;
        int odd = order >> Integer.numberOfTrailingZeros(order);
        int count = 1;
        powers[0] = order / 2;
        while (odd > 1) {
            int stored = factors[odd / 2] & BYTE_MASK;
            int factor = stored == 0 ? odd : stored;
            powers[count++] = order / factor;
            do {
                odd /= factor;
            } while (odd % factor == 0);
        }
        for (int root = order; root >= 2; root--) {
            int i = 0;
            while (i < count && power(root, powers[i], prime) != 1) {
                i++;
            }
            if (i == count) {
                return (char)root;
            }
        }
        throw new IllegalArgumentException("Expected a prime modulus");
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = number(input);
        byte[] factors = new byte[LIMIT / 2];
        for (int p = FIRST_ODD_PRIME; p * p < LIMIT; p += 2) {
            if (factors[p / 2] == 0) {
                for (int i = p * p / 2; i < factors.length; i += p) {
                    if (factors[i] == 0) {
                        factors[i] = (byte)p;
                    }
                }
            }
        }
        char[] roots = new char[LIMIT / 2];
        int[] powers = new int[MAX_FACTORS];
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < count; i++) {
            int prime = number(input);
            int slot = prime / 2;
            if (roots[slot] == 0) {
                roots[slot] = largestRoot(prime, factors, powers);
            }
            output.append((int)roots[slot]).append('\n');
        }
        System.out.print(output);
    }
}
