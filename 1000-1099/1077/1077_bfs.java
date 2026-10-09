import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[] ea = new int[m], eb = new int[m];
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            in.nextToken();
            ea[i] = (int)in.nval;
            in.nextToken();
            eb[i] = (int)in.nval;
            adj.get(ea[i]).add(new int[] {eb[i], i});
            adj.get(eb[i]).add(new int[] {ea[i], i});
        }
        int[] parent = new int[n + 1], depth = new int[n + 1];
        Arrays.fill(depth, -1);
        boolean[] tree = new boolean[m];
        // a breadth-first forest keeps the tree paths, and so the tours, short
        for (int root = 1; root <= n; root++) {
            if (depth[root] >= 0) {
                continue;
            }
            depth[root] = 0;
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            queue.add(root);
            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int[] l : adj.get(u)) {
                    if (depth[l[0]] < 0) {
                        depth[l[0]] = depth[u] + 1;
                        parent[l[0]] = u;
                        tree[l[1]] = true;
                        queue.add(l[0]);
                    }
                }
            }
        }
        StringBuilder out = new StringBuilder();
        int count = 0;
        // every road outside the forest closes its own tour with the tree path
        for (int i = 0; i < m; i++) {
            if (tree[i]) {
                continue;
            }
            int a = ea[i], b = eb[i];
            List<Integer> left = new ArrayList<>(), right = new ArrayList<>();
            while (depth[a] > depth[b]) {
                left.add(a);
                a = parent[a];
            }
            while (depth[b] > depth[a]) {
                right.add(b);
                b = parent[b];
            }
            while (a != b) {
                left.add(a);
                right.add(b);
                a = parent[a];
                b = parent[b];
            }
            left.add(a);
            for (int j = right.size() - 1; j >= 0; j--) {
                left.add(right.get(j));
            }
            out.append(left.size());
            for (int c : left) {
                out.append(" ").append(c);
            }
            out.append("\n");
            count++;
        }
        System.out.print(count + "\n" + out);
    }
}
