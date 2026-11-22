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
    static final int OUTPUT_CAPACITY = 384;
    static int put(byte[] out, int at, int value) {
        int first = at;
        do {
            out[at++] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        for (int left = first, right = at - 1; left < right; left++, right--) {
            byte saved = out[left];
            out[left] = out[right];
            out[right] = saved;
        }
        return at;
    }
    public static void main(String[] args) throws Exception {
        int n = nextInt(), count = Integer.SIZE - Integer.numberOfLeadingZeros(n - 1);
        byte[] out = new byte[OUTPUT_CAPACITY];
        int at = put(out, 0, count);
        out[at++] = '\n';
        for (int i = 0; i < count; i++) {
            if (i > 0)
                out[at++] = ' ';
            at = put(out, at, n / 2);
            n -= n / 2;
        }
        out[at++] = '\n';
        System.out.write(out, 0, at);
        System.out.flush();
        System.exit(0);
    }
}
