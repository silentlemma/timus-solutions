import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static final int COMMANDS = 4;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int cells = n * m;
        // go[k][c]: the cell reached from cell c by command k, cells numbered by rows
        int[][] go = new int[COMMANDS][cells];
        for (int k = 0; k < COMMANDS; k++)
            for (int c = 0; c < cells; c++) {
                in.nextToken();
                int row = (int)in.nval;
                in.nextToken();
                int col = (int)in.nval;
                go[k][c] = (row - 1) * m + (col - 1);
            }
        in.nextToken();
        int s = (int)in.nval;
        // the distinct cells the player may stand on, and when each was last added
        int[] cur = new int[cells], next = new int[cells], mark = new int[cells];
        int size = cells;
        for (int c = 0; c < cells; c++) {
            cur[c] = c;
            mark[c] = -1;
        }
        for (int step = 0; step < s; step++) {
            in.nextToken();
            int[] to = go[(int)in.nval - 1];
            int count = 0;
            for (int i = 0; i < size; i++) {
                int t = to[cur[i]];
                if (mark[t] != step) {
                    mark[t] = step;
                    next[count++] = t;
                }
            }
            int[] swap = cur;
            cur = next;
            next = swap;
            size = count;
        }
        Arrays.sort(cur, 0, size);
        StringBuilder out = new StringBuilder();
        out.append(size).append('\n');
        for (int i = 0; i < size; i++)
            out.append(cur[i] / m + 1).append(' ').append(cur[i] % m + 1).append('\n');
        System.out.print(out);
    }
}
