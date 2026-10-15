import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final String COLORS = "BGRWY";
    static final char EMPTY = '.';
    static int n;
    static int m;

    // the largest figure of the main colour or of the others; ties go to the
    // figure holding the lowest ball, then the leftmost of the lowest balls
    static int[] bestFigure(char[] board, char mainColor, boolean takeMain) {
        boolean[] seen = new boolean[n * m];
        int[] cells = new int[n * m];
        int[] best = null;
        int bestLow = -1;
        for (int start = 0; start < n * m; start++) {
            char color = board[start];
            if (seen[start] || color == EMPTY || (color == mainColor) != takeMain) {
                continue;
            }
            seen[start] = true;
            int size = 0;
            cells[size++] = start;
            int low = start;
            for (int k = 0; k < size; k++) {
                int v = cells[k];
                int r = v / m;
                int c = v % m;
                if (r > low / m || (r == low / m && c < low % m)) {
                    low = v;
                }
                int[] next = {v - m, v + m, v - 1, v + 1};
                boolean[] ok = {r > 0, r < n - 1, c > 0, c < m - 1};
                for (int d = 0; d < next.length; d++) {
                    int w = next[d];
                    if (ok[d] && !seen[w] && board[w] == color) {
                        seen[w] = true;
                        cells[size++] = w;
                    }
                }
            }
            if (size < 2) {
                continue;
            }
            boolean better = best == null || size > best.length
                    || (size == best.length && (low / m > bestLow / m
                            || (low / m == bestLow / m && low % m < bestLow % m)));
            if (better) {
                best = java.util.Arrays.copyOf(cells, size);
                bestLow = low;
            }
        }
        return best;
    }

    static long removeFigure(char[] board, int[] cells) {
        for (int v : cells) {
            board[v] = EMPTY;
        }
        // balls fall down, then empty columns close up to the left
        char[][] columns = new char[m][];
        int count = 0;
        for (int c = 0; c < m; c++) {
            StringBuilder column = new StringBuilder();
            for (int r = 0; r < n; r++) {
                if (board[r * m + c] != EMPTY) {
                    column.append(board[r * m + c]);
                }
            }
            if (column.length() > 0) {
                StringBuilder padded = new StringBuilder();
                for (int k = column.length(); k < n; k++) {
                    padded.append(EMPTY);
                }
                columns[count++] = padded.append(column).toString().toCharArray();
            }
        }
        for (int c = 0; c < m; c++) {
            for (int r = 0; r < n; r++) {
                board[r * m + c] = c < count ? columns[c][r] : EMPTY;
            }
        }
        long k = cells.length;
        return k * (k - 1);
    }

    static long play(char[] start, char mainColor) {
        char[] board = start.clone();
        long score = 0;
        while (true) {
            while (true) {
                int[] cells = bestFigure(board, mainColor, false);
                if (cells == null) {
                    break;
                }
                score += removeFigure(board, cells);
            }
            int[] cells = bestFigure(board, mainColor, true);
            if (cells == null) {
                return score;
            }
            score += removeFigure(board, cells);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            all.append(line).append(' ');
        }
        StringTokenizer tokens = new StringTokenizer(all.toString());
        n = Integer.parseInt(tokens.nextToken());
        m = Integer.parseInt(tokens.nextToken());
        StringBuilder rows = new StringBuilder();
        for (int r = 0; r < n; r++) {
            rows.append(tokens.nextToken());
        }
        char[] board = rows.toString().toCharArray();
        StringBuilder out = new StringBuilder();
        for (char color : COLORS.toCharArray()) {
            if (rows.indexOf(String.valueOf(color)) >= 0) {
                out.append(color).append(": ").append(play(board, color)).append('\n');
            }
        }
        System.out.print(out);
    }
}
