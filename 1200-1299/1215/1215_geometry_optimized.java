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

    static double segmentDistance(double px, double py, double ax, double ay, double bx,
                                  double by) {
        double dx = bx - ax, dy = by - ay;
        double t = (px - ax) * dx + (py - ay) * dy, length2 = dx * dx + dy * dy;
        if (t <= 0) {
            return Math.hypot(px - ax, py - ay);
        }
        if (t >= length2) {
            return Math.hypot(px - bx, py - by);
        }
        return Math.abs((px - ax) * dy - (py - ay) * dx) / Math.sqrt(length2);
    }

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        long px = in.nextLong(), py = in.nextLong();
        int n = in.nextInt();
        long[] x = new long[n], y = new long[n];
        for (int i = 0; i < n; i++) {
            x[i] = in.nextLong();
            y[i] = in.nextLong();
        }
        boolean inside = true;
        double best = Double.POSITIVE_INFINITY;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            // inside a counterclockwise polygon the point is left of every edge
            if ((x[j] - x[i]) * (py - y[i]) - (y[j] - y[i]) * (px - x[i]) < 0) {
                inside = false;
            }
            best = Math.min(best, segmentDistance(px, py, x[i], y[i], x[j], y[j]));
        }
        System.out.println(String.format(Locale.US, "%.3f", inside ? 0.0 : 2 * best));
    }
}
