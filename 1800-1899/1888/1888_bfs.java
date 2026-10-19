import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int LONGEST = 50; // experience is from 1 to 50 years

    static int p;
    static List<List<Integer>> adj = new ArrayList<>();

    // distances from start, -1 outside its component
    static int[] distances(int start) {
        int[] dist = new int[p + 1];
        Arrays.fill(dist, -1);
        int[] queue = new int[p + 1];
        int tail = 0;
        queue[tail++] = start;
        dist[start] = 0;
        for (int head = 0; head < tail; head++) {
            int u = queue[head];
            for (int v : adj.get(u)) {
                if (dist[v] < 0) {
                    dist[v] = dist[u] + 1;
                    queue[tail++] = v;
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        p = (int) in.nval;
        for (int i = 0; i <= p; i++) {
            adj.add(new ArrayList<>());
        }
        for (int k = 0; k < n; k++) {
            in.nextToken();
            int a = (int) in.nval;
            in.nextToken();
            int b = (int) in.nval;
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        // the two pilots of a flight differ by exactly one year, so a component
        // must be bipartite; within it no two pilots differ by more than their
        // distance, and BFS layers from one end of a diameter reach it
        boolean[] seen = new boolean[p + 1];
        List<Integer> roots = new ArrayList<>();
        for (int s = 1; s <= p; s++) {
            if (seen[s]) {
                continue;
            }
            int[] dist = distances(s);
            for (int u = 1; u <= p; u++) {
                if (dist[u] < 0) {
                    continue;
                }
                seen[u] = true;
                for (int v : adj.get(u)) {
                    if ((dist[u] - dist[v]) % 2 == 0) {
                        System.out.println(-1);
                        return;
                    }
                }
            }
            roots.add(s);
        }
        int[] years = new int[p + 1];
        StringBuilder out = new StringBuilder();
        if (roots.size() == 1) {
            int spread = -1;
            for (int s = 1; s <= p; s++) {
                int[] dist = distances(s);
                int far = 0;
                for (int u = 1; u <= p; u++) {
                    far = Math.max(far, dist[u]);
                }
                if (far > spread) {
                    spread = far;
                    for (int u = 1; u <= p; u++) {
                        years[u] = 1 + dist[u];
                    }
                }
            }
            out.append(spread).append('\n');
        } else {
            // separate groups: one alternates 1 and 2, the others 49 and 50
            for (int k = 0; k < roots.size(); k++) {
                int[] dist = distances(roots.get(k));
                for (int u = 1; u <= p; u++) {
                    if (dist[u] >= 0) {
                        years[u] = k == 0 ? 1 + dist[u] % 2 : LONGEST - dist[u] % 2;
                    }
                }
            }
            out.append(LONGEST - 1).append('\n');
        }
        for (int u = 1; u <= p; u++) {
            out.append(years[u]).append(u < p ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
