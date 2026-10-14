import java.util.*;

public class Main {
    static final int SIDE = 7;
    static final int ARM = 2; // the corners cut from the 7 x 7 square are 2 x 2
    static final String LETTERS = "ABCDEFG";
    static final int[] DR = {0, 1, 0, -1}, DC = {1, 0, -1, 0};
    static final int CLASSES = 3; // the residues behind the invariant

    static class Move {
        long from, over, to; // bits
        int i, j; // the cells it leaves and lands on

        Move(long from, long over, long to, int i, int j) {
            this.from = from;
            this.over = over;
            this.to = to;
            this.i = i;
            this.j = j;
        }
    }

    static List<Move> moves = new ArrayList<>();
    static HashSet<Long> dead = new HashSet<>();
    static ArrayDeque<int[]> path = new ArrayDeque<>();
    static long goal;

    static boolean onBoard(int r, int c) {
        return r >= 0 && r < SIDE && c >= 0 && c < SIDE
            && ((r >= ARM && r < SIDE - ARM) || (c >= ARM && c < SIDE - ARM));
    }

    static boolean solve(long board) {
        if (board == goal)
            return true;
        if (dead.contains(board))
            return false;
        for (Move m : moves)
            if ((board & m.from) != 0 && (board & m.over) != 0 && (board & m.to) == 0) {
                path.addLast(new int[] {m.i, m.j});
                if (solve(board ^ m.from ^ m.over ^ m.to))
                    return true;
                path.removeLast();
            }
        dead.add(board);
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String target = in.next();
        int tc = LETTERS.indexOf(target.charAt(0)), tr = target.charAt(1) - '1';
        int centre = SIDE / 2;
        // A jump changes the parity of the peg count in each class of r + c
        // (mod 3), and of r - c: so the last peg sits where r and c are both
        // congruent to the centre modulo 3.
        if ((tr - centre) % CLASSES != 0 || (tc - centre) % CLASSES != 0 || !onBoard(tr, tc)) {
            System.out.println("Impossible");
            return;
        }
        // The start is symmetric, so an edge target is a quarter turn of the top
        // one: search for the top cell, which the search finds fast, then turn.
        int turns = 0;
        while (!(tr == centre && tc == centre) && !(tr == SIDE - 1 && tc == centre)) {
            int r = SIDE - 1 - tc; // a quarter turn back
            tc = tr;
            tr = r;
            turns++;
        }
        List<int[]> cells = new ArrayList<>();
        int[][] index = new int[SIDE][SIDE];
        for (int r = 0; r < SIDE; r++)
            for (int c = 0; c < SIDE; c++)
                if (onBoard(r, c)) {
                    index[r][c] = cells.size();
                    cells.add(new int[] {r, c});
                }
        // every move as (from, over, to) bits
        for (int[] cell : cells)
            for (int d = 0; d < DR.length; d++) {
                int r = cell[0], c = cell[1];
                int r1 = r + DR[d], c1 = c + DC[d], r2 = r + 2 * DR[d], c2 = c + 2 * DC[d];
                if (onBoard(r1, c1) && onBoard(r2, c2))
                    moves.add(new Move(1L << index[r][c], 1L << index[r1][c1],
                        1L << index[r2][c2], index[r][c], index[r2][c2]));
            }
        long full = (1L << cells.size()) - 1;
        long start = full & ~(1L << index[centre][centre]);
        goal = 1L << index[tr][tc];
        solve(start);
        StringBuilder out = new StringBuilder();
        for (int[] p : path)
            out.append(name(cells, p[0], turns)).append('-').append(name(cells, p[1], turns))
                .append('\n');
        System.out.print(out);
    }

    static String name(List<int[]> cells, int i, int turns) {
        int r = cells.get(i)[0], c = cells.get(i)[1];
        for (int t = 0; t < turns; t++) {
            int nr = c; // a quarter turn forward
            c = SIDE - 1 - r;
            r = nr;
        }
        return "" + LETTERS.charAt(c) + (char)('1' + r);
    }
}
