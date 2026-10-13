import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static final int STEP = 2;    // columns two apart keep every pair of points farther than 1
    static final int LIMIT = 999; // the leftmost column, so that 1000 columns fit in [-999, 999]

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // adjacency as linked lists in arrays: head, next and target per wire end
        int[] head = new int[n + 1], next = new int[2 * n], to = new int[2 * n];
        Arrays.fill(head, -1);
        for (int i = 0; i < 2 * (n - 1); i += 2) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            to[i] = b;
            next[i] = head[a];
            head[a] = i;
            to[i + 1] = a;
            next[i + 1] = head[b];
            head[b] = i + 1;
        }
        // column = preorder index, row = depth: the subtrees of the vertices on
        // one row take disjoint ranges of columns, so no two wires cross
        int[] x = new int[n + 1], y = new int[n + 1], stack = new int[n];
        boolean[] seen = new boolean[n + 1];
        seen[1] = true;
        stack[0] = 1;
        int top = 1, order = 0;
        while (top > 0) {
            int v = stack[--top];
            x[v] = order++ * STEP - LIMIT;
            for (int e = head[v]; e >= 0; e = next[e])
                if (!seen[to[e]]) {
                    seen[to[e]] = true;
                    y[to[e]] = y[v] + 1;
                    stack[top++] = to[e];
                }
        }
        StringBuilder out = new StringBuilder();
        for (int v = 1; v <= n; v++)
            out.append(x[v]).append(' ').append(y[v]).append('\n');
        System.out.print(out);
    }
}
