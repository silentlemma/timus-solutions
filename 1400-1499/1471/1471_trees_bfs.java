import java.util.*;
public class Main {

    static final int INPUT_BUFFER = 4096;
    // refill instead of retaining the input; tokens may cross buffer boundaries.
    static final byte[] buffer = new byte[INPUT_BUFFER];
    static int position, size;
    static int read() throws java.io.IOException {
        if (position == size) {
            size = System.in.read(buffer);
            position = 0;
            if (size < 0)
                return -1;
        }
        return buffer[position++];
    }
    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c != '-' && (c < '0' || c > '9'))
            c = read();
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value * sign;
    }

    static class Edge {
        int to, weight;
        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }
    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        List<List<Edge>> edges = new ArrayList<>();
        for (int i = 0; i < n; i++)
            edges.add(new ArrayList<Edge>());
        for (int i = 1; i < n; i++) {
            int u = nextInt(), v = nextInt(), w = nextInt();
            edges.get(u).add(new Edge(v, w));
            edges.get(v).add(new Edge(u, w));
        }
        int[] parent = new int[n], depth = new int[n], distance = new int[n], size = new int[n],
              heavy = new int[n], top = new int[n], order = new int[n];
        Arrays.fill(parent, -1);
        Arrays.fill(heavy, -1);
        Arrays.fill(size, 1);
        int count = 1;
        // n <= 50000 and weights <= 1000 keep distance sums below 100 million.
        for (int i = 0; i < n; i++) {
            int v = order[i];
            for (Edge e : edges.get(v))
                if (e.to != parent[v]) {
                    int u = e.to;
                    parent[u] = v;
                    depth[u] = depth[v] + 1;
                    distance[u] = distance[v] + e.weight;
                    order[count++] = u;
                }
        }
        for (int i = n - 1; i > 0; i--) {
            int v = order[i], p = parent[v];
            size[p] += size[v];
            if (heavy[p] < 0 || size[v] > size[heavy[p]])
                heavy[p] = v;
        }
        // each light-edge jump at least doubles the subtree size.
        for (int v : order)
            if (v != 0)
                top[v] = heavy[parent[v]] == v ? top[parent[v]] : v;
        java.io.BufferedWriter out =
            new java.io.BufferedWriter(new java.io.OutputStreamWriter(System.out));
        int m = nextInt();
        for (int i = 0; i < m; i++) {
            int a = nextInt(), b = nextInt(), answer = distance[a] + distance[b];
            while (top[a] != top[b]) {
                if (depth[top[a]] < depth[top[b]]) {
                    int t = a;
                    a = b;
                    b = t;
                }
                a = parent[top[a]];
            }
            if (depth[a] > depth[b])
                a = b;
            out.write(Integer.toString(answer - 2 * distance[a]));
            out.newLine();
        }
        out.flush();
    }
}
