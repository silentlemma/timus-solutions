import java.util.Scanner;

public class Main {
    static final int POINTS = 5;
    // point k has index k - 1: start 0, middle points FIRST_MIDDLE..LAST_MIDDLE, finish END
    static final int FIRST_MIDDLE = 1, POINT_3 = 2, LAST_MIDDLE = 3, END = 4;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[][] d = new int[POINTS][POINTS];
        for (int i = 0; i < POINTS; i++)
            for (int j = 0; j < POINTS; j++)
                d[i][j] = in.nextInt();
        // points 2, 3 and 4 (indices 1, 2, 3) come in any order, except that 3
        // may not be the last of them
        int best = -1;
        int[] route = null;
        for (int a = FIRST_MIDDLE; a <= LAST_MIDDLE; a++)
            for (int b = FIRST_MIDDLE; b <= LAST_MIDDLE; b++)
                for (int c = FIRST_MIDDLE; c <= LAST_MIDDLE; c++) {
                    if (a == b || a == c || b == c || c == POINT_3)
                        continue;
                    int cost = d[0][a] + d[a][b] + d[b][c] + d[c][END];
                    if (best < 0 || cost < best) {
                        best = cost;
                        route = new int[] {0, a, b, c, END};
                    }
                }
        StringBuilder out = new StringBuilder().append(best).append('\n');
        for (int i = 0; i < POINTS; i++)
            out.append(route[i] + 1).append(i + 1 < POINTS ? ' ' : '\n');
        System.out.print(out);
    }
}
