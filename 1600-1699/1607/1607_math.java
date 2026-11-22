public class Main {

    static int nextInt() throws java.io.IOException {
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    static final int OUTPUT_SIZE = 1024, DIGITS = 10, DECIMAL = 10;
    static final byte[] output = new byte[OUTPUT_SIZE], digits = new byte[DIGITS];
    static int used;

    static void write(int c) {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }

    static void number(int value) {
        int length = 0;
        do {
            digits[length++] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        while (length > 0)
            write(digits[--length]);
    }

    static void finish() { System.out.write(output, 0, used); }

    static int price(int a, int b, int c, int d) {
        if (a >= c)
            return a;
        // These full rounds end with the offers still strictly apart.
        int rounds = (c - a - 1) / (b + d);
        return Math.min(a + (rounds + 1) * b, c - rounds * d);
    }

    public static void main(String[] args) throws java.io.IOException {
        int a = nextInt(), b = nextInt(), c = nextInt(), d = nextInt();
        number(price(a, b, c, d));
        write('\n');
        finish();
    }
}
