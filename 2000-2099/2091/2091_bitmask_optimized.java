public class Main {

    static final int INPUT_SIZE = 16384, OUTPUT_SIZE = 1024, DIGITS = 10, DECIMAL = 10;
    static final byte[] input = new byte[INPUT_SIZE], output = new byte[OUTPUT_SIZE],
                        digits = new byte[DIGITS];
    static int position, available, used;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return value;
    }

    static void write(int c) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }

    static void number(int value) {
        int length = 0;
        do {
            digits[length++] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        while (length > 0)
            write(digits[--length]);
    }

    static void finish() { System.out.write(output, 0, used); }

    static final int WORD_BITS = Long.SIZE, GROUPS = 4;

    static boolean nextBit() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        return c == '1';
    }

    static int[] choose(long[] bits, byte[] counts, int n, int m) {
        int[] bound = new int[m];
        for (int c = 0; c < m; c++)
            bound[c] = (Math.max(counts[c], n - counts[c]) + 1) / 2;
        int[] head = new int[(n + 1) / 2 + 1], next = new int[m], order = new int[m];
        java.util.Arrays.fill(head, -1);
        for (int c = m - 1; c >= 0; c--) {
            next[c] = head[bound[c]];
            head[bound[c]] = c;
        }
        int used = 0;
        for (int minimum = 0; minimum < head.length; minimum++)
            for (int c = head[minimum]; c != -1; c = next[c])
                order[used++] = c;
        int best = n + 1, first = 0, second = 1;
        int optimumBound = (n + GROUPS - 1) / GROUPS;
        for (int left = 0; left < m; left++) {
            int a = order[left];
            if (bound[a] >= best)
                break;
            for (int right = left + 1; right < m; right++) {
                int b = order[right];
                // Bounds are nondecreasing; all following pairs are no better.
                if (bound[b] >= best)
                    break;
                int both = Long.bitCount(bits[2 * a] & bits[2 * b]) +
                           Long.bitCount(bits[2 * a + 1] & bits[2 * b + 1]);
                int score = Math.max(Math.max(both, counts[a] - both),
                                     Math.max(counts[b] - both, n - counts[a] - counts[b] + both));
                if (score < best) {
                    best = score;
                    first = a;
                    second = b;
                }
                if (best == optimumBound)
                    return new int[] {best, first, second};
            }
        }
        return new int[] {best, first, second};
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), m = nextInt();
        long[] bits = new long[2 * m];
        byte[] counts = new byte[m];
        for (int r = 0; r < n; r++)
            for (int c = 0; c < m; c++)
                if (nextBit()) {
                    counts[c]++;
                    bits[2 * c + r / WORD_BITS] |= 1L << (r % WORD_BITS);
                }
        int[] answer = choose(bits, counts, n, m);
        number(answer[0]);
        write('\n');
        number(answer[1] + 1);
        write(' ');
        number(answer[2] + 1);
        write('\n');
        finish();
    }
}
