import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static int[] parent;
    static int[] from;
    static int[] to;
    static int pieces;

    static int find(int v) {
        int root = v;
        while (parent[root] != root) {
            root = parent[root];
        }
        while (parent[v] != root) {
            int next = parent[v];
            parent[v] = root;
            v = next;
        }
        return root;
    }

    static void join(int i) {
        int a = find(from[i]);
        int b = find(to[i]);
        if (a != b) {
            parent[a] = b;
            pieces--;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        int m = (int) in.nval;
        from = new int[m];
        to = new int[m];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            from[i] = (int) in.nval;
            in.nextToken();
            to[i] = (int) in.nval;
        }
        in.nextToken();
        int q = (int) in.nval;
        int[] cuts = new int[q];
        boolean[] cut = new boolean[m];
        for (int k = 0; k < q; k++) {
            in.nextToken();
            cuts[k] = (int) in.nval - 1;
            cut[cuts[k]] = true;
        }
        parent = new int[n + 1];
        for (int v = 0; v <= n; v++) {
            parent[v] = v;
        }
        pieces = n;
        // run backwards: start from the web after all cuts and put the threads
        // back one by one, last cut first
        for (int i = 0; i < m; i++) {
            if (!cut[i]) {
                join(i);
            }
        }
        int[] answers = new int[q];
        for (int k = q - 1; k >= 0; k--) {
            answers[k] = pieces;
            join(cuts[k]);
        }
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < q; k++) {
            out.append(answers[k]).append(k + 1 < q ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
