public class Main {
    static final int MAX_LENGTH = 100000, CHARS = 128, CHAR_BITS = 7;

    // refillable storage keeps input memory constant, regardless of input length.
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int at, size;
    static int read() throws java.io.IOException {
        if (at == size) {
            size = System.in.read(buffer);
            at = 0;
            if (size < 0)
                return -1;
        }
        return buffer[at++];
    }
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        boolean negative = c == '-';
        if (negative)
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int row = (int)nextLong() - 1;
        // the encoded column has at most 100000 ascii characters.
        byte[] last = new byte[MAX_LENGTH];
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        int n = 0;
        while (c > ' ') {
            last[n++] = (byte)c;
            c = read();
        }
        // a stable counting sort of the last column: the row packed in order[j] ends
        // with the j-th character of the sorted column, the first one of row j
        int[] start = new int[CHARS + 1];
        for (int i = 0; i < n; i++)
            start[last[i] + 1]++;
        for (c = 0; c < CHARS; c++)
            start[c + 1] += start[c];
        // seven bits hold ascii and seventeen hold an index below 100000.
        int[] order = new int[n];
        for (int i = 0; i < n; i++)
            order[start[last[i]]++] = (i << CHAR_BITS) | last[i];
        java.io.BufferedOutputStream out = new java.io.BufferedOutputStream(System.out);
        for (int i = 0; i < n; i++) {
            int entry = order[row];
            out.write(entry & (CHARS - 1));
            row = entry >>> CHAR_BITS;
        }
        out.write('\n');
        out.flush();
    }
}
