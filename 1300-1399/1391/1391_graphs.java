import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int LONGEST = 16;    // the longest cycle counted: no snake of length 18 gets out
    static final int SHORTEST = 4;    // the shortest cycle on a grid
    static final int LAST_SNAKE = 17; // snakes of lengths 2 .. 17 are answered

    static int h, w, root, limit;
    static int[][] nearCells;
    static int[] dist, rnk, best;
    static boolean[] onPath, needed;

    static void walk(int v, int steps) {
        for (int u : nearCells[v]) {
            if (u == root) {
                if (steps + 1 >= SHORTEST && needed[steps + 1]) {
                    best[steps + 1] = dist[root];
                    needed[steps + 1] = false;
                }
            } else if (!onPath[u] && rnk[u] > rnk[root] &&
                       steps + 1 + Math.abs(u / w - root / w) + Math.abs(u % w - root % w) <=
                           limit) {
                onPath[u] = true;
                walk(u, steps + 1);
                onPath[u] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine())
            all.append(line).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        int r0 = Integer.parseInt(st.nextToken()), c0 = Integer.parseInt(st.nextToken());
        int start = (r0 - 1) * w + c0 - 1;
        boolean[] free = new boolean[h * w];
        for (int r = 0; r < h; r++) {
            String row = st.nextToken();
            for (int c = 0; c < w; c++)
                free[r * w + c] = row.charAt(c) == '.';
        }
        free[start] = true;
        nearCells = new int[h * w][];
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        for (int v = 0; v < h * w; v++) {
            int[] list = new int[dr.length];
            int count = 0;
            for (int k = 0; k < dr.length; k++) {
                int nr = v / w + dr[k], nc = v % w + dc[k];
                if (nr >= 0 && nr < h && nc >= 0 && nc < w && free[nr * w + nc])
                    list[count++] = nr * w + nc;
            }
            nearCells[v] = Arrays.copyOf(list, count);
        }
        // distances from the entrance
        dist = new int[h * w];
        Arrays.fill(dist, -1);
        dist[start] = 0;
        int[] order = new int[h * w];
        int size = 0;
        order[size++] = start;
        for (int i = 0; i < size; i++)
            for (int u : nearCells[order[i]])
                if (dist[u] < 0) {
                    dist[u] = dist[order[i]] + 1;
                    order[size++] = u;
                }
        // rank: breadth-first position; a cycle is found from its first cell in this order
        rnk = new int[h * w];
        Arrays.fill(rnk, size);
        for (int i = 0; i < size; i++)
            rnk[order[i]] = i;
        best = new int[LONGEST + 1];
        Arrays.fill(best, -1);
        needed = new boolean[LONGEST + 1];
        for (int c = SHORTEST; c <= LONGEST; c += 2)
            needed[c] = true;
        onPath = new boolean[h * w];
        for (int i = 0; i < size; i++) {
            limit = 0;
            for (int c = SHORTEST; c <= LONGEST; c++)
                if (needed[c])
                    limit = c;
            if (limit == 0)
                break;
            root = order[i];
            onPath[root] = true;
            walk(root, 0);
            onPath[root] = false;
        }
        StringBuilder out = new StringBuilder();
        for (int length = 2; length <= LAST_SNAKE; length++) {
            int answer = -1;
            for (int c = length; c <= LONGEST; c++)
                if (best[c] >= 0 && (answer < 0 || 2 * best[c] + c < answer))
                    answer = 2 * best[c] + c;
            out.append(answer).append('\n');
        }
        System.out.print(out);
    }
}
