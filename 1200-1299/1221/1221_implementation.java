import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    static InputStream in = new BufferedInputStream(System.in);
    static int n;
    static int[][] grid, black; // black[i][j]: black cells among the first j of row i

    // Black cells of row i in columns lo..hi.
    static int ones(int i, int lo, int hi) { return black[i][hi + 1] - black[i][lo]; }

    static boolean fits(int ci, int cj, int r) {
        // row ci + d: |d| black cells, a white run of 2(r - |d|) + 1, |d| black
        for (int d = -r; d <= r; d++) {
            int i = ci + d, side = Math.abs(d), inner = r - side;
            if (ones(i, cj - r, cj - inner - 1) != side ||
                ones(i, cj + inner + 1, cj + r) != side) {
                return false;
            }
            if (ones(i, cj - inner, cj + inner) != 0) {
                return false;
            }
        }
        return true;
    }

    static int largest() {
        // the white square needs a cell on every side of the centre, so r >= 1
        for (int r = (n - 1) / 2; r >= 1; r--) {
            for (int ci = r; ci < n - r; ci++) {
                for (int cj = r; cj < n - r; cj++) {
                    // quick tests first: a white centre and tip, a black corner
                    if (grid[ci][cj] == 1 || grid[ci - r][cj] == 1 || grid[ci - r][cj - r] == 0) {
                        continue;
                    }
                    if (fits(ci, cj, r)) {
                        return 2 * r + 1;
                    }
                }
            }
        }
        return 0;
    }

    static int readInt() throws IOException {
        int c = in.read();
        while (c != -1 && (c < '0' || c > '9')) {
            c = in.read();
        }
        int v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + c - '0';
            c = in.read();
        }
        return v;
    }

    // The next 0 or 1 of the painting; the cells may come with or without spaces.
    static int readCell() throws IOException {
        int c = in.read();
        while (c != '0' && c != '1') {
            c = in.read();
        }
        return c - '0';
    }

    public static void main(String[] args) throws IOException {
        StringBuilder out = new StringBuilder();
        while ((n = readInt()) != 0) {
            grid = new int[n][n];
            black = new int[n][n + 1];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    grid[i][j] = readCell();
                    black[i][j + 1] = black[i][j] + grid[i][j];
                }
            }
            int best = largest();
            out.append(best > 0 ? String.valueOf(best) : "No solution").append('\n');
        }
        System.out.print(out);
    }
}
