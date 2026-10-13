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
        // rows A x = 1: every player move then earns the same; x scaled to sum 1 is the answer
        double[][] rows = new double[n][n + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                in.nextToken();
                rows[i][j] = in.nval;
            }
            rows[i][n] = 1;
        }
        for (int col = 0; col < n; col++) {
            int pivot = col;
            for (int r = col + 1; r < n; r++)
                if (Math.abs(rows[r][col]) > Math.abs(rows[pivot][col]))
                    pivot = r;
            double[] t = rows[col];
            rows[col] = rows[pivot];
            rows[pivot] = t;
            for (int r = col + 1; r < n; r++) {
                double f = rows[r][col] / rows[col][col];
                for (int j = col; j <= n; j++)
                    rows[r][j] -= f * rows[col][j];
            }
        }
        double[] x = new double[n];
        double total = 0;
        for (int i = n - 1; i >= 0; i--) {
            double s = rows[i][n];
            for (int j = i + 1; j < n; j++)
                s -= rows[i][j] * x[j];
            x[i] = s / rows[i][i];
            total += x[i];
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++)
            out.append(String.format(java.util.Locale.US, "%.5f", x[i] / total)).append('\n');
        System.out.print(out);
    }
}
