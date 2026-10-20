import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int FIRST_ODD_PRIME = 3;
    private static final int INPUT_BUFFER_SIZE = 65536;
    private static final int OUTPUT_WIDTH = 9;

    private static final class FastInput {
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[INPUT_BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = stream.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int character;
            do {
                character = read();
            } while (character <= ' ' && character != -1);
            int value = 0;
            while (character >= '0' && character <= '9') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }

    private static char[] smallestFactors(int limit) {
        char[] factors = new char[(limit + 1) / 2];
        for (int prime = FIRST_ODD_PRIME; prime <= limit / prime; prime += 2) {
            if (factors[prime / 2] != 0) {
                continue;
            }
            for (int value = prime * prime; value <= limit; value += 2 * prime) {
                if (factors[value / 2] == 0) {
                    factors[value / 2] = (char) prime;
                }
            }
        }
        return factors;
    }

    private static int largestFactor(int value, char[] factors) {
        if (value % 2 == 0) {
            value /= value & -value;
            if (value == 1) {
                return 2;
            }
        }
        while (factors[value / 2] != 0) {
            value /= factors[value / 2];
        }
        return value;
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt();
        int[] queries = new int[2 * count];
        int limit = 1;
        for (int i = 0; i < queries.length; i++) {
            queries[i] = input.nextInt();
            limit = Math.max(limit, queries[i]);
        }
        char[] factors = smallestFactors(limit);
        // Answers are written as bytes by hand; printing a huge StringBuilder is slow.
        byte[] output = new byte[count * OUTPUT_WIDTH];
        byte[] digits = new byte[OUTPUT_WIDTH];
        int size = 0;
        for (int i = 0; i < queries.length; i += 2) {
            int a = queries[i];
            int b = queries[i + 1];
            int common = gcd(a, b);
            if (common != 1 && a != b) {
                // Shared factors survive exactly when they are at least this threshold.
                int threshold = Math.max(
                        largestFactor(a / common, factors), largestFactor(b / common, factors));
                if (threshold > 2) {
                    common /= common & -common;
                }
                while (common > 1) {
                    int prime = common % 2 == 0 ? 2 : factors[common / 2];
                    if (prime == 0) {
                        prime = common;
                    }
                    if (prime >= threshold) {
                        break;
                    }
                    common /= prime;
                }
            }
            int length = 0;
            do {
                digits[length++] = (byte) ('0' + common % 10);
                common /= 10;
            } while (common > 0);
            while (length > 0) {
                output[size++] = digits[--length];
            }
            output[size++] = '\n';
        }
        System.out.write(output, 0, size);
        System.out.flush();
    }
}
