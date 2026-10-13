import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int CAP = 100; // the largest single credit

    static int[] cols;

    // take from the fullest columns first: lower them all towards a level
    static int taken(int level) {
        int sum = 0;
        for (int c : cols)
            sum += Math.min(CAP, Math.max(0, c - level));
        return sum;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] rows = new int[n];
        cols = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            rows[i] = (int)in.nval;
        }
        int top = 0;
        for (int j = 0; j < n; j++) {
            in.nextToken();
            cols[j] = (int)in.nval;
            top = Math.max(top, cols[j]);
        }
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            int need = rows[i];
            if (taken(0) < need) {
                System.out.println("NO");
                return;
            }
            int lo = 0, hi = top;
            while (lo < hi) { // the lowest level that takes no more than needed
                int mid = (lo + hi) / 2;
                if (taken(mid) <= need)
                    hi = mid;
                else
                    lo = mid + 1;
            }
            int[] row = matrix[i];
            int extra = need;
            for (int j = 0; j < n; j++) {
                row[j] = Math.min(CAP, Math.max(0, cols[j] - lo));
                extra -= row[j];
            }
            for (int j = 0; j < n && extra > 0; j++)
                // one more unit from columns that stand exactly at the level
                if (row[j] < CAP && cols[j] - row[j] == lo && lo > 0) {
                    row[j]++;
                    extra--;
                }
            for (int j = 0; j < n; j++)
                cols[j] -= row[j];
        }
        StringBuilder out = new StringBuilder("YES\n");
        for (int[] row : matrix) {
            for (int j = 0; j < n; j++)
                out.append(row[j]).append(j + 1 < n ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
