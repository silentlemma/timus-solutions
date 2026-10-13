import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;
    static String[] grid;

    // the black piece slides by (di, dj) when no white cell lies on that side
    // of a black one in the same column or row
    static boolean slides(int di, int dj) {
        for (int k = 0; k < n; k++) {
            boolean seenWhite = false;
            for (int t = 0; t < n; t++) {
                // walk the line from the side the piece moves towards
                int step = di + dj > 0 ? n - 1 - t : t;
                int i = di != 0 ? step : k, j = di != 0 ? k : step;
                if (grid[i].charAt(j) == '0')
                    seenWhite = true;
                else if (seenWhite)
                    return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(in.readLine().trim());
        grid = new String[n];
        for (int i = 0; i < n; i++)
            grid[i] = in.readLine().trim();
        // a sliding direction for either piece is the opposite one for the
        // other; a diagonal slide works only if both of its axis slides do, so
        // trying the four axis directions for the black piece is enough
        boolean yes = slides(-1, 0) || slides(1, 0) || slides(0, -1) || slides(0, 1);
        System.out.println(yes ? "Yes" : "No");
    }
}
