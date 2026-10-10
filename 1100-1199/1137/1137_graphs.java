import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    // stops are numbered up to this
    static final int STOPS = 1000;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        List<List<Integer>> adj = new ArrayList<>();
        for (int v = 0; v <= STOPS; v++) {
            adj.add(new ArrayList<>());
        }
        int edges = 0, start = -1;
        for (int r = 0; r < n; r++) {
            in.nextToken();
            int m = (int)in.nval;
            int[] route = new int[m + 1];
            for (int k = 0; k <= m; k++) {
                in.nextToken();
                route[k] = (int)in.nval;
            }
            if (start < 0) {
                start = route[0];
            }
            for (int k = 0; k < m; k++) {
                adj.get(route[k]).add(route[k + 1]);
            }
            edges += m;
        }
        // every old route is a cycle, so each stop is left as often as it is
        // entered; Hierholzer's walk then uses every segment once
        int[] ptr = new int[STOPS + 1];
        int[] stack = new int[edges + 1];
        int[] circuit = new int[edges + 1];
        int top = 0, size = 0;
        stack[top++] = start;
        while (top > 0) {
            int v = stack[top - 1];
            if (ptr[v] < adj.get(v).size()) {
                stack[top++] = adj.get(v).get(ptr[v]++);
            } else {
                circuit[size++] = v;
                top--;
            }
        }
        if (size != edges + 1) {
            System.out.println(0);
            return;
        }
        StringBuilder out = new StringBuilder().append(edges);
        for (int k = size - 1; k >= 0; k--) {
            out.append(' ').append(circuit[k]);
        }
        System.out.println(out);
    }
}
