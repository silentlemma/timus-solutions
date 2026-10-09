import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int KINDS = 3;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        long[] length = new long[KINDS], price = new long[KINDS];
        for (int k = 0; k < KINDS; k++) {
            in.nextToken();
            length[k] = (long)in.nval;
        }
        for (int k = 0; k < KINDS; k++) {
            in.nextToken();
            price[k] = (long)in.nval;
        }
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int a = (int)in.nval;
        in.nextToken();
        int b = (int)in.nval;
        long[] x = new long[n + 1];
        for (int i = 2; i <= n; i++) {
            in.nextToken();
            x[i] = (long)in.nval;
        }
        if (a > b) {
            int t = a;
            a = b;
            b = t;
        }
        // cost[i]: the cheapest way from a to i; it never decreases along the
        // line, so for every kind of ticket the farthest start in reach is best
        long[] cost = new long[n + 1];
        int[] from = {a, a, a};
        for (int i = a + 1; i <= b; i++) {
            cost[i] = -1;
            for (int k = 0; k < KINDS; k++) {
                while (x[i] - x[from[k]] > length[k]) {
                    from[k]++;
                }
                if (from[k] < i && (cost[i] < 0 || cost[from[k]] + price[k] < cost[i])) {
                    cost[i] = cost[from[k]] + price[k];
                }
            }
        }
        System.out.println(cost[b]);
    }
}
