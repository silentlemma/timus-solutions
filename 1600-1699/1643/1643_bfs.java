import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1 << 29;
    static final int LETTERS = 26;
    static final String MARKS = "$!*"; // the two armies and the fortress
    static int n, m;
    static char[][] grid;
    static List<List<int[]>> gates = new ArrayList<>();

    static boolean isGate(char ch) {
        return ch >= 'A' && ch <= 'Z';
    }

    // days to every district; teleports are free, so 0-1 BFS
    static int[][] bfs(int sr, int sc, int ar, int ac) {
        int[][] dist = new int[n][m];
        for (int[] row : dist)
            Arrays.fill(row, INF);
        boolean[] used = new boolean[LETTERS]; // teleport letters already spread
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        dist[sr][sc] = 0;
        queue.add(new int[] {sr, sc});
        while (!queue.isEmpty()) {
            int[] at = queue.poll();
            int r = at[0], c = at[1], d = dist[r][c];
            char ch = grid[r][c];
            if (isGate(ch) && !used[ch - 'A']) {
                used[ch - 'A'] = true;
                for (int[] g : gates.get(ch - 'A'))
                    if (dist[g[0]][g[1]] > d) {
                        dist[g[0]][g[1]] = d;
                        queue.addFirst(g);
                    }
            }
            for (int dr = -1; dr <= 1; dr++)
                for (int dc = -1; dc <= 1; dc++) {
                    int nr = r + dr, nc = c + dc;
                    if ((dr == 0 && dc == 0) || nr < 0 || nr >= n || nc < 0 || nc >= m)
                        continue;
                    if (grid[nr][nc] == '#' || (nr == ar && nc == ac))
                        continue;
                    if (dist[nr][nc] > d + 1) {
                        dist[nr][nc] = d + 1;
                        queue.addLast(new int[] {nr, nc});
                    }
                }
        }
        return dist;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < LETTERS; i++)
            gates.add(new ArrayList<>());
        grid = new char[n][];
        int[][] marks = new int[MARKS.length()][];
        for (int r = 0; r < n; r++) {
            grid[r] = in.readLine().trim().toCharArray();
            for (int c = 0; c < m; c++) {
                char ch = grid[r][c];
                if (isGate(ch))
                    gates.get(ch - 'A').add(new int[] {r, c});
                int k = MARKS.indexOf(ch);
                if (k >= 0)
                    marks[k] = new int[] {r, c};
            }
        }
        int fr = marks[2][0], fc = marks[2][1];
        int[][] first = bfs(marks[0][0], marks[0][1], fr, fc);
        int[][] second = bfs(marks[1][0], marks[1][1], fr, fc);
        int[][] attack = bfs(fr, fc, -1, -1); // moves are symmetric, so this is the way back
        // the earlier army waits at the meeting place, then both march together
        int best = INF;
        for (int r = 0; r < n; r++)
            for (int c = 0; c < m; c++)
                if (r != fr || c != fc)
                    best = Math.min(best, Math.max(first[r][c], second[r][c]) + attack[r][c]);
        System.out.println(best >= INF ? "Impossible" : String.valueOf(best));
    }
}
