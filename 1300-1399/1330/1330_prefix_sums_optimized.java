import java.io.IOException;

public class Main {
    static final int BUFFER_SIZE = 4096;
    static final int MAX_DIGITS = 10;
    static final byte[] input = new byte[BUFFER_SIZE];
    static final byte[] output = new byte[BUFFER_SIZE];
    static final byte[] digits = new byte[MAX_DIGITS];
    static int length, position, outputPosition;

    // the input is read in 4 KB blocks and parsed by hand, and the answers go
    // into a 4 KB byte buffer, instead of StreamTokenizer and strings
    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(input);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return input[position++];
    }

    static int next() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    static void writeByte(int c) {
        if (outputPosition == BUFFER_SIZE) {
            System.out.write(output, 0, outputPosition);
            outputPosition = 0;
        }
        output[outputPosition++] = (byte)c;
    }

    static void writeInt(int value) {
        if (value < 0) {
            writeByte('-');
            value = -value;
        }
        int count = 0;
        do {
            digits[count++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        while (count > 0)
            writeByte(digits[--count]);
        writeByte('\n');
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        // before[i] is the sum of the first i readings
        int[] before = new int[n + 1];
        for (int i = 1; i <= n; i++)
            before[i] = before[i - 1] + next();
        for (int q = next(); q > 0; q--) {
            int i = next(), j = next();
            writeInt(before[j] - before[i - 1]);
        }
        System.out.write(output, 0, outputPosition);
    }
}
