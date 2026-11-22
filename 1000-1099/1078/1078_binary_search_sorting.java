import java.util.Arrays;

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
        boolean negative = c == '-';
        if (negative)
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    static final int OFFSET = 10000, COORDINATES = 20001, INDEX_BITS = 9;
    static final int INDEX_MASK = (1 << INDEX_BITS) - 1;
    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        long[] order = new long[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            int a = (int)nextLong(), b = (int)nextLong();
            if (a > b) {
                int t = a;
                a = b;
                b = t;
            }
            right[i] = b;
            order[i] = (((long)(a + OFFSET) * COORDINATES + b + OFFSET) << INDEX_BITS) | i;
        }
        Arrays.sort(order);
        int[] tails = new int[n], parent = new int[n];
        int size = 0;
        for (long key : order) {
            int id = (int)(key & INDEX_MASK), low = 0, high = size;
            // Increasing right endpoints in an equal-left group cannot extend a decreasing chain.
            while (low < high) {
                int middle = (low + high) / 2;
                if (right[tails[middle]] > right[id])
                    low = middle + 1;
                else
                    high = middle;
            }
            parent[id] = low == 0 ? -1 : tails[low - 1];
            tails[low] = id;
            if (low == size)
                size++;
        }
        emit(size, '\n');
        for (int id = tails[size - 1]; id >= 0; id = parent[id])
            emit(id + 1, parent[id] < 0 ? '\n' : ' ');
        finishOutput();
    }
}
