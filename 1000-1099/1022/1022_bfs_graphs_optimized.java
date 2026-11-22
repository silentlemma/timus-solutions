public class Main {
    static final int MAX_DECIMAL_DIGITS = 10, OUTPUT_BUFFER_SIZE = 4096;
    static final byte[] output = new byte[OUTPUT_BUFFER_SIZE];
    static int outputCount;

    static void flushOutput() throws java.io.IOException {
        System.out.write(output, 0, outputCount);
        outputCount = 0;
    }

    static void emit(int value, int delimiter) throws java.io.IOException {
        if (outputCount + MAX_DECIMAL_DIGITS + 1 > output.length)
            flushOutput();
        int first = outputCount;
        do {
            output[outputCount++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        for (int left = first, right = outputCount - 1; left < right; left++, right--) {
            byte temporary = output[left];
            output[left] = output[right];
            output[right] = temporary;
        }
        output[outputCount++] = (byte)delimiter;
    }

    static void finishOutput() throws java.io.IOException {
        flushOutput();
        System.out.flush();
    }

    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong(), words = (n + Long.SIZE - 1) / Long.SIZE;
        long[][] children = new long[n][words];
        int[] parents = new int[n], queue = new int[n];
        for (int v = 0; v < n; v++)
            for (int c; (c = (int)nextLong()) != 0;) {
                int index = c - 1, word = index / Long.SIZE;
                long bit = 1L << (index % Long.SIZE);
                if ((children[v][word] & bit) == 0) {
                    children[v][word] |= bit;
                    parents[index]++;
                }
            }
        int size = 0;
        for (int v = 0; v < n; v++)
            if (parents[v] == 0)
                queue[size++] = v;
        // Scan only set child bits, not every absent edge in the boolean matrix.
        for (int i = 0; i < size; i++)
            for (int word = 0; word < words; word++) {
                long options = children[queue[i]][word];
                while (options != 0) {
                    int child = word * Long.SIZE + Long.numberOfTrailingZeros(options);
                    if (--parents[child] == 0)
                        queue[size++] = child;
                    options &= options - 1;
                }
            }
        for (int i = 0; i < size; i++)
            emit(queue[i] + 1, i + 1 == size ? '\n' : ' ');
        finishOutput();
    }
}
