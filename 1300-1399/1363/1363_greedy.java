import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int WHITE = 255;
    static final int HALF = 127; // the carried error always stays within [-127, 127]

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[] row = new int[m], res = new int[m];
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                in.nextToken();
                row[j] = (int)in.nval;
            }
            // carry the rounding error along the row, in alternate directions so
            // that a window at either side meets short prefixes in half its rows
            int err = 0;
            for (int k = 0; k < m; k++) {
                int j = i % 2 == 0 ? k : m - 1 - k;
                err -= row[j];
                res[j] = 0;
                if (err < -HALF) {
                    err += WHITE;
                    res[j] = WHITE;
                }
            }
            for (int j = 0; j < m; j++)
                out.append(res[j]).append(j + 1 < m ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
