

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

    static final int SIZE = 4, CELLS = SIZE * SIZE;

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        // the board as 16 bits, bit r * 4 + c set for a black piece
        int board = 0;
        for (int r = 0; r < SIZE; r++) {
            String row = in.next();
            for (int c = 0; c < SIZE; c++) {
                if (row.charAt(c) == 'b') {
                    board |= 1 << (r * SIZE + c);
                }
            }
        }
        // the pieces turned by a move at each cell
        int[] move = new int[CELLS];
        int[] dr = {0, 1, -1, 0, 0}, dc = {0, 0, 0, 1, -1};
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                int m = 0;
                for (int d = 0; d < dr.length; d++) {
                    int rr = r + dr[d], cc = c + dc[d];
                    if (rr >= 0 && rr < SIZE && cc >= 0 && cc < SIZE) {
                        m |= 1 << (rr * SIZE + cc);
                    }
                }
                move[r * SIZE + c] = m;
            }
        }
        // moves commute and a move made twice cancels, so a solution is a set of
        // cells: try all 2^16 sets
        int all = (1 << CELLS) - 1;
        int best = -1;
        for (int set = 0; set <= all; set++) {
            int b = board;
            for (int i = 0; i < CELLS; i++) {
                if ((set >> i & 1) == 1) {
                    b ^= move[i];
                }
            }
            int count = Integer.bitCount(set);
            if ((b == 0 || b == all) && (best < 0 || count < best)) {
                best = count;
            }
        }
        System.out.println(best < 0 ? "Impossible" : String.valueOf(best));
    }
}
