public class Main {
    // digits seen in the window
    static final int WINDOW = 10;
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the numbers are parsed by hand from a small buffer, much lighter than Scanner
    static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0)
                return -1;
        }
        return buffer[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt(), clicks = nextInt();
        // the digits are kept as bytes, ready to be written out
        byte[] digits = new byte[n];
        for (int i = 0; i < n; i++)
            digits[i] = (byte)('0' + nextInt());
        // each click moves the window one digit on, around the wheel
        byte[] out = new byte[WINDOW + 1];
        for (int i = 0; i < WINDOW; i++)
            out[i] = digits[(clicks + i) % n];
        out[WINDOW] = '\n';
        System.out.write(out);
    }
}
