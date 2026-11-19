public class Main {
    private static final int ALPHABET = 26, VALUE_LIMIT = 100000, TICKS = 1000000;
    private static final int UP = 3;
    private static final int DIRECTIONS = 4;

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
    public static void main(String[] args) throws java.io.IOException {

        FastInput input = new FastInput(System.in);
        FastOutput output = new FastOutput();
        int height = input.nextInt(), width = input.nextInt();
        byte[] grid = new byte[height * width];
        for (int i = 0; i < grid.length;) {
            int character = input.read();
            if (character > ' ')
                grid[i++] = (byte)character;
        }
        int remaining = input.nextInt(), last = 0;
        int[] memory = new int[ALPHABET];
        int row = 0, column = 0, direction = 0, current = 0;
        int[] dr = {0, 1, 0, -1}, dc = {1, 0, -1, 0};
        for (int tick = 0; tick < TICKS; tick++) {
            int operation = grid[row * width + column];
            switch (operation) {
            case '#':
                output.flush();
                return;
            case '>':
                direction = 0;
                break;
            case 'v':
                direction = 1;
                break;
            case '<':
                direction = 2;
                break;
            case '^':
                direction = UP;
                break;
            case '?':
                if (remaining > 0) {
                    last = input.nextInt();
                    remaining--;
                }
                current = last;
                break;
            case '!':
                output.number(current);
                output.byteValue('\n');
                current = 0;
                break;
            case '+':
                current++;
                break;
            case '-':
                current--;
                break;
            case '@':
                direction = (direction + (current == 0 ? UP : 1)) % DIRECTIONS;
                break;
            default:
                if (operation >= 'A' && operation <= 'Z') {
                    int index = operation - 'A', saved = current;
                    current = memory[index];
                    memory[index] = saved;
                }
            }
            if (current < -VALUE_LIMIT || current > VALUE_LIMIT) {
                output.text("OVERFLOW ERROR\n");
                output.flush();
                return;
            }
            row += dr[direction];
            column += dc[direction];
            if (row < 0 || row >= height || column < 0 || column >= width) {
                output.text("RUNTIME ERROR\n");
                output.flush();
                return;
            }
        }
        output.text("TIME LIMIT EXCEEDED\n");
        output.flush();
    }
}
