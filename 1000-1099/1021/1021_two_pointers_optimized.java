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

    static final int TARGET = 10000;
    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        // statement values fit signed 16 bits; Java promotes shorts in sums.
        short[] up = new short[n];
        for (int i = 0; i < n; i++)
            up[i] = (short)nextInt();
        int m = nextInt(), at = 0;
        boolean found = false;
        for (int j = 0; j < m; j++) {
            int value = nextInt();
            while (at < n && up[at] + value < TARGET)
                at++;
            if (at < n && up[at] + value == TARGET)
                found = true;
        }
        System.out.println(found ? "YES" : "NO");
    }
}
