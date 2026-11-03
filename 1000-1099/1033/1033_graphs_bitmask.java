public class Main {
    static final int SIDE_AREA = 9, ENTRANCE_SIDES = 4;
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

    public static void main(String[] args) throws Exception {
        int n = nextInt();
        long[] open = new long[n], seen = new long[n], front = new long[n];
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++) {
                int ch = read();
                while (ch <= ' ')
                    ch = read();
                if (ch == '.')
                    open[r] |= 1L << c;
            }
        seen[0] = front[0] = 1;
        seen[n - 1] = front[n - 1] = 1L << (n - 1);
        long active = 1 | (1L << (n - 1));
        // Each active-row event processes at least one previously unseen cell.
        while (active != 0) {
            int r = Long.numberOfTrailingZeros(active);
            active &= active - 1;
            long cells = front[r];
            front[r] = 0;
            for (int q = Math.max(0, r - 1); q <= Math.min(n - 1, r + 1); q++) {
                long next = q == r ? (cells << 1) | (cells >>> 1) : cells;
                next &= open[q] & ~seen[q];
                if (next != 0) {
                    seen[q] |= next;
                    front[q] |= next;
                    active |= 1L << q;
                }
            }
        }
        int sides = 0;
        for (int r = 0; r < n; r++) {
            sides += Long.bitCount(seen[r] & ~(open[r] << 1));
            sides += Long.bitCount(seen[r] & ~(open[r] >>> 1));
            sides += Long.bitCount(seen[r] & ~(r > 0 ? open[r - 1] : 0));
            sides += Long.bitCount(seen[r] & ~(r + 1 < n ? open[r + 1] : 0));
        }
        System.out.println((sides - ENTRANCE_SIDES) * SIDE_AREA);
    }
}
