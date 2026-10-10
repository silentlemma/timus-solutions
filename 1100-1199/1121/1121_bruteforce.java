import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final int REACH = 5;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int h = (int)in.nval;
        in.nextToken();
        int w = (int)in.nval;
        int[][] grid = new int[h][w];
        for (int r = 0; r < h; r++) {
            for (int c = 0; c < w; c++) {
                in.nextToken();
                grid[r][c] = (int)in.nval;
            }
        }
        // the cells at each distance 1..5, as offsets around a crossing
        List<List<int[]>> rings = new ArrayList<>();
        for (int d = 0; d <= REACH; d++) {
            rings.add(new ArrayList<>());
        }
        for (int dr = -REACH; dr <= REACH; dr++) {
            for (int dc = -REACH; dc <= REACH; dc++) {
                int d = Math.abs(dr) + Math.abs(dc);
                if (d >= 1 && d <= REACH) {
                    rings.get(d).add(new int[] {dr, dc});
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int r = 0; r < h; r++) {
            for (int c = 0; c < w; c++) {
                int found = -1;
                if (grid[r][c] == 0) {
                    found = 0;
                    for (int d = 1; d <= REACH && found == 0; d++) {
                        for (int[] o : rings.get(d)) {
                            int rr = r + o[0], cc = c + o[1];
                            // each type counts once however many branches share it
                            if (rr >= 0 && rr < h && cc >= 0 && cc < w) {
                                found |= grid[rr][cc];
                            }
                        }
                    }
                }
                out.append(found).append(c + 1 < w ? ' ' : '\n');
            }
        }
        System.out.print(out);
    }
}
