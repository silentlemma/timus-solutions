import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int BUFFER = 1 << 16;
    static DataInputStream in;

    static int nextInt() throws IOException {
        int c = in.read();
        while (c < '0' || c > '9') {
            c = in.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + (c - '0');
            c = in.read();
        }
        return value;
    }

    static int[][] compact(List<List<Integer>> lists) {
        int[][] out = new int[lists.size()][];
        for (int i = 0; i < out.length; i++) {
            out[i] = lists.get(i).stream().mapToInt(Integer::intValue).toArray();
        }
        return out;
    }

    static boolean[] reach(int start, int[][] adj) {
        boolean[] seen = new boolean[adj.length];
        int[] stack = new int[adj.length];
        int top = 0;
        stack[top++] = start;
        seen[start] = true;
        while (top > 0) {
            int v = stack[--top];
            for (int u : adj[v]) {
                if (!seen[u]) {
                    seen[u] = true;
                    stack[top++] = u;
                }
            }
        }
        return seen;
    }

    public static void main(String[] args) throws IOException {
        in = new DataInputStream(new BufferedInputStream(System.in, BUFFER));
        int n = nextInt();
        int m = nextInt();
        int s = nextInt() - 1;
        int t = nextInt() - 1;
        int[] from = new int[m];
        int[] to = new int[m];
        List<List<Integer>> adjList = new ArrayList<>();
        List<List<Integer>> radjList = new ArrayList<>();
        for (int v = 0; v < n; v++) {
            adjList.add(new ArrayList<>());
            radjList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            from[i] = nextInt() - 1;
            to[i] = nextInt() - 1;
            adjList.get(from[i]).add(to[i]);
            radjList.get(to[i]).add(from[i]);
        }
        int[][] adj = compact(adjList);
        int[][] radj = compact(radjList);
        // only vertices on some path from s to t matter; they form whole
        // strongly connected components
        boolean[] fromS = reach(s, adj);
        if (!fromS[t]) {
            System.out.println(0);
            return;
        }
        boolean[] toT = reach(t, radj);
        boolean[] alive = new boolean[n];
        for (int v = 0; v < n; v++) {
            alive[v] = fromS[v] && toT[v];
        }
        // Kosaraju: finishing order on the graph, then the reversed graph in
        // reverse finishing order numbers the components in topological order
        int[] order = new int[n];
        int ordered = 0;
        boolean[] done = new boolean[n];
        int[] stackV = new int[n];
        int[] stackI = new int[n];
        for (int root = 0; root < n; root++) {
            if (!alive[root] || done[root]) {
                continue;
            }
            done[root] = true;
            int top = 0;
            stackV[top] = root;
            stackI[top++] = 0;
            while (top > 0) {
                int v = stackV[top - 1];
                if (stackI[top - 1] < adj[v].length) {
                    int u = adj[v][stackI[top - 1]++];
                    if (alive[u] && !done[u]) {
                        done[u] = true;
                        stackV[top] = u;
                        stackI[top++] = 0;
                    }
                } else {
                    order[ordered++] = v;
                    top--;
                }
            }
        }
        int[] comp = new int[n];
        Arrays.fill(comp, -1);
        int count = 0;
        for (int k = ordered - 1; k >= 0; k--) {
            int root = order[k];
            if (comp[root] >= 0) {
                continue;
            }
            comp[root] = count;
            int top = 0;
            stackV[top++] = root;
            while (top > 0) {
                int v = stackV[--top];
                for (int u : radj[v]) {
                    if (alive[u] && comp[u] < 0) {
                        comp[u] = count;
                        stackV[top++] = u;
                    }
                }
            }
            count++;
        }
        int[] size = new int[count];
        int[] inside = new int[count];
        List<List<Integer>> out = new ArrayList<>();
        for (int c = 0; c < count; c++) {
            out.add(new ArrayList<>());
        }
        for (int v = 0; v < n; v++) {
            if (alive[v]) {
                size[comp[v]]++;
            }
        }
        for (int i = 0; i < m; i++) {
            int a = from[i];
            int b = to[i];
            if (alive[a] && alive[b]) {
                if (comp[a] == comp[b]) {
                    inside[comp[a]]++;
                } else {
                    out.get(comp[a]).add(comp[b]);
                }
            }
        }
        // a component with more arcs than vertices holds two cycles, and paths grow
        // exponentially; otherwise each cyclic component is one simple cycle, and
        // paths through c of them number about N^(c - 1)
        for (int c = 0; c < count; c++) {
            if (inside[c] > size[c]) {
                System.out.println(-1);
                return;
            }
        }
        // best[c]: the most cycles on a path from s into component c; arcs go
        // from lower to higher numbers, so one pass in order settles it
        int[] best = new int[count];
        for (int c = 0; c < count; c++) {
            best[c] += inside[c] == size[c] ? 1 : 0;
            for (int d : out.get(c)) {
                best[d] = Math.max(best[d], best[c]);
            }
        }
        System.out.println(Math.max(0, best[comp[t]] - 1));
    }
}
