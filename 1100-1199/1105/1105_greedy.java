import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int SHIFTS = 3;
    static final double EPS = 1e-9;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            all.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(all.toString());
        double t0 = Double.parseDouble(st.nextToken());
        double t1 = Double.parseDouble(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        double[] lo = new double[n], hi = new double[n];
        for (int i = 0; i < n; i++) {
            lo[i] = Double.parseDouble(st.nextToken());
            hi[i] = Double.parseDouble(st.nextToken());
        }
        // greedy cover: each step takes the observer reaching furthest among those
        // already present, so only neighbouring observers of the chain overlap
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> Double.compare(lo[a], lo[b]));
        List<Integer> chain = new ArrayList<>();
        double cur = t0;
        int i = 0;
        while (cur < t1 && i < n) {
            int best = -1;
            for (; i < n && lo[order[i]] <= cur; i++) {
                if (best < 0 || hi[order[i]] > hi[best]) {
                    best = order[i];
                }
            }
            if (best < 0 || hi[best] <= cur) {
                cur = i < n ? lo[order[i]] : t1;
                continue;
            }
            chain.add(best);
            cur = hi[best];
        }
        // dropping every third observer of the chain leaves each piece of time
        // alone in two of the three shifts, so the best shift keeps 2/3 of it
        int m = chain.size(), bestShift = 0;
        double bestAlone = -1;
        for (int shift = 0; shift < SHIFTS; shift++) {
            double alone = 0;
            for (int k = 0; k < m; k++) {
                if (k % SHIFTS == shift) {
                    continue;
                }
                int c = chain.get(k);
                alone += hi[c] - lo[c];
                if (k + 1 < m && (k + 1) % SHIFTS != shift) {
                    alone -= 2 * Math.max(0.0, hi[c] - lo[chain.get(k + 1)]);
                }
            }
            if (alone > bestAlone) {
                bestShift = shift;
                bestAlone = alone;
            }
        }
        if (bestAlone < (t1 - t0) * 2 / SHIFTS - EPS) {
            System.out.println(0);
            return;
        }
        StringBuilder out = new StringBuilder();
        int count = 0;
        for (int k = 0; k < m; k++) {
            if (k % SHIFTS != bestShift) {
                out.append(chain.get(k) + 1).append('\n');
                count++;
            }
        }
        System.out.print(count + "\n" + out);
    }
}
