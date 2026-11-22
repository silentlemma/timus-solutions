public class Main {
    static final int BUFFER_SIZE = 512, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = nextInt(), total = 0, largest = 0;
        for (int i = 0; i < count; i++) {
            int clearance = nextInt();
            total += clearance;
            if (clearance > largest)
                largest = clearance;
        }
        output(total + largest);
    }
    static final int OUTPUT_DIGITS = 20, DECIMAL = 10;
    static void output(long value) {
        byte[] answer = new byte[OUTPUT_DIGITS + 1];
        int at = answer.length;
        answer[--at] = '\n';
        do {
            answer[--at] = (byte)('0' + value % DECIMAL);
            value /= DECIMAL;
        } while (value != 0);
        System.out.write(answer, at, answer.length - at);
    }
}
