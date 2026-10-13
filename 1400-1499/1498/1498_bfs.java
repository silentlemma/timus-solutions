import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int[] DX = {1, -1, 0, 0}, DY = {0, 0, 1, -1};
    static int n, m, x2, y2;

    static boolean inside(int x, int y) {
        return x >= 1 && x <= n && y >= 1 && y <= m && !(x == x2 && y == y2);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        int limit = in.nextInt(), x1 = in.nextInt(), y1 = in.nextInt();
        x2 = in.nextInt();
        y2 = in.nextInt();
        // the fewest steps from the knight to every cell, around the demon
        int[][] dist = new int[n + 1][m + 1];
        for (int[] row : dist)
            Arrays.fill(row, -1);
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        dist[x1][y1] = 0;
        queue.add(new int[] {x1, y1});
        while (!queue.isEmpty()) {
            int[] c = queue.poll();
            for (int d = 0; d < DX.length; d++) {
                int nx = c[0] + DX[d], ny = c[1] + DY[d];
                if (inside(nx, ny) && dist[nx][ny] < 0) {
                    dist[nx][ny] = dist[c[0]][c[1]] + 1;
                    queue.add(new int[] {nx, ny});
                }
            }
        }
        // the strike comes from a cell next to the demon after a straight run of
        // k steps; its start must be reachable with the steps that are left
        int best = 0;
        for (int a = 0; a < DX.length; a++) {
            int ax = x2 + DX[a], ay = y2 + DY[a];
            if (!inside(ax, ay))
                continue;
            for (int d = 0; d < DX.length; d++)
                for (int k = 0;; k++) {
                    int sx = ax - k * DX[d], sy = ay - k * DY[d];
                    if (!inside(sx, sy))
                        break;
                    if (dist[sx][sy] >= 0 && dist[sx][sy] + k <= limit)
                        best = Math.max(best, k + 1);
                }
        }
        System.out.println(best);
    }
}
