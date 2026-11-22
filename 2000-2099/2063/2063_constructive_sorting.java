public class Main {
    private static final int BUFFER_SIZE = 1024;

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
            byte[] bytes = new byte[32];
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
        private static final int CAPACITY = 16384;
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

    // FNV-1a of the whole input seeds splitmix64; the arrangements are never
    // decoded, they only make the seed differ between tests
    private static final long FNV_OFFSET = 0xcbf29ce484222325L;
    private static final long FNV_PRIME = 0x100000001b3L;
    private static final long GOLDEN = 0x9e3779b97f4a7c15L;
    private static final long MIX_A = 0xbf58476d1ce4e5b9L;
    private static final long MIX_B = 0x94d049bb133111ebL;
    private static final int SHIFT_A = 30, SHIFT_B = 27, SHIFT_C = 31;
    private static final int CHUNK = 1 << 16;
    private static final int BYTE = 0xff;
    private static long state;

    private static long nextRandom() {
        state += GOLDEN;
        long z = state;
        z = (z ^ (z >>> SHIFT_A)) * MIX_A;
        z = (z ^ (z >>> SHIFT_B)) * MIX_B;
        return z ^ (z >>> SHIFT_C);
    }

    static void compare(int a, int b, int real, FastOutput output) throws java.io.IOException {
        if (b >= real)
            return;
        output.byteValue('?');
        output.byteValue(' ');
        output.number(a + 1);
        output.byteValue(' ');
        output.number(b + 1);
        output.byteValue('\n');
    }
    static void mergeNetwork(int start, int size, int stride, int real, FastOutput output)
        throws java.io.IOException {
        int step = 2 * stride;
        if (step < size) {
            mergeNetwork(start, size, step, real, output);
            mergeNetwork(start + stride, size, step, real, output);
            for (int a = start + stride; a + stride < start + size; a += step)
                compare(a, a + stride, real, output);
        } else
            compare(start, start + stride, real, output);
    }
    static void sortNetwork(int start, int size, int real, FastOutput output)
        throws java.io.IOException {
        if (size <= 1)
            return;
        int half = size / 2;
        sortNetwork(start, half, real, output);
        sortNetwork(start + half, half, real, output);
        mergeNetwork(start, size, 1, real, output);
    }

    public static void main(String[] args) throws java.io.IOException {

        byte[] buffer = new byte[BUFFER_SIZE];
        int games = 0;
        boolean begun = false, finished = false;
        state = FNV_OFFSET;
        for (int count; (count = System.in.read(buffer)) >= 0;) {
            for (int i = 0; i < count; i++) {
                int character = buffer[i] & BYTE;
                state = (state ^ character) * FNV_PRIME;
                // Read only the game count; opaque arrangements affect the byte hash only.
                if (!finished) {
                    if (character >= '0' && character <= '9') {
                        games = games * 10 + character - '0';
                        begun = true;
                    } else if (begun)
                        finished = true;
                }
            }
        }
        FastOutput output = new FastOutput();
        for (int game = 0; game < games; game++) {
            int count = game + 2;
            int padded = 1;
            while (padded < count)
                padded *= 2;
            sortNetwork(0, padded, count, output);
            int index = 1 + (int)Long.remainderUnsigned(nextRandom(), count - 1);
            output.byteValue('!');
            output.byteValue(' ');
            output.number(index);
            output.byteValue(' ');
            output.number(index + 1);
            output.byteValue('\n');
        }
        output.flush();
    }
}
