import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int TRIO = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] times = new int[n];
        for (int i = 0; i < n; i++) {
            times[i] = in.nextInt();
        }
        Arrays.sort(times);
        long total = 0;
        int left = n;
        // move the two slowest across each round, in whichever of two ways
        // is cheaper: the fastest escorts each of them, or the two fastest
        // cross, one returns, the two slowest cross and the other returns
        while (left > TRIO) {
            int a = times[0], b = times[1], y = times[left - 2], z = times[left - 1];
            total += Math.min(2 * a + y + z, a + 2 * b + z);
            left -= 2;
        }
        if (left == TRIO) {
            total += times[0] + times[1] + times[2];
        } else {
            total += times[left - 1];
        }
        System.out.println(total);
    }
}
