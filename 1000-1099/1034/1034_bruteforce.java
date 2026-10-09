import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int MOVED = 3;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // col[r] is the column of the queen in row r; sum[r + c] and diff[r - c + n]
        // count the queens on each diagonal
        int[] col = new int[n];
        int[] sum = new int[2 * n];
        int[] diff = new int[2 * n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            int x = (int)in.nval;
            in.nextToken();
            col[x - 1] = (int)in.nval - 1;
        }
        for (int r = 0; r < n; r++) {
            sum[r + col[r]]++;
            diff[r - col[r] + n]++;
        }
        long count = 0;
        for (int a = 0; a < n; a++) {
            for (int b = a + 1; b < n; b++) {
                for (int c = b + 1; c < n; c++) {
                    int[] rows = {a, b, c};
                    for (int r : rows) {
                        sum[r + col[r]]--;
                        diff[r - col[r] + n]--;
                    }
                    // all three queens move only when the columns are shifted cyclically
                    for (int shift = 1; shift < MOVED; shift++) {
                        int placed = 0;
                        for (; placed < MOVED; placed++) {
                            int r = rows[placed], cl = col[rows[(placed + shift) % MOVED]];
                            if (sum[r + cl] > 0 || diff[r - cl + n] > 0) {
                                break;
                            }
                            sum[r + cl]++;
                            diff[r - cl + n]++;
                        }
                        if (placed == MOVED) {
                            count++;
                        }
                        while (placed-- > 0) {
                            int r = rows[placed], cl = col[rows[(placed + shift) % MOVED]];
                            sum[r + cl]--;
                            diff[r - cl + n]--;
                        }
                    }
                    for (int r : rows) {
                        sum[r + col[r]]++;
                        diff[r - col[r] + n]++;
                    }
                }
            }
        }
        System.out.println(count);
    }
}
