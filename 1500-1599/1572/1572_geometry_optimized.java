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

    // four times the square of the shortest longest chord of a cover of side or
    // radius 1: a circle's diameter, a square's side, a triangle's height
    static final int[] NARROWEST = {0, 16, 4, 3};
    // four times the square of the longest segment in a hole: a circle's
    // diameter, a square's diagonal, a triangle's side
    static final int[] WIDEST = {0, 16, 8, 4};

    public static void main(String[] args) throws java.io.IOException {
        int kind = nextInt(), size = nextInt();
        int hole = WIDEST[kind] * size * size;
        int n = nextInt(), count = 0;
        // a cover held upright crosses the plane of the hole along parallel chords,
        // so it passes when its longest chord in some direction fits in the hole
        for (int i = 0; i < n; i++) {
            kind = nextInt();
            size = nextInt();
            if (NARROWEST[kind] * size * size <= hole)
                count++;
        }
        System.out.println(count);
    }
}
