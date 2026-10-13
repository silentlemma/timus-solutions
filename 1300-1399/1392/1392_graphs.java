import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int[] parent;

    static int find(int v) {
        while (parent[v] != v)
            v = parent[v] = parent[parent[v]];
        return v;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int k = (int)in.nval;
        long[] x = new long[k], y = new long[k], z = new long[k], r = new long[k];
        for (int i = 0; i < k; i++) {
            in.nextToken();
            x[i] = (long)in.nval;
            in.nextToken();
            y[i] = (long)in.nval;
            in.nextToken();
            z[i] = (long)in.nval;
            in.nextToken();
            r[i] = (long)in.nval;
        }
        parent = new int[k];
        for (int i = 0; i < k; i++)
            parent[i] = i;
        // two balls share more than one point when the centres are closer than r1 + r2
        for (int i = 0; i < k; i++)
            for (int j = i + 1; j < k; j++) {
                long dx = x[i] - x[j], dy = y[i] - y[j], dz = z[i] - z[j];
                if (dx * dx + dy * dy + dz * dz < (r[i] + r[j]) * (r[i] + r[j]))
                    parent[find(j)] = find(i);
            }
        // each group lists its planets in order; a group starts at its first planet
        List<List<Integer>> groups = new ArrayList<>();
        for (int v = 0; v < k; v++)
            groups.add(new ArrayList<>());
        for (int v = 0; v < k; v++)
            groups.get(find(v)).add(v);
        List<List<Integer>> lists = new ArrayList<>();
        for (List<Integer> g : groups)
            if (!g.isEmpty())
                lists.add(g);
        lists.sort((a, b) -> Integer.compare(a.get(0), b.get(0)));
        StringBuilder out = new StringBuilder();
        for (List<Integer> g : lists) {
            for (int i = 0; i < g.size(); i++)
                out.append(i > 0 ? ", " : "").append(g.get(i));
            out.append('\n');
        }
        System.out.print(out);
    }
}
