import java.io.IOException;

public class Main {
    static final int BUFFER_SIZE = 1024;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the numbers are parsed by hand from a small buffer, much lighter than Scanner
    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return buffer[position++];
    }

    static int nextInt() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    static final int KNOWN_HUNGRY = 2, KNOWN_FULL = 10; // given in the statement

    // "hungry" and "satisfied" differ in the first letter; the rest is skipped
    static boolean nextIsHungry() throws IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        boolean hungry = c == 'h';
        while (c > ' ')
            c = read();
        return hungry;
    }

    public static void main(String[] args) throws IOException {
        int n = nextInt();
        int hungry = KNOWN_HUNGRY, full = KNOWN_FULL;
        for (int i = 0; i < n; i++) {
            int count = nextInt();
            if (nextIsHungry())
                hungry = Math.max(hungry, count);
            else
                full = Math.min(full, count);
        }
        // the smallest satisfying amount must exceed the largest hungry one
        System.out.println(full > hungry ? String.valueOf(full) : "Inconsistent");
    }
}
