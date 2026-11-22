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

    static final long HUNDREDTHS = 100, WHOLE = 100 * HUNDREDTHS;
    static long percentage() throws java.io.IOException {
        int ch = read();
        while (ch <= ' ')
            ch = read();
        long value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = read();
        }
        value *= HUNDREDTHS;
        if (ch == '.') {
            long scale = HUNDREDTHS;
            for (ch = read(); ch >= '0' && ch <= '9'; ch = read()) {
                scale /= 10;
                value += (ch - '0') * scale;
            }
        }
        return value;
    }

    static long population(long p, long q) {
        long a = 0, b = 1, c = 1, d = 0;
        while (true) {
            long numerator = a + c, denominator = b + d;
            if (WHOLE * numerator <= p * denominator) {
                // Maximal consecutive mediants outside the strict lower bound.
                long steps = (p * b - WHOLE * a) / (WHOLE * c - p * d);
                a += steps * c;
                b += steps * d;
            } else if (WHOLE * numerator >= q * denominator) {
                long steps = (WHOLE * c - q * d) / (q * b - WHOLE * a);
                c += steps * a;
                d += steps * b;
            } else {
                return denominator;
            }
        }
    }

    public static void main(String[] args) throws java.io.IOException {
        number(population(percentage(), percentage()));
        write('\n');
        finish();
    }
}
