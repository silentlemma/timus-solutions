public class Main {
    static final int MAX_DECIMAL_DIGITS = 19;
    static byte[] decimal(long value) {
        byte[] scratch = new byte[MAX_DECIMAL_DIGITS];
        int position = scratch.length;
        do {
            scratch[--position] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        byte[] result = new byte[scratch.length - position];
        System.arraycopy(scratch, position, result, 0, result.length);
        return result;
    }

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

    static final int OUTPUT_SIZE = 16384;
    static boolean first = true;
    static void repeat(long value, long count) throws java.io.IOException {
        if (count == 0)
            return;
        byte[] digits = decimal(value);
        if (first) {
            System.out.write(digits);
            first = false;
            count--;
        }
        int width = digits.length + 1, copies = OUTPUT_SIZE / width;
        byte[] block = new byte[copies * width];
        for (int i = 0; i < copies; i++) {
            block[i * width] = ' ';
            System.arraycopy(digits, 0, block, i * width + 1, digits.length);
        }
        while (count >= copies) {
            System.out.write(block);
            count -= copies;
        }
        System.out.write(block, 0, (int)count * width);
    }
    public static void main(String[] args) throws java.io.IOException {
        long workers = nextLong(), firstDays = nextLong(), days = nextLong();
        long total = workers * firstDays, low = total / days, extra = total % days;
        // Both constant runs reuse blocks rather than issuing one write per day.
        repeat(low, days - extra);
        repeat(low + 1, extra);
        System.out.write('\n');
        System.out.flush();
    }
}
