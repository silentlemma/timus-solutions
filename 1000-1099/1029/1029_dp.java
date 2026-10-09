import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    // where the cheapest way to an office comes from
    static final int START = 0, BELOW = 1, LEFT = 2, RIGHT = 3;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int m = (int)in.nval;
        in.nextToken();
        int n = (int)in.nval;
        long[][] best = new long[m][n];
        int[][] from = new int[m][n];
        long[] fee = new long[n];
        for (int i = 0; i < m; i++) {
            // from below first, then improve along the floor in both directions
            for (int j = 0; j < n; j++) {
                in.nextToken();
                fee[j] = (long)in.nval;
                best[i][j] = fee[j] + (i > 0 ? best[i - 1][j] : 0);
                from[i][j] = i > 0 ? BELOW : START;
            }
            for (int j = 1; j < n; j++) {
                if (best[i][j - 1] + fee[j] < best[i][j]) {
                    best[i][j] = best[i][j - 1] + fee[j];
                    from[i][j] = LEFT;
                }
            }
            for (int j = n - 2; j >= 0; j--) {
                if (best[i][j + 1] + fee[j] < best[i][j]) {
                    best[i][j] = best[i][j + 1] + fee[j];
                    from[i][j] = RIGHT;
                }
            }
        }
        int i = m - 1, j = 0;
        for (int k = 1; k < n; k++) {
            if (best[i][k] < best[i][j]) {
                j = k;
            }
        }
        // walk the choices back to the first floor, then print them in order
        List<Integer> rooms = new ArrayList<>();
        rooms.add(j + 1);
        while (from[i][j] != START) {
            if (from[i][j] == BELOW) {
                i--;
            } else {
                j += from[i][j] == LEFT ? -1 : 1;
            }
            rooms.add(j + 1);
        }
        StringBuilder out = new StringBuilder();
        for (int k = rooms.size() - 1; k >= 0; k--) {
            out.append(rooms.get(k)).append(k > 0 ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
