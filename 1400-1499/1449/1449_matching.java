import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // the Hungarian method minimises the cost -A; rows and columns from 1, 0 is a helper
        long[][] cost = new long[n + 1][n + 1];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++) {
                in.nextToken();
                cost[i][j] = -(long)in.nval;
            }
        long[] u = new long[n + 1], v = new long[n + 1];
        int[] match = new int[n + 1], way = new int[n + 1]; // match[j]: the row matched to column j
        for (int i = 1; i <= n; i++) {
            match[0] = i;
            int j0 = 0;
            long[] low = new long[n + 1];
            Arrays.fill(low, Long.MAX_VALUE);
            boolean[] used = new boolean[n + 1];
            while (match[j0] != 0) {
                used[j0] = true;
                int i0 = match[j0], j1 = 0;
                long delta = Long.MAX_VALUE;
                for (int j = 1; j <= n; j++)
                    if (!used[j]) {
                        long cur = cost[i0][j] - u[i0] - v[j];
                        if (cur < low[j]) {
                            low[j] = cur;
                            way[j] = j0;
                        }
                        if (low[j] < delta) {
                            delta = low[j];
                            j1 = j;
                        }
                    }
                for (int j = 0; j <= n; j++)
                    if (used[j]) {
                        u[match[j]] += delta;
                        v[j] -= delta;
                    } else {
                        low[j] -= delta;
                    }
                j0 = j1;
            }
            while (j0 != 0) {
                int j1 = way[j0];
                match[j0] = match[j1];
                j0 = j1;
            }
        }
        // u + v <= -A, so the bribes -u, -v cover every credit and add up to the
        // heaviest matching; shifting them until a row bribe is 0 keeps all >= 0
        long shift = Long.MAX_VALUE;
        for (int i = 1; i <= n; i++)
            shift = Math.min(shift, -u[i]);
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; i++)
            out.append(-u[i] - shift).append(i == n ? '\n' : ' ');
        for (int j = 1; j <= n; j++)
            out.append(-v[j] + shift).append(j == n ? '\n' : ' ');
        System.out.print(out);
    }
}
