import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int SMALLEST_CYCLE = 3;

    static int pairs(int s) { return s * (s - 1) / 2; }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        // a pair is not critical exactly when both computers lie in the same
        // 2-edge-connected part; such a part has one computer or at least
        // three, so the sizes must split n with pairs(size) summing to pairs(n) - k
        int target = pairs(n) - k;
        List<Integer> sizes = new ArrayList<>();
        sizes.add(1);
        for (int s = SMALLEST_CYCLE; s <= n; s++) {
            sizes.add(s);
        }
        // reach[m][t] tells whether m computers can be split with t inner pairs
        boolean[][] reach = new boolean[n + 1][pairs(n) + 1];
        reach[0][0] = true;
        for (int m = 1; m <= n; m++) {
            for (int s : sizes) {
                if (s <= m) {
                    for (int t = pairs(s); t <= pairs(n); t++) {
                        reach[m][t] |= reach[m - s][t - pairs(s)];
                    }
                }
            }
        }
        if (target < 0 || !reach[n][target]) {
            System.out.println(-1);
            return;
        }
        List<Integer> parts = new ArrayList<>();
        for (int m = n, t = target; m > 0;) {
            for (int s : sizes) {
                if (s <= m && pairs(s) <= t && reach[m - s][t - pairs(s)]) {
                    parts.add(s);
                    m -= s;
                    t -= pairs(s);
                    break;
                }
            }
        }
        // each part is a cycle (or a single computer), and bridges join the
        // first computers of consecutive parts
        StringBuilder out = new StringBuilder();
        int first = 1, prev = 0;
        for (int s : parts) {
            if (s > 1) {
                for (int j = 0; j < s; j++) {
                    out.append(first + j).append(' ').append(first + (j + 1) % s).append('\n');
                }
            }
            if (prev > 0) {
                out.append(prev).append(' ').append(first).append('\n');
            }
            prev = first;
            first += s;
        }
        System.out.print(out);
    }
}
