import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static final int CYCLE_CUT = 3; // a cycle on s vertices has path(s - 1) + path(s - 3) sets
    static long[] enemy;
    static long[] path; // independent sets of a path on s vertices
    static Map<Long, Long> memo = new HashMap<>();

    static long count(long mask) {
        if (mask == 0) {
            return 1;
        }
        Long known = memo.get(mask);
        if (known != null) {
            return known;
        }
        // split into connected parts, which multiply
        long low = mask & -mask;
        long part = low;
        long frontier = low;
        while (frontier != 0) {
            long bit = frontier & -frontier;
            frontier ^= bit;
            long grow = enemy[Long.numberOfTrailingZeros(bit)] & mask & ~part;
            part |= grow;
            frontier |= grow;
        }
        long result;
        if (part != mask) {
            result = count(part) * count(mask & ~part);
        } else {
            int size = Long.bitCount(mask);
            int pivot = -1;
            int most = -1;
            int least = size;
            for (long rest = mask; rest != 0; rest &= rest - 1) {
                int v = Long.numberOfTrailingZeros(rest);
                int degree = Long.bitCount(enemy[v] & mask);
                least = Math.min(least, degree);
                if (degree > most) {
                    pivot = v;
                    most = degree;
                }
            }
            if (least == size - 1) {
                result = size + 1; // all pairs are enemies: nobody or one robot
            } else if (most <= 2) {
                result = least <= 1 ? path[size] : path[size - 1] + path[size - CYCLE_CUT];
            } else {
                // branch on a vertex of most enemies: leave it out, or take it
                // and drop all its enemies
                long bit = 1L << pivot;
                result = count(mask & ~bit) + count(mask & ~(enemy[pivot] | bit));
            }
        }
        memo.put(mask, result);
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        enemy = new long[n];
        for (int i = 0; i < n; i++) {
            String row = in.next();
            for (int j = 0; j < n; j++) {
                if (i != j && row.charAt(j) == '0') {
                    enemy[i] |= 1L << j;
                }
            }
        }
        // a working group is a clique of friends, that is an independent set of
        // the graph of non-friends; every group plus the empty one is a day, so
        // the day of rusting is the number of independent sets, empty included
        path = new long[n + 2];
        path[0] = 1;
        path[1] = 2;
        for (int s = 2; s <= n; s++) {
            path[s] = path[s - 1] + path[s - 2];
        }
        System.out.println(count((1L << n) - 1));
    }
}
