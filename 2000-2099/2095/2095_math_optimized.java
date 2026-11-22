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
    static final int FIRST = 2;
    static int prefix(int value) {
        int step = FIRST;
        while (value >= step) {
            int quotient = value / step;
            int remainder = value - quotient * step;
            int jumps = remainder / (2 * quotient) + 1;
            value -= quotient * jumps;
            step += jumps;
        }
        return value;
    }
    static int interval(int left, int right) {
        if (left == 1)
            return prefix(right);
        int lower = left - 1, upper = right, step = FIRST;
        while (upper >= step) {
            if (lower == upper)
                return 0;
            int upperQuotient = upper / step;
            int upperRemainder = upper - upperQuotient * step;
            int jumps = upperRemainder / (2 * upperQuotient) + 1;
            int lowerQuotient = lower / step;
            if (lowerQuotient != 0) {
                int lowerRemainder = lower - lowerQuotient * step;
                int lowerJumps = lowerRemainder / (2 * lowerQuotient) + 1;
                if (lowerJumps < jumps)
                    jumps = lowerJumps;
            }
            upper -= upperQuotient * jumps;
            lower -= lowerQuotient * jumps;
            step += jumps;
        }
        return upper - lower;
    }

    public static void main(String[] args) throws Exception {
        int left = nextInt(), right = nextInt(), answer = interval(left, right);
        int at = buffer.length;
        buffer[--at] = '\n';
        do {
            buffer[--at] = (byte)('0' + answer % DECIMAL);
            answer /= DECIMAL;
        } while (answer != 0);
        System.out.write(buffer, at, buffer.length - at);
        System.out.flush();
        Runtime.getRuntime().halt(0);
    }
}
