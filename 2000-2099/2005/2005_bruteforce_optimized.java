public class Main {

    static final int INPUT_SIZE = 16384, OUTPUT_SIZE = 1024, DIGITS = 10, DECIMAL = 10;
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
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = read();
        }
        return value;
    }

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

    static final int POINTS = 5, END = POINTS - 1, FIRST_MIDDLE = 1, LAST_MIDDLE = 3;
    static final int MIDDLE_SUM = FIRST_MIDDLE + 2 + LAST_MIDDLE;

    static int[] bestRoute(int[] distance) {
        int best = Integer.MAX_VALUE, first = 0, second = 0, last = 0;
        // Penultimate index is 1 or 3; each choice leaves exactly two orders.
        for (int c = FIRST_MIDDLE; c <= LAST_MIDDLE; c += 2)
            for (int a = FIRST_MIDDLE; a <= LAST_MIDDLE; a++) {
                if (a == c)
                    continue;
                int b = MIDDLE_SUM - a - c;
                int cost = distance[a] + distance[a * POINTS + b] + distance[b * POINTS + c] +
                           distance[c * POINTS + END];
                if (cost < best) {
                    best = cost;
                    first = a;
                    second = b;
                    last = c;
                }
            }
        return new int[] {best, 0, first, second, last, END};
    }

    public static void main(String[] args) throws java.io.IOException {
        int[] distance = new int[POINTS * POINTS];
        for (int i = 0; i < distance.length; i++)
            distance[i] = nextInt();
        int[] route = bestRoute(distance);
        number(route[0]);
        write('\n');
        for (int i = 1; i < route.length; i++) {
            number(route[i] + 1);
            write(i + 1 < route.length ? ' ' : '\n');
        }
        finish();
    }
}
