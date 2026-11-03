public class Main {
    static final int BUFFER_SIZE = 4096;
    static final int OUTPUT_BUFFER_SIZE = 24;
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
        int symbol = read();
        while (symbol <= ' ' && symbol != -1)
            symbol = read();
        int value = 0;
        while (symbol >= '0' && symbol <= '9') {
            value = value * 10 + symbol - '0';
            symbol = read();
        }
        return value;
    }

    static void siftDown(int[] values, int root, int size) {
        int value = values[root];
        for (int child = root * 2 + 1; child < size; child = root * 2 + 1) {
            if (child + 1 < size && values[child + 1] > values[child])
                child++;
            if (values[child] <= value)
                break;
            values[root] = values[child];
            root = child;
        }
        values[root] = value;
    }

    static void sort(int[] values) {
        for (int root = values.length / 2 - 1; root >= 0; root--)
            siftDown(values, root, values.length);
        for (int end = values.length - 1; end > 0; end--) {
            int maximum = values[0];
            values[0] = values[end];
            values[end] = maximum;
            siftDown(values, 0, end);
        }
    }

    static int[] safeRemovals(int[] values, long budget) {
        sort(values);
        int removed = 0, spells = 0, active = 0;
        for (int start = 0; start < values.length;) {
            int end = start + 1;
            while (end < values.length && values[end] == values[start])
                end++;
            int count = end - start;
            long threshold = values[start];
            if (count * threshold > budget)
                break;
            if ((active + count) * threshold > budget) {
                spells++;
                active = 0;
            }
            active += count;
            removed += count;
            start = end;
        }
        return new int[] {removed, spells + (active > 0 ? 1 : 0)};
    }

    static int appendInt(byte[] output, int length, int value) {
        int first = length;
        do {
            output[length++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        for (int last = length - 1; first < last; first++, last--) {
            byte digit = output[first];
            output[first] = output[last];
            output[last] = digit;
        }
        return length;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        long budget = nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++)
            values[i] = nextInt();
        int[] answer = safeRemovals(values, budget);
        // Both answers are at most n<=1000; no string formatting is needed.
        byte[] output = new byte[OUTPUT_BUFFER_SIZE];
        int length = appendInt(output, 0, answer[0]);
        output[length++] = ' ';
        length = appendInt(output, length, answer[1]);
        output[length++] = '\n';
        System.out.write(output, 0, length);
        System.out.flush();
    }
}
