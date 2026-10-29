public class Main {
    private static final int BUFFER_SIZE = 1024;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int available;

    // the input is read in 1 KB blocks and each word is only measured, byte by
    // byte, instead of joining the lines and splitting them into strings
    private static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = read();
        } while (ch <= ' ' && ch >= 0);
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int height = nextInt();
        int width = nextInt();
        int count = nextInt();
        int lines = 1;
        int used = -1;
        for (int i = 0; i < count; ++i) {
            int ch;
            do {
                ch = read();
            } while (ch <= ' ' && ch >= 0);
            int length = 0;
            while (ch > ' ') {
                ++length;
                ch = read();
            }
            // a word after another one on the line needs a space before it
            if (used + 1 + length > width) {
                ++lines;
                used = -1;
            }
            used += 1 + length;
        }
        System.out.println((lines + height - 1) / height);
    }
}
