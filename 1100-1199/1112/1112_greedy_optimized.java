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
        int n = nextInt();
        int[] left = new int[n], right = new int[n];
        for (int i = 0; i < n; i++) {
            left[i] = nextInt();
            right[i] = nextInt();
        }
        // n <= 99 makes stable insertion sort cheap and avoids comparator objects.
        for (int i = 1; i < n; i++) {
            int a = left[i], b = right[i], j = i;
            while (j > 0 && right[j - 1] > b) {
                left[j] = left[j - 1];
                right[j] = right[j - 1];
                j--;
            }
            left[j] = a;
            right[j] = b;
        }
        // selected intervals overwrite only input slots already consumed by the scan.
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (count == 0 || left[i] >= right[count - 1]) {
                left[count] = left[i];
                right[count++] = right[i];
            }
        }
        StringBuilder out = new StringBuilder().append(count).append('\n');
        for (int i = 0; i < count; i++)
            out.append(left[i]).append(' ').append(right[i]).append('\n');
        System.out.print(out);
    }
}
