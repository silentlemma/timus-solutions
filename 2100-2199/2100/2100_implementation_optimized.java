import java.io.IOException;

public class Main {
    private static final int UNLUCKY = 13;
    private static final int PRICE = 100;
    private static final int BUFFER_SIZE = 1 << 10;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int length;

    // the input is read in 1 KB blocks, and the '+' signs of each reply are
    // counted byte by byte, instead of Scanner and strings
    private static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int readInt() throws IOException {
        int c;
        do {
            c = read();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        // the guests plus Marshall and Lily
        int people = n + 2;
        for (int i = 0; i < n; i++) {
            int c;
            do {
                c = read();
            } while (c <= ' ' && c != -1);
            while (c > ' ') {
                if (c == '+') {
                    people++;
                }
                c = read();
            }
        }
        // a dummy takes the extra seat
        if (people == UNLUCKY) {
            people++;
        }
        System.out.println(people * PRICE);
    }
}
