import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
    static final int SIDE_AREA = 9, ENTRANCE_SIDES = 4;
    static final int[] DI = {-1, 1, 0, 0}, DJ = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        char[][] grid = new char[n][];
        for (int i = 0; i < n; i++) {
            grid[i] = in.next().toCharArray();
        }
        // visit every empty cell reachable from either entrance; each side of
        // such a cell that faces a block or the outer wall is a visible wall
        boolean[][] seen = new boolean[n][n];
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {0, 0});
        queue.add(new int[] {n - 1, n - 1});
        seen[0][0] = seen[n - 1][n - 1] = true;
        int sides = 0;
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int d = 0; d < DI.length; d++) {
                int a = cell[0] + DI[d], b = cell[1] + DJ[d];
                if (a < 0 || b < 0 || a >= n || b >= n || grid[a][b] == '#') {
                    sides++;
                } else if (!seen[a][b]) {
                    seen[a][b] = true;
                    queue.add(new int[] {a, b});
                }
            }
        }
        // the outer sides of the two entrance cells are openings, not walls
        System.out.println((sides - ENTRANCE_SIDES) * SIDE_AREA);
    }
}
