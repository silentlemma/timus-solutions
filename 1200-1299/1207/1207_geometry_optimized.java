import java.io.IOException;

public class Main {
    // refilling permits any input length while retaining only a small input chunk.
    private static final int BUFFER_SIZE = 4096;
    private static final byte[] BUFFER = new byte[BUFFER_SIZE];
    private static int position, length;
    // coordinates differ by at most 2000000; products and cross products fit in 64 bits.
    private static int[] x, y;

    private static int readByte() throws IOException {
        if (position == length) {
            length = System.in.read(BUFFER);
            position = 0;
            if (length < 0) {
                return -1;
            }
        }
        return BUFFER[position++];
    }

    private static int readInt() throws IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = readByte();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return sign * value;
    }

    private static boolean less(int i, int j) { return (long)x[i] * y[j] > (long)y[i] * x[j]; }

    private static void siftDown(int[] order, int root, int size) {
        int value = order[root];
        for (int child = root * 2 + 1; child < size; child = root * 2 + 1) {
            if (child + 1 < size && less(order[child], order[child + 1])) {
                child++;
            }
            if (!less(value, order[child])) {
                break;
            }
            order[root] = order[child];
            root = child;
        }
        order[root] = value;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        x = new int[n];
        y = new int[n];
        // the lowest point (the leftmost of the lowest) sees all others within
        // half a turn, so they can be sorted by angle with cross products
        int pivot = 0;
        for (int i = 0; i < n; i++) {
            x[i] = readInt();
            y[i] = readInt();
            if (y[i] < y[pivot] || (y[i] == y[pivot] && x[i] < x[pivot])) {
                pivot = i;
            }
        }
        int px = x[pivot], py = y[pivot];
        int[] order = new int[n - 1];
        for (int i = 0, k = 0; i < n; i++) {
            x[i] -= px;
            y[i] -= py;
            if (i != pivot) {
                order[k++] = i;
            }
        }
        // heap sort keeps primitive indices and needs no temporary array.
        for (int i = order.length / 2 - 1; i >= 0; i--) {
            siftDown(order, i, order.length);
        }
        for (int end = order.length - 1; end > 0; end--) {
            int value = order[0];
            order[0] = order[end];
            order[end] = value;
            siftDown(order, 0, end);
        }
        // the middle one leaves (n - 2) / 2 points on each side of the line
        System.out.println((pivot + 1) + " " + (order[(n - 2) / 2] + 1));
    }
}
