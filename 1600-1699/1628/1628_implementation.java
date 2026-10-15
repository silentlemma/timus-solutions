import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int m = (int)in.nval;
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        HashSet<Long> black = new HashSet<>();
        int[] xs = new int[k], ys = new int[k];
        int[] rowCount = new int[m + 2], colCount = new int[n + 2];
        for (int i = 0; i < k; i++) {
            in.nextToken();
            xs[i] = (int)in.nval;
            in.nextToken();
            ys[i] = (int)in.nval;
            black.add((long)xs[i] * (n + 2) + ys[i]);
            rowCount[xs[i]]++;
            colCount[ys[i]]++;
        }
        int[][] rows = new int[m + 2][], cols = new int[n + 2][];
        for (int x = 0; x < m + 2; x++)
            rows[x] = new int[rowCount[x]];
        for (int y = 0; y < n + 2; y++)
            cols[y] = new int[colCount[y]];
        Arrays.fill(rowCount, 0);
        Arrays.fill(colCount, 0);
        for (int i = 0; i < k; i++) {
            rows[xs[i]][rowCount[xs[i]]++] = ys[i];
            cols[ys[i]][colCount[ys[i]]++] = xs[i];
        }
        long count = 0;
        // A white run of length 2 or more is a strip by itself; a single white
        // cell is one only if it is closed in the other direction too.
        for (int x = 1; x <= m; x++) {
            int[] r = rows[x];
            Arrays.sort(r);
            int prev = 0;
            for (int i = 0; i <= r.length; i++) {
                int b = i < r.length ? r[i] : n + 1, length = b - prev - 1;
                int y = prev + 1;
                boolean up = x == 1 || black.contains((long)(x - 1) * (n + 2) + y);
                boolean down = x == m || black.contains((long)(x + 1) * (n + 2) + y);
                if (length >= 2 || (length == 1 && up && down))
                    count++;
                prev = b;
            }
        }
        for (int y = 1; y <= n; y++) {
            int[] c = cols[y];
            Arrays.sort(c);
            int prev = 0;
            for (int i = 0; i <= c.length; i++) {
                int b = i < c.length ? c[i] : m + 1;
                if (b - prev - 1 >= 2)
                    count++;
                prev = b;
            }
        }
        System.out.println(count);
    }
}
