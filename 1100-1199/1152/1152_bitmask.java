import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int n;
    static int[] monsters, volleys, memo;

    static int alive(int mask) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if ((mask >> i & 1) == 1) {
                sum += monsters[i];
            }
        }
        return sum;
    }

    // the least damage still to come with these balconies occupied; the
    // monsters left after each volley fire once
    static int damage(int mask) {
        if (mask == 0) {
            return 0;
        }
        if (memo[mask] >= 0) {
            return memo[mask];
        }
        int best = -1;
        for (int v : volleys) {
            if ((mask & v) != 0) {
                int rest = mask & ~v, cost = alive(rest) + damage(rest);
                if (best < 0 || cost < best) {
                    best = cost;
                }
            }
        }
        return memo[mask] = best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        monsters = new int[n];
        for (int i = 0; i < n; i++) {
            monsters[i] = in.nextInt();
        }
        // a volley at i clears balconies i - 1, i and i + 1 around the circle
        volleys = new int[n];
        for (int i = 0; i < n; i++) {
            volleys[i] = 1 << (i + n - 1) % n | 1 << i | 1 << (i + 1) % n;
        }
        memo = new int[1 << n];
        Arrays.fill(memo, -1);
        System.out.println(damage((1 << n) - 1));
    }
}
