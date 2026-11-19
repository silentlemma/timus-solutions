public class Main {
    private static final int INITIAL_HALF_EDGES = 16;
    private static final int WORD_BITS = 32;

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
    public static void main(String[] args) throws java.io.IOException {
        FastInput input = new FastInput(System.in);
        FastOutput output = new FastOutput();
        int count = input.nextInt(), used = 0;
        int[] offset = new int[count + 1], room = new int[INITIAL_HALF_EDGES];
        long[] keys = new long[INITIAL_HALF_EDGES];
        for (int vertex = 0; vertex < count; vertex++) {
            offset[vertex] = used;
            int degree = input.nextInt();
            for (int i = 0; i < degree; i++) {
                int neighbour = input.nextInt() - 1;
                if (used == keys.length) {
                    keys = java.util.Arrays.copyOf(keys, used * 2);
                    room = java.util.Arrays.copyOf(room, used * 2);
                }
                long pair = (long)Math.min(vertex, neighbour) * count + Math.max(vertex, neighbour);
                keys[used] = (pair << WORD_BITS) | used;
                room[used++] = vertex;
            }
        }
        offset[count] = used;
        keys = java.util.Arrays.copyOf(keys, used);
        room = java.util.Arrays.copyOf(room, used);
        java.util.Arrays.sort(keys);
        int[] mate = new int[used];
        for (int start = 0; start < used;) {
            long pair = keys[start] >>> WORD_BITS;
            int end = start + 1;
            while (end < used && (keys[end] >>> WORD_BITS) == pair)
                end++;
            if (pair / count == pair % count) {
                for (int i = start; i < end; i += 2) {
                    int a = (int)keys[i], b = (int)keys[i + 1];
                    mate[a] = b;
                    mate[b] = a;
                }
            } else {
                // Input rows are ordered, so the two endpoint lists occupy equal halves.
                int half = (end - start) / 2;
                for (int i = 0; i < half; i++) {
                    int a = (int)keys[start + i], b = (int)keys[start + half + i];
                    mate[a] = b;
                    mate[b] = a;
                }
            }
            start = end;
        }
        byte[] colours = new byte[used];
        boolean[] virtualUsed = new boolean[count];
        int[] cursor = offset.clone(), stack = new int[used / 2 + count + 2];
        int dummyCursor = 0;
        for (int start = 0; start <= count; start++) {
            int top = 1;
            stack[0] = start;
            while (top != 0) {
                int vertex = stack[top - 1];
                if (vertex == count) {
                    while (dummyCursor < count &&
                           ((offset[dummyCursor + 1] - offset[dummyCursor]) % 2 == 0 ||
                            virtualUsed[dummyCursor]))
                        dummyCursor++;
                    if (dummyCursor == count)
                        top--;
                    else {
                        virtualUsed[dummyCursor] = true;
                        stack[top++] = dummyCursor++;
                    }
                } else {
                    while (cursor[vertex] < offset[vertex + 1] && colours[cursor[vertex]] != 0)
                        cursor[vertex]++;
                    if (cursor[vertex] < offset[vertex + 1]) {
                        int edge = cursor[vertex]++;
                        colours[edge] = 'G';
                        colours[mate[edge]] = 'Y';
                        stack[top++] = room[mate[edge]];
                    } else if ((offset[vertex + 1] - offset[vertex]) % 2 != 0 &&
                               !virtualUsed[vertex]) {
                        virtualUsed[vertex] = true;
                        stack[top++] = count;
                    } else
                        top--;
                }
            }
        }
        for (int vertex = 0; vertex < count; vertex++) {
            for (int edge = offset[vertex]; edge < offset[vertex + 1]; edge++) {
                if (edge != offset[vertex])
                    output.byteValue(' ');
                output.byteValue(colours[edge]);
            }
            output.byteValue('\n');
        }
        output.flush();
    }
}
