import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

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
        int n = in.nextInt();
        int[] left = new int[n], right = new int[n];
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            left[i] = in.nextInt();
            right[i] = in.nextInt();
            if (left[i] > right[i]) {
                int t = left[i];
                left[i] = right[i];
                right[i] = t;
            }
            order[i] = i;
        }
        // a segment inside another is strictly shorter, so by length the inner
        // one always comes first
        Arrays.sort(order, (a, b) -> Integer.compare(right[a] - left[a], right[b] - left[b]));
        int[] best = new int[n], prev = new int[n];
        Arrays.fill(best, 1);
        Arrays.fill(prev, -1);
        for (int p = 0; p < n; p++) {
            int i = order[p];
            for (int q = 0; q < p; q++) {
                int j = order[q];
                if (left[i] < left[j] && right[j] < right[i] && best[j] + 1 > best[i]) {
                    best[i] = best[j] + 1;
                    prev[i] = j;
                }
            }
        }
        int end = 0;
        for (int i = 1; i < n; i++) {
            if (best[i] > best[end]) {
                end = i;
            }
        }
        List<Integer> chain = new ArrayList<>();
        for (; end >= 0; end = prev[end]) {
            chain.add(end + 1);
        }
        Collections.reverse(chain);
        StringBuilder out = new StringBuilder();
        out.append(chain.size()).append("\n");
        for (int i = 0; i < chain.size(); i++) {
            out.append(i > 0 ? " " : "").append(chain.get(i));
        }
        System.out.println(out);
    }
}
