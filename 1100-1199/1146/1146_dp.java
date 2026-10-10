import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[][] grid = new int[n][n];
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                in.nextToken();
                grid[r][c] = (int)in.nval;
            }
        }
        int best = grid[0][0];
        for (int top = 0; top < n; top++) {
            // column sums of the rows from top to bottom, then the best run of
            // neighbouring columns by Kadane's scan
            int[] cols = new int[n];
            for (int bottom = top; bottom < n; bottom++) {
                int run = 0;
                for (int c = 0; c < n; c++) {
                    cols[c] += grid[bottom][c];
                    run = run < 0 ? cols[c] : run + cols[c];
                    best = Math.max(best, run);
                }
            }
        }
        System.out.println(best);
    }
}
