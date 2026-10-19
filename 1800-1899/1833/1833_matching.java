import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static List<List<Integer>> adj = new ArrayList<>();
    static int[] matchLeft, matchRight, stamp;
    static int round = 0;

    // Kuhn's augmenting search on the doubled graph: left copies and right
    // copies of the canoeists, adj[u] the right neighbours of left u
    static boolean augment(int u) {
        for (int v : adj.get(u)) {
            if (stamp[v] == round) {
                continue;
            }
            stamp[v] = round;
            if (matchRight[v] < 0 || augment(matchRight[v])) {
                matchLeft[u] = v;
                matchRight[v] = u;
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        int k = (int) in.nval;
        in.nextToken();
        int m = (int) in.nval;
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            in.nextToken();
            int a = (int) in.nval - 1;
            in.nextToken();
            int b = (int) in.nval - 1;
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        // each crew must get at least k between its two members; this linear
        // program has a half-integral optimum, k/2 for each copy of a canoeist
        // in a minimum vertex cover of the doubled bipartite graph
        matchLeft = new int[n];
        matchRight = new int[n];
        stamp = new int[n];
        Arrays.fill(matchLeft, -1);
        Arrays.fill(matchRight, -1);
        Arrays.fill(stamp, -1);
        for (int u = 0; u < n; u++, round++) {
            augment(u);
        }
        // Konig: left copies unreachable from free left copies by
        // alternating paths, and right copies reachable, form a minimum cover
        boolean[] seenLeft = new boolean[n], seenRight = new boolean[n];
        int[] queue = new int[n];
        int size = 0;
        for (int u = 0; u < n; u++) {
            if (matchLeft[u] < 0) {
                seenLeft[u] = true;
                queue[size++] = u;
            }
        }
        for (int i = 0; i < size; i++) {
            for (int v : adj.get(queue[i])) {
                if (seenRight[v]) {
                    continue;
                }
                seenRight[v] = true;
                int w = matchRight[v];
                if (w >= 0 && !seenLeft[w]) {
                    seenLeft[w] = true;
                    queue[size++] = w;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int v = 0; v < n; v++) {
            int copies = (seenLeft[v] ? 0 : 1) + (seenRight[v] ? 1 : 0);
            out.append(String.format("%.1f", copies * k / 2.0)).append('\n');
        }
        System.out.print(out);
    }
}
