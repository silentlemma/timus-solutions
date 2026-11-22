public class Main {
    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = read();
        }
        return value;
    }

    static final int MAX_BITS = 17;
    static final int[] fibonacci = new int[MAX_BITS + 2];
    static {
        fibonacci[1] = 1;
        for (int i = 2; i < fibonacci.length; i++)
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }
    static int maximum(int n) {
        int a = 0, b = 1, answer = 0;
        for (int remaining = Integer.SIZE - 1 - Integer.numberOfLeadingZeros(n); remaining >= 0;
             remaining--) {
            if (((n >> remaining) & 1) != 0) {
                // The smaller binary prefix permits all remaining bits, so Fibonacci bounds apply.
                int bound = remaining == 0
                                ? a
                                : fibonacci[remaining + 1] * (a + b) + fibonacci[remaining] * a;
                answer = Math.max(answer, bound);
                a += b;
            } else
                b += a;
        }
        return Math.max(answer, a);
    }
    public static void main(String[] args) throws java.io.IOException {
        for (int n; (n = (int)nextLong()) != 0;) {
            number(maximum(n));
            writeByte('\n');
        }
        finishOutput();
    }

    static final int OUTPUT_SIZE = 4096, OUTPUT_DIGITS = 20;
    static final byte[] output = new byte[OUTPUT_SIZE], digits = new byte[OUTPUT_DIGITS];
    static int used;
    static void writeByte(int value) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)value;
    }
    static void number(long value) {
        int size = 0;
        do {
            digits[size++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        while (size > 0)
            writeByte(digits[--size]);
    }
    static void finishOutput() {
        System.out.write(output, 0, used);
        used = 0;
    }
}
