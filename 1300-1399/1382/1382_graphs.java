import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // variable i is true when friend i's first statement is the true one,
        // and literal 2 v means v while 2 v + 1 means not v (person p is key p, card q is -q)
        Map<Integer, List<Integer>> groups = new LinkedHashMap<>();
        for (int i = 0; i < n; i++) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            in.nextToken();
            int c = (int)in.nval;
            groups.computeIfAbsent(i + 1, x -> new ArrayList<>()).add(2 * i);
            groups.computeIfAbsent(-a, x -> new ArrayList<>()).add(2 * i);
            groups.computeIfAbsent(b, x -> new ArrayList<>()).add(2 * i + 1);
            groups.computeIfAbsent(-c, x -> new ArrayList<>()).add(2 * i + 1);
        }
        int count = n;
        List<int[]> clauses = new ArrayList<>(); // one of the two literals must hold
        for (List<Integer> members : groups.values()) {
            // at most one: helper s_j means some of the first j members holds
            int prev = -1;
            for (int lit : members) {
                int s = count++;
                clauses.add(new int[] {lit ^ 1, 2 * s});
                if (prev >= 0) {
                    clauses.add(new int[] {2 * prev + 1, 2 * s});
                    clauses.add(new int[] {2 * prev + 1, lit ^ 1});
                }
                prev = s;
            }
        }
        int m = 2 * count;
        List<List<Integer>> graph = new ArrayList<>();
        for (int v = 0; v < m; v++)
            graph.add(new ArrayList<>());
        for (int[] cl : clauses) {
            graph.get(cl[0] ^ 1).add(cl[1]);
            graph.get(cl[1] ^ 1).add(cl[0]);
        }
        // Tarjan's components, numbered from the sinks up
        int[] index = new int[m], low = new int[m], comp = new int[m];
        Arrays.fill(index, -1);
        boolean[] onStack = new boolean[m];
        int[] stack = new int[m];
        int top = 0, counter = 0, comps = 0;
        int[] workV = new int[m + 1], workK = new int[m + 1];
        for (int root = 0; root < m; root++) {
            if (index[root] >= 0)
                continue;
            int w = 0;
            workV[w] = root;
            workK[w++] = 0;
            while (w > 0) {
                int v = workV[--w], k = workK[w];
                List<Integer> adj = graph.get(v);
                if (k == 0) {
                    index[v] = low[v] = counter++;
                    stack[top++] = v;
                    onStack[v] = true;
                } else {
                    low[v] = Math.min(low[v], low[adj.get(k - 1)]);
                }
                boolean descended = false;
                while (k < adj.size()) {
                    int u = adj.get(k++);
                    if (index[u] < 0) {
                        workV[w] = v;
                        workK[w++] = k;
                        workV[w] = u;
                        workK[w++] = 0;
                        descended = true;
                        break;
                    }
                    if (onStack[u])
                        low[v] = Math.min(low[v], index[u]);
                }
                if (!descended && low[v] == index[v]) {
                    while (true) {
                        int u = stack[--top];
                        onStack[u] = false;
                        comp[u] = comps;
                        if (u == v)
                            break;
                    }
                    comps++;
                }
            }
        }
        // a literal holds when its component comes before its negation's
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++)
            out.append(comp[2 * i] < comp[2 * i + 1] ? 1 : 2).append(i + 1 < n ? ' ' : '\n');
        System.out.print(out);
    }
}
