import java.util.*;

public class Main {
    static final int[][] MOVES = {{1, 2},   {2, 1},   {2, -1}, {1, -2},
                                  {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};
    static int n;
    static boolean[][] seen;
    static List<int[]> path = new ArrayList<>();

    static List<int[]> free(int c, int r) {
        List<int[]> out = new ArrayList<>();
        for (int[] m : MOVES) {
            int nc = c + m[0], nr = r + m[1];
            if (nc >= 0 && nc < n && nr >= 0 && nr < n && !seen[nc][nr])
                out.add(new int[] {nc, nr});
        }
        return out;
    }

    static boolean tour(int c, int r) {
        seen[c][r] = true;
        path.add(new int[] {c, r});
        if (path.size() == n * n)
            return true;
        // Warnsdorff's rule: try first the squares with the fewest onward
        // moves, and the search still backtracks, so it is exact
        List<int[]> next = free(c, r);
        next.sort(Comparator.comparingInt(sq -> free(sq[0], sq[1]).size()));
        for (int[] sq : next) {
            if (tour(sq[0], sq[1]))
                return true;
        }
        seen[c][r] = false;
        path.remove(path.size() - 1);
        return false;
    }

    public static void main(String[] args) {
        n = new Scanner(System.in).nextInt();
        seen = new boolean[n][n];
        boolean found = false;
        for (int c = 0; c < n && !found; c++) {
            for (int r = 0; r < n && !found; r++)
                found = tour(c, r);
        }
        if (!found) {
            System.out.println("IMPOSSIBLE");
            return;
        }
        StringBuilder out = new StringBuilder();
        for (int[] sq : path)
            out.append((char)('a' + sq[0])).append(sq[1] + 1).append('\n');
        System.out.print(out);
    }
}
