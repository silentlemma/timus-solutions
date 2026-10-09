import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    // smallest total cost of a perfect matching of rows to columns, with
    // potentials u, v kept so that reduced costs stay non-negative
    static long hungarian(int[][] cost, int n) {
        long[] u = new long[n + 1], v = new long[n + 1];
        int[] owner = new int[n + 1], way = new int[n + 1];
        for (int row = 1; row <= n; row++) {
            owner[0] = row;
            int col = 0;
            long[] low = new long[n + 1];
            Arrays.fill(low, Long.MAX_VALUE);
            boolean[] used = new boolean[n + 1];
            do {
                used[col] = true;
                int r = owner[col], next = 0;
                long delta = Long.MAX_VALUE;
                for (int j = 1; j <= n; j++) {
                    if (!used[j]) {
                        long cur = cost[r - 1][j - 1] - u[r] - v[j];
                        if (cur < low[j]) {
                            low[j] = cur;
                            way[j] = col;
                        }
                        if (low[j] < delta) {
                            delta = low[j];
                            next = j;
                        }
                    }
                }
                for (int j = 0; j <= n; j++) {
                    if (used[j]) {
                        u[owner[j]] += delta;
                        v[j] -= delta;
                    } else {
                        low[j] -= delta;
                    }
                }
                col = next;
            } while (owner[col] != 0);
            while (col != 0) {
                int prev = way[col];
                owner[col] = owner[prev];
                col = prev;
            }
        }
        return -v[0];
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[][] cost = new int[n][n];
        long total = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                in.nextToken();
                total += (int)in.nval;
                // type j stays in container i; everything else in its column moves
                cost[i][j] = -(int)in.nval;
            }
        }
        System.out.println(total + hungarian(cost, n));
    }
}
