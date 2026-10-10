import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[] count = new int[n + 1];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            count[(int)in.nval]++;
        }
        // card k shows k - 1 and k, so the number x fits cards x and x + 1,
        // and going up from the smallest number, card x is useless to
        // anything later, so it is taken first
        boolean[] used = new boolean[n + 2];
        for (int x = 0; x <= n; x++) {
            for (int card = x; card <= x + 1 && count[x] > 0; card++) {
                if (card >= 1 && card <= n && !used[card]) {
                    used[card] = true;
                    count[x]--;
                }
            }
            if (count[x] > 0) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}
