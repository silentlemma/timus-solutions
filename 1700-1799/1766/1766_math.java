import java.util.Locale;
import java.util.Scanner;

public class Main {
    static final int SIDE = 8;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long[][] grid = new long[SIDE][SIDE], score = new long[SIDE][SIDE];
        for (int r = 0; r < SIDE; r++)
            for (int c = 0; c < SIDE; c++) grid[r][c] = in.nextLong();
        // moving from u to a neighbour v with weight w(v) / W(u), where W(u) sums
        // the weights around u, the walk is balanced by w(u) W(u) in every cell,
        // and after so many steps it has settled into that distribution
        long total = 0;
        for (int r = 0; r < SIDE; r++) {
            for (int c = 0; c < SIDE; c++) {
                long around = 0;
                for (int y = Math.max(0, r - 1); y <= Math.min(SIDE - 1, r + 1); y++)
                    for (int x = Math.max(0, c - 1); x <= Math.min(SIDE - 1, c + 1); x++)
                        if (y != r || x != c) around += grid[y][x];
                score[r][c] = grid[r][c] * around;
                total += score[r][c];
            }
        }
        StringBuilder out = new StringBuilder();
        for (int r = 0; r < SIDE; r++) {
            for (int c = 0; c < SIDE; c++) {
                if (c > 0) out.append(' ');
                out.append(String.format(Locale.US, "%.15f", (double) score[r][c] / total));
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
