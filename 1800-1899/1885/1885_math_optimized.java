public class Main {
    static final int INPUT_SIZE = 1024, OUTPUT_SIZE = 64, BYTE_MASK = 255;
    static final byte[] input = new byte[INPUT_SIZE], output = new byte[OUTPUT_SIZE];
    static int position, available, used;

    static int read() throws java.io.IOException {
        if (position >= available) {
            available = System.in.read(input);
            position = 0;
            if (available <= 0)
                return -1;
        }
        return input[position++] & BYTE_MASK;
    }

    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative || c == '+')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    static void unsigned(long value) {
        int start = used;
        do {
            output[used++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        for (int left = start, right = used - 1; left < right; left++, right--) {
            byte temporary = output[left];
            output[left] = output[right];
            output[right] = temporary;
        }
    }

    static final int FRACTION_DIGITS = 12;

    static void rational(long numerator, long denominator, int delimiter) {
        unsigned(numerator / denominator);
        output[used++] = '.';
        long remainder = numerator % denominator;
        for (int i = 0; i < FRACTION_DIGITS; i++) {
            remainder *= 10;
            output[used++] = (byte)('0' + remainder / denominator);
            remainder %= denominator;
        }
        output[used++] = (byte)delimiter;
    }

    static void answer(long h, long t, long v, long x) {
        rational(Math.max(0, h - t * x), v - x, ' ');
        if (t * x <= h)
            rational(t, 1, '\n');
        else
            rational(h, x, '\n');
    }

    public static void main(String[] args) throws java.io.IOException {
        long h = nextLong(), t = nextLong(), v = nextLong(), x = nextLong();
        answer(h, t, v, x);
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
