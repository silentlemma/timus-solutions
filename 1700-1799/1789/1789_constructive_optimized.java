public class Main {

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

    private static void number(int value) {
        byte[] digits = new byte[10];
        int first = digits.length;
        do {
            digits[--first] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        System.out.write(digits, first, digits.length - first);
    }

    public static void main(String[] args) {
        int size = new FastInput(System.in).nextInt();
        number(size == 2 ? 2 : 2 * (size - 2));
        System.out.write('\n');
        if (size == 2) {
            number(1);
            System.out.write(' ');
            number(1);
        } else {
            // Sweep both ways to cover the two possible parity classes.
            boolean first = true;
            for (int cell = 2; cell < size; cell++) {
                if (!first) {
                    System.out.write(' ');
                }
                number(cell);
                first = false;
            }
            for (int cell = size - 1; cell >= 2; cell--) {
                System.out.write(' ');
                number(cell);
            }
        }
        System.out.write('\n');
    }
}
