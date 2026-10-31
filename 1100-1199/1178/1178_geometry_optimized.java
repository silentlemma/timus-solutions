import java.util.Arrays;
public class Main {

    // refill a small buffer instead of retaining the input or allocating tokens.
    static final int BUFFER_SIZE = 4096;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, length;
    static int read() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(BUFFER);
            position = 0;
            if (length < 0)
                return -1;
        }
        return BUFFER[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value * sign;
    }

    static final int MAX_COORD = 1000000000;
    static final int INDEX_BITS = 14;
    static final long INDEX_MASK = (1L << INDEX_BITS) - 1;
    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        long[] cities = new long[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nextInt();
            y[i] = nextInt();
            // shifted x needs 31 bits, index needs 14; the key fits in signed long.
            cities[i] = ((long)(x + MAX_COORD) << INDEX_BITS) | i;
        }
        Arrays.sort(cities);
        // no three collinear means at most two equal x values; order such a pair by y.
        for (int i = 1; i < n; i++) {
            if ((cities[i - 1] >> INDEX_BITS) == (cities[i] >> INDEX_BITS) &&
                y[(int)(cities[i - 1] & INDEX_MASK)] > y[(int)(cities[i] & INDEX_MASK)]) {
                long swap = cities[i];
                cities[i] = cities[i - 1];
                cities[i - 1] = swap;
            }
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i += 2) {
            out.append((cities[i] & INDEX_MASK) + 1)
                .append(' ')
                .append((cities[i + 1] & INDEX_MASK) + 1)
                .append('\n');
        }
        System.out.print(out);
    }
}
