import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt(), n = in.nextInt(), k = in.nextInt();
        long[][] binom = new long[m + 1][m + 1];
        for (int i = 0; i <= m; i++) {
            binom[i][0] = 1;
            for (int j = 1; j <= i; j++)
                binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
        }
        // step[c][d]: ways to follow a column with c ones by one with d ones,
        // turning at most k zeros into ones (at most 2^40 of them)
        long[][] step = new long[m + 1][m + 1];
        for (int c = 0; c <= m; c++)
            for (int t = 0; t <= k && t <= m - c; t++)
                for (int s = 0; s <= c; s++)
                    step[c][s + t] += binom[m - c][t] * binom[c][s];
        // ways[c]: fillings of the columns so far whose last column has c ones
        BigInteger[] ways = new BigInteger[m + 1];
        for (int c = 0; c <= m; c++)
            ways[c] = BigInteger.valueOf(binom[m][c]);
        for (int col = 1; col < n; col++) {
            BigInteger[] next = new BigInteger[m + 1];
            for (int d = 0; d <= m; d++) {
                next[d] = BigInteger.ZERO;
                for (int c = 0; c <= m; c++)
                    next[d] = next[d].add(ways[c].multiply(BigInteger.valueOf(step[c][d])));
            }
            ways = next;
        }
        BigInteger total = BigInteger.ZERO;
        for (BigInteger w : ways)
            total = total.add(w);
        System.out.println(total);
    }
}
