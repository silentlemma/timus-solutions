public class Main {

    static final int OUTPUT_SIZE = 128, DIGITS = 10, DECIMAL = 10;
    static final byte[] output = new byte[OUTPUT_SIZE], digits = new byte[DIGITS];
    static int used;

    static void write(int c) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }

    static void number(int value) {
        int length = 0;
        do {
            digits[length++] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        while (length > 0)
            write(digits[--length]);
    }

    static void finish() { System.out.write(output, 0, used); }

    static final int INPUT_SIZE = 128;
    static final byte[] input = new byte[INPUT_SIZE];
    static int position, available;

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

    static long solve(long count, long groups) {
        long small = count / groups, larger = count % groups;
        long squares = (groups - larger) * small * small + larger * (small + 1) * (small + 1);
        return (count * count - squares) / 2;
    }

    public static void main(String[] args) throws java.io.IOException {
        int tests = nextInt();
        while (tests-- > 0) {
            number((int)solve(nextInt(), nextInt()));
            write('\n');
        }
        finish();
    }
}
