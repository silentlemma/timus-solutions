import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL_DIGITS = 10;
    private static final int BUFFER_SIZE = 1 << 15;
    private static final byte[] YES = {'Y', 'E', 'S', '\n'};

    private static int number(BufferedInputStream input) throws IOException {
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

    private static void writeNumber(BufferedOutputStream output, byte[] digits, int value)
        throws IOException {
        int first = digits.length;
        do {
            digits[--first] = (byte)('0' + value % 10);
            value /= 10;
        } while (value > 0);
        output.write(digits, first, digits.length - first);
    }

    private static void writeGroup(BufferedOutputStream output, boolean[] falls, boolean group,
                                   int count) throws IOException {
        byte[] digits = new byte[DECIMAL_DIGITS];
        writeNumber(output, digits, count);
        output.write('\n');
        boolean separator = false;
        for (int edge = 0; edge < falls.length; edge++) {
            if (falls[edge] == group) {
                if (separator) {
                    output.write(' ');
                }
                writeNumber(output, digits, edge + 1);
                separator = true;
            }
        }
        output.write('\n');
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in, BUFFER_SIZE);
        BufferedOutputStream output = new BufferedOutputStream(System.out, BUFFER_SIZE);
        int n = number(input), first = number(input), previous = first, count = 0;
        boolean[] falls = new boolean[n];
        // The signed differences cancel. Record only whether each edge falls.
        for (int edge = 0; edge < n; edge++) {
            int current = edge + 1 < n ? number(input) : first;
            if (previous > current) {
                falls[edge] = true;
                count++;
            }
            previous = current;
        }
        if (count == 0) {
            falls[0] = true;
            count = 1;
        }
        output.write(YES);
        writeGroup(output, falls, true, count);
        writeGroup(output, falls, false, n - count);
        output.flush();
    }
}
