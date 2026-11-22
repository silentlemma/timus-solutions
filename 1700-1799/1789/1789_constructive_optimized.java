public class Main {
    static final int BUFFER_SIZE = 256, MAX_INTEGER_BYTES = 12, DECIMAL = 10;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available, used;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
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
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = DECIMAL * value + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    static void flush() {
        System.out.write(buffer, 0, used);
        used = 0;
    }

    static void write(int c) {
        if (used == buffer.length)
            flush();
        buffer[used++] = (byte)c;
    }

    static void number(int value) {
        if (used + MAX_INTEGER_BYTES > buffer.length)
            flush();
        long magnitude = value;
        if (magnitude < 0) {
            buffer[used++] = '-';
            magnitude = -magnitude;
        }
        int first = used;
        do {
            buffer[used++] = (byte)('0' + magnitude % DECIMAL);
            magnitude /= DECIMAL;
        } while (magnitude != 0);
        for (int left = first, right = used - 1; left < right; left++, right--) {
            byte temporary = buffer[left];
            buffer[left] = buffer[right];
            buffer[right] = temporary;
        }
    }

    static void finish() { flush(); }

    public static void main(String[] args) throws java.io.IOException {
        int size = nextInt();
        number(size == 2 ? 2 : 2 * (size - 2));
        write('\n');
        if (size == 2) {
            number(1);
            write(' ');
            number(1);
        } else {
            boolean first = true;
            for (int cell = 2; cell < size; cell++) {
                if (!first)
                    write(' ');
                number(cell);
                first = false;
            }
            for (int cell = size - 1; cell >= 2; cell--) {
                write(' ');
                number(cell);
            }
        }
        write('\n');
        finish();
    }
}
