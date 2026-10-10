import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int INF = 1 << 30;
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tok = new StringTokenizer("");

    // The next number of the input, skipping the "*" lines between blocks.
    static int next() throws IOException {
        String token;
        do {
            while (!tok.hasMoreTokens()) {
                tok = new StringTokenizer(in.readLine());
            }
            token = tok.nextToken();
        } while (token.equals("*"));
        return Integer.parseInt(token);
    }

    public static void main(String[] args) throws IOException {
        int levels = next();
        // the cheapest cost of reaching each planet of the current level
        int[] cost = {0};
        for (int level = 0; level < levels; level++) {
            int k = next();
            int[] nxt = new int[k];
            Arrays.fill(nxt, INF);
            for (int planet = 0; planet < k; planet++) {
                for (int src = next(); src != 0; src = next()) {
                    int price = next();
                    if (cost[src - 1] < INF) {
                        nxt[planet] = Math.min(nxt[planet], cost[src - 1] + price);
                    }
                }
            }
            cost = nxt;
        }
        System.out.println(Arrays.stream(cost).min().getAsInt());
    }
}
