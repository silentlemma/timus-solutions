import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static int n;
    static int[] cover;
    static Map<Integer, Integer> failed = new HashMap<>();
    static List<Integer> drops = new ArrayList<>();

    // pick at most budget cities covering the set left, appending to drops
    static boolean search(int left, int budget) {
        if (left == 0) {
            return true;
        }
        if (budget == 0 || failed.getOrDefault(left, -1) >= budget) {
            return false;
        }
        int[] gain = new int[n];
        int best = 0;
        for (int v = 0; v < n; v++) {
            gain[v] = Integer.bitCount(cover[v] & left);
            best = Math.max(best, gain[v]);
        }
        if (Integer.bitCount(left) > budget * best) {
            failed.put(left, budget);
            return false;
        }
        // the uncovered city with the fewest cities able to hit it
        int u = -1;
        for (int v = 0; v < n; v++) {
            if ((left >> v & 1) == 1
                    && (u < 0 || Integer.bitCount(cover[v]) < Integer.bitCount(cover[u]))) {
                u = v;
            }
        }
        List<Integer> options = new ArrayList<>();
        for (int v = 0; v < n; v++) {
            if ((cover[u] >> v & 1) == 1) {
                options.add(v);
            }
        }
        options.sort((a, b) -> gain[b] - gain[a]);
        List<Integer> tried = new ArrayList<>();
        for (int v : options) {
            int hit = cover[v] & left;
            // skip a drop that hits only part of what a tried one hits
            boolean dominated = false;
            for (int t : tried) {
                dominated |= (hit & ~t) == 0;
            }
            if (dominated) {
                continue;
            }
            tried.add(hit);
            drops.add(v);
            if (search(left & ~hit, budget - 1)) {
                return true;
            }
            drops.remove(drops.size() - 1);
        }
        failed.put(left, budget);
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        int r = in.nextInt();
        int[] x = new int[n], y = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = in.nextInt();
            y[i] = in.nextInt();
        }
        // cover[i]: the cities a bottle dropped on city i destroys
        cover = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int dx = x[i] - x[j], dy = y[i] - y[j];
                if (dx * dx + dy * dy <= r * r) {
                    cover[i] |= 1 << j;
                }
            }
        }
        int everything = (1 << n) - 1;
        int budget = 1;
        while (!search(everything, budget)) {
            budget++;
        }
        StringBuilder out = new StringBuilder();
        out.append(drops.size()).append('\n');
        for (int i = 0; i < drops.size(); i++) {
            out.append(i > 0 ? " " : "").append(drops.get(i) + 1);
        }
        System.out.println(out);
    }
}
