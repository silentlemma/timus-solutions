import java.util.Locale;

public class Main {

    // refill a small buffer instead of retaining the input or allocating tokens.
    static final int BUFFER_SIZE = 4096;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, length;
    static int read() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(BUFFER);
            position = 0;
            if (length < 0)
                return -1;
        }
        return BUFFER[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
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

    static final int SIDES = 4;

    public static void main(String[] args) throws java.io.IOException {
        double a = nextInt(), r = nextInt();
        double half = a / 2, area;
        if (r <= half) {
            area = Math.PI * r * r;
        } else if (r * r >= 2 * half * half) {
            area = a * a;
        } else {
            // the circle minus the four caps cut off by the sides
            double cap = r * r * Math.acos(half / r) - half * Math.sqrt(r * r - half * half);
            area = Math.PI * r * r - SIDES * cap;
        }
        System.out.println(String.format(Locale.US, "%.3f", area));
    }
}
