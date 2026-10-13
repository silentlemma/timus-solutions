import java.util.Scanner;

public class Main {
    static final int BLACK = 0, DRAW = 1, WHITE = 2; // results, better for white upwards
    static final int SIZE = 8;
    static final int SECOND = 6; // the black pawn may move two squares from rank 7
    static final int[][] DIAGONALS = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

    // memo[turn][bf][br][pf][pr]: the result plus one, 0 when unknown
    static int[][][][][] memo = new int[2][SIZE][SIZE][SIZE][SIZE];

    static boolean inside(int f, int r) { return f >= 0 && f < SIZE && r >= 0 && r < SIZE; }

    // can the bishop reach square (qf, qr) on an otherwise empty board?
    static boolean sees(int bf, int br, int qf, int qr) {
        for (int[] d : DIAGONALS)
            for (int f = bf + d[0], r = br + d[1]; inside(f, r); f += d[0], r += d[1])
                if (f == qf && r == qr)
                    return true;
        return false;
    }

    static int white(int bf, int br, int pf, int pr) {
        if (memo[0][bf][br][pf][pr] > 0)
            return memo[0][bf][br][pf][pr] - 1;
        int best = BLACK;
    search:
        for (int[] d : DIAGONALS)
            for (int f = bf + d[0], r = br + d[1]; inside(f, r); f += d[0], r += d[1]) {
                if (f == pf && r == pr) {
                    best = WHITE; // the bishop takes the pawn
                    break search;
                }
                best = Math.max(best, black(f, r, pf, pr));
            }
        memo[0][bf][br][pf][pr] = best + 1;
        return best;
    }

    static int black(int bf, int br, int pf, int pr) {
        if (memo[1][bf][br][pf][pr] > 0)
            return memo[1][bf][br][pf][pr] - 1;
        int best = WHITE + 1; // no move yet
        if (br == pr - 1 && (bf == pf - 1 || bf == pf + 1))
            best = BLACK; // the pawn takes the bishop and cannot be stopped
        if (!(bf == pf && br == pr - 1)) {
            if (pr - 1 == 0)
                // a queen: white wins only by taking it at once
                best = Math.min(best, sees(bf, br, pf, 0) ? WHITE : BLACK);
            else {
                best = Math.min(best, white(bf, br, pf, pr - 1));
                if (pr == SECOND && !(bf == pf && br == pr - 2))
                    best = Math.min(best, white(bf, br, pf, pr - 2));
            }
        }
        if (best > WHITE)
            best = DRAW; // a blocked pawn is a draw
        memo[1][bf][br][pf][pr] = best + 1;
        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String bishop = in.next(), pawn = in.next();
        int result = white(bishop.charAt(0) - 'a', bishop.charAt(1) - '1', pawn.charAt(0) - 'a',
                           pawn.charAt(1) - '1');
        System.out.println(new String[] {"BLACK", "DRAW", "WHITE"}[result]);
    }
}
