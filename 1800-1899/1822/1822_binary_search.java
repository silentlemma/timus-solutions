import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;

public class Main {
    static final long PERCENT = 100;
    static final long OUTPUT_SCALE = 100000000;

    static int n;
    static long limit;
    static int[] own, order, start, kids;

    // x = 100 num/den: a noble with c vassals waits for ceil(num c/den)
    // of them, so the wait is that order statistic of their ready days
    static boolean readyBy(long num, long den) {
        long[] ready = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            int v = order[i];
            int c = start[v + 1] - start[v];
            long need = (num * c + den - 1) / den, wait = 0;
            if (need > 0) {
                long[] times = new long[c];
                for (int j = 0; j < c; j++) {
                    times[j] = ready[kids[start[v] + j]];
                }
                Arrays.sort(times);
                wait = times[(int) need - 1];
            }
            ready[v] = wait + own[v];
        }
        return ready[1] <= limit;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int) in.nval;
        in.nextToken();
        limit = (long) in.nval;
        own = new int[n + 1];
        int[] parent = new int[n + 1];
        start = new int[n + 2];
        for (int i = 2; i <= n; i++) {
            in.nextToken();
            parent[i] = (int) in.nval;
            in.nextToken();
            own[i] = (int) in.nval;
            start[parent[i] + 1]++;
        }
        // vassals of v are kids[start[v] .. start[v + 1])
        for (int v = 1; v <= n; v++) {
            start[v + 1] += start[v];
        }
        kids = new int[Math.max(n - 1, 0)];
        int[] fill = start.clone();
        for (int i = 2; i <= n; i++) {
            kids[fill[parent[i]]++] = i;
        }
        order = new int[n];
        order[0] = 1;
        for (int i = 0, size = 1; i < size; i++) {
            int v = order[i];
            for (int j = start[v]; j < start[v + 1]; j++) {
                order[size++] = kids[j];
            }
        }
        // the answer is a largest fraction m/c over the vassal counts c
        boolean[] seen = new boolean[n + 1];
        List<long[]> fractions = new ArrayList<>();
        for (int v = 1; v <= n; v++) {
            int c = start[v + 1] - start[v];
            if (c > 0 && !seen[c]) {
                seen[c] = true;
                for (int m = 0; m <= c; m++) {
                    fractions.add(new long[] {m, c});
                }
            }
        }
        if (fractions.isEmpty()) {
            fractions.add(new long[] {1, 1});
        }
        fractions.sort((a, b) -> Long.compare(a[0] * b[1], b[0] * a[1]));
        int lo = 0, hi = fractions.size() - 1;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (readyBy(fractions.get(mid)[0], fractions.get(mid)[1])) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        long[] best = fractions.get(lo);
        long answer = (PERCENT * best[0] * OUTPUT_SCALE + best[1] / 2) / best[1];
        System.out.printf(Locale.US, "%d.%08d%n", answer / OUTPUT_SCALE, answer % OUTPUT_SCALE);
    }
}
