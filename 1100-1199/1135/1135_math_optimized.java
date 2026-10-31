public class Main {
    static final int BUFFER_SIZE = 4096;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, length;
    static int read() throws java.io.IOException {
        if (length < 0)
            return -1;
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

    public static void main(String[] args) throws java.io.IOException {
        int remaining = nextInt();
        long right = 0, turns = 0;
        // Each left-facing person contributes all earlier right-facing people.
        while (remaining > 0) {
            int c = read();
            if (c < 0)
                break;
            if (c == '>') {
                right++;
                remaining--;
            } else if (c == '<') {
                turns += right;
                remaining--;
            }
        }
        System.out.println(turns);
    }
}
