import java.io.BufferedOutputStream;
import java.io.IOException;

public class Main {
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the readings are parsed by hand from a small buffer; the closing -1 is told
    // by its minus sign, and -1 is returned for it
    static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0)
                return -1;
        }
        return buffer[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        if (c < 0 || c == '-')
            return -1;
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int width = nextInt();
        // indices of the window whose values decrease from front to back: the
        // front is the maximum, and a value never matters once a later one is larger
        int[] values = new int[width], indices = new int[width];
        // the window never holds more than width readings: a ring buffer from head
        int head = 0, size = 0;
        BufferedOutputStream out = new BufferedOutputStream(System.out, BUFFER_SIZE);
        // each maximum is written by hand, digit by digit from the end of a line
        final int NUMBER_CAPACITY = 10;
        byte[] digits = new byte[NUMBER_CAPACITY];
        digits[NUMBER_CAPACITY - 1] = '\n';
        for (int index = 0;; index++) {
            int value = nextInt();
            if (value < 0)
                break;
            if (size > 0 && indices[head] <= index - width) {
                head = (head + 1) % width;
                size--;
            }
            while (size > 0 && values[(head + size - 1) % width] <= value)
                size--;
            int tail = (head + size) % width;
            values[tail] = value;
            indices[tail] = index;
            size++;
            if (index + 1 >= width) {
                int maximum = values[head], start = NUMBER_CAPACITY - 1;
                do {
                    digits[--start] = (byte)('0' + maximum % 10);
                    maximum /= 10;
                } while (maximum > 0);
                out.write(digits, start, NUMBER_CAPACITY - start);
            }
        }
        out.flush();
    }
}
