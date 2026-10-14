import java.util.*;

public class Main {
    static final int SHOOTERS = 3;
    static final int AIR = -1; // a shot into the air
    static final int INDEX_SUM = 0 + 1 + 2;
    static final double EPS = 1e-12; // survival chances closer than this count as equal

    static double[] acc = new double[SHOOTERS];
    static int[] order = new int[SHOOTERS];

    // the most accurate living opponent of all three; the earlier one on a tie
    static int strongest(int shooter) {
        int best = -1;
        for (int i = 0; i < SHOOTERS; i++)
            if (i != shooter && (best < 0 || acc[i] > acc[best]))
                best = i;
        return best;
    }

    // two left, first to shoot: first wins p / (p + q - p q)
    static double[] duel(int first, int second) {
        double p = acc[first], q = acc[second];
        double[] c = new double[SHOOTERS];
        c[first] = p / (p + q - p * q);
        c[second] = 1 - c[first];
        return c;
    }

    // the duel left after a hit, with the next living shooter first
    static double[] afterHit(int turn, int killed) {
        int first = order[(turn + 1) % SHOOTERS];
        if (first == killed)
            first = order[(turn + 2) % SHOOTERS];
        return duel(first, INDEX_SUM - killed - first);
    }

    // chances when all three live and order[turn] shoots; A never misses, so
    // the shooting stops at A's turn at the latest
    static double[] three(int turn) {
        int shooter = order[turn];
        if (shooter == 0)
            return afterHit(turn, strongest(shooter));
        double p = acc[shooter];
        double[] miss = three((turn + 1) % SHOOTERS);
        Map<Integer, double[]> outcomes = new HashMap<>();
        outcomes.put(AIR, miss);
        double best = miss[shooter];
        for (int target = 0; target < SHOOTERS; target++) {
            if (target == shooter)
                continue;
            double[] hit = afterHit(turn, target), mixed = new double[SHOOTERS];
            for (int i = 0; i < SHOOTERS; i++)
                mixed[i] = p * hit[i] + (1 - p) * miss[i];
            outcomes.put(target, mixed);
            best = Math.max(best, mixed[shooter]);
        }
        // on a tie the strongest opponent is shot, then A, B, C, then the air
        for (int choice : new int[] {strongest(shooter), 0, 1, 2, AIR})
            if (outcomes.containsKey(choice) && outcomes.get(choice)[shooter] >= best - EPS)
                return outcomes.get(choice);
        return miss;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        for (int i = 0; i < SHOOTERS; i++)
            acc[i] = in.nextDouble();
        double[] total = new double[SHOOTERS];
        int orders = 0;
        for (int a = 0; a < SHOOTERS; a++)
            for (int b = 0; b < SHOOTERS; b++) {
                if (b == a)
                    continue;
                order = new int[] {a, b, INDEX_SUM - a - b};
                double[] c = three(0);
                for (int i = 0; i < SHOOTERS; i++)
                    total[i] += c[i];
                orders++;
            }
        double share = 1.0 / orders;
        System.out.printf(Locale.US, "%.5f %.5f %.5f\n", total[0] * share, total[1] * share,
                          total[2] * share);
    }
}
