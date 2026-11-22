public class Main {
    static final int SIDE = 8, BUFFER_SIZE = 256, BYTE_MASK = 255;
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

    static int count(int column, int row) {
        int oneX = (column > 0 ? 1 : 0) + (column < SIDE - 1 ? 1 : 0);
        int twoX = (column > 1 ? 1 : 0) + (column < SIDE - 2 ? 1 : 0);
        int oneY = (row > 0 ? 1 : 0) + (row < SIDE - 1 ? 1 : 0);
        int twoY = (row > 1 ? 1 : 0) + (row < SIDE - 2 ? 1 : 0);
        return oneX * twoY + twoX * oneY;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        byte[] answer = new byte[2 * n];
        for (int i = 0; i < n; i++) {
            int c = read();
            while (c >= 0 && c <= ' ')
                c = read();
            int column = c - 'a', row = read() - '1';
            // The choices of a valid horizontal and vertical shift are independent.
            answer[2 * i] = (byte)('0' + count(column, row));
            answer[2 * i + 1] = '\n';
        }
        System.out.write(answer);
    }
}
