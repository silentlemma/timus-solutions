import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int DEGREE = 3;

    static boolean realMap(int w, int h, char[][] lines) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < w * h; i++)
            adj.add(new ArrayList<>());
        int edges = 0;
        for (int r = 0; r < lines.length; r++)
            for (int c = 0; c < lines[r].length; c++) {
                char ch = lines[r][c];
                if ((r % 2 == 0 && c % 2 == 0) || ch == ' ')
                    continue;
                // the symbol must fit its gap: - between columns, | between rows, \ or / across
                int dr, dc;
                if (r % 2 == 0 && ch == '-') {
                    dr = 0;
                    dc = 1;
                } else if (c % 2 == 0 && ch == '|') {
                    dr = 1;
                    dc = 0;
                } else if (r % 2 == 1 && c % 2 == 1 && (ch == '\\' || ch == '/')) {
                    dr = 1;
                    dc = ch == '/' ? -1 : 1;
                } else {
                    return false;
                }
                int a = (r - dr) / 2 * w + (c - dc) / 2, b = a + dr * w + dc;
                adj.get(a).add(new int[] {b, edges});
                adj.get(b).add(new int[] {a, edges});
                edges++;
            }
        for (List<int[]> v : adj)
            if (v.size() != DEGREE)
                return false;
        // iterative low-link search: a tree edge to v is a bridge if low[v] > tin[parent]
        int[] tin = new int[w * h], low = new int[w * h];
        Arrays.fill(tin, -1);
        tin[0] = 0;
        int timer = 0;
        int[] sv = new int[w * h], via = new int[w * h], next = new int[w * h];
        int top = 0;
        sv[0] = 0;
        via[0] = -1;
        next[0] = 0;
        top = 1;
        while (top > 0) {
            int v = sv[top - 1];
            if (next[top - 1] < adj.get(v).size()) {
                int[] l = adj.get(v).get(next[top - 1]++);
                if (l[1] == via[top - 1])
                    continue;
                if (tin[l[0]] < 0) {
                    tin[l[0]] = low[l[0]] = ++timer;
                    sv[top] = l[0];
                    via[top] = l[1];
                    next[top] = 0;
                    top++;
                } else {
                    low[v] = Math.min(low[v], tin[l[0]]);
                }
                continue;
            }
            top--;
            if (top > 0) {
                int p = sv[top - 1];
                low[p] = Math.min(low[p], low[v]);
                if (low[v] > tin[p])
                    return false;
            }
        }
        for (int t : tin)
            if (t < 0)
                return false;
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] head = in.readLine().trim().split("\\s+");
        int m = Integer.parseInt(head[0]), n = Integer.parseInt(head[1]);
        char[][] picture = new char[n][m];
        for (int r = 0; r < n; r++) {
            Arrays.fill(picture[r], ' ');
            String line = in.readLine();
            if (line == null)
                continue;
            for (int c = 0; c < m && c < line.length(); c++)
                picture[r][c] = line.charAt(c);
        }
        System.out.println(realMap((m + 1) / 2, (n + 1) / 2, picture) ? "Island world"
                                                                      : "Just a picture");
    }
}
