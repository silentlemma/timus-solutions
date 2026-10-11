import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static final int NONE = 0, PAWN = 1, QUEEN = 2, ROOK = 3, BISHOP = 4, KNIGHT = 5;
    static final int[] PROMOTIONS = {QUEEN, ROOK, BISHOP, KNIGHT};
    static final int[][] KING = {{1, 0}, {-1, 0}, {0, 1},  {0, -1},
                                 {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    static final int[][] JUMPS = {{1, 2},   {2, 1},   {2, -1}, {1, -2},
                                  {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};
    // the double steps start from these rows, counted from 0
    static final int WHITE_START = 1, EN_PASSANT_ROW = 3;
    // a square is packed into 5 bits per coordinate in the memo keys
    static final int SHIFT = 5;
    // the king steps list the four straight directions before the diagonal ones
    static final int FIRST_DIAGONAL = 4;

    // a black move: what Black's pawn or piece is and where, and the king
    static class Reply {
        final int kind, bx, by, kx, ky;

        Reply(int kind, int bx, int by, int kx, int ky) {
            this.kind = kind;
            this.bx = bx;
            this.by = by;
            this.kx = kx;
            this.ky = ky;
        }
    }

    // a white move: where the pawn lands and what is left of Black's pawn or piece
    static class Option {
        final int wx, wy, kind, bx, by;

        Option(int wx, int wy, int kind, int bx, int by) {
            this.wx = wx;
            this.wy = wy;
            this.kind = kind;
            this.bx = bx;
            this.by = by;
        }
    }

    static int n;
    static Map<Long, Boolean> memo = new HashMap<>();

    static boolean inside(int x, int y) { return x >= 0 && x < n && y >= 0 && y < n; }

    // Squares the black piece can reach, ignoring the white pawn.
    static List<int[]> pieceMoves(int kind, int bx, int by, int kx, int ky) {
        List<int[]> out = new ArrayList<>();
        if (kind == KNIGHT) {
            for (int[] d : JUMPS) {
                int x = bx + d[0], y = by + d[1];
                if (inside(x, y) && !(x == kx && y == ky)) {
                    out.add(new int[] {x, y});
                }
            }
            return out;
        }
        // the queen uses all eight rays, the rook the first four, the bishop the last four
        int from = kind == BISHOP ? FIRST_DIAGONAL : 0, to = kind == ROOK ? FIRST_DIAGONAL
                                                                          : KING.length;
        for (int r = from; r < to; r++) {
            int x = bx + KING[r][0], y = by + KING[r][1];
            while (inside(x, y) && !(x == kx && y == ky)) {
                out.add(new int[] {x, y});
                x += KING[r][0];
                y += KING[r][1];
            }
        }
        return out;
    }

    // Whether White wins against every reply, Black to move.
    static boolean blackFails(int wx, int wy, int kind, int bx, int by, int kx, int ky) {
        if (Math.max(Math.abs(kx - wx), Math.abs(ky - wy)) == 1) {
            return false; // the king takes the pawn
        }
        if (kind == PAWN && by - 1 == wy && Math.abs(bx - wx) == 1) {
            return false;
        }
        List<int[]> squares = new ArrayList<>();
        if (kind != NONE && kind != PAWN) {
            squares = pieceMoves(kind, bx, by, kx, ky);
            for (int[] s : squares) {
                if (s[0] == wx && s[1] == wy) {
                    return false;
                }
            }
        }
        List<Reply> moves = new ArrayList<>();
        for (int[] d : KING) {
            int x = kx + d[0], y = ky + d[1];
            // the pawn attacks the two squares diagonally in front of it
            boolean attacked = y == wy + 1 && Math.abs(x - wx) == 1;
            if (inside(x, y) && !attacked && (kind == NONE || !(x == bx && y == by))) {
                moves.add(new Reply(kind, bx, by, x, y));
            }
        }
        if (kind == PAWN) {
            int ahead = by - 1;
            if (ahead >= 0 && free(bx, ahead, wx, wy, kx, ky)) {
                if (ahead == 0) {
                    for (int p : PROMOTIONS) {
                        moves.add(new Reply(p, bx, ahead, kx, ky));
                    }
                } else {
                    moves.add(new Reply(PAWN, bx, ahead, kx, ky));
                    if (by == n - 2 && free(bx, by - 2, wx, wy, kx, ky)) {
                        moves.add(new Reply(PAWN, bx, by - 2, kx, ky));
                    }
                }
            }
        } else if (kind != NONE) {
            for (int[] s : squares) {
                moves.add(new Reply(kind, s[0], s[1], kx, ky));
            }
        }
        if (moves.isEmpty()) {
            return false; // nothing to move: the pawn has not promoted
        }
        for (Reply m : moves) {
            if (!whiteWins(wx, wy, m.kind, m.bx, m.by, m.kx, m.ky)) {
                return false;
            }
        }
        return true;
    }

    static boolean free(int x, int y, int ax, int ay, int bx, int by) {
        return !(x == ax && y == ay) && !(x == bx && y == by);
    }

    static boolean whiteWins(int wx, int wy, int kind, int bx, int by, int kx, int ky) {
        long key = kind;
        for (int v : new int[] {wx, wy, bx + 1, by + 1, kx, ky}) {
            key = key << SHIFT | v;
        }
        Boolean known = memo.get(key);
        if (known != null) {
            return known;
        }
        memo.put(key, false);
        // the black pawn or piece no longer blocks once it is gone
        int px = kind == NONE ? -1 : bx, py = kind == NONE ? -1 : by;
        List<Option> options = new ArrayList<>();
        if (free(wx, wy + 1, kx, ky, px, py)) {
            options.add(new Option(wx, wy + 1, kind, bx, by));
            if (wy == WHITE_START && free(wx, wy + 2, kx, ky, px, py)) {
                // a black pawn beside the landing square takes it en passant
                boolean beside = kind == PAWN && by == EN_PASSANT_ROW && Math.abs(bx - wx) == 1;
                if (!beside) {
                    options.add(new Option(wx, wy + 2, kind, bx, by));
                }
            }
        }
        for (int dx = -1; dx <= 1; dx += 2) {
            if (kind != NONE && bx == wx + dx && by == wy + 1) {
                options.add(new Option(wx + dx, wy + 1, NONE, -1, -1));
            }
        }
        boolean result = false;
        for (Option o : options) {
            if (o.wy == n - 1 || blackFails(o.wx, o.wy, o.kind, o.bx, o.by, kx, ky)) {
                result = true;
                break;
            }
        }
        memo.put(key, result);
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        String w = in.next(), b = in.next(), k = in.next();
        boolean win = whiteWins(w.charAt(0) - 'a', Integer.parseInt(w.substring(1)) - 1, PAWN,
                                b.charAt(0) - 'a', Integer.parseInt(b.substring(1)) - 1,
                                k.charAt(0) - 'a', Integer.parseInt(k.substring(1)) - 1);
        System.out.println(win ? "WHITE WINS" : "BLACK WINS");
    }
}
