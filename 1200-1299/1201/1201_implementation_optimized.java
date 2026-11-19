

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

    static final String[] NAMES = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"};
    static final int[] LENGTHS = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    static final int WEEK = 7, YEAR = 365, CELL = 5;
    static final int LEAP = 4, CENTURY = 100, ERA = 400;

    public static void main(String[] args) {
        int[] lengths = LENGTHS.clone();
        FastInput in = new FastInput(System.in);
        int d = in.nextInt(), m = in.nextInt(), y = in.nextInt();
        if (y % LEAP == 0 && (y % CENTURY != 0 || y % ERA == 0)) {
            lengths[1]++;
        }
        // days from 1 January of year 1, a Monday, to the first of the month
        int past = y - 1;
        int before = YEAR * past + past / LEAP - past / CENTURY + past / ERA;
        for (int i = 0; i < m - 1; i++) {
            before += lengths[i];
        }
        int first = before % WEEK, days = lengths[m - 1];
        int cols = (first + days + WEEK - 1) / WEEK;
        StringBuilder out = new StringBuilder();
        for (int row = 0; row < WEEK; row++) {
            out.append(NAMES[row]);
            for (int col = 0; col < cols; col++) {
                int day = col * WEEK + row - first + 1;
                boolean last = col == cols - 1;
                // every column is five characters wide, the last one four,
                // unless the bracketed date sits in it
                if (day == d) {
                    out.append(String.format(" [%2d]", day));
                } else if (day >= 1 && day <= days) {
                    out.append(String.format(last ? "  %2d" : "  %2d ", day));
                } else {
                    for (int i = 0; i < (last ? CELL - 1 : CELL); i++) {
                        out.append(' ');
                    }
                }
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
