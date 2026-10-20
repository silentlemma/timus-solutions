import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final long MAX_ANSWER = 1000000000000L;
    private static final int BUFFER_SIZE = 65536;

    private static final class FastInput {
        private final InputStream source = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = source.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int current = read();
            while (current <= ' ' && current != -1) {
                current = read();
            }
            int value = 0;
            while (current >= '0' && current <= '9') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        long[] negative = new long[n];
        int negativeCount = 0;
        long answer = 1;
        boolean possible = true;
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < n; i++) {
            long divisor = input.nextInt();
            int affirmative = input.nextInt();
            if (possible) {
                if (affirmative == 0) {
                    if (answer % divisor == 0) {
                        possible = false;
                    } else {
                        negative[negativeCount++] = divisor;
                    }
                } else {
                    long factor = divisor / gcd(answer, divisor);
                    if (answer > MAX_ANSWER / factor) {
                        possible = false;
                    } else if (factor != 1) {
                        answer *= factor;
                        // Every change at least doubles the least common multiple.
                        for (int j = 0; j < negativeCount; j++) {
                            if (answer % negative[j] == 0) {
                                possible = false;
                                break;
                            }
                        }
                    }
                }
            }
            output.append(possible ? answer : -1).append('\n');
        }
        System.out.print(output);
    }
}
