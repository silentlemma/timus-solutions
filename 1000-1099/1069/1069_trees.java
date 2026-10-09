import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    static final int MAX_N = 7500;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int[] code = new int[MAX_N];
        int m = 0;
        while (in.nextToken() == StreamTokenizer.TT_NUMBER) {
            code[m++] = (int)in.nval;
        }
        int n = m + 1;
        // a vertex stays until all its neighbours but one are removed, and each
        // removed neighbour writes the vertex once
        int[] deg = new int[n + 1];
        Arrays.fill(deg, 1);
        for (int i = 0; i < m; i++) {
            deg[code[i]]++;
        }
        PriorityQueue<Integer> leaves = new PriorityQueue<>();
        for (int u = 1; u <= n; u++) {
            if (deg[u] == 1) {
                leaves.add(u);
            }
        }
        int[][] adj = new int[n + 1][];
        int[] size = new int[n + 1];
        for (int u = 1; u <= n; u++) {
            adj[u] = new int[deg[u]];
        }
        for (int i = 0; i < m; i++) {
            int c = code[i];
            int leaf = leaves.poll();
            adj[leaf][size[leaf]++] = c;
            adj[c][size[c]++] = leaf;
            if (--deg[c] == 1) {
                leaves.add(c);
            }
        }
        StringBuilder out = new StringBuilder();
        for (int u = 1; u <= n; u++) {
            Arrays.sort(adj[u], 0, size[u]);
            out.append(u).append(':');
            for (int i = 0; i < size[u]; i++) {
                out.append(' ').append(adj[u][i]);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
