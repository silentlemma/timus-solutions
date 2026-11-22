public class Main {

    static final int INPUT_SIZE = 1024, OUTPUT_SIZE = 1024, DIGITS = 10, DECIMAL = 10;
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
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return value;
    }
    static void write(int c) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }
    static void number(int value) {
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

    static int element(int index, int zeros) {
        int tail = index - zeros + 1;
        if (tail <= 0)
            return 0;
        return (tail & 1) != 0 ? (tail + 1) / 2 : -tail / 2;
    }
    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), k = nextInt(), zeros = n - k + 1;
        for (int i = 0; i < n; i++) {
            if (i != 0)
                write(' ');
            number(element(i, zeros));
        }
        write('\n');
        finish();
    }
}
