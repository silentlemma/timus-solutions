import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static final int FLOWS = 12;
    static final int MINUTES = 10;
    static final int NIBBLE = 4; // a need is at most 10 minutes, four bits in the memo key

    // the flows each flow crosses or merges with, read off the crossing: 1-3
    // come from the south, 4-6 from the east, 7-9 from the north and 10-12 from
    // the west, each turning right, going straight on and turning left
    static final int[][] CROSSES = {
        {9, 11}, {4, 5, 6, 9, 11, 12}, {5, 6, 7, 8, 11, 12}, {2, 12}, {2, 3, 7, 8, 9, 12},
        {2, 3, 8, 9, 10, 11}, {3, 5}, {3, 5, 6, 10, 11, 12}, {1, 2, 5, 6, 11, 12},
        {6, 8}, {1, 2, 3, 6, 8, 9}, {2, 3, 4, 5, 8, 9}};
    static List<int[]> sets = new ArrayList<>();
    static int widest = 0;
    static Map<Long, Boolean> memo = new HashMap<>();

    // whether left green phases can serve every flow its need
    static boolean fits(int[] need, int left) {
        int top = 0;
        int total = 0;
        long key = left;
        for (int i = 0; i < FLOWS; i++) {
            total += need[i];
            key = key << NIBBLE | need[i];
            if (need[i] > need[top]) {
                top = i;
            }
        }
        if (need[top] > left || total > widest * left) {
            return false;
        }
        if (total == 0) {
            return true;
        }
        Boolean known = memo.get(key);
        if (known != null) {
            return known;
        }
        // some minute must open the flow that still needs the most
        boolean ok = false;
        for (int[] set : sets) {
            boolean opens = false;
            for (int i : set) {
                opens |= i == top;
            }
            if (!opens || ok) {
                continue;
            }
            int[] rest = need.clone();
            for (int i : set) {
                rest[i] = Math.max(rest[i] - 1, 0);
            }
            ok = fits(rest, left - 1);
        }
        memo.put(key, ok);
        return ok;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] cars = new int[FLOWS];
        int[] speed = new int[FLOWS];
        for (int i = 0; i < FLOWS; i++) {
            cars[i] = in.nextInt();
        }
        for (int i = 0; i < FLOWS; i++) {
            speed[i] = in.nextInt();
        }
        int[] conflict = new int[FLOWS];
        for (int flow = 0; flow < FLOWS; flow++) {
            for (int other : CROSSES[flow]) {
                conflict[flow] |= 1 << (other - 1);
            }
        }
        // a minute lets through a set of flows that cross nowhere; it never hurts
        // to open more, so only the maximal such sets matter
        for (int mask = 1; mask < 1 << FLOWS; mask++) {
            boolean free = true;
            boolean maximal = true;
            List<Integer> set = new ArrayList<>();
            for (int i = 0; i < FLOWS; i++) {
                boolean inside = (mask >> i & 1) == 1;
                boolean cross = (conflict[i] & mask) != 0;
                free &= !(inside && cross);
                maximal &= inside || cross;
                if (inside) {
                    set.add(i);
                }
            }
            if (free && maximal) {
                sets.add(set.stream().mapToInt(Integer::intValue).toArray());
                widest = Math.max(widest, set.size());
            }
        }
        int lo = 0;
        int hi = 0;
        for (int c : cars) {
            hi = Math.max(hi, c);
        }
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int[] need = new int[FLOWS];
            boolean small = true;
            for (int i = 0; i < FLOWS; i++) {
                need[i] = cars[i] > mid ? (cars[i] - mid + speed[i] - 1) / speed[i] : 0;
                small &= need[i] <= MINUTES;
            }
            if (small && fits(need, MINUTES)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        System.out.println(lo);
    }
}
