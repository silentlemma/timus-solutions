import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int NEED = 2; // a run needs two generating intervals inside it to be split

    // g[l][r]: columns l .. r-1 must be a union of chosen intervals inside them.
    // Going right, an interval that two smaller chosen ones already cover is
    // dropped, and those it leaned on move right: the smallest such family.
    static void smallestFamily(boolean[][] g, int width) {
        for (int right = 1; right <= width; right++) {
            while (true) {
                int[] count = new int[width + 1];
                int covered = 0, rest = 0; // chosen inside [t, u), those starting before t
                int u = right, t = right - 1;
                boolean redundant = true;
                while (u > t) {
                    covered -= count[u];
                    for (int left = 0; left < u; left++) {
                        if (!g[left][u])
                            continue;
                        count[left]++;
                        if (left >= t)
                            covered++;
                        else
                            rest++;
                    }
                    if (covered + rest < NEED) {
                        redundant = false;
                        break;
                    }
                    while (covered < NEED) {
                        t--;
                        covered += count[t];
                        rest -= count[t];
                    }
                    u--;
                }
                if (!redundant)
                    break;
                int w = u;
                while (!g[w][right])
                    w++;
                g[w][right] = false;
                for (int end = right - 1; w > u; end--) {
                    int x = u;
                    while (x < w && !g[x][end])
                        x++;
                    if (x == w)
                        continue;
                    g[x][end] = false;
                    g[w][end] = true;
                    w = x;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        while (!st.hasMoreTokens())
            st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken());
        while (!st.hasMoreTokens())
            st = new StringTokenizer(in.readLine());
        int m = Integer.parseInt(st.nextToken());
        // the black pixels of a column form one run from top to bottom
        int[] top = new int[m], bottom = new int[m];
        for (int c = 0; c < m; c++) {
            top[c] = n;
            bottom[c] = -1;
        }
        boolean[][] g = new boolean[m + 1][m + 1];
        for (int row = 0; row < n; row++) {
            String line = in.readLine().trim();
            while (line.isEmpty())
                line = in.readLine().trim();
            for (int col = 0; col < m;) {
                if (line.charAt(col) == '0') {
                    col++;
                    continue;
                }
                int left = col;
                while (col < m && line.charAt(col) == '1') {
                    top[col] = Math.min(top[col], row);
                    bottom[col] = Math.max(bottom[col], row);
                    col++;
                }
                g[left][col] = true;
            }
        }
        smallestFamily(g, m);
        // a chosen interval of columns spans every row where all of them are black
        StringBuilder out = new StringBuilder();
        int count = 0;
        for (int lo = 0; lo < m; lo++)
            for (int hi = lo + 1; hi <= m; hi++) {
                if (!g[lo][hi])
                    continue;
                int first = 0, last = n - 1;
                for (int c = lo; c < hi; c++) {
                    first = Math.max(first, top[c]);
                    last = Math.min(last, bottom[c]);
                }
                out.append(first + 1).append(' ').append(lo + 1).append(' ');
                out.append(last + 1).append(' ').append(hi).append('\n');
                count++;
            }
        System.out.print(count + "\n" + out);
    }
}
