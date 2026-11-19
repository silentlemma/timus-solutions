import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

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

    static Set<String> readSet(FastInput in) {
        int count = in.nextInt();
        Set<String> items = new HashSet<>();
        for (int i = 0; i < count; i++)
            items.add(in.next());
        return items;
    }

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        Set<String> menu = readSet(in);
        int k = in.nextInt();
        List<Set<String>> blocks = new ArrayList<>();
        for (int i = 0; i <= k; i++)
            blocks.add(readSet(in));
        int m = in.nextInt();
        // the first student was fine, so the meal is m products of the rest
        List<String> safe = new ArrayList<>();
        for (String p : menu) {
            if (!blocks.get(0).contains(p))
                safe.add(p);
        }
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= k; i++) {
            int risky = 0;
            for (String p : safe) {
                if (blocks.get(i).contains(p))
                    risky++;
            }
            if (m == 0 || risky == 0)
                out.append("YES\n");
            else if (safe.size() - risky < m)
                out.append("NO\n"); // every possible meal holds a dangerous product
            else
                out.append("MAYBE\n");
        }
        System.out.print(out);
    }
}
