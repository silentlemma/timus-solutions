import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 65536;
    private static final int OUTPUT_WIDTH = 16;

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int length;
        private int position;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
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
            } while (character <= ' ');
            boolean negative = character == '-';
            if (negative) {
                character = read();
            }
            int value = 0;
            while (character >= '0' && character <= '9') {
                value = value * 10 + character - '0';
                character = read();
            }
            return negative ? -value : value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int stepCount = input.nextInt();
        int queryCount = input.nextInt();
        int[] steps = new int[stepCount];
        for (int i = 0; i < stepCount; i++) {
            steps[i] = input.nextInt();
        }
        int[] queries = new int[queryCount];
        int maximum = 0;
        for (int i = 0; i < queryCount; i++) {
            int value = input.nextInt();
            queries[i] = value;
            maximum = Math.max(maximum, value < 0 ? -value - 1 : value);
        }

        int capacity = Math.min(stepCount, maximum);
        int[] blockLeft = new int[capacity];
        int[] blockRight = new int[capacity];
        int[] blockCenter = new int[capacity];
        int blockCount = 0;
        int left = 0;
        int right = maximum;
        long offset = 0;
        for (int step : steps) {
            offset += left + offset < 0 ? step : -(long) step;
            if (left + offset < 0 && right + offset >= 0) {
                int split = (int) -offset;
                int negatives = split - left;
                int positives = right - split + 1;
                blockCenter[blockCount] = 2 * split - 1;
                // Mirror the smaller side into the side kept for later steps.
                if (negatives <= positives) {
                    blockLeft[blockCount] = left;
                    blockRight[blockCount] = split;
                    left = split;
                } else {
                    blockLeft[blockCount] = split;
                    blockRight[blockCount] = right + 1;
                    right = split - 1;
                }
                blockCount++;
            }
        }

        long[] answers = new long[maximum + 1];
        for (int i = left; i <= right; i++) {
            answers[i] = i + offset;
        }
        while (blockCount > 0) {
            blockCount--;
            int center = blockCenter[blockCount];
            for (int i = blockLeft[blockCount]; i < blockRight[blockCount]; i++) {
                answers[i] = -answers[center - i] - 1;
            }
        }

        // Digits are written by hand, since printing a huge StringBuilder is slow.
        byte[] output = new byte[queryCount * OUTPUT_WIDTH];
        byte[] digits = new byte[OUTPUT_WIDTH];
        int size = 0;
        for (int value : queries) {
            long answer = value < 0 ? -answers[-value - 1] - 1 : answers[value];
            if (answer < 0) {
                output[size++] = '-';
                answer = -answer;
            }
            int count = 0;
            do {
                digits[count++] = (byte) ('0' + answer % 10);
                answer /= 10;
            } while (answer > 0);
            while (count > 0) {
                output[size++] = digits[--count];
            }
            output[size++] = '\n';
        }
        System.out.write(output, 0, size);
        System.out.flush();
    }
}
