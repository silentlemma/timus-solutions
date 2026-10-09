import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int MAX_COORD = 32000;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // stars come by y, then x: the level of a star is the number of stars
        // already seen with x not greater than its own; a Fenwick tree counts them
        int[] tree = new int[MAX_COORD + 2];
        int[] count = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            int x = (int)in.nval;
            in.nextToken();
            int level = 0;
            for (int j = x + 1; j > 0; j -= j & -j) {
                level += tree[j];
            }
            count[level]++;
            for (int j = x + 1; j <= MAX_COORD + 1; j += j & -j) {
                tree[j]++;
            }
        }
        StringBuilder out = new StringBuilder();
        for (int c : count) {
            out.append(c).append('\n');
        }
        System.out.print(out);
    }
}
