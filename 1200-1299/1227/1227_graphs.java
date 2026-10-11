import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int m;
    static int[] parent;
    // every road as its far end and its length
    static List<List<long[]>> adj = new ArrayList<>();

    static int find(int v) {
        while (parent[v] != v) {
            parent[v] = parent[parent[v]];
            v = parent[v];
        }
        return v;
    }

    // Distances from start within its tree, -1 elsewhere.
    static long[] distances(int start) {
        long[] dist = new long[m + 1];
        Arrays.fill(dist, -1);
        dist[start] = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        stack.push(start);
        while (!stack.isEmpty()) {
            int v = stack.pop();
            for (long[] e : adj.get(v)) {
                int u = (int)e[0];
                if (dist[u] < 0) {
                    dist[u] = dist[v] + e[1];
                    stack.push(u);
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tok = new StringTokenizer(in.readLine());
        m = Integer.parseInt(tok.nextToken());
        int n = Integer.parseInt(tok.nextToken());
        long s = Long.parseLong(tok.nextToken());
        parent = new int[m + 1];
        for (int v = 0; v <= m; v++) {
            parent[v] = v;
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < n; i++) {
            tok = new StringTokenizer(in.readLine());
            int p = Integer.parseInt(tok.nextToken()), q = Integer.parseInt(tok.nextToken());
            long r = Long.parseLong(tok.nextToken());
            int a = find(p), b = find(q);
            if (a == b) {
                // a cycle, a loop or a second road: drive round it as long as needed
                System.out.println("YES");
                return;
            }
            parent[a] = b;
            adj.get(p).add(new long[] {q, r});
            adj.get(q).add(new long[] {p, r});
        }
        // a forest: the longest route is a diameter of one of its trees
        long best = 0;
        boolean[] seen = new boolean[m + 1];
        for (int v = 1; v <= m; v++) {
            if (seen[v]) {
                continue;
            }
            long[] d = distances(v);
            int end = v;
            for (int u = 1; u <= m; u++) {
                if (d[u] >= 0) {
                    seen[u] = true;
                    if (d[u] > d[end]) {
                        end = u;
                    }
                }
            }
            for (long x : distances(end)) {
                best = Math.max(best, x);
            }
        }
        System.out.println(best >= s ? "YES" : "NO");
    }
}
