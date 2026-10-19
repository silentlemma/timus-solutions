import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int MONKEYS = 5;
    static long[] xs = new long[MONKEYS];
    static long[] ys = new long[MONKEYS];

    // y / x = b - c x along a shot, so the slopes y / x of points on one shot
    // lie on a line in x; compared with all fractions cleared
    static boolean oneShot(int i, int j, int k) {
        long left = (ys[k] * xs[i] - ys[i] * xs[k]) * xs[j] * (xs[j] - xs[i]);
        long right = (ys[j] * xs[i] - ys[i] * xs[j]) * xs[k] * (xs[k] - xs[i]);
        return left == right;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for (int i = 0; i < MONKEYS; i++) {
            xs[i] = in.nextLong();
            ys[i] = in.nextLong();
        }
        int full = (1 << MONKEYS) - 1;
        List<Integer> shots = new ArrayList<>();
        for (int i = 0; i < MONKEYS; i++) {
            shots.add(1 << i);
        }
        for (int i = 0; i < MONKEYS; i++) {
            for (int j = 0; j < MONKEYS; j++) {
                // gravity bends the path down: the slope y / x must fall as x grows
                if (xs[i] < xs[j] && ys[i] * xs[j] > ys[j] * xs[i]) {
                    int mask = 0;
                    for (int k = 0; k < MONKEYS; k++) {
                        if (oneShot(i, j, k)) {
                            mask |= 1 << k;
                        }
                    }
                    shots.add(mask);
                }
            }
        }
        int[] need = new int[full + 1];
        Arrays.fill(need, MONKEYS);
        need[0] = 0;
        for (int mask = 0; mask <= full; mask++) {
            for (int shot : shots) {
                need[mask | shot] = Math.min(need[mask | shot], need[mask] + 1);
            }
        }
        System.out.println(need[full]);
    }
}
