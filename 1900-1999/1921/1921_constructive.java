import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static int nextInt() throws IOException {
        int value;
        do {
            value = INPUT.read();
        } while (value <= ' ' && value >= 0);
        int result = 0;
        while (value > ' ') {
            result = result * 10 + value - '0';
            value = INPUT.read();
        }
        return result;
    }

    static String[] constructBoard(int rows, int columns, int palette, int level) {
        int target = level - 1;
        int longest = Math.max(rows, columns);
        int rowColors = Math.min(rows, 2);
        int columnColors = Math.min(columns, 2);
        if (longest < target || (palette == 1 && longest != target)
                || (palette > 1 && target == 1 && palette < rowColors * columnColors)) {
            return null;
        }
        String[] board = new String[rows];
        for (int row = 0; row < rows; ++row) {
            char[] line = new char[columns];
            for (int column = 0; column < columns; ++column) {
                int color = 0;
                if (palette > 1) {
                    if (target == 1) {
                        color = (row % 2) * columnColors + column % 2;
                    } else if (columns >= target) {
                        color = (row + column / target) % 2;
                    } else {
                        color = (column + row / target) % 2;
                    }
                }
                line[column] = (char) ('A' + color);
            }
            board[row] = new String(line);
        }
        return board;
    }

    public static void main(String[] args) throws IOException {
        int rows = nextInt();
        int columns = nextInt();
        int palette = nextInt();
        int level = nextInt();
        String[] board = constructBoard(rows, columns, palette, level);
        StringBuilder output = new StringBuilder();
        if (board == null) {
            output.append("NO\n");
        } else {
            output.append("YES\n");
            for (String row : board) {
                output.append(row).append('\n');
            }
        }
        System.out.print(output);
    }
}
