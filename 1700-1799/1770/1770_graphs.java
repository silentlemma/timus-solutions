import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int FAR = 1 << 20;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken());
        int[][] a = new int[n][n], d = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) a[i][j] = Integer.parseInt(st.nextToken());
        }
        // every road must cost at least the table in both directions, so the
        // cheapest roads allowed are taken: a free road where the table says 0
        // both ways, a road with a board seen from i where it says 1 and 0
        char[][] grid = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                d[i][j] = i == j ? 0 : FAR;
                grid[i][j] = '0';
                if (i != j && a[i][j] + a[j][i] <= 1) {
                    d[i][j] = a[i][j];
                    grid[i][j] = (char) ('1' + a[i][j]);
                }
            }
        }
        // these roads give the smallest costs any network can have, so the table
        // is right exactly when they give it
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                int[] di = d[i], dk = d[k];
                int dik = di[k];
                for (int j = 0; j < n; j++) {
                    if (dik + dk[j] < di[j]) di[j] = dik + dk[j];
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (d[i][j] != a[i][j]) {
                    System.out.println("NO");
                    return;
                }
            }
        }
        StringBuilder out = new StringBuilder("YES\n");
        for (char[] row : grid) out.append(row).append('\n');
        System.out.print(out);
    }
}
