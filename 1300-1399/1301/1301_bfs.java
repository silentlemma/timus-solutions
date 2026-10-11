import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int TOP = 0, BOTTOM = 1, NORTH = 2, SOUTH = 3, EAST = 4, WEST = 5, SIDES = 6;
    static final int GO_EAST = 0, GO_WEST = 1, GO_NORTH = 2, GO_SOUTH = 3, MOVES = 4;
    static final int SIZE = 12;
    static final int[] DX = {1, -1, 0, 0};
    static final int[] DY = {0, 0, 1, -1};

    // a roll moves every face to a new side; only the side that holds the
    // starting top face matters, so each roll (east, west, north, south)
    // maps every side to the side it lands on
    static final int[][] ROLL = {
        {EAST, WEST, NORTH, SOUTH, BOTTOM, TOP},
        {WEST, EAST, NORTH, SOUTH, TOP, BOTTOM},
        {NORTH, SOUTH, BOTTOM, TOP, EAST, WEST},
        {SOUTH, NORTH, TOP, BOTTOM, EAST, WEST},
    };

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static String next() throws IOException {
        while (!words.hasMoreTokens()) {
            String line = in.readLine();
            if (line == null)
                return null;
            words = new StringTokenizer(line);
        }
        return words.nextToken();
    }

    static int number() throws IOException { return Integer.parseInt(next()); }

    public static void main(String[] args) throws IOException {
        int width = number(), height = number();
        int a = number(), b = number();
        int c = number(), d = number();
        boolean[][][] blocked = new boolean[SIZE][SIZE][MOVES];
        String kind = "";
        for (String w = next(); w != null; w = next()) {
            if (w.equals("v") || w.equals("h")) {
                kind = w;
                continue;
            }
            int n = Integer.parseInt(w), m = number();
            // a v wall stands between (n, m) and (n + 1, m), an h wall between
            // (n, m) and (n, m + 1), and each blocks the move both ways
            if (kind.equals("v")) {
                blocked[n][m][GO_EAST] = blocked[n + 1][m][GO_WEST] = true;
            } else {
                blocked[n][m][GO_NORTH] = blocked[n][m + 1][GO_SOUTH] = true;
            }
        }
        int[][][] dist = new int[SIZE][SIZE][SIDES];
        for (int[][] plane : dist) {
            for (int[] row : plane)
                Arrays.fill(row, -1);
        }
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        dist[a][b][TOP] = 0;
        queue.add(new int[] {a, b, TOP});
        while (!queue.isEmpty()) {
            int[] s = queue.poll();
            int x = s[0], y = s[1], side = s[2];
            if (x == c && y == d && side == TOP) {
                System.out.println(dist[x][y][side]);
                return;
            }
            for (int k = 0; k < MOVES; k++) {
                int nx = x + DX[k], ny = y + DY[k];
                if (nx < 1 || nx > width || ny < 1 || ny > height || blocked[x][y][k])
                    continue;
                int ns = ROLL[k][side];
                if (dist[nx][ny][ns] < 0) {
                    dist[nx][ny][ns] = dist[x][y][side] + 1;
                    queue.add(new int[] {nx, ny, ns});
                }
            }
        }
        System.out.println("No solution");
    }
}
