

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

    static final int PARAMS = 3, MAJORITY = 2;

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        int n = in.nextInt();
        String[] names = new String[n];
        int[][] stats = new int[n][PARAMS];
        for (int i = 0; i < n; i++) {
            names[i] = in.next();
            for (int p = 0; p < PARAMS; p++) {
                stats[i][p] = in.nextInt();
            }
        }
        // reach[i][j]: i beats j, directly or through a chain of wins
        boolean[][] reach = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int better = 0;
                for (int p = 0; p < PARAMS; p++) {
                    if (stats[i][p] > stats[j][p]) {
                        better++;
                    }
                }
                reach[i][j] = i != j && better >= MAJORITY;
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (reach[i][k]) {
                    for (int j = 0; j < n; j++) {
                        reach[i][j] |= reach[k][j];
                    }
                }
            }
        }
        StringBuilder out = new StringBuilder();
        // a Jedi can win when every other one can be beaten along such a chain
        for (int i = 0; i < n; i++) {
            boolean all = true;
            for (int j = 0; j < n; j++) {
                all &= i == j || reach[i][j];
            }
            if (all) {
                out.append(names[i]).append('\n');
            }
        }
        System.out.print(out);
    }
}
