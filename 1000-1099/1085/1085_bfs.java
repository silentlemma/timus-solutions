import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int TICKET = 4;
    static StreamTokenizer in;

    static int next() throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int n = next(), m = next();
        int[][] routes = new int[m][];
        List<List<Integer>> routesAt = new ArrayList<>();
        for (int s = 0; s <= n; s++) {
            routesAt.add(new ArrayList<>());
        }
        for (int r = 0; r < m; r++) {
            routes[r] = new int[next()];
            for (int i = 0; i < routes[r].length; i++) {
                routes[r][i] = next();
                routesAt.get(routes[r][i]).add(r);
            }
        }
        int k = next();
        long[] total = new long[n + 1];
        boolean[] ok = new boolean[n + 1];
        Arrays.fill(ok, true);
        for (int f = 0; f < k; f++) {
            int money = next(), start = next(), card = next();
            // fewest rides from the start to every stop; a ride covers a whole route
            int[] rides = new int[n + 1];
            Arrays.fill(rides, -1);
            boolean[] used = new boolean[m];
            rides[start] = 0;
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            queue.add(start);
            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int r : routesAt.get(u)) {
                    if (used[r]) {
                        continue;
                    }
                    used[r] = true;
                    for (int v : routes[r]) {
                        if (rides[v] < 0) {
                            rides[v] = rides[u] + 1;
                            queue.add(v);
                        }
                    }
                }
            }
            for (int t = 1; t <= n; t++) {
                int cost = card == 1 ? 0 : TICKET * rides[t];
                if (rides[t] < 0 || cost > money) {
                    ok[t] = false;
                } else {
                    total[t] += cost;
                }
            }
        }
        int stop = 0;
        for (int t = 1; t <= n; t++) {
            if (ok[t] && (stop == 0 || total[t] < total[stop])) {
                stop = t;
            }
        }
        System.out.println(stop == 0 ? "0" : stop + " " + total[stop]);
    }
}
