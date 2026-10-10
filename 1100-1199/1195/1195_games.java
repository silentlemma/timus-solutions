import java.util.Scanner;

public class Main {
    static final int[][] LINES = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6},
                                  {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}};
    // outcomes for the side to move: win, draw, loss
    static final int WIN = 1, DRAW = 0, LOSS = -1;
    static char[] board;

    static boolean won(char mark) {
        for (int[] line : LINES) {
            if (board[line[0]] == mark && board[line[1]] == mark && board[line[2]] == mark) {
                return true;
            }
        }
        return false;
    }

    // the best outcome for the side about to move with mark
    static int play(char mark, char other) {
        int best = LOSS;
        boolean moved = false;
        for (int i = 0; i < board.length; i++) {
            if (board[i] == '#') {
                moved = true;
                board[i] = mark;
                best = Math.max(best, won(mark) ? WIN : -play(other, mark));
                board[i] = '#';
            }
        }
        return moved ? best : DRAW;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder rows = new StringBuilder();
        while (in.hasNext()) {
            rows.append(in.next());
        }
        board = rows.toString().toCharArray();
        // three moves each have been made, so crosses move now
        int result = play('X', 'O');
        System.out.println(result == WIN ? "Crosses win" : result == DRAW ? "Draw" : "Ouths win");
    }
}
