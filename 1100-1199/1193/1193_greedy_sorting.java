public class Main {
    static final int MAX_LONG_DIGITS = 20;
    static long nextLong() throws java.io.IOException {
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        boolean negative = c == '-';
        if (negative || c == '+')
            c = System.in.read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 - (c - '0');
            c = System.in.read();
        }
        return negative ? value : -value;
    }
    static int nextInt() throws java.io.IOException { return (int)nextLong(); }
    static final int OUTPUT_SIZE = 256, DECIMAL = 10;
    static final byte[] output = new byte[OUTPUT_SIZE];
    static int used;
    static void finish() {
        System.out.write(output, 0, used);
        used = 0;
    }
    static void write(int c) {
        if (used == output.length)
            finish();
        output[used++] = (byte)c;
    }
    static void number(long value) {
        if (value < 0)
            write('-');
        long remaining = value > 0 ? -value : value;
        int first = used;
        // Each real answer here has at most20digits; reserve before reversing.
        if (used + MAX_LONG_DIGITS >= output.length) {
            finish();
            first = 0;
        }
        do {
            output[used++] = (byte)('0' - remaining % DECIMAL);
            remaining /= DECIMAL;
        } while (remaining != 0);
        for (int left = first, right = used - 1; left < right; left++, right--) {
            byte saved = output[left];
            output[left] = output[right];
            output[right] = saved;
        }
    }
    static final int MAX_READY = 600, TALK_SHIFT = 10, DEADLINE_MASK = 1023;
    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        int[] at = new int[MAX_READY + 1];
        int first = MAX_READY, last = 0;
        for (int i = 0; i < n; i++) {
            int ready = nextInt(), talk = nextInt(), deadline = nextInt();
            at[ready] = (talk << TALK_SHIFT) | deadline;
            first = Math.min(first, ready);
            last = Math.max(last, ready);
        }
        int busy = 0, worst = 0;
        for (int ready = first; ready <= last; ready++) {
            int record = at[ready];
            if (record != 0) {
                busy = Math.max(busy, ready) + (record >>> TALK_SHIFT);
                worst = Math.max(worst, busy - (record & DEADLINE_MASK));
            }
        }
        number(worst);
        write('\n');
        finish();
    }
}
