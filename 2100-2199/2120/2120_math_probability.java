import java.io.IOException;

public class Main {
    private static final int BUFFER_SIZE = 65536;
    private static final int BYTE_MASK = 255;
    private static final int UNKNOWN = -1;
    private static final int END_OF_INPUT = -1;

    private static final class FastInput {
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0) {
                    return END_OF_INPUT;
                }
            }
            return buffer[position++] & BYTE_MASK;
        }

        int nextInt() throws IOException {
            int current = read();
            while (current <= ' ' && current != END_OF_INPUT) {
                current = read();
            }
            boolean negative = current == '-';
            if (negative) {
                current = read();
            }
            int value = 0;
            while (current >= '0' && current <= '9') {
                value = value * 10 + current - '0';
                current = read();
            }
            return negative ? -value : value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        long unknownCount = 0;
        long unknownLabels = 0;
        long knownOccurrences = 0;
        long knownWeight = 0;
        for (int label = 1; label <= n; ++label) {
            int degree = input.nextInt();
            if (degree == UNKNOWN) {
                ++unknownCount;
                unknownLabels += label;
            } else {
                long occurrences = degree - 1L;
                knownOccurrences += occurrences;
                knownWeight += label * occurrences;
            }
        }
        long answer = (long) n * (n + 1) / 2 + n * knownWeight;
        if (unknownCount > 0) {
            long remaining = n - 2L - knownOccurrences;
            long multiplier = n * remaining;
            // Divide the label sum first to keep every product in signed 64 bits.
            answer += multiplier * (unknownLabels / unknownCount);
            answer += multiplier * (unknownLabels % unknownCount) / unknownCount;
        }
        System.out.println(answer);
    }
}
