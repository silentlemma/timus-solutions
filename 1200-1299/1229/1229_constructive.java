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
        in.nextToken();
        int m = (int)in.nval;
        int[][] first = new int[n][m], second = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                in.nextToken();
                first[i][j] = (int)in.nval;
            }
        }
        int label = 0;
        // cover every 2 x 2 block with two bricks: lying flat unless a brick of
        // the first layer fills its top or bottom row, and then standing, which
        // no first-layer brick can match, as that brick holds a cell of each column
        for (int i = 0; i < n; i += 2) {
            for (int j = 0; j < m; j += 2) {
                boolean flat =
                    first[i][j] != first[i][j + 1] && first[i + 1][j] != first[i + 1][j + 1];
                int a = ++label, b = ++label;
                if (flat) {
                    second[i][j] = second[i][j + 1] = a;
                    second[i + 1][j] = second[i + 1][j + 1] = b;
                } else {
                    second[i][j] = second[i + 1][j] = a;
                    second[i][j + 1] = second[i + 1][j + 1] = b;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int[] row : second) {
            for (int j = 0; j < m; j++) {
                out.append(row[j]).append(j + 1 < m ? ' ' : '\n');
            }
        }
        System.out.print(out);
    }
}
