import java.util.Arrays;
public class Main {

    static final int INPUT_BUFFER = 4096;
    // refill instead of retaining the input; tokens may cross buffer boundaries.
    static final byte[] buffer = new byte[INPUT_BUFFER];
    static int position, size;
    static int read() throws java.io.IOException {
        if (position == size) {
            size = System.in.read(buffer);
            position = 0;
            if (size < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c != '-' && (c < '0' || c > '9'))
            c = read();
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

    public static void main(String[] args) throws java.io.IOException {
        int m = nextInt(), n = nextInt(), k = nextInt();
        int stride = n + 2, columnStride = m + 2;
        // row-major and column-major keys are below 901 million since dimensions <= 30000.
        int[] rows = new int[k], columns = new int[k];
        for (int i = 0; i < k; i++) {
            int x = nextInt(), y = nextInt();
            rows[i] = x * stride + y;
            columns[i] = y * columnStride + x;
        }
        Arrays.sort(rows);
        Arrays.sort(columns);
        int answer = 0, at = 0;
        for (int x = 1; x <= m; x++) {
            int previous = 0;
            while (true) {
                int next = at < k && rows[at] / stride == x ? rows[at++] % stride : n + 1;
                int length = next - previous - 1, cell = x * stride + previous + 1;
                if (length >= 2 ||
                    (length == 1 && (x == 1 || Arrays.binarySearch(rows, cell - stride) >= 0) &&
                     (x == m || Arrays.binarySearch(rows, cell + stride) >= 0)))
                    answer++;
                if (next == n + 1)
                    break;
                previous = next;
            }
        }
        at = 0;
        for (int y = 1; y <= n; y++) {
            int previous = 0;
            while (true) {
                int next = at < k && columns[at] / columnStride == y ? columns[at++] % columnStride
                                                                     : m + 1;
                if (next - previous - 1 >= 2)
                    answer++;
                if (next == m + 1)
                    break;
                previous = next;
            }
        }
        System.out.println(answer);
    }
}
