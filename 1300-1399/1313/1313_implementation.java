import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer words = new StringTokenizer("");
        while (!words.hasMoreTokens())
            words = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(words.nextToken());
        String[][] grid = new String[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                while (!words.hasMoreTokens())
                    words = new StringTokenizer(in.readLine());
                grid[i][j] = words.nextToken();
            }
        }
        // diagonal s holds the cells with row + column = s; each is read from
        // its lowest row up
        StringBuilder out = new StringBuilder();
        for (int s = 0; s <= 2 * n - 2; s++) {
            for (int i = Math.min(s, n - 1); i >= Math.max(0, s - n + 1); i--) {
                if (out.length() > 0)
                    out.append(' ');
                out.append(grid[i][s - i]);
            }
        }
        System.out.println(out);
    }
}
