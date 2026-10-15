import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        long p = in.nextLong();
        // salaries by rank must avoid a strictly decreasing triple; the state is
        // a, the largest salary so far, and b, the largest salary that follows a
        // larger one (0 if none); ways[a][b] counts such prefixes modulo p
        long[][] ways = new long[k + 1][k + 1];
        long[][] next = new long[k + 1][k + 1];
        for (int z = 1; z <= k; z++) {
            ways[z][0] = 1 % p;
        }
        for (int step = 1; step < n; step++) {
            for (long[] row : next) {
                java.util.Arrays.fill(row, 0);
            }
            // a new salary z is allowed when z >= b, and turns (a, b) into (a, z) if
            // z < a, or into (z, b) if z >= a
            // z < a: (a, b) -> (a, z) for every b <= z, a prefix sum along the row
            for (int a = 1; a <= k; a++) {
                long running = 0;
                for (int c = 0; c < a; c++) {
                    running = (running + ways[a][c]) % p;
                    if (c > 0) {
                        next[a][c] = running;
                    }
                }
            }
            // z >= a: (a, b) -> (z, b) for every a <= z, a prefix sum down the column
            for (int b = 0; b < k; b++) {
                long running = 0;
                for (int z = b + 1; z <= k; z++) {
                    running = (running + ways[z][b]) % p;
                    next[z][b] = (next[z][b] + running) % p;
                }
            }
            long[][] swap = ways;
            ways = next;
            next = swap;
        }
        long total = 0;
        for (long[] row : ways) {
            for (long x : row) {
                total = (total + x) % p;
            }
        }
        // month total + 1 counted from the first month, numbered 1..p in its year
        System.out.println(total + 1);
    }
}
