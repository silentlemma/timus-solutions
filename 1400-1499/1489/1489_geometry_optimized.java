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

    static long nextHundredths() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative || c == '+')
            c = read();
        long value = 0;
        int fraction = -1;
        while (c > ' ') {
            if (c == '.')
                fraction = 0;
            else {
                value = 10 * value + c - '0';
                if (fraction >= 0)
                    fraction++;
            }
            c = read();
        }
        if (fraction < 0)
            fraction = 0;
        while (fraction++ < 2)
            value *= 10;
        return negative ? -value : value;
    }

    static void fixed(long units, long scale, int delimiter) {
        unsigned(units / scale);
        output[used++] = '.';
        long fraction = units % scale;
        for (long divisor = scale / 10; divisor != 0; divisor /= 10) {
            output[used++] = (byte)('0' + fraction / divisor);
            fraction %= divisor;
        }
        output[used++] = (byte)delimiter;
    }
    static long[] fold(long a, long b, long c, long x, long y) {
        if (x < c)
            return new long[] {0, y - b - c, c - x};
        if (x > c + a)
            return new long[] {a, y - b - c, x - c - a};
        if (y < b)
            return new long[] {x - c, b - y, c};
        if (y < b + c)
            return new long[] {x - c, 0, b + c - y};
        if (y <= 2 * b + c)
            return new long[] {x - c, y - b - c, 0};
        return new long[] {x - c, b, y - 2 * b - c};
    }

    static final long COORDINATE_SCALE = 100, FRACTION_SCALE = 1000000000000L;

    static void distance(long squared) {
        long units = Math.round(Math.sqrt(squared) / COORDINATE_SCALE * FRACTION_SCALE);
        fixed(units, FRACTION_SCALE, '\n');
    }

    public static void main(String[] args) throws java.io.IOException {
        long a = nextLong() * COORDINATE_SCALE;
        long b = nextLong() * COORDINATE_SCALE;
        long c = nextLong() * COORDINATE_SCALE;
        long[] p = fold(a, b, c, nextHundredths(), nextHundredths());
        long[] q = fold(a, b, c, nextHundredths(), nextHundredths());
        long squared = 0;
        for (int i = 0; i < p.length; i++)
            squared += (p[i] - q[i]) * (p[i] - q[i]);
        distance(squared);
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
