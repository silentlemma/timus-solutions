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

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        long ax = in.nextLong(), ay = in.nextLong(), bx = in.nextLong(), by = in.nextLong();
        long cx = in.nextLong(), cy = in.nextLong();
        String token = in.next();
        // an unbounded rope may become infinity; then both extensions are zero.
        double rope = Double.parseDouble(token);
        long dx = bx - ax, dy = by - ay, length = dx * dx + dy * dy;
        // the nearest point of the bed: C projected onto AB, kept inside it
        double t = 0;
        if (length != 0)
            t = Math.max(0.0, Math.min(1.0, (double)((cx - ax) * dx + (cy - ay) * dy) / length));
        double nearest = Math.hypot(ax + t * dx - cx, ay + t * dy - cy);
        double farthest = Math.max(Math.hypot(ax - cx, ay - cy), Math.hypot(bx - cx, by - cy));
        System.out.println(String.format(Locale.US, "%.2f", Math.max(0.0, nearest - rope)));
        System.out.println(String.format(Locale.US, "%.2f", Math.max(0.0, farthest - rope)));
    }
}
