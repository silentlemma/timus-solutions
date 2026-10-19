import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int DIRECTIONS = 4;
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static String nextToken() throws IOException {
        int value;
        do { value = INPUT.read(); } while (value <= ' ' && value >= 0);
        StringBuilder token = new StringBuilder();
        while (value > ' ') { token.append((char) value); value = INPUT.read(); }
        return token.toString();
    }

    private static void expand(int player, int color, int[][] neighbors, int[] degree,
                               int[] colors, int[] owners, int[][] territories, int[] sizes) {
        for (int cursor = 0; cursor < sizes[player]; ++cursor) {
            int cell = territories[player][cursor];
            for (int index = 0; index < degree[cell]; ++index) {
                int adjacent = neighbors[cell][index];
                if (owners[adjacent] == -1 && colors[adjacent] == color) {
                    owners[adjacent] = player;
                    territories[player][sizes[player]++] = adjacent;
                }
            }
        }
    }

    static int[] territorySizes(String[] board, int[] moves) {
        int rows = board.length, columns = board[0].length();
        int cells = rows * columns;
        int[] colors = new int[cells];
        int[][] neighbors = new int[cells][DIRECTIONS];
        int[] degree = new int[cells];
        for (int row = 0; row < rows; ++row) {
            for (int column = 0; column < columns; ++column) {
                int cell = row * columns + column;
                colors[cell] = board[row].charAt(column) - '0';
                if (row > 0) neighbors[cell][degree[cell]++] = cell - columns;
                if (row + 1 < rows) neighbors[cell][degree[cell]++] = cell + columns;
                if (column > 0) neighbors[cell][degree[cell]++] = cell - 1;
                if (column + 1 < columns) neighbors[cell][degree[cell]++] = cell + 1;
            }
        }
        int[] owners = new int[cells];
        Arrays.fill(owners, -1);
        int[][] territories = new int[2][cells];
        int[] sizes = new int[2];
        int[] seeds = {cells - columns, columns - 1};
        for (int player = 0; player < 2; ++player) {
            owners[seeds[player]] = player;
            territories[player][sizes[player]++] = seeds[player];
            expand(player, colors[seeds[player]], neighbors, degree, colors, owners,
                   territories, sizes);
        }
        for (int turn = 0; turn < moves.length; ++turn) {
            expand(turn % 2, moves[turn], neighbors, degree, colors, owners, territories, sizes);
        }
        return sizes;
    }

    public static void main(String[] args) throws IOException {
        int rows = Integer.parseInt(nextToken());
        int columns = Integer.parseInt(nextToken());
        String[] board = new String[rows];
        for (int row = 0; row < rows; ++row) board[row] = nextToken();
        int count = Integer.parseInt(nextToken());
        int[] moves = new int[count];
        for (int index = 0; index < count; ++index) moves[index] = Integer.parseInt(nextToken());
        int[] result = territorySizes(board, moves);
        System.out.println(result[0]);
        System.out.println(result[1]);
    }
}
