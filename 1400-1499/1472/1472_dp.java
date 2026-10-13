import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static final long NONE = -1; // no subordinate yet: a private cannot be cut

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] boss = new int[n + 1], price = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            in.nextToken();
            boss[i] = (int)in.nval;
            in.nextToken();
            price[i] = (int)in.nval;
        }
        // cut[v]: the cheapest way to separate v from every private below it
        long[] cut = new long[n + 1];
        Arrays.fill(cut, NONE);
        for (int v = n; v >= 2; v--) {
            long cost = cut[v] == NONE ? price[v] : Math.min(price[v], cut[v]);
            int p = boss[v];
            cut[p] = cut[p] == NONE ? cost : cut[p] + cost;
        }
        System.out.println(cut[1] + ".00");
    }
}
