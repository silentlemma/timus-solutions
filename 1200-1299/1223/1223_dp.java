import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int FLOORS = 1000;
    // ten eggs already allow a binary search over all the floors
    static final int EGGS = 10;

    public static void main(String[] args) throws IOException {
        // best[k][n]: the fewest drops that settle n floors with k eggs; with d
        // drops and k eggs one can tell apart reach(d, k) floors, where
        // reach(d, k) = reach(d - 1, k - 1) + reach(d - 1, k) + 1
        int[][] best = new int[EGGS + 1][FLOORS + 1];
        int[] reach = new int[EGGS + 1];
        for (int d = 1; reach[1] < FLOORS; d++) {
            int[] next = new int[EGGS + 1];
            for (int k = 1; k <= EGGS; k++) {
                next[k] = Math.min(FLOORS, reach[k - 1] + reach[k] + 1);
                for (int n = reach[k] + 1; n <= next[k]; n++) {
                    best[k][n] = d;
                }
            }
            reach = next;
        }
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        StringBuilder out = new StringBuilder();
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int eggs = (int)in.nval;
            in.nextToken();
            int floors = (int)in.nval;
            if (eggs == 0 && floors == 0) {
                break;
            }
            out.append(best[Math.min(eggs, EGGS)][floors]).append('\n');
        }
        System.out.print(out);
    }
}
