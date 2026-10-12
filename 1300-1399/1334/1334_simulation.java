import java.util.Scanner;

public class Main {
    static final int SIZE = 8;
    static final int[][] DIAGONALS = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    static int[][] board = new int[SIZE][SIZE]; // 0 empty, 1 white, 2 black

    static boolean inside(int c, int r) { return c >= 0 && c < SIZE && r >= 0 && r < SIZE; }

    // some checker has a checker of the other color next to it on a diagonal
    // and a free square right behind that one
    static boolean canCapture() {
        for (int c = 0; c < SIZE; c++) {
            for (int r = 0; r < SIZE; r++) {
                if (board[c][r] == 0)
                    continue;
                for (int[] d : DIAGONALS) {
                    int oc = c + d[0], or = r + d[1], lc = c + 2 * d[0], lr = r + 2 * d[1];
                    if (inside(lc, lr) && board[oc][or] != 0 && board[oc][or] != board[c][r] &&
                        board[lc][lr] == 0)
                        return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for (int number = 1; in.hasNext(); number++) {
            String move = in.next().toLowerCase();
            int c = move.charAt(0) - 'a', r = Integer.parseInt(move.substring(1)) - 1;
            board[c][r] = number % 2 == 1 ? 1 : 2; // white moves on the odd lines
            if (canCapture()) {
                System.out.println(number);
                return;
            }
        }
        System.out.println("Draw");
    }
}
