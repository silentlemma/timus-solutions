import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Main {
    // a connection is two hubs and a length
    static final int FIELDS = 3, LENGTH = 2;

    static int[] parent;

    static int find(int v) {
        while (parent[v] != v) {
            parent[v] = parent[parent[v]];
            v = parent[v];
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[][] edges = new int[m][];
        for (int k = 0; k < m; k++) {
            int[] e = new int[FIELDS];
            for (int f = 0; f < FIELDS; f++) {
                in.nextToken();
                e[f] = (int)in.nval;
            }
            edges[k] = e;
        }
        Arrays.sort(edges, Comparator.comparingInt(e -> e[LENGTH]));
        parent = new int[n + 1];
        for (int v = 0; v <= n; v++) {
            parent[v] = v;
        }
        // Kruskal's tree: its longest cable is the smallest possible longest
        // cable of any plan that connects every hub
        List<int[]> chosen = new ArrayList<>();
        for (int[] e : edges) {
            int ra = find(e[0]), rb = find(e[1]);
            if (ra != rb) {
                parent[ra] = rb;
                chosen.add(e);
            }
        }
        StringBuilder out = new StringBuilder();
        out.append(chosen.get(chosen.size() - 1)[LENGTH])
            .append('\n')
            .append(chosen.size())
            .append('\n');
        for (int[] e : chosen) {
            out.append(e[0]).append(' ').append(e[1]).append('\n');
        }
        System.out.print(out);
    }
}
