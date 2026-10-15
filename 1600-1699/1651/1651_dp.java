import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1 << 30;
    static final int TOP = 10000; // the largest vertex number

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int)in.nval;
        int[] chain = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            chain[i] = (int)in.nval;
        }
        int end = chain[n - 1];
        if (chain[0] == end) {
            System.out.println(end);
            return;
        }
        // dp[i]: fewest edges from position i to the final vertex, taking only
        // edges of p from i on; reaching the final vertex anywhere ends it
        int[] dp = new int[n], step = new int[n];
        Arrays.fill(dp, INF);
        Arrays.fill(step, -1);
        // per vertex: the best dp after leaving it and where, latest on ties
        int[] bestValue = new int[TOP + 1], bestAt = new int[TOP + 1];
        Arrays.fill(bestValue, INF);
        dp[n - 1] = 0;
        for (int i = n - 2; i >= 0; i--) {
            int u = chain[i];
            if (dp[i + 1] < bestValue[u]) {
                bestValue[u] = dp[i + 1];
                bestAt[u] = i + 1;
            }
            if (u == end) {
                dp[i] = 0;
            } else if (bestValue[u] < INF) {
                dp[i] = bestValue[u] + 1;
                step[i] = bestAt[u];
            }
        }
        StringBuilder sb = new StringBuilder().append(chain[0]);
        for (int i = 0; chain[i] != end;) {
            i = step[i];
            sb.append(' ').append(chain[i]);
        }
        System.out.println(sb);
    }
}
