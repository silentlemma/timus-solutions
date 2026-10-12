import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine())
            all.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(all.toString());
        int n = Integer.parseInt(words.nextToken()), m = Integer.parseInt(words.nextToken());
        int[] k = new int[n], first = new int[n], last = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            k[i] = Integer.parseInt(words.nextToken());
            first[i] = Integer.parseInt(words.nextToken());
            last[i] = Integer.parseInt(words.nextToken());
            total += k[i];
        }
        int target = Math.min(m, total);
        // best[j]: the cheapest way to make exactly j brooms at the factories so far
        double[] best = new double[target + 1];
        Arrays.fill(best, Double.POSITIVE_INFINITY);
        best[0] = 0;
        int reach = 0;
        for (int i = 0; i < n; i++) {
            double step = k[i] > 1 ? (double)(last[i] - first[i]) / (k[i] - 1) : 0.0;
            // cost[x]: x brooms at this factory, the j-th one costing first + step (j - 1)
            double[] cost = new double[k[i] + 1];
            for (int x = 0; x <= k[i]; x++)
                cost[x] = (double)x * first[i] + step * x * (x - 1) / 2;
            reach = Math.min(target, reach + k[i]);
            double[] fresh = best.clone();
            for (int j = 1; j <= reach; j++) {
                double here = fresh[j];
                for (int x = 1, most = Math.min(j, k[i]); x <= most; x++) {
                    double value = best[j - x] + cost[x];
                    if (value < here)
                        here = value;
                }
                fresh[j] = here;
            }
            best = fresh;
        }
        StringBuilder out = new StringBuilder();
        if (target < m)
            out.append("Maximum possible amount: ").append(target).append('\n');
        out.append(String.format(Locale.US, "Minimum possible cost: %.2f", best[target]));
        out.append('\n');
        System.out.print(out);
    }
}
