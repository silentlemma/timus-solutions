public class Main {
    static final int MAX_COORD = 100, SPAN = 2 * MAX_COORD + 1;
    static final int WORD_BITS = Long.SIZE, WORDS = (SPAN + WORD_BITS - 1) / WORD_BITS;
    static final int BUFFER_SIZE = 1024, DECIMAL = 10;
    static final byte[] input = new byte[BUFFER_SIZE];
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
        int sign = 1;
        if (c == '-' || c == '+') {
            if (c == '-')
                sign = -1;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return sign * value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), left = 0, right = 0, lower = 0, upper = 0;
        long[] points = new long[SPAN * WORDS];
        for (int i = 0; i < n; i++) {
            int x = nextInt(), y = nextInt(), column = x + MAX_COORD;
            left = Math.min(left, x);
            right = Math.max(right, x);
            lower = Math.min(lower, y);
            upper = Math.max(upper, y);
            points[(y + MAX_COORD) * WORDS + column / WORD_BITS] |= 1L << (column % WORD_BITS);
        }
        int width = right - left + 1, used = 0;
        byte[] output = new byte[(upper - lower + 1) * (width + 1)];
        for (int y = upper; y >= lower; y--) {
            int begin = used;
            byte background = (byte)(y == 0 ? '-' : '.');
            for (int x = 0; x < width; x++)
                output[used++] = background;
            output[begin - left] = (byte)(y == 0 ? '+' : '|');
            for (int word = 0; word < WORDS; word++) {
                long bits = points[(y + MAX_COORD) * WORDS + word];
                while (bits != 0) {
                    int x = word * WORD_BITS + Long.numberOfTrailingZeros(bits) - MAX_COORD;
                    output[begin + x - left] = '*';
                    bits &= bits - 1;
                }
            }
            output[used++] = '\n';
        }
        System.out.write(output);
    }
}
