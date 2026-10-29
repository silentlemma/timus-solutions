import java.io.IOException;

public class Main {
    static final int BUFFER_SIZE = 1024;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the input is read in 1 KB blocks and parsed by hand, which needs much
    // less memory than Scanner
    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return buffer[position++];
    }

    static int nextInt() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws IOException {
        int x = nextInt(), y = nextInt();
        // each turn of the loop swaps x and y, and there are x + y turns; the
        // sum survives, so an odd sum of positive numbers means one swap
        if (x > 0 && y > 0 && (x + y) % 2 == 1) {
            int t = x;
            x = y;
            y = t;
        }
        System.out.println(x + " " + y);
    }
}
