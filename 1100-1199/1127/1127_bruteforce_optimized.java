public class Main {
    private static final int BYTE_VALUES = 256;

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
    private static final int FACES = 6, ROTATIONS = 24, COLOURS = 10;
    private static final int FRONT = 0, RIGHT = 1, LEFT = 2, BACK = 3;
    private static final int[] SPIN = {2, 0, 3, 1, 4, 5}, TIP = {4, 1, 2, 5, 3, 0};

    public static void main(String[] args) {
        int[][] rotations = new int[ROTATIONS][FACES];
        for (int face = 0; face < FACES; face++)
            rotations[0][face] = face;
        int used = 1;
        int[] next = new int[FACES];
        for (int at = 0; at < used; at++) {
            for (int[] turn : new int[][] {SPIN, TIP}) {
                for (int face = 0; face < FACES; face++)
                    next[face] = rotations[at][turn[face]];
                boolean seen = false;
                for (int previous = 0; previous < used; previous++)
                    if (java.util.Arrays.equals(next, rotations[previous])) {
                        seen = true;
                        break;
                    }
                if (!seen)
                    System.arraycopy(next, 0, rotations[used++], 0, FACES);
            }
        }
        FastInput input = new FastInput(System.in);
        int count = input.nextInt(), assigned = 0, best = 0;
        int[] id = new int[BYTE_VALUES], cube = new int[FACES];
        java.util.Arrays.fill(id, -1);
        // A ring is four base-ten colour IDs: exactly 10000 primitive counters.
        int[] rings = new int[COLOURS * COLOURS * COLOURS * COLOURS];
        for (int index = 0; index < count; index++) {
            for (int face = 0; face < FACES;) {
                int letter = input.read();
                if (letter <= ' ')
                    continue;
                if (id[letter] < 0)
                    id[letter] = assigned++;
                cube[face++] = id[letter];
            }
            // All six faces differ, so the 24 visible ordered side rings are distinct.
            for (int[] rotation : rotations) {
                int ring = cube[rotation[FRONT]];
                ring = ring * COLOURS + cube[rotation[RIGHT]];
                ring = ring * COLOURS + cube[rotation[BACK]];
                ring = ring * COLOURS + cube[rotation[LEFT]];
                best = Math.max(best, ++rings[ring]);
            }
        }
        System.out.println(best);
    }
}
