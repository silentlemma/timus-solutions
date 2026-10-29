import java.io.IOException;

public class Main {
    static final int BUFFER_SIZE = 1024;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the numbers are parsed by hand from a small buffer, much lighter than Scanner
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

    static final int FAR = 2000; // beyond every coordinate

    public static void main(String[] args) throws IOException {
        int n = nextInt(), x = nextInt();
        // the nearest obstacles on both sides; walking away from the exit is
        // promised to meet one, so the one needed below always exists
        int left = -FAR, right = FAR;
        for (int i = 0; i < n; i++) {
            int w = nextInt();
            if (w < 0)
                left = Math.max(left, w);
            else
                right = Math.min(right, w);
        }
        if (x < left || x > right)
            System.out.println("Impossible"); // an obstacle stands between the start and the exit
        else if (x > 0)
            System.out.println(x + " " + (-2 * left + x));
        else
            System.out.println((2 * right - x) + " " + (-x));
    }
}
