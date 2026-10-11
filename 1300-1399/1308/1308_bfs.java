import java.util.*;

public class Main {
    static final int ROLLS = 70;
    static final int DIRS = 6;
    static final double TURN = 60; // degrees between neighbouring directions
    static final int OFF = 80;     // coordinates stay within ROLLS of the origin
    static final int SIZE = 2 * OFF + 1;
    static final int PRICE = 3; // where a move keeps its number of rolls
    // the six directions of a hexagonal lattice, as integer combinations of
    // the first two of them
    static final int[] UA = {1, 0, -1, -1, 0, 1};
    static final int[] UB = {0, 1, 1, 0, -1, -1};
    static final double[] CLASSES = {0, 90}; // edges at 0 and 180, or at 90 and 270 degrees

    static int index(int a, int b, int d) { return ((a + OFF) * SIZE + (b + OFF)) * DIRS + d; }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double tx = Double.parseDouble(in.next()), ty = Double.parseDouble(in.next());
        // a jump through the base in half steps: (1 + sqrt 3) / 2 = 1/2 + sin 60
        double side = (1 + 2 * Math.sin(Math.toRadians(TURN))) / 2;
        double best = Math.hypot(tx, ty); // no rolls at all
        int[] cost = new int[SIZE * SIZE * DIRS];
        for (double start : CLASSES) {
            double[] wx = new double[DIRS], wy = new double[DIRS];
            for (int k = 0; k < DIRS; k++) {
                wx[k] = Math.cos(Math.toRadians(start + TURN * k));
                wy[k] = Math.sin(Math.toRadians(start + TURN * k));
            }
            // a state is a triangle lying on the table: twice its apex position
            // (in steps of the base jump) and the direction from the apex to the
            // base edge; it costs one roll to reach from the start
            Arrays.fill(cost, ROLLS);
            List<List<int[]>> buckets = new ArrayList<>();
            for (int c = 0; c <= ROLLS; c++)
                buckets.add(new ArrayList<>());
            for (int u : new int[] {0, DIRS / 2}) {
                int[] s = {UA[u], UB[u], (u + DIRS / 2) % DIRS};
                cost[index(s[0], s[1], s[2])] = 1;
                buckets.get(1).add(s);
            }
            for (int c = 1; c < ROLLS; c++) {
                List<int[]> bucket = buckets.get(c);
                for (int i = 0; i < bucket.size(); i++) {
                    int a = bucket.get(i)[0], b = bucket.get(i)[1], d = bucket.get(i)[2];
                    if (cost[index(a, b, d)] != c)
                        continue;
                    // roll onto the base: its centre is half a step beyond the apex
                    int ea = a + UA[d], eb = b + UB[d];
                    double x = side * (ea * wx[0] + eb * wx[1]);
                    double y = side * (ea * wy[0] + eb * wy[1]);
                    best = Math.min(best, Math.hypot(x - tx, y - ty));
                    // a side face is one roll away, the far side of the base two
                    int[][] next = {
                        {a, b, (d + 1) % DIRS, 1},
                        {a, b, (d + DIRS - 1) % DIRS, 1},
                        {a + 2 * UA[d], b + 2 * UB[d], (d + DIRS / 2) % DIRS, 2},
                    };
                    for (int[] n : next) {
                        int nc = c + n[PRICE];
                        if (nc < ROLLS && cost[index(n[0], n[1], n[2])] > nc) {
                            cost[index(n[0], n[1], n[2])] = nc;
                            buckets.get(nc).add(new int[] {n[0], n[1], n[2]});
                        }
                    }
                }
            }
        }
        System.out.printf(Locale.US, "%.4f%n", best);
    }
}
