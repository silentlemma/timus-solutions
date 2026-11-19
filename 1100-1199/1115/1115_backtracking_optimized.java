import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    private static final int RNG_MULTIPLIER = 97;
    private static final int MAX_SHIP_LENGTH = 100;

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

    // no row is longer than all the ships together: 99 * 100
    static final int BITS = 64;

    static final int SEARCH_LIMIT = 256, ATTEMPTS = 128, RNG_MOD = 65536;

    static int n, m, calls;
    static boolean limited;
    static int[] ships, rows, owner;
    static Integer[] order;

    static boolean has(long[] reach, int words, int index, int value) {
        return (reach[index * words + value / BITS] >>> (value % BITS) & 1) != 0;
    }

    static boolean pick(int pos, int[] free, long[] reach, int words, int k, int need) {
        if (limited && ++calls > SEARCH_LIMIT) {
            return false;
        }
        if (need == 0) {
            return fill(pos + 1);
        }
        if (!has(reach, words, k, need)) {
            return false;
        }
        int last = -1;
        for (int j = k; j < free.length; j++) {
            int length = ships[free[j]];
            // equal ships are interchangeable: try each length once per place
            if (length == last || length > need || !has(reach, words, j + 1, need - length)) {
                continue;
            }
            last = length;
            owner[free[j]] = order[pos];
            if (pick(pos, free, reach, words, j + 1, need - length)) {
                return true;
            }
            owner[free[j]] = -1;
            if (limited && calls > SEARCH_LIMIT) {
                return false;
            }
        }
        return false;
    }

    static boolean fill(int pos) {
        int count = 0;
        for (int i = 0; i < n; i++)
            if (owner[i] < 0)
                count++;
        int[] free = new int[count];
        int at = 0;
        for (int i = 0; i < n; i++)
            if (owner[i] < 0)
                free[at++] = i;
        if (pos == m - 1) {
            int sum = 0;
            for (int index : free)
                sum += ships[index];
            if (sum != rows[order[pos]])
                return false;
            for (int index : free)
                owner[index] = order[pos];
            return true;
        }
        int target = 0;
        for (int q = pos; q < m; q++)
            target = Math.max(target, rows[order[q]]);
        int words = target / BITS + 1;
        // Positive lengths make sums above every remaining target irrelevant.
        // Flat suffix blocks remove per-row arrays and oversized 10000-bit storage.
        long[] reach = new long[(count + 1) * words];
        reach[count * words] = 1;
        for (int k = count - 1; k >= 0; k--) {
            int current = k * words, previous = current + words;
            System.arraycopy(reach, previous, reach, current, words);
            int by = ships[free[k]], whole = by / BITS, bits = by % BITS;
            for (int i = words - 1; i >= whole; i--) {
                long value = reach[previous + i - whole] << bits;
                if (bits != 0 && i - whole > 0)
                    value |= reach[previous + i - whole - 1] >>> (BITS - bits);
                reach[current + i] |= value;
            }
        }
        for (int q = pos; q < m; q++)
            if (!has(reach, words, 0, rows[order[q]]))
                return false;
        return pick(pos, free, reach, words, 0, rows[order[pos]]);
    }

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        n = in.nextInt();
        m = in.nextInt();
        Integer[] boxed = new Integer[n];
        for (int i = 0; i < n; i++) {
            boxed[i] = in.nextInt();
        }
        Arrays.sort(boxed, Collections.reverseOrder());
        ships = new int[n];
        for (int i = 0; i < n; i++) {
            ships[i] = boxed[i];
        }
        rows = new int[m];
        for (int i = 0; i < m; i++) {
            rows[i] = in.nextInt();
        }
        // try the shortest rows first as a heuristic
        order = new Integer[m];
        for (int r = 0; r < m; r++) {
            order[r] = r;
        }
        Arrays.sort(
            order,
            (a,
             b) -> rows[a] != rows[b] ? Integer.compare(rows[a], rows[b]) : Integer.compare(a, b));
        owner = new int[n];
        Arrays.fill(owner, -1);
        int state = 1;
        // restart costly searches in a reproducible order; the final search is complete
        for (int attempt = 0; attempt <= ATTEMPTS; attempt++) {
            calls = 0;
            limited = attempt < ATTEMPTS;
            if (fill(0)) {
                break;
            }
            for (int i = m - 1; i > 0; i--) {
                state = (state * RNG_MULTIPLIER + 1) % RNG_MOD;
                int j = state % (i + 1);
                int temp = order[i];
                order[i] = order[j];
                order[j] = temp;
            }
            int[] rank = new int[MAX_SHIP_LENGTH + 1];
            for (int i = 0; i <= MAX_SHIP_LENGTH; i++) {
                rank[i] = i;
            }
            for (int i = MAX_SHIP_LENGTH; i > 1; i--) {
                state = (state * RNG_MULTIPLIER + 1) % RNG_MOD;
                int j = 1 + state % i;
                int temp = rank[i];
                rank[i] = rank[j];
                rank[j] = temp;
            }
            for (int i = 0; i < n; i++) {
                boxed[i] = ships[i];
            }
            Arrays.sort(boxed, (a, b) -> Integer.compare(rank[a], rank[b]));
            for (int i = 0; i < n; i++) {
                ships[i] = boxed[i];
            }
        }
        StringBuilder out = new StringBuilder();
        for (int r = 0; r < m; r++) {
            List<String> row = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (owner[i] == r) {
                    row.add(String.valueOf(ships[i]));
                }
            }
            out.append(row.size()).append('\n').append(String.join(" ", row)).append('\n');
        }
        System.out.print(out);
    }
}
