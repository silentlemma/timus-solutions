public class Main {
    private static final int WORD_BITS = 32;
    private static final long UNSIGNED_INT_MASK = 0xffffffffL;

    private static final class FastInput {
        private static final int BUFFER_SIZE = 1024;
        private final java.io.InputStream input;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position, length;
        private String cached;

        FastInput(java.io.InputStream input) { this.input = input; }

        private int read() {
            if (position == length) {
                try {
                    do {
                        length = input.read(buffer);
                    } while (length == 0);
                } catch (java.io.IOException failure) {
                    throw new IllegalStateException(failure);
                }
                position = 0;
                if (length < 0) {
                    length = 0;
                    return -1;
                }
            }
            return buffer[position++] & 255;
        }

        private String token() {
            int character = read();
            while (character >= 0 && character <= ' ') {
                character = read();
            }
            if (character < 0) {
                return null;
            }
            byte[] bytes = new byte[WORD_BITS];
            int size = 0;
            while (character > ' ') {
                if (size == bytes.length) {
                    bytes = java.util.Arrays.copyOf(bytes, 2 * bytes.length);
                }
                bytes[size++] = (byte)character;
                character = read();
            }
            return new String(bytes, 0, size, java.nio.charset.StandardCharsets.UTF_8);
        }

        String line() {
            int character = read();
            if (character < 0)
                return null;
            byte[] bytes = new byte[64];
            int size = 0;
            while (character >= 0 && character != '\n') {
                if (size == bytes.length)
                    bytes = java.util.Arrays.copyOf(bytes, size * 2);
                bytes[size++] = (byte)character;
                character = read();
            }
            if (size > 0 && bytes[size - 1] == '\r')
                size--;
            return new String(bytes, 0, size, java.nio.charset.StandardCharsets.UTF_8);
        }

        boolean hasNext() {
            if (cached == null) {
                cached = token();
            }
            return cached != null;
        }

        boolean hasNextLong() {
            if (!hasNext()) {
                return false;
            }
            try {
                Long.parseLong(cached);
                return true;
            } catch (NumberFormatException invalid) {
                return false;
            }
        }

        String next() {
            String value;
            if (cached == null) {
                value = token();
            } else {
                value = cached;
                cached = null;
            }
            if (value == null) {
                throw new java.util.NoSuchElementException();
            }
            return value;
        }

        long nextLong() {
            if (cached != null) {
                return Long.parseLong(next());
            }
            int character = read();
            while (character >= 0 && character <= ' ') {
                character = read();
            }
            if (character < 0) {
                throw new java.util.NoSuchElementException();
            }
            boolean negative = character == '-';
            if (negative || character == '+') {
                character = read();
            }
            long value = 0;
            while (character >= '0' && character <= '9') {
                // Negative accumulation also represents Long.MIN_VALUE exactly.
                value = value * 10 - (character - '0');
                character = read();
            }
            return negative ? value : -value;
        }

        int nextInt() { return (int)nextLong(); }
        double nextDouble() { return Double.parseDouble(next()); }
        FastInput useLocale(java.util.Locale ignored) { return this; }
    }

    private static final class FastOutput {
        private static final int CAPACITY = 1024;
        private final byte[] buffer = new byte[CAPACITY];
        private final byte[] digits = new byte[20];
        private int size;

        void flush() throws java.io.IOException {
            System.out.write(buffer, 0, size);
            size = 0;
            System.out.flush();
        }

        void byteValue(int value) throws java.io.IOException {
            if (size == buffer.length)
                flush();
            buffer[size++] = (byte)value;
        }

        void number(long value) throws java.io.IOException {
            if (value < 0)
                byteValue('-');
            // Keep the magnitude negative so Long.MIN_VALUE is representable.
            long remaining = value > 0 ? -value : value;
            int start = digits.length;
            do {
                digits[--start] = (byte)('0' - remaining % 10);
                remaining /= 10;
            } while (remaining != 0);
            while (start < digits.length)
                byteValue(digits[start++]);
        }

        void text(String value) throws java.io.IOException {
            for (byte character : value.getBytes(java.nio.charset.StandardCharsets.UTF_8))
                byteValue(character);
        }
    }
    static int x(long point) { return (int)(point >> WORD_BITS); }
    static int y(long point) { return ((int)point) ^ Integer.MIN_VALUE; }
    static long cross(long a, long b, long c) {
        return ((long)x(b) - x(a)) * ((long)y(c) - y(a)) -
            ((long)y(b) - y(a)) * ((long)x(c) - x(a));
    }
    public static void main(String[] args) throws java.io.IOException {
        FastInput input = new FastInput(System.in);
        int count = input.nextInt(), gap = input.nextInt();
        long[] points = new long[count];
        for (int i = 0; i < count; i++) {
            int x = input.nextInt(), y = input.nextInt();
            // Flipping the low sign bit preserves signed y order within equal x.
            points[i] = ((long)x << WORD_BITS) | ((y ^ Integer.MIN_VALUE) & UNSIGNED_INT_MASK);
        }
        java.util.Arrays.sort(points);
        int[] hull = new int[2 * count];
        int size = 0;
        for (int i = 0; i < count; i++) {
            while (size >= 2 &&
                   cross(points[hull[size - 2]], points[hull[size - 1]], points[i]) <= 0)
                size--;
            hull[size++] = i;
        }
        int lower = size;
        for (int i = count - 2; i >= 0; i--) {
            while (size > lower &&
                   cross(points[hull[size - 2]], points[hull[size - 1]], points[i]) <= 0)
                size--;
            hull[size++] = i;
        }
        if (size > 1)
            size--;
        double length = 2 * Math.PI * gap;
        for (int i = 0; i < size; i++) {
            long a = points[hull[i]], b = points[hull[(i + 1) % size]];
            length += Math.hypot((double)x(a) - x(b), (double)y(a) - y(b));
        }
        System.out.println(Math.round(length));
    }
}
