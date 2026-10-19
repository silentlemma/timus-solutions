import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    static double[] xs;
    static double[] ys;

    static double far(int a, int b) {
        return Math.hypot(xs[a] - xs[b], ys[a] - ys[b]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken());
        xs = new double[n];
        ys = new double[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Double.parseDouble(st.nextToken());
            ys[i] = Double.parseDouble(st.nextToken());
        }
        List<List<Integer>> adjacent = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacent.add(new ArrayList<>());
        }
        for (int k = 0; k < n - 1; k++) {
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            adjacent.get(a).add(b);
            adjacent.get(b).add(a);
        }
        int[] order = new int[n];
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        int size = 1;
        for (int i = 0; i < size; i++) {
            int u = order[i];
            for (int v : adjacent.get(u)) {
                if (v != parent[u]) {
                    parent[v] = u;
                    order[size++] = v;
                }
            }
        }
        double inf = Double.POSITIVE_INFINITY;
        // the walk through a subtree starts at its root and ends at one of
        // its leaves: ends[u] lists them, cost[u] the shortest walk ending
        // at each
        int[][] ends = new int[n][];
        double[][] cost = new double[n][];
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            List<Integer> children = new ArrayList<>();
            for (int v : adjacent.get(u)) {
                if (v != parent[u]) {
                    children.add(v);
                }
            }
            if (children.isEmpty()) {
                ends[u] = new int[] {u};
                cost[u] = new double[] {0};
                continue;
            }
            int k = children.size();
            // link[a][b]: leave child a at its best end and fly to child b
            double[][] link = new double[k][k];
            int total = 0;
            for (int a = 0; a < k; a++) {
                int[] e = ends[children.get(a)];
                double[] c = cost[children.get(a)];
                total += e.length;
                for (int b = 0; b < k; b++) {
                    link[a][b] = inf;
                    for (int j = 0; j < e.length; j++) {
                        link[a][b] = Math.min(link[a][b], c[j] + far(e[j], children.get(b)));
                    }
                }
            }
            // enter[m][b]: the children in mask m are done and b, in m, came
            // last
            double[][] enter = new double[1 << k][k];
            for (double[] row : enter) {
                Arrays.fill(row, inf);
            }
            for (int b = 0; b < k; b++) {
                enter[1 << b][b] = far(u, children.get(b));
            }
            for (int m = 1; m < (1 << k); m++) {
                for (int a = 0; a < k; a++) {
                    if (enter[m][a] == inf) {
                        continue;
                    }
                    for (int b = 0; b < k; b++) {
                        if ((m >> b & 1) == 0) {
                            int next = m | 1 << b;
                            enter[next][b] = Math.min(enter[next][b], enter[m][a] + link[a][b]);
                        }
                    }
                }
            }
            double[] full = enter[(1 << k) - 1];
            ends[u] = new int[total];
            cost[u] = new double[total];
            int at = 0;
            for (int b = 0; b < k; b++) {
                int v = children.get(b);
                for (int j = 0; j < ends[v].length; j++) {
                    ends[u][at] = ends[v][j];
                    cost[u][at++] = full[b] + cost[v][j];
                }
                ends[v] = null;
                cost[v] = null;
            }
        }
        double best = inf;
        for (int j = 0; j < ends[0].length; j++) {
            best = Math.min(best, cost[0][j] + far(ends[0][j], 0));
        }
        System.out.println(String.format(Locale.US, "%.10f", best));
    }
}
