import java.util.Scanner;

public class Main {
    static final int DIGITS = 10;

    // ways[s]: strings of k digits with digit sum s
    static long[] sums(int k) {
        long[] ways = {1};
        for (int i = 0; i < k; i++) {
            long[] next = new long[ways.length + DIGITS - 1];
            for (int s = 0; s < ways.length; s++) {
                for (int d = 0; d < DIGITS; d++) {
                    next[s + d] += ways[s];
                }
            }
            ways = next;
        }
        return ways;
    }

    // pairs of a k-digit and an m-digit string with equal digit sums
    static long matching(int k, int m) {
        long[] a = sums(k), b = sums(m);
        long total = 0;
        for (int s = 0; s < a.length && s < b.length; s++) {
            total += a[s] * b[s];
        }
        return total;
    }

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // size[in the first half][odd] counts positions; lucky both ways means the
        // odd digits of the first half sum like the even ones of the second half,
        // and the even digits of the first half like the odd ones of the second
        int[][] size = new int[2][2];
        for (int p = 1; p <= n; p++) {
            size[p <= n / 2 ? 1 : 0][p % 2]++;
        }
        System.out.println(matching(size[1][1], size[0][0]) * matching(size[1][0], size[0][1]));
    }
}
