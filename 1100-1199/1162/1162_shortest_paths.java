import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    // sums closer than this count as equal
    static final double EPS = 1e-9;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer tok = new StringTokenizer(all.toString());
        int n = Integer.parseInt(tok.nextToken()), m = Integer.parseInt(tok.nextToken());
        int s = Integer.parseInt(tok.nextToken());
        double v = Double.parseDouble(tok.nextToken());
        List<int[]> ends = new ArrayList<>();
        List<double[]> terms = new ArrayList<>();
        for (int k = 0; k < m; k++) {
            int a = Integer.parseInt(tok.nextToken()), b = Integer.parseInt(tok.nextToken());
            double rab = Double.parseDouble(tok.nextToken()),
                   cab = Double.parseDouble(tok.nextToken());
            double rba = Double.parseDouble(tok.nextToken()),
                   cba = Double.parseDouble(tok.nextToken());
            ends.add(new int[] {a, b});
            terms.add(new double[] {rab, cab});
            ends.add(new int[] {b, a});
            terms.add(new double[] {rba, cba});
        }
        // best[c] is the most money of currency c that can be held; a pass
        // that still improves something after n passes has found a gaining cycle
        double[] best = new double[n + 1];
        Arrays.fill(best, -1);
        best[s] = v;
        boolean changed = false;
        for (int pass = 0; pass < n; pass++) {
            changed = false;
            for (int e = 0; e < ends.size(); e++) {
                int from = ends.get(e)[0], to = ends.get(e)[1];
                double rate = terms.get(e)[0], fee = terms.get(e)[1];
                if (best[from] - fee >= 0) {
                    double got = (best[from] - fee) * rate;
                    if (got > best[to] + EPS) {
                        best[to] = got;
                        changed = true;
                    }
                }
            }
            if (best[s] > v + EPS || !changed) {
                break;
            }
        }
        System.out.println(best[s] > v + EPS || changed ? "YES" : "NO");
    }
}
