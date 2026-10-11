import java.io.*;
import java.util.*;

public class Main {
    static final long INF = 1L << 62;
    static long period;
    static long[][] phase;

    // the first train in direction d at station j not before time t
    static long next(int d, int j, long t) {
        return t + ((phase[d][j] - t) % period + period) % period;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[] pos = new long[n];
        for (int i = 1; i < n; i++) {
            in.nextToken();
            pos[i] = pos[i - 1] + (long)in.nval;
        }
        in.nextToken();
        int start = (int)in.nval - 1;
        in.nextToken();
        period = (long)in.nval;
        in.nextToken();
        long firstUp = (long)in.nval;
        in.nextToken();
        long firstDown = (long)in.nval;
        if (n == 1) {
            System.out.println(0);
            return;
        }
        // trains run forever: towards N they pass station i at firstUp + pos[i]
        // plus multiples of the period, towards 1 at firstDown + pos[N] - pos[i]
        phase = new long[2][n];
        for (int i = 0; i < n; i++) {
            phase[0][i] = (firstUp + pos[i]) % period;
            phase[1][i] = (firstDown + pos[n - 1] - pos[i]) % period;
        }
        int full = (1 << n) - 1;
        long[] arrive = new long[(full + 1) * n];
        long best = INF;
        for (int d0 = 0; d0 < 2; d0++) {
            long t0 = phase[d0][start];
            // arrive[mask * n + j]: earliest time standing at j with mask inspected
            Arrays.fill(arrive, INF);
            for (int k = 0; k < n; k++)
                if ((d0 == 0 && k > start) || (d0 == 1 && k < start))
                    arrive[(1 << start | 1 << k) * n + k] = t0 + Math.abs(pos[k] - pos[start]);
            for (int mask = 0; mask < full; mask++) {
                if ((mask >> start & 1) == 0)
                    continue;
                for (int j = 0; j < n; j++) {
                    long t = arrive[mask * n + j];
                    if (t == INF)
                        continue;
                    for (int d = 0; d < 2; d++) {
                        long dep = next(d, j, t + 1);
                        for (int k = 0; k < n; k++) {
                            if ((d == 0 && k <= j) || (d == 1 && k >= j) || (mask >> k & 1) == 1)
                                continue;
                            int at = (mask | 1 << k) * n + k;
                            arrive[at] = Math.min(arrive[at], dep + Math.abs(pos[k] - pos[j]));
                        }
                    }
                }
            }
            // with everything inspected, ride straight back to the start
            for (int j = 0; j < n; j++) {
                long t = arrive[full * n + j];
                if (t == INF || j == start)
                    continue;
                int d = start > j ? 0 : 1;
                best = Math.min(best, next(d, j, t + 1) + Math.abs(pos[start] - pos[j]) - t0);
            }
        }
        System.out.println(best);
    }
}
