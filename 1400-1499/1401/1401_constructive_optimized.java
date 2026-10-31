import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.StreamTokenizer;

public class Main {
    static int[][] board;
    static int count;

    // recursion replaces heap-allocated square objects; n <= 9 bounds depth.
    static void tile(int top, int left, int side, int hr, int hc) {
        int label = ++count, half = side / 2;
        for (int dr = 1; dr >= 0; dr--)
            for (int dc = 1; dc >= 0; dc--) {
                int r0 = top + dr * half, c0 = left + dc * half, r, c;
                if (r0 <= hr && hr < r0 + half && c0 <= hc && hc < c0 + half) {
                    r = hr;
                    c = hc;
                } else {
                    r = top + half - 1 + dr;
                    c = left + half - 1 + dc;
                    board[r][c] = label;
                }
                if (half > 1)
                    tile(r0, c0, half, r, c);
            }
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int x = (int)in.nval;
        in.nextToken();
        int y = (int)in.nval;
        int size = 1 << n;
        board = new int[size][size];
        tile(0, 0, size, x - 1, y - 1);
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        // reuse one row of text instead of retaining the complete output.
        StringBuilder row = new StringBuilder();
        for (int[] cells : board) {
            row.setLength(0);
            for (int c = 0; c < size; c++)
                row.append(cells[c]).append(c + 1 < size ? ' ' : '\n');
            out.write(row.toString());
        }
        out.flush();
    }
}
