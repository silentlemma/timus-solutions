import java.util.*;

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

    static final long HUNDRED = 100;        // times are kept in hundredths of a second, exactly
    static final long STAND = 15 * HUNDRED; // the lift stands this long on the first floor
    static final long BOARD = 5 * HUNDRED;  // getting into the lift
    static final int DIGITS = 2;

    // a number with at most two decimals, as an exact integer of hundredths
    static long hundredths(String word) {
        int dot = word.indexOf('.');
        String whole = dot < 0 ? word : word.substring(0, dot);
        String frac = dot < 0 ? "" : word.substring(dot + 1);
        frac = (frac + "00").substring(0, DIGITS);
        return Long.parseLong(whole) * HUNDRED + Long.parseLong(frac);
    }

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        if (!in.hasNextLong())
            return;
        long n = in.nextLong(), k = in.nextLong();
        long u = hundredths(in.next()), v = hundredths(in.next());
        // walking all the way down needs no lift
        long bestFloor = 1, bestTime = (n - 1) * u;
        long ready = (k - 1) * v + STAND; // the lift may leave the first floor from then on
        for (long f = 2; f <= n; f++) {
            // Petya calls the lift on reaching floor f; it comes up, waits for
            // the boarding and goes down again
            long start = Math.max(ready, (n - f) * u);
            long total = start + (f - 1) * v + BOARD + (f - 1) * v;
            // a later floor means less walking, so ties go to it
            if (total <= bestTime) {
                bestFloor = f;
                bestTime = total;
            }
        }
        System.out.println(bestFloor);
    }
}
