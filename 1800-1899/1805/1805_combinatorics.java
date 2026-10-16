import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int TURNS = 4;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long k = in.nextLong();
        // the four cells a quarter turn takes into each other form an orbit; a
        // grille opens exactly one cell of every orbit
        int[][] orbit = new int[n][n];
        for (int[] row : orbit) Arrays.fill(row, -1);
        int orbits = 0;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (orbit[r][c] != -1) continue;
                int rr = r, cc = c;
                for (int t = 0; t < TURNS; t++) {
                    orbit[rr][cc] = orbits;
                    int keep = rr;
                    rr = cc;
                    cc = n - 1 - keep;
                }
                orbits++;
            }
        }
        // left[o]: cells of orbit o not passed yet, -1 once its window is cut
        int[] left = new int[orbits];
        Arrays.fill(left, TURNS);
        StringBuilder out = new StringBuilder();
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                int o = orbit[r][c];
                if (left[o] == -1) {
                    out.append('0');
                    continue;
                }
                left[o]--;
                // grilles with a 0 here: every open orbit picks one of its
                // remaining cells
                long withZero = 1;
                for (int rest : left) {
                    if (rest != -1) withZero *= rest;
                }
                if (k <= withZero) {
                    out.append('0');
                } else {
                    k -= withZero;
                    out.append('1');
                    left[o] = -1;
                }
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
