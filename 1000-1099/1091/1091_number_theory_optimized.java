import java.util.Arrays;

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

    static final long CAPACITY = 10000;

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        int k = in.nextInt(), s = in.nextInt();
        long[][] binom = new long[s + 1][s + 1];
        for (int n = 0; n <= s; n++) {
            binom[n][0] = 1;
            for (int r = 1; r <= n; r++) {
                binom[n][r] = binom[n - 1][r - 1] + binom[n - 1][r];
            }
        }
        // Moebius function by a sieve: -1 per prime factor, 0 with a square factor
        long[] mu = new long[s + 1];
        boolean[] prime = new boolean[s + 1];
        Arrays.fill(mu, 1);
        Arrays.fill(prime, true);
        for (int p = 2; p <= s; p++) {
            if (!prime[p]) {
                continue;
            }
            for (int m = p; m <= s; m += p) {
                prime[m] = m == p;
                mu[m] = -mu[m];
            }
            for (int m = p * p; m <= s; m += p * p) {
                mu[m] = 0;
            }
        }
        // inclusion-exclusion: sets of multiples of d count with the sign -mu(d)
        long total = 0;
        for (int d = 2; d <= s; d++) {
            if (s / d >= k) {
                total -= mu[d] * binom[s / d][k];
            }
        }
        System.out.println(Math.min(total, CAPACITY));
    }
}
