import java.io.*;

public class Main {
    static final int MIN_HEIGHT = 170, MAX_HEIGHT = 200, HEIGHTS = MAX_HEIGHT - MIN_HEIGHT + 1;
    static final int[] counts = new int[HEIGHTS];
    static int[][] grid;
    static int middle, current = HEIGHTS - 1;

    static void fill(int dr, int dc) {
        for (int sr = -1; sr <= 1; sr += 2) {
            if (dr == 0 && sr < 0)
                continue;
            for (int sc = -1; sc <= 1; sc += 2) {
                if (dc == 0 && sc < 0)
                    continue;
                while (counts[current] == 0)
                    current--;
                grid[middle + sr * dr][middle + sc * dc] = MIN_HEIGHT + current;
                counts[current]--;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        middle = n / 2;
        grid = new int[n][n];
        for (int i = 0; i < n * n; i++) {
            in.nextToken();
            counts[(int)in.nval - MIN_HEIGHT]++;
        }
        // Emit (nearer,farther) ranks directly, each with its mirror cells.
        for (int near = 0; near <= middle; near++)
            for (int far = near; far <= middle; far++) {
                fill(near, far);
                if (near != far)
                    fill(far, near);
            }
        StringBuilder out = new StringBuilder();
        for (int[] row : grid) {
            for (int c = 0; c < n; c++) {
                if (c > 0)
                    out.append(' ');
                out.append(row[c]);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
