import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int ROWS = 7;
    private static final int COLUMNS = 9;
    private static final int CONNECT = 4;
    private static final int DIRECTION_COUNT = 4;
    private static final int MAX_MOVES = ROWS * COLUMNS;
    private static final int FIRST_WIN = 2 * (CONNECT - 1);
    private static final int[] SHIFTS = new int[DIRECTION_COUNT];
    private static final long[] MASKS = new long[DIRECTION_COUNT];

    private static void makeMasks() {
        int[] rowSteps = {1, 0, 1, -1};
        int[] columnSteps = {0, 1, 1, 1};
        for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
            int dr = rowSteps[direction];
            int dc = columnSteps[direction];
            SHIFTS[direction] = dc * ROWS + dr;
            for (int column = 0; column < COLUMNS; column++) {
                for (int row = 0; row < ROWS; row++) {
                    int endRow = row + (CONNECT - 1) * dr;
                    int endColumn = column + (CONNECT - 1) * dc;
                    if (endRow >= 0 && endRow < ROWS && endColumn < COLUMNS) {
                        MASKS[direction] |= 1L << (column * ROWS + row);
                    }
                }
            }
        }
    }

    private static boolean hasWon(long board) {
        for (int direction = 0; direction < DIRECTION_COUNT; direction++) {
            int shift = SHIFTS[direction];
            long pair = board & (board >>> shift);
            // The mask excludes lines that wrap across column boundaries.
            if ((pair & (pair >>> (2 * shift)) & MASKS[direction]) != 0) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        char[] moves = reader.readLine().trim().toCharArray();
        makeMasks();
        int wins = 0;
        int draws = 0;
        for (int start = 0; start < moves.length; start++) {
            int[] heights = new int[COLUMNS];
            long[] boards = new long[2];
            int placed = 0;
            int limit = Math.min(MAX_MOVES, moves.length - start);
            for (int turn = 0; turn < limit; turn++) {
                int column = moves[start + turn] - '1';
                if (heights[column] < ROWS) {
                    int player = turn & 1;
                    boards[player] |= 1L << (column * ROWS + heights[column]);
                    heights[column]++;
                    placed++;
                    if (turn >= FIRST_WIN && hasWon(boards[player])) {
                        wins++;
                        break;
                    }
                }
                if (turn + 1 == MAX_MOVES && placed == MAX_MOVES) {
                    draws++;
                }
            }
        }
        System.out.println(wins + " " + draws);
    }
}
