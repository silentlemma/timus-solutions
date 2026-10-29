import java.io.IOException;

public class Main {
    private static final int BUFFER_SIZE = 1 << 10;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int length;

    // the numbers are parsed by hand from a small buffer, much lighter than Scanner
    private static int readByte() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int nextInt() throws IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = readByte();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value * sign;
    }

    public static void main(String[] args) throws IOException {
        int capacity = nextInt(), minutes = nextInt();
        int jam = 0;
        for (int i = 0; i < minutes; i++) {
            // the light lets capacity cars through, but never more than are waiting
            jam += nextInt() - capacity;
            if (jam < 0) {
                jam = 0;
            }
        }
        System.out.println(jam);
    }
}
