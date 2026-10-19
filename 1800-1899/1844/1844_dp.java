import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");

    static String next() throws IOException {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(in.readLine());
        }
        return st.nextToken();
    }

    public static void main(String[] args) throws IOException {
        int tests = Integer.parseInt(next());
        StringBuilder out = new StringBuilder();
        while (tests-- > 0) {
            int n = Integer.parseInt(next());
            int m = Integer.parseInt(next());
            int k = Integer.parseInt(next());
            boolean[] sandroCalls = new boolean[n];
            int[] sandroMages = new int[n];
            for (int i = 0; i < n; i++) {
                sandroCalls[i] = next().equals("+");
                sandroMages[i] = Integer.parseInt(next());
            }
            boolean[] zagamiusCalls = new boolean[m];
            int[] zagamiusMages = new int[m];
            for (int j = 0; j < m; j++) {
                zagamiusCalls[j] = next().equals("+");
                zagamiusMages[j] = Integer.parseInt(next());
            }
            // cell (i, j): Sandro has done i steps and Zagamius j; it is taken
            // when both offices hold one mage, and a step is blocked exactly
            // when it leads into a taken cell. Row n + 1 is all taken.
            boolean[][] taken = new boolean[n + 2][m + 1];
            java.util.Arrays.fill(taken[n + 1], true);
            boolean[] withSandro = new boolean[k + 1];
            for (int i = 0; i <= n; i++) {
                if (i > 0) {
                    withSandro[sandroMages[i - 1]] = sandroCalls[i - 1];
                }
                int shared = 0; // mages in both offices
                for (int j = 0; j <= m; j++) {
                    if (j > 0 && withSandro[zagamiusMages[j - 1]]) {
                        shared += zagamiusCalls[j - 1] ? 1 : -1;
                    }
                    taken[i][j] = shared > 0;
                }
            }
            boolean[][] reach = new boolean[n + 1][m + 1];
            reach[0][0] = true;
            boolean stuck = false;
            for (int i = 0; i <= n && !stuck; i++) {
                for (int j = 0; j <= m; j++) {
                    if (!reach[i][j]) {
                        continue;
                    }
                    boolean down = !taken[i + 1][j];
                    boolean right = j < m && !taken[i][j + 1];
                    if (!down && !right && (i < n || j < m)) {
                        stuck = true;
                        break;
                    }
                    if (down) {
                        reach[i + 1][j] = true;
                    }
                    if (right) {
                        reach[i][j + 1] = true;
                    }
                }
            }
            out.append(stuck ? ":-(" : ":-)").append('\n');
        }
        System.out.print(out);
    }
}
