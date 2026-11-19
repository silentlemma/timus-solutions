import java.util.HashSet;
import java.util.Set;

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

    static final int LIMIT = 200; // the values repeat with PERIOD from 52 on, well below this
    static final int PERIOD = 34;
    static final int TAKE = 3; // a move takes up to three files out of play

    public static void main(String[] args) {
        long n = new FastInput(System.in).nextLong();
        // Dawson's chess: a row of n files plays like the octal game 0.137, where
        // a move takes one file (only if it is all), two (leaving one row) or three
        // (leaving up to two rows); White, moving first, wins when the value is not 0
        int[] g = new int[LIMIT + 1];
        for (int size = 1; size <= LIMIT; size++) {
            Set<Integer> seen = new HashSet<>();
            if (size == 1)
                seen.add(0);
            if (size >= 2)
                seen.add(g[size - 2]);
            for (int left = 0; left <= size - TAKE; left++)
                seen.add(g[left] ^ g[size - TAKE - left]);
            while (seen.contains(g[size]))
                g[size]++;
        }
        if (n > LIMIT)
            n = LIMIT - PERIOD + (n - LIMIT) % PERIOD;
        System.out.println(g[(int)n] != 0 ? "White" : "Black");
    }
}
