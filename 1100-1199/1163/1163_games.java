import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    // a draught is hit when its centre is this close to the path of the
    // centre of the moving one, two radii of 0.4
    static final double REACH = 0.8;
    static final double EPS = 1e-9;
    static final int SIDE = 8, PIECES = 2 * SIDE;

    static int[][] kills = new int[PIECES][];
    static byte[] memo; // -1 unknown, else whether the player to move wins

    // the player to move, red (0) or white (1), wins from here
    static boolean wins(int alive, int turn) {
        int key = alive << 1 | turn;
        if (memo[key] >= 0) {
            return memo[key] == 1;
        }
        int own = alive & (turn == 1 ? ((1 << SIDE) - 1) << SIDE : (1 << SIDE) - 1);
        boolean result = false;
        for (int p = 0; p < PIECES && !result; p++) {
            if ((own >> p & 1) == 1) {
                for (int s : kills[p]) {
                    if (!wins(alive & ~s, 1 - turn)) {
                        result = true;
                        break;
                    }
                }
            }
        }
        memo[key] = (byte)(result ? 1 : 0);
        return result;
    }

    // the same angle in [0, 2 pi)
    static double turnAround(double a) {
        double full = 2 * Math.PI;
        return (a % full + full) % full;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in).useLocale(Locale.US);
        double[] x = new double[PIECES], y = new double[PIECES];
        for (int k = 0; k < PIECES; k++) {
            x[k] = in.nextDouble();
            y[k] = in.nextDouble();
        }
        // every direction kills the draughts within REACH of its ray; the set
        // changes only where the ray becomes tangent to some draught, so the
        // tangent directions and the gaps between them give every possible set
        for (int p = 0; p < PIECES; p++) {
            double[] angles = new double[2 * (PIECES - 1)];
            int count = 0;
            for (int q = 0; q < PIECES; q++) {
                if (q != p) {
                    double d = Math.hypot(x[q] - x[p], y[q] - y[p]);
                    double centre = Math.atan2(y[q] - y[p], x[q] - x[p]);
                    double half = Math.asin(Math.min(1.0, REACH / d));
                    angles[count++] = turnAround(centre - half);
                    angles[count++] = turnAround(centre + half);
                }
            }
            Arrays.sort(angles);
            double[] tries = Arrays.copyOf(angles, 2 * count);
            for (int k = 0; k < count; k++) {
                double next = k + 1 < count ? angles[k + 1] : angles[0] + 2 * Math.PI;
                tries[count + k] = (angles[k] + next) / 2;
            }
            TreeSet<Integer> sets = new TreeSet<>();
            for (double t : tries) {
                double ux = Math.cos(t), uy = Math.sin(t);
                int mask = 1 << p;
                for (int q = 0; q < PIECES; q++) {
                    double dx = x[q] - x[p], dy = y[q] - y[p];
                    boolean ahead = dx * ux + dy * uy >= 0;
                    if (q != p && ahead && Math.abs(dx * uy - dy * ux) <= REACH + EPS) {
                        mask |= 1 << q;
                    }
                }
                sets.add(mask);
            }
            kills[p] = sets.stream().mapToInt(Integer::intValue).toArray();
        }
        memo = new byte[1 << (PIECES + 1)];
        Arrays.fill(memo, (byte)-1);
        System.out.println(wins((1 << PIECES) - 1, 0) ? "RED" : "WHITE");
    }
}
