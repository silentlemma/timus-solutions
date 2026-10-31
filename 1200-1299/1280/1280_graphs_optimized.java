import java.io.IOException;

public class Main {

    // refilling this buffer bounds input storage independently of input size.
    static final int INPUT_BUFFER = 4096;
    static final byte[] buffer = new byte[INPUT_BUFFER];
    static int pos, len;

    static int read() throws IOException {
        if (pos == len) {
            len = System.in.read(buffer);
            pos = 0;
            if (len <= 0)
                return -1;
        }
        return buffer[pos++];
    }

    static int next() throws IOException {
        int c = read();
        while (c != -1 && c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static final int WORD_BITS = Long.SIZE;
    public static void main(String[] args) throws IOException {
        int n = next(), m = next();
        int words = (n + WORD_BITS - 1) / WORD_BITS;
        // n <= 1000: one bit per possible rule replaces two integer arrays.
        long[] rules = new long[n * words];
        for (int i = 0; i < m; i++) {
            int from = next() - 1, to = next() - 1;
            rules[from * words + to / WORD_BITS] |= 1L << (to % WORD_BITS);
        }
        int[] place = new int[n];
        for (int i = 0; i < n; i++)
            place[next() - 1] = i;
        // the plan is right exactly when every rule points forward in it; a
        // rule from a subject to itself can never hold
        boolean ok = true;
        for (int from = 0; from < n; from++) {
            for (int to = 0; to < n; to++) {
                long bit = 1L << (to % WORD_BITS);
                if ((rules[from * words + to / WORD_BITS] & bit) != 0 && place[from] >= place[to])
                    ok = false;
            }
        }
        System.out.println(ok ? "YES" : "NO");
    }
}
