import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int SIDE = 5, PORT_COUNT = 4, CELLS = SIDE * SIDE, MIN_TILES = 3;
    private static final int TOP = 0, RIGHT = 1, BOTTOM = 2, LEFT = 3;
    private static final int[] ROW_STEP = {-1, 0, 1, 0}, COLUMN_STEP = {0, 1, 0, -1};
    private static final int[] OPPOSITE = {BOTTOM, LEFT, TOP, RIGHT};
    private static final int[][] CONNECTIONS = {{LEFT, BOTTOM, RIGHT, TOP},
                                                {RIGHT, TOP, LEFT, BOTTOM}};
    private static final char[] DIRECTIONS = {'L', 'R', 'U', 'D'};
    private static final int[] HOLE_ROW = {0, 0, 1, -1}, HOLE_COLUMN = {1, -1, 0, 0};

    static boolean winning(char[] board) {
        for (int side = 0; side < PORT_COUNT; ++side) {
            for (int offset = 0; offset < SIDE; ++offset) {
                int row = side == TOP ? 0 : (side == BOTTOM ? SIDE - 1 : offset);
                int column = side == LEFT ? 0 : (side == RIGHT ? SIDE - 1 : offset);
                int incoming = side, count = 0;
                boolean[] visited = new boolean[CELLS * PORT_COUNT], tiles = new boolean[CELLS];
                while (true) {
                    int index = row * SIDE + column, state = index * PORT_COUNT + incoming;
                    if (board[index] == '*' || visited[state])
                        break;
                    visited[state] = true;
                    if (!tiles[index]) {
                        tiles[index] = true;
                        ++count;
                    }
                    int outgoing = CONNECTIONS[board[index] == '/' ? 0 : 1][incoming];
                    row += ROW_STEP[outgoing];
                    column += COLUMN_STEP[outgoing];
                    if (row < 0 || row >= SIDE || column < 0 || column >= SIDE) {
                        if (outgoing != side && count >= MIN_TILES)
                            return true;
                        break;
                    }
                    incoming = OPPOSITE[outgoing];
                }
            }
        }
        return false;
    }

    static String solve(char[] board) {
        if (winning(board))
            return "WIN";
        int empty = 0;
        while (board[empty] != '*')
            ++empty;
        int row = empty / SIDE, column = empty % SIDE;
        for (int motion = 0; motion < PORT_COUNT; ++motion) {
            for (int amount = 1; amount < SIDE; ++amount) {
                int endRow = row + HOLE_ROW[motion] * amount;
                int endColumn = column + HOLE_COLUMN[motion] * amount;
                if (endRow < 0 || endRow >= SIDE || endColumn < 0 || endColumn >= SIDE)
                    continue;
                char[] changed = board.clone();
                int hole = empty;
                for (int step = 0; step < amount; ++step) {
                    int following = hole + HOLE_ROW[motion] * SIDE + HOLE_COLUMN[motion];
                    changed[hole] = changed[following];
                    changed[following] = '*';
                    hole = following;
                }
                if (winning(changed))
                    return Character.toString(DIRECTIONS[motion]) + amount;
            }
        }
        return "FAIL";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder board = new StringBuilder();
        for (int row = 0; row < SIDE; ++row)
            board.append(in.readLine().trim());
        System.out.println(solve(board.toString().toCharArray()));
    }
}
