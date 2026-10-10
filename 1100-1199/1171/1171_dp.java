import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int SIDE = 4, ROOMS = SIDE * SIDE;
    static final long NONE = -(1L << 62);
    // moves inside a level: name, row step, column step
    static final String NAMES = "NESW";
    static final int[] DR = {-1, 0, 1, 0}, DC = {0, 1, 0, -1};

    static int n, start;
    static int[][] food, door;
    // best[lv][s][e][k]: most food on a path of k rooms from s to e
    static int[][][][] best;
    static int[][][] choice;
    static long total, count;

    static int step(int u, int d) {
        int r = u / SIDE + DR[d], c = u % SIDE + DC[d];
        return r >= 0 && r < SIDE && c >= 0 && c < SIDE ? r * SIDE + c : -1;
    }

    static void walk(int lv, int s, int u, int mask, int k, int sum) {
        if (sum > best[lv][s][u][k]) {
            best[lv][s][u][k] = sum;
        }
        for (int d = 0; d < DR.length; d++) {
            int v = step(u, d);
            if (v >= 0 && (mask >> v & 1) == 0) {
                walk(lv, s, v, mask | 1 << v, k + 1, sum + food[lv][v]);
            }
        }
    }

    // appends a path of `left` rooms from u to e with exactly `rest` food
    static boolean findMoves(int lv, int u, int e, int mask, int left, int rest,
                             StringBuilder path) {
        if (left == 1) {
            return u == e && rest == food[lv][u];
        }
        for (int d = 0; d < DR.length; d++) {
            int v = step(u, d);
            if (v >= 0 && (mask >> v & 1) == 0) {
                path.append(NAMES.charAt(d));
                if (findMoves(lv, v, e, mask | 1 << v, left - 1, rest - food[lv][u], path)) {
                    return true;
                }
                path.setLength(path.length() - 1);
            }
        }
        return false;
    }

    // maximises den * food - num * rooms; returns the per-level choices and
    // leaves their food and room count in total and count
    static int[][] bestPath(long num, long den) {
        long[] after = new long[ROOMS];
        for (int lv = n - 1; lv >= 0; lv--) {
            long[] here = new long[ROOMS];
            for (int s = 0; s < ROOMS; s++) {
                here[s] = NONE;
                for (int e = 0; e < ROOMS; e++) {
                    if ((lv < n - 1 && door[lv][e] == 0) || after[e] == NONE) {
                        continue;
                    }
                    for (int k = 1; k <= ROOMS; k++) {
                        int w = best[lv][s][e][k];
                        long v = den * w - num * k + after[e];
                        if (w >= 0 && v > here[s]) {
                            here[s] = v;
                            choice[lv][s] = new int[] {s, e, k};
                        }
                    }
                }
            }
            after = here;
        }
        int[][] plan = new int[n][];
        total = count = 0;
        for (int lv = 0, s = start; lv < n; lv++) {
            plan[lv] = choice[lv][s];
            total += best[lv][s][plan[lv][1]][plan[lv][2]];
            count += plan[lv][2];
            s = plan[lv][1];
        }
        return plan;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        food = new int[n][ROOMS];
        door = new int[n][ROOMS];
        for (int lv = 0; lv < n; lv++) {
            for (int u = 0; u < ROOMS; u++) {
                in.nextToken();
                food[lv][u] = (int)in.nval;
            }
            for (int u = 0; u < ROOMS; u++) {
                in.nextToken();
                door[lv][u] = (int)in.nval;
            }
        }
        in.nextToken();
        int r = (int)in.nval;
        in.nextToken();
        start = (r - 1) * SIDE + (int)in.nval - 1;
        best = new int[n][ROOMS][ROOMS][ROOMS + 1];
        choice = new int[n][ROOMS][];
        for (int lv = 0; lv < n; lv++) {
            for (int s = 0; s < ROOMS; s++) {
                for (int[] row : best[lv][s]) {
                    java.util.Arrays.fill(row, -1);
                }
                walk(lv, s, s, 1 << s, 1, food[lv][s]);
            }
        }
        // Dinkelbach: move to the better ratio until no path beats the current
        long num = 0, den = 1;
        int[][] chosen = null;
        while (true) {
            int[][] plan = bestPath(num, den);
            if (total * den <= num * count) {
                break;
            }
            num = total;
            den = count;
            chosen = plan;
        }
        StringBuilder moves = new StringBuilder();
        for (int lv = 0; lv < n; lv++) {
            if (lv > 0) {
                moves.append('D');
            }
            int[] p = chosen[lv];
            findMoves(lv, p[0], p[1], 1 << p[0], p[2], best[lv][p[0]][p[1]][p[2]], moves);
        }
        System.out.printf("%.4f%n%d%n", (double)num / den, moves.length());
        if (moves.length() > 0) {
            System.out.println(moves);
        }
    }
}
