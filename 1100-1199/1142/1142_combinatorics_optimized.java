public class Main {
    static final int BUFFER_SIZE = 1024, BYTE_MASK = 255, LARGEST = 10;
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
    static int next() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        if (c < 0 || c == '-')
            return -1;
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }
    public static void main(String[] args) throws java.io.IOException {
        long[] ways = new long[LARGEST + 1];
        ways[0] = 1;
        for (int n = 1; n <= LARGEST; n++) {
            long choose = 1;
            for (int k = 1; k <= n; k++) {
                choose = choose * (n - k + 1) / k;
                ways[n] += choose * ways[n - k];
            }
        }
        StringBuilder output = new StringBuilder();
        for (int n; (n = next()) >= 0;)
            output.append(ways[n]).append('\n');
        System.out.print(output);
    }
}
