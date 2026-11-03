import java.io.IOException;

public class Main {
    static final int BUFFER_SIZE = 8192;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;
    static int read() throws IOException {
        if (position >= available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int nextInt() throws IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        // Accumulate negatively so -2147483648 does not overflow during parsing.
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 - (c - '0');
            c = read();
        }
        return negative ? value : -value;
    }
    public static void main(String[] args) throws IOException {
        int n = nextInt(), previous = nextInt(), left = 1;
        long best = -1;
        for (int right = 2; right <= n; right++) {
            int current = nextInt();
            long difference = (long)current - previous;
            if (difference < 0)
                difference = -difference;
            if (difference > best) {
                best = difference;
                left = right - 1;
            }
            previous = current;
        }
        System.out.println(left + " " + (left + 1));
    }
}
