import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final long SCALE = 1000;
    static final long SAFE = 256 * SCALE;
    static final int DEODORANT = 1, PERFUME = 2, BOTH = DEODORANT | PERFUME;
    static final long DOWN_NUM = 3, DOWN_DEN = 4;
    static final long UP_NUM = 11, UP_DEN = 10;
    static final int INF = 1 << 30;

    static class Move {
        final int kind, deodorized, perfumed, set;

        Move(int kind, int deodorized, int perfumed, int set) {
            this.kind = kind;
            this.deodorized = deodorized;
            this.perfumed = perfumed;
            this.set = set;
        }
    }

    static List<Move> moves = new ArrayList<>();
    static long[] total;
    static int full;

    static List<Integer> collect(int need, long change) {
        List<Integer> sets = new ArrayList<>();
        for (int m = 1; m <= full; m++) {
            if ((m & need) == need && (total[m] + change) % SAFE == 0) {
                sets.add(m);
            }
        }
        return sets;
    }

    // keep the sets not inside another one: carrying more costs nothing,
    // since fruit already outside can be brought back and carried again
    static void addMaximal(List<Integer> sets, int kind, int i, int j) {
        sets.sort((a, b) -> Integer.bitCount(b) - Integer.bitCount(a));
        List<Integer> kept = new ArrayList<>();
        for (int a : sets) {
            boolean inside = false;
            for (int b : kept) {
                if ((a & b) == a) {
                    inside = true;
                    break;
                }
            }
            if (!inside) {
                kept.add(a);
                moves.add(new Move(kind, i, j, a));
            }
        }
    }

    static String names(int set, int n) {
        StringBuilder s = new StringBuilder();
        s.append(Integer.bitCount(set));
        for (int k = 0; k < n; k++) {
            if ((set >> k & 1) == 1) {
                s.append(' ').append(k + 1);
            }
        }
        return s.toString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // aromas times 1000 keep 3/4, 11/10 and both together whole
        long[] w = new long[n];
        for (int i = 0; i < n; i++) {
            w[i] = in.nextInt() * SCALE;
        }
        full = (1 << n) - 1;
        total = new long[full + 1];
        for (int m = 1; m <= full; m++) {
            total[m] = total[m & (m - 1)] + w[Integer.numberOfTrailingZeros(m)];
        }
        // what each spray adds to the total of a set holding the fruit
        long[] weaker = new long[n], stronger = new long[n];
        for (int i = 0; i < n; i++) {
            weaker[i] = w[i] * DOWN_NUM / DOWN_DEN - w[i];
            stronger[i] = w[i] * UP_NUM / UP_DEN - w[i];
        }
        addMaximal(collect(0, 0), 0, -1, -1);
        for (int i = 0; i < n; i++) {
            addMaximal(collect(1 << i, weaker[i]), DEODORANT, i, -1);
            addMaximal(collect(1 << i, stronger[i]), PERFUME, -1, i);
            for (int j = 0; j < n; j++) {
                long change = weaker[i] + stronger[j];
                if (i == j) {
                    change = w[i] * DOWN_NUM * UP_NUM / (DOWN_DEN * UP_DEN) - w[i];
                }
                addMaximal(collect(1 << i | 1 << j, change), BOTH, i, j);
            }
        }
        // carrying more is never worse, so of the moves with the same sprays
        // only the largest sets are kept, and none inside a set needing fewer
        // sprays
        moves.sort((a, b) -> Integer.bitCount(b.set) - Integer.bitCount(a.set));
        List<Move> kept = new ArrayList<>();
        for (int kind = 0; kind <= BOTH; kind++) {
            int start = kept.size();
            for (Move mv : moves) {
                if (mv.kind != kind) {
                    continue;
                }
                boolean inside = false;
                for (int k = 0; k < kept.size() && !inside; k++) {
                    Move other = kept.get(k);
                    boolean fewer = (other.kind & kind) == other.kind;
                    inside = (k >= start || fewer) && (mv.set & other.set) == mv.set;
                }
                if (!inside) {
                    kept.add(mv);
                }
            }
        }
        int count = kept.size();
        int[] kindOf = new int[count], setOf = new int[count];
        for (int k = 0; k < count; k++) {
            kindOf[k] = kept.get(k).kind;
            setOf[k] = kept.get(k).set;
        }
        // best[used][mask]: fewest exits that get the fruit of mask out
        int[][] best = new int[BOTH + 1][full + 1];
        int[][] choice = new int[BOTH + 1][full + 1];
        for (int used = 0; used <= BOTH; used++) {
            for (int m = 1; m <= full; m++) {
                best[used][m] = INF;
            }
        }
        for (int mask = 1; mask <= full; mask++) {
            for (int used = 0; used <= BOTH; used++) {
                int[] here = best[used];
                for (int k = 0; k < count; k++) {
                    if ((kindOf[k] & used) != 0 || (setOf[k] & mask) == 0) {
                        continue;
                    }
                    int value = best[used | kindOf[k]][mask & ~setOf[k]] + 1;
                    if (value < here[mask]) {
                        here[mask] = value;
                        choice[used][mask] = k;
                    }
                }
            }
        }
        moves = kept;
        if (best[0][full] >= INF) {
            System.out.println("IMPOSSIBLE");
            return;
        }
        List<String> lines = new ArrayList<>();
        for (int mask = full, used = 0; mask != 0; ) {
            Move mv = moves.get(choice[used][mask]);
            int back = mv.set & ~mask;
            if (back != 0) {
                lines.add("return " + names(back, n));
            }
            if (mv.deodorized >= 0) {
                lines.add("dearomatize " + (mv.deodorized + 1));
            }
            if (mv.perfumed >= 0) {
                lines.add("aromatize " + (mv.perfumed + 1));
            }
            lines.add("take " + names(mv.set, n));
            used |= mv.kind;
            mask &= ~mv.set;
        }
        StringBuilder out = new StringBuilder();
        out.append(lines.size()).append('\n');
        for (String line : lines) {
            out.append(line).append('\n');
        }
        System.out.print(out);
    }
}
