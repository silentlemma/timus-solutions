import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int IDS = 32768; // station indices go up to 32767
    static List<List<Integer>> adj = new ArrayList<>();
    static StreamTokenizer in =
        new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int next() throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    static int[] bfs(int start) {
        int[] dist = new int[IDS];
        Arrays.fill(dist, -1);
        int[] queue = new int[IDS];
        int tail = 0;
        dist[start] = 0;
        queue[tail++] = start;
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
        for (int i = 0; i < IDS; i++)
            adj.add(new ArrayList<>());
        boolean[] present = new boolean[IDS];
        int n = next();
        for (int i = 0; i < n; i++) {
            int[] line = new int[next()];
            for (int j = 0; j < line.length; j++) {
                line[j] = next();
                present[line[j]] = true;
            }
            for (int j = 0; j + 1 < line.length; j++) {
                adj.get(line[j]).add(line[j + 1]);
                adj.get(line[j + 1]).add(line[j]);
            }
        }
        int m = next();
        int[] seen = new int[m];
        for (int i = 0; i < m; i++)
            seen[i] = next();
        // the stations seen must be a walk through the network ...
        for (int i = 0; i < m; i++) {
            if (seen[i] < 0 || seen[i] >= IDS || !present[seen[i]])
                return;
            if (i > 0 && !adj.get(seen[i - 1]).contains(seen[i]))
                return;
        }
        int[] first = bfs(seen[0]);
        // ... and a shortest one, or no target fits it
        if (first[seen[m - 1]] != m - 1)
            return;
        int[] last = bfs(seen[m - 1]);
        StringBuilder out = new StringBuilder();
        // a target fits when the walk can go on to it along a shortest path
        for (int t = 0; t < IDS; t++) {
            if (first[t] >= 0 && last[t] >= 0 && first[t] == m - 1 + last[t]) {
                out.append(t).append('\n');
            }
        }
        System.out.print(out);
    }
}
