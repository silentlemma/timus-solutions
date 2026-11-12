import java.io.IOException;

public class Main {
    static final int INPUT_SIZE = 8192, OUTPUT_SIZE = 64, DECIMAL_DIGITS = 9;
    static final long STEP_SCALE = 12, CENTER_SCALE = 6, FIRST_SCALE = 4;
    static final long DECIMAL_SCALE = 1000000000;

    static final class Input {
        final byte[] buffer = new byte[INPUT_SIZE];
        int position, length;
        int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return buffer[position++];
        }
        long number() throws IOException {
            int c = read();
            while (c >= 0 && c <= ' ')
                c = read();
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return sign * value;
        }
    }

    static void fraction(StringBuilder output, long numerator, long denominator) {
        if (numerator < 0) {
            output.append('-');
            numerator = -numerator;
        }
        long whole = numerator / denominator, remainder = numerator % denominator, part = 0;
        for (int i = 0; i < DECIMAL_DIGITS; ++i) {
            remainder *= 10;
            part = part * 10 + remainder / denominator;
            remainder %= denominator;
        }
        if (2 * remainder >= denominator && ++part == DECIMAL_SCALE) {
            part = 0;
            ++whole;
        }
        output.append(whole).append('.');
        for (long power = DECIMAL_SCALE / 10; power != 0; power /= 10)
            output.append((char)('0' + part / power % 10));
    }

    public static void main(String[] args) throws IOException {
        Input in = new Input();
        long n = in.number(), sum = 0, weighted = 0;
        for (long i = 0; i < n; ++i) {
            long value = in.number();
            sum += value;
            weighted += i * value;
        }
        StringBuilder output = new StringBuilder(OUTPUT_SIZE);
        fraction(output, (FIRST_SCALE * n - 2) * sum - CENTER_SCALE * weighted, n * (n + 1));
        output.append(' ');
        fraction(output, STEP_SCALE * weighted - CENTER_SCALE * (n - 1) * sum, n * (n * n - 1));
        output.append('\n');
        System.out.print(output);
    }
}
