import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        long[] plan = new long[n + m - 1];
        for (int i = 0; i < plan.length; i++) plan[i] = Long.parseLong(st.nextToken());
        long stock = 0;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            // after t months of the same change x the stock is stock + t x, which
            // must reach the plan of that month; x is rounded up, also below zero
            long x = Long.MIN_VALUE;
            for (int t = 1; t <= m; t++) {
                x = Math.max(x, -Math.floorDiv(stock - plan[i + t - 1], t));
            }
            if (i > 0) out.append(' ');
            out.append(x);
            stock += x;
        }
        System.out.println(out);
    }
}
