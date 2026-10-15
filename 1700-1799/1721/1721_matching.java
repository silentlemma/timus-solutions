import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    // two people can team up only if their ranks differ by exactly 2, so
    // half the rank changes parity along every pair: the graph is bipartite
    static final int GAP = 2;
    static final int SIDES = 2;

    static int[][] adj;
    static int[] mateLeft, mateRight, dist;

    static boolean layers() {
        int[] queue = new int[adj.length];
        int tail = 0;
        for (int u = 0; u < adj.length; u++) {
            dist[u] = -1;
            if (mateLeft[u] < 0) {
                dist[u] = 0;
                queue[tail++] = u;
            }
        }
        boolean found = false;
        for (int h = 0; h < tail; h++) {
            int u = queue[h];
            for (int v : adj[u]) {
                int w = mateRight[v];
                if (w < 0) {
                    found = true;
                } else if (dist[w] < 0) {
                    dist[w] = dist[u] + 1;
                    queue[tail++] = w;
                }
            }
        }
        return found;
    }

    static boolean augment(int u) {
        for (int v : adj[u]) {
            int w = mateRight[v];
            if (w < 0 || (dist[w] == dist[u] + 1 && augment(w))) {
                mateLeft[u] = v;
                mateRight[v] = u;
                return true;
            }
        }
        dist[u] = -1;
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String[] names = new String[n];
        boolean[] writes = new boolean[n], tests = new boolean[n];
        int[] ranks = new int[n];
        List<List<Integer>> side = new ArrayList<>();
        for (int s = 0; s < SIDES; s++) {
            side.add(new ArrayList<>());
        }
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(in.readLine());
            names[i] = st.nextToken();
            String kind = st.nextToken();
            ranks[i] = Integer.parseInt(st.nextToken());
            writes[i] = !kind.equals("testdata");
            tests[i] = !kind.equals("statements");
            side.get(ranks[i] / GAP % SIDES).add(i);
        }
        List<Integer> left = side.get(0), right = side.get(1);
        adj = new int[left.size()][];
        for (int i = 0; i < left.size(); i++) {
            int a = left.get(i);
            List<Integer> edges = new ArrayList<>();
            for (int j = 0; j < right.size(); j++) {
                int b = right.get(j);
                boolean close = Math.abs(ranks[a] - ranks[b]) == GAP;
                if (close && ((writes[a] && tests[b]) || (writes[b] && tests[a]))) {
                    edges.add(j);
                }
            }
            adj[i] = edges.stream().mapToInt(Integer::intValue).toArray();
        }
        mateLeft = new int[left.size()];
        mateRight = new int[right.size()];
        dist = new int[left.size()];
        Arrays.fill(mateLeft, -1);
        Arrays.fill(mateRight, -1);
        int total = 0;
        while (layers()) {
            for (int u = 0; u < left.size(); u++) {
                if (mateLeft[u] < 0 && augment(u)) {
                    total++;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        out.append(total).append('\n');
        for (int u = 0; u < left.size(); u++) {
            if (mateLeft[u] < 0) {
                continue;
            }
            int a = left.get(u), b = right.get(mateLeft[u]);
            if (writes[a] && tests[b]) {
                out.append(names[a]).append(' ').append(names[b]).append('\n');
            } else {
                out.append(names[b]).append(' ').append(names[a]).append('\n');
            }
        }
        System.out.print(out);
    }
}
