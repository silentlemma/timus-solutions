import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] parent;

    static int find(int v) {
        while (parent[v] != v) {
            parent[v] = parent[parent[v]];
            v = parent[v];
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        // the vertices of the grid are (i, j) -> i * (m + 1) + j; balance[v] is the number
        // of front stitches minus the number of back stitches that end at v
        int width = m + 1, vertices = (n + 1) * width;
        parent = new int[vertices];
        for (int v = 0; v < vertices; v++) {
            parent[v] = v;
        }
        int[] balance = new int[vertices];
        boolean[] stitched = new boolean[vertices];
        for (int side = 0; side < 2; side++) {
            int sign = side == 0 ? 1 : -1;
            for (int i = 0; i < n; i++) {
                String row = in.readLine().trim();
                for (int j = 0; j < m; j++) {
                    char c = row.charAt(j);
                    int[][] ends = {{i * width + j, (i + 1) * width + j + 1},
                                    {(i + 1) * width + j, i * width + j + 1}};
                    boolean[] present = {c == '\\' || c == 'X', c == '/' || c == 'X'};
                    for (int d = 0; d < 2; d++) {
                        if (!present[d]) {
                            continue;
                        }
                        int a = ends[d][0], b = ends[d][1];
                        balance[a] += sign;
                        balance[b] += sign;
                        stitched[a] = stitched[b] = true;
                        parent[find(a)] = find(b);
                    }
                }
            }
        }
        // a group needs one thread per two unbalanced stitch ends, and at least one
        long[] groupEnds = new long[vertices];
        boolean[] used = new boolean[vertices];
        for (int v = 0; v < vertices; v++) {
            if (stitched[v]) {
                int r = find(v);
                used[r] = true;
                groupEnds[r] += Math.abs(balance[v]);
            }
        }
        long threads = 0;
        for (int v = 0; v < vertices; v++) {
            if (used[v]) {
                threads += groupEnds[v] > 0 ? groupEnds[v] / 2 : 1;
            }
        }
        System.out.println(threads);
    }
}
