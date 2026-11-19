public class Main {
    private static final long LEADING_PLACE = 100000000000L;

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

    private static final class FastOutput {
        private static final int CAPACITY = 1024;
        private final byte[] buffer = new byte[CAPACITY];
        private final byte[] digits = new byte[20];
        private int size;

        void flush() throws java.io.IOException {
            System.out.write(buffer, 0, size);
            size = 0;
            System.out.flush();
        }

        void byteValue(int value) throws java.io.IOException {
            if (size == buffer.length)
                flush();
            buffer[size++] = (byte)value;
        }

        void number(long value) throws java.io.IOException {
            if (value < 0)
                byteValue('-');
            // Keep the magnitude negative so Long.MIN_VALUE is representable.
            long remaining = value > 0 ? -value : value;
            int start = digits.length;
            do {
                digits[--start] = (byte)('0' - remaining % 10);
                remaining /= 10;
            } while (remaining != 0);
            while (start < digits.length)
                byteValue(digits[start++]);
        }

        void text(String value) throws java.io.IOException {
            for (byte character : value.getBytes(java.nio.charset.StandardCharsets.UTF_8))
                byteValue(character);
        }
    }

    static final int DIGITS = 12;
    static final long[] BASES = {2, 3, 5, 7, 11, 13}; // enough for every number below 3 * 10^12
    static final int HALF = 20;
    static final long LOW = (1L << HALF) - 1;

    // a * b mod n for n below 2^40: b is split into 20-bit halves so that no
    // product passes 2^60
    static long mulmod(long a, long b, long n) {
        long high = a * (b >> HALF) % n;
        return ((high << HALF) % n + a * (b & LOW)) % n;
    }

    static long powmod(long a, long e, long n) {
        long r = 1;
        for (a %= n; e > 0; e >>= 1, a = mulmod(a, a, n)) {
            if ((e & 1) == 1)
                r = mulmod(r, a, n);
        }
        return r;
    }

    // Miller-Rabin with fixed bases, exact for all 12-digit numbers
    static boolean isPrime(long n) {
        if (n < 2)
            return false;
        for (long p : BASES) {
            if (n % p == 0)
                return n == p;
        }
        long d = n - 1;
        int s = 0;
        for (; d % 2 == 0; d /= 2)
            s++;
        for (long a : BASES) {
            long x = powmod(a, d, n);
            boolean witness = x != 1 && x != n - 1;
            for (int i = 1; i < s && witness; i++) {
                x = mulmod(x, x, n);
                witness = x != n - 1;
            }
            if (witness)
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws java.io.IOException {
        FastInput input = new FastInput(System.in);
        FastOutput output = new FastOutput();
        int count = input.nextInt(), seen = 0;
        long number = 0;
        while (seen < count) {
            int character = input.read();
            if (character < 0)
                break;
            if (character >= '0' && character <= '9') {
                number = number * 10 + character - '0';
                seen++;
            }
        }
        for (int i = count; i < DIGITS; i++)
            number *= 10;
        if (count < DIGITS)
            while (!isPrime(number))
                number++;
        long place = LEADING_PLACE;
        while (place > number && place > 1) {
            output.byteValue('0');
            place /= 10;
        }
        output.number(number);
        output.byteValue('\n');
        output.flush();
    }
}
