import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TreeSet;

public class Main {
    static int n;
    static int[][] adj;
    static int[] match, parent, base;
    static boolean[] used, blossom;

    static int lca(int a, int b) {
        boolean[] seen = new boolean[n];
        while (true) {
            a = base[a];
            seen[a] = true;
            if (match[a] < 0) {
                break;
            }
            a = parent[match[a]];
        }
        while (true) {
            b = base[b];
            if (seen[b]) {
                return b;
            }
            b = parent[match[b]];
        }
    }

    static void mark(int v, int b, int child) {
        while (base[v] != b) {
            blossom[base[v]] = true;
            blossom[base[match[v]]] = true;
            parent[v] = child;
            child = match[v];
            v = parent[match[v]];
        }
    }

    // Edmonds' search from an exposed vertex: an alternating tree whose odd
    // cycles (blossoms) are shrunk into their base vertex
    static int findPath(int root) {
        used = new boolean[n];
        parent = new int[n];
        Arrays.fill(parent, -1);
        for (int i = 0; i < n; i++) {
            base[i] = i;
        }
        used[root] = true;
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int v = queue.poll();
            for (int to : adj[v]) {
                if (base[v] == base[to] || match[v] == to) {
                    continue;
                }
                if (to == root || (match[to] >= 0 && parent[match[to]] >= 0)) {
                    int b = lca(v, to);
                    blossom = new boolean[n];
                    mark(v, b, to);
                    mark(to, b, v);
                    for (int i = 0; i < n; i++) {
                        if (blossom[base[i]]) {
                            base[i] = b;
                            if (!used[i]) {
                                used[i] = true;
                                queue.add(i);
                            }
                        }
                    }
                } else if (parent[to] < 0) {
                    parent[to] = v;
                    if (match[to] < 0) {
                        return to;
                    }
                    used[match[to]] = true;
                    queue.add(match[to]);
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        List<TreeSet<Integer>> sets = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            sets.add(new TreeSet<>());
        }
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int a = (int)in.nval;
            if (in.nextToken() == StreamTokenizer.TT_EOF) {
                break;
            }
            int b = (int)in.nval;
            if (a != b && a >= 1 && a <= n && b >= 1 && b <= n) {
                sets.get(a - 1).add(b - 1);
                sets.get(b - 1).add(a - 1);
            }
        }
        adj = new int[n][];
        for (int v = 0; v < n; v++) {
            adj[v] = sets.get(v).stream().mapToInt(Integer::intValue).toArray();
        }
        match = new int[n];
        base = new int[n];
        Arrays.fill(match, -1);
        for (int v = 0; v < n; v++) {
            if (match[v] < 0) {
                for (int u : adj[v]) {
                    if (match[u] < 0) {
                        match[u] = v;
                        match[v] = u;
                        break;
                    }
                }
            }
        }
        for (int root = 0; root < n; root++) {
            if (match[root] < 0 && adj[root].length > 0) {
                for (int v = findPath(root); v >= 0;) {
                    int pv = parent[v], next = match[pv];
                    match[v] = pv;
                    match[pv] = v;
                    v = next;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        int count = 0;
        for (int v = 0; v < n; v++) {
            if (v < match[v]) {
                count += 2;
                out.append(v + 1).append(' ').append(match[v] + 1).append('\n');
            }
        }
        System.out.print(count + "\n" + out);
    }
}
