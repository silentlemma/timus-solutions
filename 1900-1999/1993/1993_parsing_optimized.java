public class Main {
    private static final int ROLE_COUNT = 3;

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
    static boolean isLetter(char character) {
        return character >= 'a' && character <= 'z' || character >= 'A' && character <= 'Z';
    }

    static boolean phrase(FastOutput output, String text, int start, int end, boolean first)
        throws java.io.IOException {
        for (int i = start; i < end; i++) {
            char character = text.charAt(i);
            if (character >= 'A' && character <= 'Z')
                character += 'a' - 'A';
            if (first && character >= 'a' && character <= 'z')
                character -= 'a' - 'A';
            first = false;
            output.byteValue(character);
        }
        return first;
    }
    public static void main(String[] args) throws java.io.IOException {
        FastInput input = new FastInput(System.in);
        FastOutput output = new FastOutput();
        String sentence = input.line();
        int clauseStart = 0;
        boolean first = true;
        while (clauseStart < sentence.length()) {
            int clauseEnd = sentence.indexOf(',', clauseStart);
            if (clauseEnd < 0)
                clauseEnd = sentence.length();
            int[] start = new int[ROLE_COUNT], end = new int[ROLE_COUNT];
            int prefixStart = -1, prefixEnd = -1;
            for (int at = clauseStart; at < clauseEnd;) {
                char character = sentence.charAt(at);
                int role = "{([".indexOf(character);
                if (role >= 0) {
                    start[role] = at + 1;
                    end[role] = sentence.indexOf("})]".charAt(role), at + 1);
                    at = end[role] + 1;
                } else if (isLetter(character)) {
                    prefixStart = at++;
                    while (at < clauseEnd && isLetter(sentence.charAt(at)))
                        at++;
                    prefixEnd = at;
                } else
                    at++;
            }
            if (!first)
                output.text(", ");
            if (prefixStart >= 0) {
                first = phrase(output, sentence, prefixStart, prefixEnd, first);
                output.byteValue(' ');
            }
            for (int role = 0; role < ROLE_COUNT; role++) {
                if (role != 0)
                    output.byteValue(' ');
                first = phrase(output, sentence, start[role], end[role], first);
            }
            clauseStart = clauseEnd + 1;
        }
        output.byteValue('\n');
        output.flush();
    }
}
