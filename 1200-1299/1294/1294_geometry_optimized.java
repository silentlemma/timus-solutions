import java.util.*;

public class Main {
    private static final int AREA_DENOMINATOR = 4;

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

    static final long KM = 1000; // input distances are in thousands of kilometres

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        // a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
        // inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
        long a = in.nextLong(), b = in.nextLong(), c = in.nextLong(), d = in.nextLong();
        long den = a * b - c * d;
        long diff = a * a + b * b - c * c - d * d;
        if (den == 0 || Math.abs(diff) >= 2 * Math.abs(den) || b * c <= a * d) {
            System.out.println("Impossible.");
            return;
        }
        long num = a * b * (c * c + d * d) - c * d * (a * a + b * b);
        if (den < 0) {
            num = -num;
            den = -den;
        }
        long km = (long)(KM * Math.sqrt((double)num / den));
        // Compare the half-kilometre boundary exactly, dividing before scaling.
        long scale = AREA_DENOMINATOR * KM * KM;
        long bound = scale * (num / den) + scale * (num % den) / den;
        if ((2 * km + 1) * (2 * km + 1) <= bound)
            ++km;
        System.out.println("Distance is " + km + " km.");
    }
}
