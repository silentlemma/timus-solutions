import java.util.Locale;

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

    static final long SCALE = 100; // coordinates come with two decimals: work in hundredths

    static long hundredths(String s) {
        int dot = s.indexOf('.');
        String whole = dot < 0 ? s : s.substring(0, dot);
        String part = ((dot < 0 ? "" : s.substring(dot + 1)) + "00").substring(0, 2);
        long p = Long.parseLong(part);
        return Long.parseLong(whole) * SCALE + (s.startsWith("-") ? -p : p);
    }

    // The face A x B in the middle of the column lies at z = 0 with its
    // corner (c, b + c) at the origin; every other face folds up from it.
    static long[] fold(long a, long b, long c, long x, long y) {
        if (x < c)
            return new long[] {0, y - b - c, c - x};
        if (x > c + a)
            return new long[] {a, y - b - c, x - c - a};
        if (y < b)
            return new long[] {x - c, b - y, c};
        if (y < b + c)
            return new long[] {x - c, 0, b + c - y};
        if (y <= 2 * b + c)
            return new long[] {x - c, y - b - c, 0};
        return new long[] {x - c, b, y - 2 * b - c};
    }

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        long a = in.nextLong() * SCALE, b = in.nextLong() * SCALE, c = in.nextLong() * SCALE;
        long[] p = fold(a, b, c, hundredths(in.next()), hundredths(in.next()));
        long[] q = fold(a, b, c, hundredths(in.next()), hundredths(in.next()));
        long squared = 0;
        for (int i = 0; i < p.length; i++)
            squared += (p[i] - q[i]) * (p[i] - q[i]);
        System.out.println(String.format(Locale.US, "%.10f", Math.sqrt(squared) / SCALE));
    }
}
