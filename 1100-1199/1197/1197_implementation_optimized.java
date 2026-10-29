import java.io.IOException;

public class Main {
    // the numbers and the squares are read byte by byte from System.in instead
    // of Scanner
    private static int readInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    static final int SIDE = 8;
    static final int[][] JUMPS = {{1, 2},   {2, 1},   {2, -1}, {1, -2},
                                  {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};

    public static void main(String[] args) throws IOException {
        int n = readInt();
        // every answer is one digit, at most 8, so the output is two bytes per
        // square, written at once
        byte[] out = new byte[2 * n];
        for (int t = 0; t < n; t++) {
            int c;
            do {
                c = System.in.read();
            } while (c <= ' ');
            int col = c - 'a', row = System.in.read() - '1', count = 0;
            // the knight attacks every square one jump away that is on the board
            for (int[] jump : JUMPS) {
                int x = col + jump[0], r = row + jump[1];
                if (x >= 0 && x < SIDE && r >= 0 && r < SIDE) {
                    count++;
                }
            }
            out[2 * t] = (byte)('0' + count);
            out[2 * t + 1] = '\n';
        }
        System.out.write(out);
    }
}
