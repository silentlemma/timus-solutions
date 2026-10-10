import java.util.Scanner;

public class Main {
    static final int SIZE = 4, PATTERN = 3, CELLS = SIZE * SIZE, ALL = (1 << CELLS) - 1;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] rows = new String[SIZE], pattern = new String[PATTERN];
        for (int i = 0; i < SIZE; i++) {
            rows[i] = in.next();
        }
        for (int i = 0; i < PATTERN; i++) {
            pattern[i] = in.next();
        }
        int board = 0;
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                if (rows[r].charAt(c) == 'B') {
                    board |= 1 << (r * SIZE + c);
                }
            }
        }
        // the flips of a move in each cell, the pattern clipped at the edges
        int[] moves = new int[CELLS];
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                for (int dr = 0; dr < PATTERN; dr++) {
                    for (int dc = 0; dc < PATTERN; dc++) {
                        int rr = r + dr - 1, cc = c + dc - 1;
                        boolean inside = rr >= 0 && rr < SIZE && cc >= 0 && cc < SIZE;
                        if (pattern[dr].charAt(dc) == '1' && inside) {
                            moves[r * SIZE + c] |= 1 << (rr * SIZE + cc);
                        }
                    }
                }
            }
        }
        // moves commute and a second move in a cell undoes the first, so a
        // solution is a set of cells; flips[s] is the effect of the set s
        int[] flips = new int[1 << CELLS];
        int best = -1;
        for (int s = 0; s < (1 << CELLS); s++) {
            if (s > 0) {
                flips[s] = flips[s & (s - 1)] ^ moves[Integer.numberOfTrailingZeros(s)];
            }
            if (flips[s] == board || flips[s] == (board ^ ALL)) {
                int count = Integer.bitCount(s);
                if (best < 0 || count < best) {
                    best = count;
                }
            }
        }
        System.out.println(best < 0 ? "Impossible" : String.valueOf(best));
    }
}
