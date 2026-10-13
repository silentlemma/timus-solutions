import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int WIN = 3, DRAW = 1;
    static List<List<Integer>> graph = new ArrayList<>();
    static int[] idx, low, comp, stack;
    static boolean[] onStack;
    static int counter = 0, comps = 0, top = 0;
    static int[][] said;

    // Tarjan's strongly connected components
    static void visit(int v) {
        idx[v] = low[v] = counter++;
        stack[top++] = v;
        onStack[v] = true;
        for (int u : graph.get(v)) {
            if (idx[u] < 0) {
                visit(u);
                low[v] = Math.min(low[v], low[u]);
            } else if (onStack[u])
                low[v] = Math.min(low[v], idx[u]);
        }
        if (low[v] == idx[v]) {
            int u;
            do {
                u = stack[--top];
                onStack[u] = false;
                comp[u] = comps;
            } while (u != v);
            comps++;
        }
    }

    // 2-SAT on "captain i tells the truth" (literal 2i) or lies (2i + 1),
    // and i scored against j exactly when the literal of statement (i, j) holds
    static int literal(int i, int j) { return said[i][j] == 1 ? 2 * i : 2 * i + 1; }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        said = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                in.nextToken();
                said[i][j] = (int)in.nval;
            }
        for (int v = 0; v < 2 * n; v++)
            graph.add(new ArrayList<>());
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if (said[i][j] >= 0 && said[j][i] >= 0) {
                    // somebody scores in every match: a or b, so not a -> b
                    int a = literal(i, j), b = literal(j, i);
                    graph.get(a ^ 1).add(b);
                    graph.get(b ^ 1).add(a);
                }
        idx = new int[2 * n];
        low = new int[2 * n];
        comp = new int[2 * n];
        stack = new int[2 * n];
        onStack = new boolean[2 * n];
        Arrays.fill(idx, -1);
        for (int v = 0; v < 2 * n; v++)
            if (idx[v] < 0)
                visit(v);
        boolean[] truthful = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (comp[2 * i] == comp[2 * i + 1]) {
                System.out.println("Impossible");
                return;
            }
            // Tarjan numbers components in reverse topological order
            truthful[i] = comp[2 * i] < comp[2 * i + 1];
        }
        int[][] table = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                boolean a = said[i][j] < 0 || (said[i][j] == 1) == truthful[i];
                boolean b = said[j][i] < 0 || (said[j][i] == 1) == truthful[j];
                if (a && b)
                    table[i][j] = table[j][i] = DRAW;
                else if (a)
                    table[i][j] = WIN;
                else
                    table[j][i] = WIN;
            }
        StringBuilder out = new StringBuilder();
        for (int[] row : table)
            for (int j = 0; j < n; j++)
                out.append(row[j]).append(j + 1 < n ? ' ' : '\n');
        System.out.print(out);
    }
}
