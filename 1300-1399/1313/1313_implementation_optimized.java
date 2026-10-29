import java.io.IOException;

public class Main {
    private static final int MAX_OUTPUT_WIDTH = 4;
    private static final int HUNDREDS_PLACE = 100;
    private static final int BUFFER_SIZE = 1 << 10;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int length;

    // the numbers are parsed by hand from a small buffer, faster than StringTokenizer
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
        // every number is at most 100, so the picture is one flat byte array
        byte[] grid = new byte[n * n];
        for (int i = 0; i < grid.length; i++) {
            grid[i] = (byte)readInt();
        }
        // the numbers are written digit by digit into a 1 KB buffer
        byte[] out = new byte[BUFFER_SIZE];
        int used = 0;
        // diagonal holds the cells with row + column = diagonal; each is read from
        // its lowest row up
        for (int diagonal = 0; diagonal < 2 * n - 1; diagonal++) {
            int low = Math.max(0, diagonal - n + 1);
            for (int row = Math.min(diagonal, n - 1); row >= low; row--) {
                if (used + MAX_OUTPUT_WIDTH > out.length) {
                    System.out.write(out, 0, used);
                    used = 0;
                }
                int value = grid[row * n + diagonal - row];
                if (value >= HUNDREDS_PLACE) {
                    out[used++] = '1';
                }
                if (value >= 10) {
                    out[used++] = (byte)('0' + value / 10 % 10);
                }
                out[used++] = (byte)('0' + value % 10);
                out[used++] = ' ';
            }
        }
        out[used - 1] = '\n';
        System.out.write(out, 0, used);
    }
}
