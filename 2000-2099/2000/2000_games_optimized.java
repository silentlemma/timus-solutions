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

    static int firstScore(char[] values, int first, int second, int total) {
        int score = 0;
        if (first == second) {
            int left = 0;
            for (int i = 0; i < first; i++)
                left += values[i];
            score = values[first] + Math.max(left, total - left - values[first]);
        } else if (first < second) {
            int boundary = (first + second) / 2;
            for (int i = 0; i <= boundary; i++)
                score += values[i];
        } else {
            int boundary = (first + second + 1) / 2;
            for (int i = boundary; i < values.length; i++)
                score += values[i];
        }
        return score;
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = nextInt(), total = 0;
        // Values <= 10000 fit unsigned16bits; total <= 100000*10000 fits int.
        char[] values = new char[count];
        for (int i = 0; i < count; i++) {
            values[i] = (char)nextInt();
            total += values[i];
        }
        int first = nextInt() - 1, second = nextInt() - 1;
        int score = firstScore(values, first, second, total);
        number(score);
        write(' ');
        number(total - score);
        write('\n');
        finish();
    }
}
