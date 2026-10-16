import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final long INF = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        List<List<long[]>> updates = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            updates.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(in.readLine());
            int x = Integer.parseInt(st.nextToken());
            long y = Long.parseLong(st.nextToken()), d = Long.parseLong(st.nextToken());
            long kind = st.nextToken().charAt(0);
            updates.get(x).add(new long[] {y, d, kind});
        }
        // updates only go up, so the versions can be taken in order; the
        // client is either still licensed (0) or already pirated (1)
        long[][] best = new long[n + 1][2];
        for (long[] row : best) {
            row[0] = INF;
            row[1] = INF;
        }
        best[1][0] = 0;
        for (int v = 1; v <= n; v++) {
            for (long[] u : updates.get(v)) {
                int to = (int) u[0];
                char kind = (char) u[2];
                for (int state = 0; state < 2; state++) {
                    if (best[v][state] == INF || (kind == 'L' && state == 1)) {
                        continue;
                    }
                    long cost = best[v][state] + u[1];
                    int after = kind == 'P' ? 1 : state;
                    best[to][after] = Math.min(best[to][after], cost);
                }
            }
        }
        long answer = Math.min(best[n][0], best[n][1]);
        System.out.println(answer == INF ? "Offline" : "Online\n" + answer);
    }
}
