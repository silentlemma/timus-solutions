import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        if (in.nextToken() == StreamTokenizer.TT_EOF)
            return;
        int n = (int)in.nval;
        int[][] flags = new int[n][]; // x, y and the number of each flag
        for (int i = 0; i < n; i++) {
            in.nextToken();
            int x = (int)in.nval;
            in.nextToken();
            flags[i] = new int[] {x, (int)in.nval, i + 1};
        }
        Arrays.sort(flags, (a, b) -> b[1] - a[1]);
        // down the slope the x coordinates must zigzag; the longest zigzag keeps
        // the first flag, the last one of every run in one direction, and the end
        StringBuilder out = new StringBuilder().append(flags[0][2]);
        int count = 1;
        for (int i = 1; i < n; i++) {
            boolean last = i == n - 1;
            boolean turns =
                !last && (flags[i][0] > flags[i - 1][0]) != (flags[i + 1][0] > flags[i][0]);
            if (last || turns) {
                out.append(' ').append(flags[i][2]);
                count++;
            }
        }
        System.out.println(count);
        System.out.println(out);
    }
}
