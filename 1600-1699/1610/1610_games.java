import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        if (in.nextToken() == StreamTokenizer.TT_EOF)
            return;
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        in.nextToken();
        int root = (int)in.nval;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            in.nextToken();
            int k = (int)in.nval;
            in.nextToken();
            int prev = (int)in.nval;
            for (int j = 1; j < k; j++) {
                in.nextToken();
                int v = (int)in.nval;
                adj.get(prev).add(v);
                adj.get(v).add(prev);
                prev = v;
            }
        }
        // depth-first search without recursion, so every other edge joins a
        // vertex to one of its ancestors
        int[] parent = new int[n + 1], depth = new int[n + 1], pos = new int[n + 1];
        int[] order = new int[n];
        Arrays.fill(depth, -1);
        int size = 0;
        order[size++] = root;
        depth[root] = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            int v = stack.peek();
            if (pos[v] == adj.get(v).size()) {
                stack.pop();
                continue;
            }
            int u = adj.get(v).get(pos[v]++);
            if (depth[u] < 0) {
                depth[u] = depth[v] + 1;
                parent[u] = v;
                order[size++] = u;
                stack.push(u);
            }
        }
        // every non-tree edge closes a cycle with the tree path between its ends
        boolean[] onCycle = new boolean[n + 1]; // the edge from v to its parent lies on a cycle
        List<List<int[]>> cycles = new ArrayList<>(); // cycles listed at their top vertex
        for (int i = 0; i <= n; i++)
            cycles.add(new ArrayList<>());
        for (int v = 1; v <= n; v++)
            for (int u : adj.get(v))
                if (depth[u] < depth[v] && u != parent[v]) {
                    int[] members = new int[depth[v] - depth[u]];
                    int x = v;
                    for (int j = 0; x != u; j++, x = parent[x]) {
                        onCycle[x] = true;
                        members[j] = x;
                    }
                    cycles.get(u).add(members);
                }
        // a tree edge to a child of value g is worth g + 1; a cycle fuses into
        // loops on its top vertex: one loop (worth 1) per edge, so its length
        // parity, together with everything hanging from its other vertices
        int[] value = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            int v = order[i], g = 0;
            for (int u : adj.get(v))
                if (parent[u] == v && !onCycle[u])
                    g ^= value[u] + 1;
            for (int[] members : cycles.get(v)) {
                g ^= (members.length + 1) % 2; // a cycle has as many edges as vertices
                for (int x : members)
                    g ^= value[x];
            }
            value[v] = g;
        }
        System.out.println(value[root] != 0 ? "First" : "Second");
    }
}
