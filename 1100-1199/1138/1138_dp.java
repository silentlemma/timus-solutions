import java.util.Scanner;

public class Main {
    // a raise must be a whole number of percent of this base
    static final int PERCENT = 100;

    static int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), s = in.nextInt();
        if (s > n) {
            System.out.println(0);
            return;
        }
        // jobs[a] is the longest run of jobs from salary s ending at salary
        // a; a raise from a is a whole percent exactly when it is a multiple
        // of a / gcd(a, 100)
        int[] jobs = new int[n + 1];
        jobs[s] = 1;
        int best = 1;
        for (int a = s; a <= n; a++) {
            if (jobs[a] == 0) {
                continue;
            }
            best = Math.max(best, jobs[a]);
            int step = a / gcd(a, PERCENT);
            for (int b = a + step; b <= n; b += step) {
                jobs[b] = Math.max(jobs[b], jobs[a] + 1);
            }
        }
        System.out.println(best);
    }
}
