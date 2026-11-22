public class Main {
    static final int INPUT_CAPACITY = 64, DECIMAL = 10;
    static final byte[] buffer = new byte[INPUT_CAPACITY];
    static int position, available;
    static int read() throws java.io.IOException {
        if (position == available) {
            do {
                available = System.in.read(buffer);
            } while (available == 0);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative || c == '+')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }
    static final int OUTPUT_CAPACITY = 32;
    public static void main(String[] args) throws Exception {
        int x = nextInt(), y = nextInt();
        if (x > 0 && y > 0 && ((x ^ y) & 1) != 0) {
            int swap = x;
            x = y;
            y = swap;
        }
        byte[] out = new byte[OUTPUT_CAPACITY];
        int at = out.length;
        out[--at] = '\n';
        for (int i = 1; i >= 0; i--) {
            int value = i == 1 ? y : x;
            boolean negative = value < 0;
            if (negative)
                value = -value;
            do {
                out[--at] = (byte)('0' + value % DECIMAL);
                value /= DECIMAL;
            } while (value != 0);
            if (negative)
                out[--at] = '-';
            if (i == 1)
                out[--at] = ' ';
        }
        System.out.write(out, at, out.length - at);
        System.out.flush();
        System.exit(0);
    }
}
