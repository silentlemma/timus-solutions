import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;
    private static final int SPACE = ' ';
    private static final byte WHITE = '.';
    private static final byte BLACK = '#';
    private static final byte NEWLINE = '\n';

    private static class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int current;
            do {
                current = read();
            } while (current <= SPACE);
            int value = 0;
            while (current > SPACE) {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }

        String next() throws IOException {
            int current;
            do {
                current = read();
            } while (current <= SPACE);
            StringBuilder token = new StringBuilder();
            while (current > SPACE) {
                token.append((char) current);
                current = read();
            }
            return token.toString();
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int m = input.nextInt();
        int limit = input.nextInt();
        int height = input.nextInt();
        int width = input.nextInt();
        int[] offsets = new int[height * width];
        int blackCount = 0;
        for (int row = 0; row < height; row++) {
            String pattern = input.next();
            for (int col = 0; col < width; col++) {
                if (pattern.charAt(col) == BLACK) {
                    offsets[blackCount++] = row * m + col;
                }
            }
        }

        byte[] board = new byte[n * m];
        byte[] placements = new byte[n * m];
        int repainted = 0;
        int count = input.nextInt();
        if (blackCount > 0) {
            for (int step = 1; step <= count; step++) {
                int row = input.nextInt() - 1;
                int col = input.nextInt() - 1;
                int base = row * m + col;
                // Two uses already repaint every black cell of this placement.
                if (placements[base] == 2) {
                    continue;
                }
                placements[base]++;
                for (int offset = 0; offset < blackCount; offset++) {
                    int cell = base + offsets[offset];
                    if (board[cell] == 0) {
                        board[cell] = 1;
                    } else if (board[cell] == 1) {
                        board[cell] = 2;
                        repainted++;
                        if (repainted == limit) {
                            System.out.println("Wasted after stamp #" + step);
                            return;
                        }
                    }
                }
            }
        }

        BufferedOutputStream output = new BufferedOutputStream(System.out);
        byte[] line = new byte[m + 1];
        line[m] = NEWLINE;
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                line[col] = board[row * m + col] == 0 ? WHITE : BLACK;
            }
            output.write(line);
        }
        output.flush();
    }
}
