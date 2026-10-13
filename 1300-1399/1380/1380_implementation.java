import java.util.Scanner;

public class Main {
    static final int SIZE = 8;
    static final int PAWN = 1, KNIGHT = 2, BISHOP = 3, ROOK = 4, QUEEN = 5, KING = 6;
    static final int TO_FILE = 3, TO_RANK = 4; // a move reads like e2-e4

    // row r is rank r + 1, column f is file a + f
    static int[][] board = new int[SIZE][SIZE];
    static int taken;

    static boolean inside(int f, int r) { return 0 <= f && f < SIZE && 0 <= r && r < SIZE; }

    // can the piece on (f, r) move to (tf, tr), ignoring checks
    static boolean reaches(int f, int r, int tf, int tr) {
        int piece = board[r][f], target = board[tr][tf];
        int side = Integer.signum(piece), kind = Math.abs(piece);
        int df = tf - f, dr = tr - r;
        if ((df == 0 && dr == 0) || target * side > 0)
            return false;
        if (kind == PAWN) {
            int home = side > 0 ? 1 : SIZE - 2; // a pawn may step two squares from here
            if (df == 0 && target == 0)
                return dr == side || (dr == 2 * side && r == home && board[r + side][f] == 0);
            return Math.abs(df) == 1 && dr == side && target * side < 0;
        }
        if (kind == KNIGHT)
            return Math.abs(df * dr) == 2;
        if (kind == KING)
            return Math.abs(df) <= 1 && Math.abs(dr) <= 1;
        boolean straight = df == 0 || dr == 0, diagonal = Math.abs(df) == Math.abs(dr);
        if (!((kind == BISHOP && diagonal) || (kind == ROOK && straight) ||
              (kind == QUEEN && (straight || diagonal))))
            return false;
        int sf = Integer.signum(df), sr = Integer.signum(dr);
        for (f += sf, r += sr; f != tf || r != tr; f += sf, r += sr)
            if (board[r][f] != 0)
                return false;
        return true;
    }

    // is any king of this side attacked
    static boolean inCheck(int side) {
        for (int kr = 0; kr < SIZE; kr++)
            for (int kf = 0; kf < SIZE; kf++)
                if (board[kr][kf] == KING * side)
                    for (int r = 0; r < SIZE; r++)
                        for (int f = 0; f < SIZE; f++)
                            if (board[r][f] * side < 0 && reaches(f, r, kf, kr))
                                return true;
        return false;
    }

    // makes the move if it is legal and keeps the piece it took in `taken`
    static boolean legal(int side, int f, int r, int tf, int tr) {
        if (!inside(f, r) || !inside(tf, tr) || board[r][f] * side <= 0 || !reaches(f, r, tf, tr))
            return false;
        taken = board[tr][tf];
        board[tr][tf] = board[r][f];
        board[r][f] = 0;
        if (inCheck(side)) {
            board[r][f] = board[tr][tf];
            board[tr][tf] = taken;
            return false;
        }
        return true;
    }

    static boolean hasMove(int side) {
        for (int r = 0; r < SIZE; r++)
            for (int f = 0; f < SIZE; f++)
                if (board[r][f] * side > 0)
                    for (int tr = 0; tr < SIZE; tr++)
                        for (int tf = 0; tf < SIZE; tf++)
                            if (legal(side, f, r, tf, tr)) {
                                board[r][f] = board[tr][tf];
                                board[tr][tf] = taken;
                                return true;
                            }
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for (int r = SIZE - 1; r >= 0; r--)
            for (int f = 0; f < SIZE; f++)
                board[r][f] = in.nextInt();
        int count = in.nextInt();
        int side = in.next().equals("White") ? 1 : -1;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < count; i++) {
            String move = in.next();
            int f = move.charAt(0) - 'a', r = move.charAt(1) - '1';
            int tf = move.charAt(TO_FILE) - 'a', tr = move.charAt(TO_RANK) - '1';
            if (!legal(side, f, r, tf, tr)) {
                out.append("Incorrect\n");
                break;
            }
            side = -side;
            boolean check = inCheck(side), free = hasMove(side);
            out.append(!free ? (check ? "Mate" : "Draw") : (check ? "Check" : "Correct"))
                .append('\n');
            if (!free)
                break;
        }
        out.append('\n');
        for (int r = SIZE - 1; r >= 0; r--)
            for (int f = 0; f < SIZE; f++)
                out.append(board[r][f]).append(f + 1 < SIZE ? ' ' : '\n');
        System.out.print(out);
    }
}
