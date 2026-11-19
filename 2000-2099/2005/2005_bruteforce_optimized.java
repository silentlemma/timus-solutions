

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

    static final int POINTS = 5;
    // point k has index k - 1: start 0, middle points FIRST_MIDDLE..LAST_MIDDLE, finish END
    static final int FIRST_MIDDLE = 1, POINT_3 = 2, LAST_MIDDLE = 3, END = 4;

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        int[][] d = new int[POINTS][POINTS];
        for (int i = 0; i < POINTS; i++)
            for (int j = 0; j < POINTS; j++)
                d[i][j] = in.nextInt();
        // points 2, 3 and 4 (indices 1, 2, 3) come in any order, except that 3
        // may not be the last of them
        int best = -1;
        int[] route = null;
        for (int a = FIRST_MIDDLE; a <= LAST_MIDDLE; a++)
            for (int b = FIRST_MIDDLE; b <= LAST_MIDDLE; b++)
                for (int c = FIRST_MIDDLE; c <= LAST_MIDDLE; c++) {
                    if (a == b || a == c || b == c || c == POINT_3)
                        continue;
                    int cost = d[0][a] + d[a][b] + d[b][c] + d[c][END];
                    if (best < 0 || cost < best) {
                        best = cost;
                        route = new int[] {0, a, b, c, END};
                    }
                }
        StringBuilder out = new StringBuilder().append(best).append('\n');
        for (int i = 0; i < POINTS; i++)
            out.append(route[i] + 1).append(i + 1 < POINTS ? ' ' : '\n');
        System.out.print(out);
    }
}
