import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 65536;

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position >= length) {
                length = input.read(buffer);
                position = 0;
                if (length <= 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int value = read();
            while (value <= ' ' && value != -1) {
                value = read();
            }
            int result = 0;
            while (value >= '0' && value <= '9') {
                result = result * 10 + value - '0';
                value = read();
            }
            return result;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int rows = input.nextInt();
        int width = input.nextInt();
        int height = input.nextInt();
        int santaWidth = input.nextInt();
        int[] leftIndex = new int[rows];
        int[] leftValue = new int[rows];
        int[] rightIndex = new int[rows];
        int[] rightValue = new int[rows];
        int leftHead = 0;
        int leftTail = 0;
        int rightHead = 0;
        int rightTail = 0;
        int best = 0;

        for (int index = 0; index < rows; index++) {
            int currentLeft = input.nextInt();
            int currentRight = input.nextInt();
            int first = index - height;
            while (leftHead < leftTail && leftIndex[leftHead] < first) {
                leftHead++;
            }
            while (rightHead < rightTail && rightIndex[rightHead] < first) {
                rightHead++;
            }
            while (leftHead < leftTail && leftValue[leftTail - 1] <= currentLeft) {
                leftTail--;
            }
            while (rightHead < rightTail && rightValue[rightTail - 1] <= currentRight) {
                rightTail--;
            }
            leftIndex[leftTail] = index;
            leftValue[leftTail++] = currentLeft;
            rightIndex[rightTail] = index;
            rightValue[rightTail++] = currentRight;
            best = Math.max(best, leftValue[leftHead] + rightValue[rightHead]);
        }

        System.out.print(Math.max(0, width - santaWidth + 1 - best) + "\n");
    }
}
