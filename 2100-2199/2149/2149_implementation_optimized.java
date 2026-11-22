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

    static final int STEP = 5; // four characters of a pigeon and a separating column
    public static void main(String[] args) throws java.io.IOException {
        // halves counts the pigeons that break the pattern with the left half looking
        // left, parity those that break the pattern with even positions looking left,
        // and the two opposite patterns break exactly at the other pigeons
        int n = nextInt(), halves = 0, parity = 0;
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        // Only the first character of each pigeon affects the answer.
        for (int i = 0; i < n; i++) {
            boolean left = c == '<';
            if (left != (i < n / 2))
                halves++;
            if (left != (i % 2 == 0))
                parity++;
            int advance = i + 1 < n ? STEP : STEP - 1;
            while (advance-- > 0)
                c = read();
        }
        // The two lower rows cannot affect the four pattern distances.
        output(Math.min(Math.min(halves, n - halves), Math.min(parity, n - parity)));
    }

    static final int DECIMAL = 10, LONG_DIGITS = 20;
    static void output(long value) throws java.io.IOException {
        byte[] answer = new byte[LONG_DIGITS + 1];
        int at = answer.length;
        answer[--at] = '\n';
        do {
            answer[--at] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        System.out.write(answer, at, answer.length - at);
    }
}
