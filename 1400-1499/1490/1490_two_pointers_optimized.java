public class Main {
    static final int MAX_DECIMAL_DIGITS = 19;
    static void emit(long value) throws java.io.IOException {
        byte[] bytes = new byte[MAX_DECIMAL_DIGITS + 1];
        int position = bytes.length - 1;
        bytes[position] = '\n';
        do {
            bytes[--position] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        System.out.write(bytes, position, bytes.length - position);
        System.out.flush();
    }

    static final int BUFFER_SIZE = 1024, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position >= available) {
            available = System.in.read(buffer);
            position = 0;
            if (available <= 0)
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
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static final long QUARTERS = 4;

    public static void main(String[] args) throws java.io.IOException {

        long r = nextLong();
        long y = r, total = 0, radiusSquared = r * r;
        // In column x, exactly y nearest corners lie strictly inside the disc.
        // The boundary moves down at most r times over the whole scan.
        for (long x = 0; x < r; x++) {
            while (y > 0 && x * x + (y - 1) * (y - 1) >= radiusSquared)
                y--;
            total += y;
        }
        emit(QUARTERS * total);
    }
}
