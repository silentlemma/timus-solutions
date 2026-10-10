import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    // no row is longer than all the ships together: 99 * 100
    static final int MAX_SUM = 10000, BITS = 64, WORDS = (MAX_SUM + BITS - 1) / BITS;

    static final int SEARCH_LIMIT = 256, ATTEMPTS = 128, RNG_MOD = 65536;

    static int n, m, calls;
    static boolean limited;
    static int[] ships, rows, owner;
    static Integer[] order;

    static boolean has(long[] s, int v) { return (s[v / BITS] >>> (v % BITS) & 1) == 1; }

    // s | s << by
    static long[] shiftOr(long[] s, int by) {
        long[] out = s.clone();
        int w = by / BITS, b = by % BITS;
        for (int i = WORDS - 1; i >= w; i--) {
            long v = s[i - w] << b;
            if (b > 0 && i - w - 1 >= 0) {
                v |= s[i - w - 1] >>> (BITS - b);
            }
            out[i] |= v;
        }
        return out;
    }

    static boolean pick(int pos, int[] free, long[][] reach, int k, int need) {
        if (limited && ++calls > SEARCH_LIMIT) {
            return false;
        }
        if (need == 0) {
            return fill(pos + 1);
        }
        if (!has(reach[k], need)) {
            return false;
        }
        int last = -1;
        for (int j = k; j < free.length; j++) {
            int length = ships[free[j]];
            // equal ships are interchangeable: try each length once per place
            if (length == last || length > need || !has(reach[j + 1], need - length)) {
                continue;
            }
            last = length;
            owner[free[j]] = order[pos];
            if (pick(pos, free, reach, j + 1, need - length)) {
                return true;
            }
            owner[free[j]] = -1;
            if (limited && calls > SEARCH_LIMIT) {
                return false;
            }
        }
        return false;
    }

    static boolean fill(int pos) {
        int[] free = new int[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (owner[i] < 0) {
                free[count++] = i;
            }
        }
        free = Arrays.copyOf(free, count);
        if (pos == m - 1) {
            // the last row takes every ship that is left
            int sum = 0;
            for (int i : free) {
                sum += ships[i];
            }
            if (sum != rows[order[pos]]) {
                return false;
            }
            for (int i : free) {
                owner[i] = order[pos];
            }
            return true;
        }
        // reach[k]: the sums that the free ships from k on can make
        long[][] reach = new long[count + 1][];
        reach[count] = new long[WORDS];
        reach[count][0] = 1;
        for (int k = count - 1; k >= 0; k--) {
            reach[k] = shiftOr(reach[k + 1], ships[free[k]]);
        }
        for (int q = pos; q < m; q++) {
            if (!has(reach[0], rows[order[q]])) {
                return false;
            }
        }
        return pick(pos, free, reach, 0, rows[order[pos]]);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        Integer[] boxed = new Integer[n];
        for (int i = 0; i < n; i++) {
            boxed[i] = in.nextInt();
        }
        Arrays.sort(boxed, Collections.reverseOrder());
        ships = new int[n];
        for (int i = 0; i < n; i++) {
            ships[i] = boxed[i];
        }
        rows = new int[m];
        for (int i = 0; i < m; i++) {
            rows[i] = in.nextInt();
        }
        // try the shortest rows first as a heuristic
        order = new Integer[m];
        for (int r = 0; r < m; r++) {
            order[r] = r;
        }
        Arrays.sort(order, (a, b) -> rows[a] != rows[b] ? Integer.compare(rows[a], rows[b])
                                                        : Integer.compare(a, b));
        owner = new int[n];
        Arrays.fill(owner, -1);
        int state = 1;
        // restart costly searches in a reproducible order; the final search is complete
        for (int attempt = 0; attempt <= ATTEMPTS; attempt++) {
            calls = 0;
            limited = attempt < ATTEMPTS;
            if (fill(0)) {
                break;
            }
            for (int i = m - 1; i > 0; i--) {
                state = (state * 97 + 1) % RNG_MOD;
                int j = state % (i + 1);
                int temp = order[i];
                order[i] = order[j];
                order[j] = temp;
            }
            int[] rank = new int[101];
            for (int i = 0; i <= 100; i++) {
                rank[i] = i;
            }
            for (int i = 100; i > 1; i--) {
                state = (state * 97 + 1) % RNG_MOD;
                int j = 1 + state % i;
                int temp = rank[i];
                rank[i] = rank[j];
                rank[j] = temp;
            }
            for (int i = 0; i < n; i++) {
                boxed[i] = ships[i];
            }
            Arrays.sort(boxed, (a, b) -> Integer.compare(rank[a], rank[b]));
            for (int i = 0; i < n; i++) {
                ships[i] = boxed[i];
            }
        }
        StringBuilder out = new StringBuilder();
        for (int r = 0; r < m; r++) {
            List<String> row = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (owner[i] == r) {
                    row.add(String.valueOf(ships[i]));
                }
            }
            out.append(row.size()).append('\n').append(String.join(" ", row)).append('\n');
        }
        System.out.print(out);
    }
}
