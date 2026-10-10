import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = reader.readLine(); line != null; line = reader.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer in = new StringTokenizer(all.toString());
        int m = Integer.parseInt(in.nextToken()), n = Integer.parseInt(in.nextToken());
        StringBuilder out = new StringBuilder();
        if (m == 0 || n == 0) {
            for (int r = 0; r < m; r++) {
                out.append('\n');
            }
            System.out.print(out);
            return;
        }
        String[] fin = new String[m];
        for (int r = 0; r < m; r++) {
            fin[r] = in.nextToken();
        }
        // row r as a bit mask of its cells visited an odd number of times
        long[] odd = new long[m];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                odd[r] |= (Long.parseLong(in.nextToken()) & 1) << c;
            }
        }
        // the offsets of integer length, the cell itself included
        List<int[]> offsets = new ArrayList<>();
        for (int dr = 1 - m; dr < m; dr++) {
            for (int dc = 1 - n; dc < n; dc++) {
                int q = dr * dr + dc * dc, root = (int)Math.round(Math.sqrt(q));
                if (root * root == q) {
                    offsets.add(new int[] {dr, dc});
                }
            }
        }
        long full = (1L << n) - 1;
        for (int r = 0; r < m; r++) {
            // bit c is set when cell (r, c) was flipped an odd number of times
            long flips = 0;
            for (int[] o : offsets) {
                if (r + o[0] >= 0 && r + o[0] < m) {
                    long row = odd[r + o[0]];
                    flips ^= (o[1] >= 0 ? row >>> o[1] : row << -o[1]) & full;
                }
            }
            for (int c = 0; c < n; c++) {
                boolean black = (fin[r].charAt(c) == 'B') ^ ((flips >>> c & 1) == 1);
                out.append(black ? 'B' : 'W');
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
