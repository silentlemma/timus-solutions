import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int LOG = 17; // 2^17 > 100000 cells
    static BufferedReader in;
    static StringTokenizer words = new StringTokenizer("");

    static String word() throws IOException {
        while (!words.hasMoreTokens()) {
            words = new StringTokenizer(in.readLine());
        }
        return words.nextToken();
    }

    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        int h = Integer.parseInt(word());
        int w = Integer.parseInt(word());
        int cells = h * w;
        boolean[] open = new boolean[cells];
        for (int r = 0; r < h; r++) {
            String row = word();
            for (int c = 0; c < w; c++) {
                open[r * w + c] = row.charAt(c) == '#';
            }
        }
        // the open cells form a tree; root it at the first open cell and keep, for
        // every cell, its parent, depth, the direction of the step from the parent
        // (as the index offset) and the number of turns from the root
        int root = 0;
        while (!open[root]) {
            root++;
        }
        int[][] up = new int[LOG][cells];
        int[] parent = up[0];
        int[] depth = new int[cells];
        int[] step = new int[cells];
        int[] turns = new int[cells];
        java.util.Arrays.fill(parent, -1);
        parent[root] = root;
        int[] order = new int[cells];
        int size = 0;
        order[size++] = root;
        for (int k = 0; k < size; k++) {
            int v = order[k];
            int r = v / w;
            int c = v % w;
            int[] next = {v - w, v + w, v - 1, v + 1};
            boolean[] fits = {r > 0, r < h - 1, c > 0, c < w - 1};
            for (int d = 0; d < next.length; d++) {
                int u = next[d];
                if (fits[d] && open[u] && parent[u] < 0) {
                    parent[u] = v;
                    depth[u] = depth[v] + 1;
                    step[u] = u - v;
                    turns[u] = turns[v] + (v != root && step[v] != u - v ? 1 : 0);
                    order[size++] = u;
                }
            }
        }
        // closed cells point at themselves, which keeps the jump table in range
        for (int v = 0; v < cells; v++) {
            parent[v] = parent[v] < 0 ? v : parent[v];
        }
        for (int b = 1; b < LOG; b++) {
            for (int v = 0; v < cells; v++) {
                up[b][v] = up[b - 1][up[b - 1][v]];
            }
        }
        int q = Integer.parseInt(word());
        StringBuilder out = new StringBuilder();
        while (q-- > 0) {
            int r1 = Integer.parseInt(word());
            int c1 = Integer.parseInt(word());
            int r2 = Integer.parseInt(word());
            int c2 = Integer.parseInt(word());
            int a = (r1 - 1) * w + c1 - 1;
            int b = (r2 - 1) * w + c2 - 1;
            if (depth[a] < depth[b]) {
                int t = a;
                a = b;
                b = t;
            }
            int answer = 0;
            if (a != b) {
                int a1 = a;
                int b1 = b;
                boolean below = false;
                if (depth[a] > depth[b]) {
                    // lift a to just below b's depth: if it then hangs from b, b is
                    // an ancestor and only the way down from b counts
                    for (int k = depth[a] - depth[b] - 1, bit = 0; k > 0; k >>= 1, bit++) {
                        if ((k & 1) == 1) {
                            a1 = up[bit][a1];
                        }
                    }
                    below = parent[a1] == b;
                    if (!below) {
                        a1 = parent[a1];
                    }
                }
                if (below) {
                    answer = turns[a] - turns[a1];
                } else {
                    for (int bit = LOG - 1; bit >= 0; bit--) {
                        if (up[bit][a1] != up[bit][b1]) {
                            a1 = up[bit][a1];
                            b1 = up[bit][b1];
                        }
                    }
                    // a1 and b1 are the children of the meeting cell on the two
                    // sides; the path turns there unless it goes straight through
                    boolean straight = step[a1] == -step[b1];
                    answer = turns[a] - turns[a1] + turns[b] - turns[b1] + (straight ? 0 : 1);
                }
            }
            out.append(answer).append('\n');
        }
        System.out.print(out);
    }
}
