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

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        // the sections are not stored: only the two before the current one are kept
        int previous = nextInt();
        int last = nextInt();
        int best = 0;
        int position = 2;
        for (int middle = 2; middle < n; middle++) {
            int value = nextInt();
            int sum = previous + last + value;
            if (sum > best) {
                best = sum;
                position = middle;
            }
            previous = last;
            last = value;
        }

        number(best);
        write(' ');
        number(position);
        write('\n');
        finish();
    }
}
