import java.util.*;

public class Main {
    static final long MOD = 1000000000;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        String[] grid = new String[n];
        for (int i = 0; i < n; i++)
            grid[i] = in.next();
        int[][] id = new int[n][m];
        int v = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                id[i][j] = grid[i].charAt(j) == '.' ? v++ : -1;
        // the Laplacian of the bedroom graph; by the matrix-tree theorem any
        // cofactor counts its spanning trees (0 when it is disconnected)
        long[][] lap = new long[v][v];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                int u = id[i][j];
                if (u < 0)
                    continue;
                int[] next = {i + 1 < n ? id[i + 1][j] : -1, j + 1 < m ? id[i][j + 1] : -1};
                for (int w : next)
                    if (w >= 0) {
                        lap[u][u]++;
                        lap[w][w]++;
                        lap[u][w]--;
                        lap[w][u]--;
                    }
            }
        int size = v - 1;
        long[][] a = new long[size][size];
        for (int i = 0; i < size; i++)
            for (int j = 0; j < size; j++)
                a[i][j] = (lap[i][j] % MOD + MOD) % MOD;
        // Elimination by Euclid's algorithm on rows: it only subtracts multiples
        // of rows and swaps them, so it works modulo 10^9, which is not prime.
        long det = 1;
        for (int k = 0; k < size; k++) {
            for (int i = k + 1; i < size; i++)
                while (a[i][k] != 0) {
                    long q = a[k][k] / a[i][k];
                    for (int j = k; j < size; j++)
                        a[k][j] = ((a[k][j] - q * a[i][j]) % MOD + MOD) % MOD;
                    long[] t = a[k];
                    a[k] = a[i];
                    a[i] = t;
                    det = (MOD - det) % MOD;
                }
            det = det * a[k][k] % MOD;
        }
        System.out.println(det);
    }
}
