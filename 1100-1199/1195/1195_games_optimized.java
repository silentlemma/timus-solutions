public class Main {
    static final int SIDE = 3, CELLS = SIDE * SIDE;
    static final int[][] LINES = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6},
                                  {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}};
    static final int WIN = 1, DRAW = 0, LOSS = -1;
    static final char[] board = new char[CELLS];

    static boolean won(char mark) {
        for (int[] line : LINES)
            if (board[line[0]] == mark && board[line[1]] == mark && board[line[2]] == mark)
                return true;
        return false;
    }

    static int play(char mark, char other) {
        int best = LOSS;
        boolean moved = false;
        for (int cell = 0; cell < CELLS; cell++)
            if (board[cell] == '#') {
                moved = true;
                board[cell] = mark;
                int result = won(mark) ? WIN : -play(other, mark);
                board[cell] = '#';
                if (result == WIN)
                    return WIN;
                if (result > best)
                    best = result;
            }
        return moved ? best : DRAW;
    }

    public static void main(String[] args) throws Exception {
        for (int cell = 0; cell < CELLS; cell++) {
            int ch = System.in.read();
            while (ch <= ' ')
                ch = System.in.read();
            board[cell] = (char)ch;
        }
        int result = play('X', 'O');
        System.out.println(result == WIN ? "Crosses win" : result == DRAW ? "Draw" : "Ouths win");
    }
}
