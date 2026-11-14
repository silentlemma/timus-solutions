import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int MAX_DIGIT = 9;

    private static int readInt(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    private static int firstCheapest(BufferedInputStream input, int count, int width)
        throws IOException {
        if (width > count) {
            return 0;
        }
        byte[] window = new byte[width];
        int slot = 0, length = 0, sum = 0;
        int best = 0, minimum = MAX_DIGIT * width + 1;
        for (int position = 1; position <= count;) {
            int c = input.read();
            if (c == -1) {
                break;
            }
            if (c == '*') {
                slot = length = sum = 0;
            } else if (c >= '0' && c <= '9') {
                if (length == width) {
                    sum -= window[slot];
                } else {
                    length++;
                }
                int digit = c - '0';
                window[slot++] = (byte)digit;
                sum += digit;
                if (slot == width) {
                    slot = 0;
                }
                if (length == width && sum < minimum) {
                    best = position - width + 1;
                    minimum = sum;
                    if (sum == 0) {
                        return best;
                    }
                }
            } else {
                continue;
            }
            position++;
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = readInt(input);
        int width = readInt(input);
        System.out.println(firstCheapest(input, count, width));
    }
}
