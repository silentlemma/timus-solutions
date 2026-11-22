public class Main {

    // these inputs contain only nonnegative integers; avoid scanner's regex machinery.
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    static final int OUTPUT_SIZE = 4096, DECIMAL_DIGITS = 10;
    static final byte[] output = new byte[OUTPUT_SIZE], digits = new byte[DECIMAL_DIGITS];
    static int used;

    static void emit(int c) throws java.io.IOException {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }

    static void number(int value) throws java.io.IOException {
        int size = 0;
        do {
            digits[size++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value > 0);
        while (size > 0)
            emit(digits[--size]);
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        // The same ascending construction is emitted without a full text builder.
        for (int i = 1; i <= n; i++) {
            number(i);
            emit(i < n ? ' ' : '\n');
        }
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
