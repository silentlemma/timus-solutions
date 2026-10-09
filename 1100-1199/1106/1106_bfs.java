import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        List<List<Integer>> adj = new ArrayList<>();
        for (int v = 0; v <= n; v++) {
            adj.add(new ArrayList<>());
        }
        for (int v = 1; v <= n; v++) {
            while (in.nextToken() != StreamTokenizer.TT_EOF && in.nval != 0) {
                adj.get(v).add((int)in.nval);
            }
        }
        // colour a BFS tree of every component by depth parity: each member has a
        // tree neighbour, its parent or a child, in the other team
        int[] side = new int[n + 1];
        Arrays.fill(side, -1);
        for (int root = 1; root <= n; root++) {
            if (side[root] >= 0) {
                continue;
            }
            side[root] = 0;
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            queue.add(root);
            while (!queue.isEmpty()) {
                int v = queue.poll();
                for (int u : adj.get(v)) {
                    if (side[u] < 0) {
                        side[u] = 1 - side[v];
                        queue.add(u);
                    }
                }
            }
        }
        StringBuilder team = new StringBuilder();
        int count = 0;
        for (int v = 1; v <= n; v++) {
            if (side[v] == 0) {
                team.append(count++ > 0 ? " " : "").append(v);
            }
        }
        System.out.println(count + "\n" + team);
    }
}
