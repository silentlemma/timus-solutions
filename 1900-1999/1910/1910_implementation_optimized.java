import java.io.IOException;

public class Main {
    private static final int BUFFER_SIZE = 1 << 10;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int length;

    // the input is read in blocks and parsed by hand instead of Scanner
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
        // the sections are not stored: only the two before the current one are kept
        int previous = readInt();
        int last = readInt();
        int best = 0;
        int position = 2;
        for (int middle = 2; middle < n; middle++) {
            int value = readInt();
            int sum = previous + last + value;
            if (sum > best) {
                best = sum;
                position = middle;
            }
            previous = last;
            last = value;
        }
        System.out.println(best + " " + position);
    }
}
