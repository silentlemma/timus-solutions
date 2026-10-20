import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final long MOD = 1_000_000_007L;
    private static final int BUFFER_SIZE = 65536;

    private static int rows;
    private static int columns;
    private static boolean[] blockedAbove;
    private static boolean[] blockedLeft;

    private static class FastScanner {
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
            int symbol;
            do {
                symbol = read();
            } while (symbol <= ' ' && symbol != -1);
            int value = 0;
            while (symbol > ' ') {
                value = value * 10 + symbol - '0';
                symbol = read();
            }
            return value;
        }
    }

    private static long[] countPaths(int startRow, int startColumn) {
        long[] ways = new long[columns];
        long upper = 0;
        for (int row = startRow; row < rows; row++) {
            int offset = row * columns;
            for (int column = startColumn; column < columns; column++) {
                int position = offset + column;
                if (row == startRow && column == startColumn) {
                    ways[column] = 1;
                    continue;
                }
                long value = blockedAbove[position] ? 0 : ways[column];
                if (column > startColumn && !blockedLeft[position]) {
                    value += ways[column - 1];
                }
                if (value >= MOD) {
                    value -= MOD;
                }
                ways[column] = value;
            }
            if (row == rows - 2) {
                upper = ways[columns - 1];
            }
        }
        return new long[] {upper, ways[columns - 2]};
    }

    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner();
        rows = input.nextInt();
        columns = input.nextInt();
        int missing = input.nextInt();
        blockedAbove = new boolean[rows * columns];
        blockedLeft = new boolean[rows * columns];
        for (int edge = 0; edge < missing; edge++) {
            int firstRow = input.nextInt() - 1;
            int firstColumn = input.nextInt() - 1;
            int secondRow = input.nextInt() - 1;
            int secondColumn = input.nextInt() - 1;
            if (firstRow == secondRow) {
                int column = Math.max(firstColumn, secondColumn);
                blockedLeft[firstRow * columns + column] = true;
            } else {
                int row = Math.max(firstRow, secondRow);
                blockedAbove[row * columns + firstColumn] = true;
            }
        }

        int last = rows * columns - 1;
        if (blockedLeft[1] || blockedAbove[columns] || blockedLeft[last] || blockedAbove[last]) {
            System.out.println(0);
            return;
        }

        long[] upper = countPaths(0, 1);
        long[] lower = countPaths(1, 0);
        // Tail swapping cancels intersecting path pairs in this determinant.
        long answer = (upper[0] * lower[1] % MOD - upper[1] * lower[0] % MOD + MOD) % MOD;
        System.out.println(2 * answer % MOD);
    }
}
