public class Main {

    static final int INPUT_SIZE = 256, OUTPUT_SIZE = 128, DIGITS = 20, DECIMAL = 10;
    static final byte[] input = new byte[INPUT_SIZE], output = new byte[OUTPUT_SIZE],
                        digits = new byte[DIGITS];
    static int position, available, used;
    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }
    static void write(int c) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }
    static void number(long value) {
        if (value < 0) {
            write('-');
            value = -value;
        }
        int length = 0;
        do {
            digits[length++] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        while (length > 0)
            write(digits[--length]);
    }
    static void finish() { System.out.write(output, 0, used); }

    static void text(String value) {
        for (int i = 0; i < value.length(); i++)
            write(value.charAt(i));
    }

    static int distance(int pages, int cover, int start, int stop) {
        int whole = pages + 2 * cover;
        if (start < stop)
            return 2 * cover + (stop - start - 1) * whole;
        if (start > stop)
            return 2 * pages + 2 * cover + (start - stop - 1) * whole;
        return pages;
    }
    public static void main(String[] args) throws java.io.IOException {
        number(distance(nextInt(), nextInt(), nextInt(), nextInt()));
        write('\n');
        finish();
    }
}
