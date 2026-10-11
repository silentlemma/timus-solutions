import java.io.*;
import java.util.*;

public class Main {
    static final long INF = 1L << 60;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[] bx = new int[n], by = new int[n], sx = new int[m], sy = new int[m], cap = new int[m];
        int[] load = new int[m];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            bx[i] = (int)in.nval;
            in.nextToken();
            by[i] = (int)in.nval;
            in.nextToken();
        }
        for (int j = 0; j < m; j++) {
            in.nextToken();
            sx[j] = (int)in.nval;
            in.nextToken();
            sy[j] = (int)in.nval;
            in.nextToken();
            cap[j] = (int)in.nval;
        }
        int[][] plan = new int[n][m], dist = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                in.nextToken();
                plan[i][j] = (int)in.nval;
                load[j] += plan[i][j];
                dist[i][j] = Math.abs(bx[i] - sx[j]) + Math.abs(by[i] - sy[j]) + 1;
            }
        // nodes 0..m-1 are shelters and m is the spare room; j -> k moves one
        // worker of some building from shelter j to k, j -> m uses a free place
        // at j, and m -> k lets shelter k end up one worker short
        int v = m + 1;
        long[][] w = new long[v][v];
        int[][] via = new int[v][v];
        for (long[] row : w)
            Arrays.fill(row, INF);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (plan[i][j] == 0)
                    continue;
                for (int k = 0; k < m; k++) {
                    long c = dist[i][k] - dist[i][j];
                    if (k != j && c < w[j][k]) {
                        w[j][k] = c;
                        via[j][k] = i;
                    }
                }
            }
        for (int j = 0; j < m; j++) {
            if (load[j] < cap[j])
                w[j][m] = 0;
            w[m][j] = 0;
        }
        // Bellman-Ford from all nodes at once; a change in round v means a
        // negative cycle, which the predecessors lead into
        long[] d = new long[v];
        int[] pred = new int[v];
        int last = -1;
        for (int round = 0; round < v; round++) {
            last = -1;
            for (int j = 0; j < v; j++)
                for (int k = 0; k < v; k++)
                    if (w[j][k] < INF && d[j] + w[j][k] < d[k]) {
                        d[k] = d[j] + w[j][k];
                        pred[k] = j;
                        last = k;
                    }
            if (last < 0)
                break;
        }
        if (last < 0) {
            System.out.println("OPTIMAL");
            return;
        }
        for (int step = 0; step < v; step++)
            last = pred[last];
        // shift one worker along each shelter-to-shelter edge of the cycle
        int k = last;
        do {
            int j = pred[k];
            if (j < m && k < m) {
                plan[via[j][k]][j]--;
                plan[via[j][k]][k]++;
            }
            k = j;
        } while (k != last);
        StringBuilder sb = new StringBuilder("SUBOPTIMAL\n");
        for (int[] row : plan) {
            for (int j = 0; j < m; j++)
                sb.append(row[j]).append(j + 1 < m ? ' ' : '\n');
        }
        System.out.print(sb);
    }
}
