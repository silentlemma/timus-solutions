import java.math.BigInteger;

public class Main {
    private static final int CORNER_COORDINATES = 4;
    private static final int DISTANCE_SCALE = 8;
    private static final int LAST_COORDINATE = 3;

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
    private static BigInteger px, py, twiceX, twiceY, inside;
    private static BigInteger[] numerators, denominators;
    private static long[] scales;

    static void distance(int index, int x1, int y1, int x2, int y2) {
        long dx = x2 - x1, dy = y2 - y1, h = dx * dx + dy * dy;
        if (h == 0) {
            numerators[index] = BigInteger.valueOf((long)x1 * x1 + (long)y1 * y1)
                                    .subtract(px.multiply(BigInteger.valueOf(2L * x1)))
                                    .subtract(py.multiply(BigInteger.valueOf(2L * y1)));
            scales[index] = 1;
            return;
        }
        long cx = x1 + x2, cy = y1 + y2;
        BigInteger qx = twiceX.subtract(BigInteger.valueOf(cx));
        BigInteger qy = twiceY.subtract(BigInteger.valueOf(cy));
        BigInteger first = qx.multiply(BigInteger.valueOf(dx - dy))
                               .add(qy.multiply(BigInteger.valueOf(dy + dx)))
                               .abs();
        BigInteger second = qx.multiply(BigInteger.valueOf(dx + dy))
                                .add(qy.multiply(BigInteger.valueOf(dy - dx)))
                                .abs();
        BigInteger extent = BigInteger.valueOf(h);
        if (first.compareTo(extent) <= 0 && second.compareTo(extent) <= 0) {
            if (inside == null) {
                // An interior query is bounded by the bounded square coordinates.
                long x = px.longValueExact(), y = py.longValueExact();
                inside = BigInteger.valueOf(-x * x - y * y);
            }
            numerators[index] = inside;
            scales[index] = 1;
            return;
        }
        // Subtract |P|^2, common to every distance. The resulting numerator is
        // linear in the unbounded query coordinates instead of quadratic.
        BigInteger base = BigInteger.valueOf(cx * cx + cy * cy + h)
                              .subtract(px.multiply(BigInteger.valueOf(CORNER_COORDINATES * cx)))
                              .subtract(py.multiply(BigInteger.valueOf(CORNER_COORDINATES * cy)))
                              .subtract(first)
                              .subtract(second);
        long missingFirst = first.compareTo(extent) < 0 ? h - first.longValueExact() : 0;
        long missingSecond = second.compareTo(extent) < 0 ? h - second.longValueExact() : 0;
        if (missingFirst == 0 && missingSecond == 0) {
            numerators[index] = base;
            scales[index] = CORNER_COORDINATES;
        } else {
            // h < 8*10^8, so the sum of these bounded squares fits in long.
            long correction = missingFirst * missingFirst + missingSecond * missingSecond;
            numerators[index] =
                base.multiply(BigInteger.valueOf(2 * h)).subtract(BigInteger.valueOf(correction));
            scales[index] = DISTANCE_SCALE * h;
        }
    }

    static int compare(int first, int second) {
        if (scales[first] == scales[second])
            return numerators[first].compareTo(numerators[second]);
        return numerators[first]
            .multiply(denominators[second])
            .compareTo(numerators[second].multiply(denominators[first]));
    }

    public static void main(String[] args) throws java.io.IOException {
        FastInput input = new FastInput(System.in);
        FastOutput output = new FastOutput();
        int count = input.nextInt();
        int[] corners = new int[CORNER_COORDINATES * count];
        for (int i = 0; i < corners.length; i++)
            corners[i] = input.nextInt();
        px = new BigInteger(input.next());
        py = new BigInteger(input.next());
        twiceX = px.shiftLeft(1);
        twiceY = py.shiftLeft(1);
        numerators = new BigInteger[count];
        denominators = new BigInteger[count];
        scales = new long[count];
        int[] order = new int[count], scratch = new int[count];
        for (int i = 0; i < count; i++) {
            distance(i, corners[CORNER_COORDINATES * i], corners[CORNER_COORDINATES * i + 1],
                     corners[CORNER_COORDINATES * i + 2],
                     corners[CORNER_COORDINATES * i + LAST_COORDINATE]);
            denominators[i] = BigInteger.valueOf(scales[i]);
            order[i] = i;
        }
        // Stable primitive merge sort preserves input IDs on exact rational ties.
        for (int width = 1; width < count; width *= 2) {
            for (int start = 0; start < count; start += 2 * width) {
                int middle = Math.min(count, start + width), end =
                                                                 Math.min(count, start + 2 * width);
                int left = start, right = middle;
                for (int at = start; at < end; at++) {
                    if (left < middle && (right == end || compare(order[left], order[right]) <= 0))
                        scratch[at] = order[left++];
                    else
                        scratch[at] = order[right++];
                }
            }
            int[] swap = order;
            order = scratch;
            scratch = swap;
        }
        for (int i = 0; i < count; i++) {
            if (i != 0)
                output.byteValue(' ');
            output.number(order[i] + 1);
        }
        output.byteValue('\n');
        output.flush();
    }
}
