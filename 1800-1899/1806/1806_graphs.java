import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static final int DIGITS = 10;
    static Map<Long, Integer> index = new HashMap<>();
    static long[] best;
    static int[] before;
    static PriorityQueue<long[]> heap = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));

    static void relax(long value, long time, int from) {
        Integer v = index.get(value);
        if (v != null && (best[v] == -1 || time < best[v])) {
            best[v] = time;
            before[v] = from;
            heap.add(new long[] {time, v});
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        StringTokenizer tokens = new StringTokenizer(in.readLine());
        long[] cost = new long[DIGITS], place = new long[DIGITS];
        for (int p = 0; p < DIGITS; p++) cost[p] = Long.parseLong(tokens.nextToken());
        place[DIGITS - 1] = 1;
        for (int p = DIGITS - 2; p >= 0; p--) place[p] = place[p + 1] * DIGITS;
        long[] number = new long[n];
        for (int i = 0; i < n; i++) {
            number[i] = Long.parseLong(in.readLine().trim());
            index.put(number[i], i);
        }
        best = new long[n];
        before = new int[n];
        Arrays.fill(best, -1);
        Arrays.fill(before, -1);
        best[0] = 0;
        heap.add(new long[] {0, 0});
        long[] digit = new long[DIGITS];
        while (!heap.isEmpty()) {
            long[] top = heap.poll();
            long d = top[0];
            int u = (int) top[1];
            if (d > best[u]) continue;
            if (u == n - 1) break;
            long value = number[u];
            for (int p = 0; p < DIGITS; p++) digit[p] = value / place[p] % DIGITS;
            // neighbours with the first change at digit p share a prefix of p
            for (int p = 0; p < DIGITS; p++) {
                long low = value - digit[p] * place[p];
                for (int other = 0; other < DIGITS; other++) {
                    if (other != digit[p]) relax(low + other * place[p], d + cost[p], u);
                }
                for (int q = p + 1; q < DIGITS; q++) {
                    if (digit[q] != digit[p]) {
                        long swapped = value + (digit[q] - digit[p]) * (place[p] - place[q]);
                        relax(swapped, d + cost[p], u);
                    }
                }
            }
        }
        if (best[n - 1] == -1) {
            System.out.println(-1);
            return;
        }
        List<Integer> path = new ArrayList<>();
        for (int v = n - 1; v != -1; v = before[v]) path.add(v + 1);
        StringBuilder out = new StringBuilder();
        out.append(best[n - 1]).append('\n').append(path.size()).append('\n');
        for (int i = path.size() - 1; i >= 0; i--) {
            out.append(path.get(i)).append(i > 0 ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
