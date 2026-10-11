import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        // g[a][b]: total conductance between two nodes
        double[][] g = new double[n][n];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            int a = (int)in.nval - 1;
            in.nextToken();
            int b = (int)in.nval - 1;
            in.nextToken();
            double c = 1 / in.nval;
            g[a][b] += c;
            g[b][a] += c;
        }
        // nodes cut off from node 1 carry no current and would make the
        // system singular
        boolean[] seen = new boolean[n];
        seen[0] = true;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int u = stack.pop();
            for (int v = 0; v < n; v++)
                if (g[u][v] > 0 && !seen[v]) {
                    seen[v] = true;
                    stack.push(v);
                }
        }
        List<Integer> inner = new ArrayList<>();
        for (int v = 1; v < n - 1; v++)
            if (seen[v])
                inner.add(v);
        // Kirchhoff at each inner node with potential 1 at node 1, 0 at node N
        int k = inner.size();
        double[][] a = new double[k][k + 1];
        for (int i = 0; i < k; i++) {
            int u = inner.get(i);
            for (int v = 0; v < n; v++)
                a[i][i] += g[u][v];
            for (int j = 0; j < k; j++)
                a[i][j] -= g[u][inner.get(j)];
            a[i][k] = g[u][0];
        }
        for (int c = 0; c < k; c++) {
            int p = c;
            for (int r = c + 1; r < k; r++)
                if (Math.abs(a[r][c]) > Math.abs(a[p][c]))
                    p = r;
            double[] t = a[c];
            a[c] = a[p];
            a[p] = t;
            for (int r = 0; r < k; r++)
                if (r != c && a[r][c] != 0) {
                    double f = a[r][c] / a[c][c];
                    for (int j = c; j <= k; j++)
                        a[r][j] -= f * a[c][j];
                }
        }
        double[] volt = new double[n];
        volt[0] = 1;
        for (int i = 0; i < k; i++)
            volt[inner.get(i)] = a[i][k] / a[i][i];
        double current = 0;
        for (int v = 1; v < n; v++)
            current += g[0][v] * (1 - volt[v]);
        System.out.println(String.format(Locale.ROOT, "%.2f", 1 / current));
    }
}
