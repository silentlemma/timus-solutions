public class Main {

    static final int INPUT_SIZE = 1024, OUTPUT_SIZE = 1024, DIGITS = 10, DECIMAL = 10;
    static final byte[] input = new byte[INPUT_SIZE], output = new byte[OUTPUT_SIZE],
                        digits = new byte[DIGITS];
    static int position, available, used;
    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }
    static void write(int c) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }
    static void number(int value) {
        if (value < 0) {
            write('-');
            value = -value;
        }
        int length = 0;
        do {
            digits[length++] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        while (length > 0)
            write(digits[--length]);
    }
    static void finish() { System.out.write(output, 0, used); }

    static void text(String value) {
        for (int i = 0; i < value.length(); i++)
            write(value.charAt(i));
    }

    static final int FAR = 2000;
    static boolean blocks(int exit, int wall) {
        return (exit > 0 && wall > 0 && wall < exit) || (exit < 0 && wall < 0 && wall > exit);
    }
    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), exit = nextInt(), left = -FAR, right = FAR;
        for (int i = 0; i < n; i++) {
            int wall = nextInt();
            if (blocks(exit, wall)) {
                text("Impossible\n");
                finish();
                return;
            }
            if (wall < 0)
                left = Math.max(left, wall);
            else
                right = Math.min(right, wall);
        }
        if (exit > 0) {
            number(exit);
            write(' ');
            number(exit - 2 * left);
        } else {
            number(2 * right - exit);
            write(' ');
            number(-exit);
        }
        write('\n');
        finish();
    }
}
