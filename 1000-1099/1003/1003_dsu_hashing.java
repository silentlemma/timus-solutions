import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    private static final int END_OF_INPUT = -1;

    private static BufferedReader in;
    private static StringTokenizer tokens = new StringTokenizer("");

    // Disjoint sets of prefix positions; parity[x] is the parity of the number
    // of ones between x and its parent.
    private static int[] parent;
    private static int[] parity;
    private static int[] rank;
    private static int found;
    private static int foundParity;

    private static String next() throws IOException {
        while (!tokens.hasMoreTokens()) {
            tokens = new StringTokenizer(in.readLine());
        }
        return tokens.nextToken();
    }

    private static void find(int x) {
        int acc = 0;
        int root = x;
        while (parent[root] != root) {
            acc ^= parity[root];
            root = parent[root];
        }
        int rest = acc;
        while (parent[x] != x) {
            int up = parent[x];
            int own = parity[x];
            parent[x] = root;
            parity[x] = rest;
            rest ^= own;
            x = up;
        }
        found = root;
        foundParity = acc;
    }

    // Records that x and y differ by parity w; false on a contradiction.
    private static boolean union(int x, int y, int w) {
        find(x);
        int rx = found;
        int px = foundParity;
        find(y);
        int ry = found;
        int py = foundParity;
        if (rx == ry) {
            return (px ^ py) == w;
        }
        if (rank[rx] < rank[ry]) {
            int t = rx;
            rx = ry;
            ry = t;
        }
        parent[ry] = rx;
        parity[ry] = px ^ py ^ w;
        if (rank[rx] == rank[ry]) {
            rank[rx]++;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int length;
        while ((length = Integer.parseInt(next())) != END_OF_INPUT) {
            int q = Integer.parseInt(next());
            parent = new int[2 * q];
            parity = new int[2 * q];
            rank = new int[2 * q];
            HashMap<Integer, Integer> ids = new HashMap<>();
            int answer = q;
            for (int i = 0; i < q; i++) {
                int l = Integer.parseInt(next());
                int r = Integer.parseInt(next());
                int w = next().equals("odd") ? 1 : 0;
                if (answer != q) {
                    continue;
                }
                // ones in [l, r] = prefix(r) - prefix(l - 1)
                if (!union(id(ids, l - 1), id(ids, r), w)) {
                    answer = i;
                }
            }
            out.println(answer);
        }
        out.flush();
    }

    private static int id(HashMap<Integer, Integer> ids, int pos) {
        Integer v = ids.get(pos);
        if (v == null) {
            v = ids.size();
            ids.put(pos, v);
            parent[v] = v;
        }
        return v;
    }
}
