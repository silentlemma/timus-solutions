public class Main {
    private static final int BUFFER_SIZE = 1024;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int available;

    // the input is read in 1 KB blocks and parsed by hand, which needs much
    // less memory than Scanner
    private static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = read();
        } while (ch <= ' ' && ch >= 0);
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = nextInt();
        int[] sizes = new int[count];
        // At most 101 groups: in-place insertion avoids loading Arrays.sort.
        for (int i = 0; i < count; ++i) {
            int value = nextInt(), j = i;
            while (j > 0 && sizes[j - 1] > value) {
                sizes[j] = sizes[j - 1];
                j--;
            }
            sizes[j] = value;
        }
        // win a majority of the groups, choosing the smallest ones; a group of s
        // voters needs s / 2 + 1 supporters
        int supporters = 0;
        for (int i = 0; i <= count / 2; ++i) {
            supporters += sizes[i] / 2 + 1;
        }
        output(supporters);
    }

    static final int DECIMAL = 10, LONG_DIGITS = 20;
    static void output(long value) throws java.io.IOException {
        byte[] answer = new byte[LONG_DIGITS + 1];
        int at = answer.length;
        answer[--at] = '\n';
        do {
            answer[--at] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        System.out.write(answer, at, answer.length - at);
    }
}
