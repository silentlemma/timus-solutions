import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static boolean[] reach(List<List<Integer>> links) {
        boolean[] seen = new boolean[links.size()];
        seen[0] = true;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty())
            for (int u : links.get(stack.pop()))
                if (!seen[u]) {
                    seen[u] = true;
                    stack.push(u);
                }
        return seen;
    }

    // Bellman-Ford from every node at once: is some cycle negative
    static boolean negativeCycle(int nodes, int[] from, int[] to, int[] weight, int count,
                                 int sign) {
        long[] dist = new long[nodes];
        for (int round = 0; round < nodes; round++) {
            boolean changed = false;
            for (int e = 0; e < count; e++)
                if (dist[from[e]] + sign * weight[e] < dist[to[e]]) {
                    dist[to[e]] = dist[from[e]] + sign * weight[e];
                    changed = true;
                }
            if (!changed)
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int s = (int)in.nval + 1;
        // rule[j][i][k]: cockroaches next month in a flat with j, i below, k above
        int[][][] rule = new int[s][s][s];
        for (int j = 0; j < s; j++)
            for (int i = 0; i < s; i++)
                for (int k = 0; k < s; k++) {
                    in.nextToken();
                    rule[j][i][k] = (int)in.nval;
                }
        // a finite floor plan read upwards is a closed walk through the pair (0, 0)
        // of the graph on pairs of neighbours; a step (a, b) -> (b, c) changes the
        // total by rule[b][a][c] - b, so the totals of a walk give the change
        List<List<Integer>> outOf = new ArrayList<>(), into = new ArrayList<>();
        for (int v = 0; v < s * s; v++) {
            outOf.add(new ArrayList<>());
            into.add(new ArrayList<>());
        }
        for (int a = 0; a < s; a++)
            for (int b = 0; b < s; b++)
                for (int c = 0; c < s; c++) {
                    outOf.get(a * s + b).add(b * s + c);
                    into.get(b * s + c).add(a * s + b);
                }
        boolean[] forward = reach(outOf), backward = reach(into);
        int total = s * s * s, count = 0;
        int[] from = new int[total], to = new int[total], weight = new int[total];
        for (int a = 0; a < s; a++)
            for (int b = 0; b < s; b++)
                for (int c = 0; c < s; c++) {
                    int v = a * s + b, u = b * s + c;
                    if (forward[v] && backward[v] && forward[u] && backward[u]) {
                        from[count] = v;
                        to[count] = u;
                        weight[count++] = rule[b][a][c] - b;
                    }
                }
        boolean fall = negativeCycle(s * s, from, to, weight, count, 1);
        boolean rise = negativeCycle(s * s, from, to, weight, count, -1);
        System.out.println(fall ? (rise ? "<>" : "<") : (rise ? ">" : "="));
    }
}
