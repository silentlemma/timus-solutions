import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final int WORD = 64;
    static DataInputStream in = new DataInputStream(System.in);

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0') c = in.read();
        int v = 0;
        while (c >= '0') {
            v = v * 10 + (c - '0');
            c = in.read();
        }
        return v;
    }

    static int n, words, half, now;
    static long[][] reach;
    static int[] size, cost, from, to, rare;
    static List<List<int[]>> into = new ArrayList<>();
    static long[] full, missing;

    static boolean feasible(int m) {
        for (int a = 0; a < n; a++) {
            // one operator of a covering pair pays for at least half
            if (size[a] < half) continue;
            boolean any = false;
            for (int w = 0; w < words; w++) {
                missing[w] = full[w] ^ reach[a][w];
                any = any || missing[w] != 0;
            }
            if (!any) return true;
            int t = 0;
            for (int y : rare) {
                if ((missing[y / WORD] >>> (y % WORD) & 1) == 1) {
                    t = y;
                    break;
                }
            }
            for (int[] pair : into.get(t)) {
                if (pair[0] >= m) continue;
                boolean covers = true;
                for (int w = 0; w < words && covers; w++) {
                    covers = (reach[pair[1]][w] & missing[w]) == missing[w];
                }
                if (covers) return true;
            }
        }
        return false;
    }

    // take the edges between two prefixes in or out
    static void move(int target) {
        for (; now < target; now++) {
            reach[from[now]][to[now] / WORD] ^= 1L << (to[now] % WORD);
            size[from[now]]++;
        }
        for (; now > target; now--) {
            reach[from[now - 1]][to[now - 1] / WORD] ^= 1L << (to[now - 1] % WORD);
            size[from[now - 1]]--;
        }
    }

    public static void main(String[] args) throws IOException {
        n = readInt();
        int k = readInt();
        Map<Long, Integer> cheapest = new HashMap<>();
        for (int i = 0; i < k; i++) {
            int x = readInt(), y = readInt(), c = readInt();
            long key = (long) (x - 1) * n + (y - 1);
            Integer old = cheapest.get(key);
            if (old == null || c < old) cheapest.put(key, c);
        }
        // the edges sorted by cost; the first m of them are those of cost up to
        // the m-th cost
        long[][] list = new long[cheapest.size()][];
        int total = 0;
        for (Map.Entry<Long, Integer> e : cheapest.entrySet()) {
            list[total++] = new long[] {e.getValue(), e.getKey()};
        }
        Arrays.sort(list, (p, q) -> Long.compare(p[0], q[0]));
        cost = new int[total];
        from = new int[total];
        to = new int[total];
        for (int i = 0; i < total; i++) {
            cost[i] = (int) list[i][0];
            from[i] = (int) (list[i][1] / n);
            to[i] = (int) (list[i][1] % n);
        }
        words = (n + WORD - 1) / WORD;
        // reach[x]: the targets x pays for, as a bit set
        reach = new long[n][words];
        size = new int[n];
        for (int y = 0; y < n; y++) into.add(new ArrayList<>());
        for (int i = 0; i < total; i++) into.get(to[i]).add(new int[] {i, from[i]});
        // the target with the fewest ways in comes first when picking a witness
        Integer[] order = new Integer[n];
        for (int y = 0; y < n; y++) order[y] = y;
        Arrays.sort(order, (p, q) -> into.get(p).size() - into.get(q).size());
        rare = new int[n];
        for (int y = 0; y < n; y++) rare[y] = order[y];
        full = new long[words];
        Arrays.fill(full, -1L);
        if (n % WORD != 0) full[words - 1] = (1L << (n % WORD)) - 1;
        missing = new long[words];
        half = (n + 1) / 2;
        move(total);
        if (total == 0 || !feasible(total)) {
            System.out.println("No solution");
            return;
        }
        int lo = 1, hi = total;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            move(mid);
            if (feasible(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        System.out.println(cost[lo - 1]);
    }
}
