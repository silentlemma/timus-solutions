public class Main {
    static final int INPUT_SIZE = 128;
    static final byte[] input = new byte[INPUT_SIZE];
    static int position, available;

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
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), k = nextInt();
        // numbers of valid prefixes ending with a zero and with another digit,
        // where the first digit is not zero
        long zero = 0, other = k - 1;
        for (int i = 1; i < n; i++) {
            long nextZero = other;
            other = (zero + other) * (k - 1);
            zero = nextZero;
        }
        output(zero + other);
    }

    static final int DECIMAL = 10;
    static void output(long value) throws java.io.IOException {
        byte[] answer = input;
        int at = answer.length;
        answer[--at] = '\n';
        do {
            answer[--at] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        System.out.write(answer, at, answer.length - at);
    }
}
