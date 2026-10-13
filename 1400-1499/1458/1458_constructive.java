import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        // the soldiers to turn, for an all-W parade
        int[][] turn = new int[n][n];
        for (int i = 0; i < n; i++) {
            String line = in.readLine().trim();
            for (int j = 0; j < n; j++)
                turn[i][j] = line.charAt(j) == 'B' ? 1 : 0;
        }
        // pressing every cell of row a and column b turns only (a, b) when N is
        // even, so (i, j) is pressed when its row, its column and itself add up odd
        int[] row = new int[n], col = new int[n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                row[i] ^= turn[i][j];
                col[j] ^= turn[i][j];
            }
        long total = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                total += row[i] ^ col[j] ^ turn[i][j];
        // an all-B parade needs exactly the other cells
        int flip = 2 * total > (long)n * n ? 1 : 0;
        if (flip == 1)
            total = (long)n * n - total;
        StringBuilder out = new StringBuilder();
        out.append(total).append('\n');
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if ((row[i] ^ col[j] ^ turn[i][j]) != flip)
                    out.append(i + 1).append(' ').append(j + 1).append('\n');
        PrintWriter writer = new PrintWriter(System.out);
        writer.print(out);
        writer.flush();
    }
}
