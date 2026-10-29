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
        int n = nextInt();
        // the exclamation marks are counted byte by byte instead of reading them
        // as a string
        int step = 0;
        for (int ch = read(); ch >= 0; ch = read()) {
            if (ch == '!') {
                ++step;
            }
        }
        // multiply n, n - step, ... while the factor stays positive
        int product = 1;
        for (int factor = n; factor > 0; factor -= step) {
            product *= factor;
        }
        System.out.println(product);
    }
}
