import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int PLAYERS = 3;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        int[][] own = new int[PLAYERS][];
        for (int p = 0; p < PLAYERS; p++) {
            in.nextToken();
            own[p] = new int[(int)in.nval];
            for (int i = 0; i < own[p].length; i++) {
                in.nextToken();
                own[p][i] = (int)in.nval;
            }
        }
        // walk the three sorted lists together, always moving past the
        // smallest current number
        int[] at = new int[PLAYERS];
        int common = 0;
        while (true) {
            boolean done = false;
            for (int p = 0; p < PLAYERS; p++) {
                done = done || at[p] == own[p].length;
            }
            if (done) {
                break;
            }
            int low = own[0][at[0]];
            int high = low;
            for (int p = 1; p < PLAYERS; p++) {
                low = Math.min(low, own[p][at[p]]);
                high = Math.max(high, own[p][at[p]]);
            }
            if (low == high) {
                common++;
            }
            for (int p = 0; p < PLAYERS; p++) {
                if (own[p][at[p]] == low) {
                    at[p]++;
                }
            }
        }
        System.out.println(common);
    }
}
