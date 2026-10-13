import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[] from = new int[m], to = new int[m], profit = new int[m];
        int[] indeg = new int[n + 1], start = new int[n + 2];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            from[i] = (int)in.nval;
            in.nextToken();
            to[i] = (int)in.nval;
            in.nextToken();
            profit[i] = (int)in.nval;
            indeg[to[i]]++;
            start[from[i] + 1]++;
        }
        in.nextToken();
        int s = (int)in.nval;
        in.nextToken();
        int f = (int)in.nval;
        // pipelines grouped by their first station
        for (int v = 1; v <= n; v++)
            start[v + 1] += start[v];
        int[] edge = new int[m], fill = Arrays.copyOf(start, n + 1);
        for (int i = 0; i < m; i++)
            edge[fill[from[i]]++] = i;
        // the network has no cycles: take the stations in topological order and
        // keep the best profit of a route from S to each of them, -1 if unreachable
        long[] best = new long[n + 1];
        Arrays.fill(best, -1);
        best[s] = 0;
        int[] order = new int[n];
        int size = 0;
        for (int v = 1; v <= n; v++)
            if (indeg[v] == 0)
                order[size++] = v;
        for (int k = 0; k < size; k++) {
            int v = order[k];
            for (int e = start[v]; e < start[v + 1]; e++) {
                int i = edge[e], w = to[i];
                if (best[v] >= 0 && best[v] + profit[i] > best[w])
                    best[w] = best[v] + profit[i];
                if (--indeg[w] == 0)
                    order[size++] = w;
            }
        }
        System.out.println(best[f] < 0 ? "No solution" : String.valueOf(best[f]));
    }
}
