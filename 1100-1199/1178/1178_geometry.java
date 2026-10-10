import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = br.readLine(); line != null; line = br.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = Integer.parseInt(in.nextToken());
        long[] x = new long[n + 1], y = new long[n + 1];
        Integer[] cities = new Integer[n];
        for (int i = 1; i <= n; i++) {
            x[i] = Long.parseLong(in.nextToken());
            y[i] = Long.parseLong(in.nextToken());
            cities[i - 1] = i;
        }
        Arrays.sort(cities,
                    (a, b) -> x[a] != x[b] ? Long.compare(x[a], x[b]) : Long.compare(y[a], y[b]));
        // neighbours in (x, y) order: each road lies in its own strip of x, and
        // two roads can share only the border line, where they end at different
        // cities because no three cities are on one line
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < n; k += 2) {
            out.append(cities[k]).append(' ').append(cities[k + 1]).append('\n');
        }
        System.out.print(out);
    }
}
