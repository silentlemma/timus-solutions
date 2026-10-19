import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 65536;

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
            } while (current <= ' ' && current >= 0);
            int value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = input.nextInt();
        int m = input.nextInt();
        int lastDiagonal = n + m;
        long[][] rows = new long[n + 1][m + 1];
        long[][] diagonals = new long[lastDiagonal + 1][n + 1];
        long total = 0;
        for (int row = 1; row <= n; row++) {
            for (int column = 1; column <= m; column++) {
                long value = input.nextInt();
                rows[row][column] = rows[row][column - 1] + value;
                diagonals[row + column][row] = value;
                total += value;
            }
        }
        for (int sum = 2; sum <= lastDiagonal; sum++) {
            for (int row = 1; row <= n; row++) {
                diagonals[sum][row] += diagonals[sum][row - 1];
            }
        }

        int queries = input.nextInt();
        StringBuilder output = new StringBuilder();
        for (int query = 0; query < queries; query++) {
            int wind = input.nextInt();
            if (wind >= lastDiagonal - 2) {
                output.append(total).append(" 1 1\n");
                continue;
            }
            long[] below = new long[m + 1];
            long best = -1;
            int bestRow = 1;
            int bestColumn = 1;
            for (int row = n; row >= 1; row--) {
                int bottom = Math.min(n, row + wind + 1);
                for (int column = 1; column <= m; column++) {
                    int right = Math.min(m, column + wind);
                    long value = below[column] + rows[row][right] - rows[row][column - 1];
                    int sum = row + column + wind + 1;
                    // Moving upward adds a row and removes the old far diagonal.
                    if (sum <= lastDiagonal) {
                        value -= diagonals[sum][bottom] - diagonals[sum][row];
                    }
                    below[column] = value;
                    if (value > best || (value == best && row < bestRow)) {
                        best = value;
                        bestRow = row;
                        bestColumn = column;
                    }
                }
            }
            output.append(best).append(' ').append(bestRow).append(' ');
            output.append(bestColumn).append('\n');
        }
        System.out.print(output);
    }
}
