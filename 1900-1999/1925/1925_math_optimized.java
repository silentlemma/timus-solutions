public class Main {
    private static final int BUFFER_SIZE = 1024;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int available;

    // the input is read in 1 KB blocks and parsed by hand, which needs much
    // less memory than Scanner
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
        int count = nextInt();
        // the readings are added up as they are read, so they are never stored
        int answer = nextInt() - 2;
        for (int i = 0; i < count; ++i) {
            int displayed = nextInt();
            int entered = nextInt();
            answer += displayed - entered - 2;
        }
        System.out.println(answer >= 0 ? Integer.toString(answer) : "Big Bang!");
    }
}
