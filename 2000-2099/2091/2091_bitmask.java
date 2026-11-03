public class Main {
    static final int WORD_BITS = 64, GROUPS = 4;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

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
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), m = nextInt();
        long[] low = new long[m], high = new long[m];
        int[] counts = new int[m];
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (nextInt() != 0) {
                    counts[c]++;
                    if (r < WORD_BITS)
                        low[c] |= 1L << r;
                    else
                        high[c] |= 1L << (r - WORD_BITS);
                }
            }
        }
        int best = n + 1, first = 0, second = 1;
        for (int a = 0; a < m; a++) {
            for (int b = a + 1; b < m; b++) {
                // Both is the intersection; other groups follow by subtraction.
                int both = Long.bitCount(low[a] & low[b]) + Long.bitCount(high[a] & high[b]);
                int score = Math.max(Math.max(both, counts[a] - both),
                                     Math.max(counts[b] - both, n - counts[a] - counts[b] + both));
                if (score < best) {
                    best = score;
                    first = a;
                    second = b;
                }
                if (best == (n + GROUPS - 1) / GROUPS) {
                    System.out.println(best + "\n" + (first + 1) + " " + (second + 1));
                    return;
                }
            }
        }
        System.out.println(best + "\n" + (first + 1) + " " + (second + 1));
    }
}
