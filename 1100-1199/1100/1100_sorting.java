import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.StreamTokenizer;

public class Main {
    static final int MOST = 100;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] team = new int[n], solved = new int[n];
        int[] count = new int[MOST + 2];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            team[i] = (int)in.nval;
            in.nextToken();
            solved[i] = (int)in.nval;
            count[MOST - solved[i] + 1]++;
        }
        // bubble sort never swaps equal scores, so teams with the same score keep
        // their input order: a stable counting sort by score does the same
        for (int s = 1; s <= MOST + 1; s++) {
            count[s] += count[s - 1];
        }
        int[] order = new int[n];
        for (int i = 0; i < n; i++) {
            order[count[MOST - solved[i]]++] = i;
        }
        PrintWriter out = new PrintWriter(System.out);
        StringBuilder line = new StringBuilder();
        for (int i : order) {
            line.setLength(0);
            line.append(team[i]).append(' ').append(solved[i]);
            out.println(line);
        }
        out.flush();
    }
}
