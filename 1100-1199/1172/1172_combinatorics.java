import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static final int ISLANDS = 3;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // plane[b][c][i]: sequences of islands that start on the tourist's
        // island 0, use a, b and c cities of the islands (a fixed per plane),
        // never repeat an island twice in a row and end on island i
        BigInteger[][][] prev = null;
        for (int a = 1; a <= n; a++) {
            BigInteger[][][] cur = new BigInteger[n + 1][n + 1][ISLANDS];
            for (int b = 0; b <= n; b++) {
                for (int c = 0; c <= n; c++) {
                    BigInteger[] cell = cur[b][c];
                    java.util.Arrays.fill(cell, BigInteger.ZERO);
                    if (a == 1 && b == 0 && c == 0) {
                        cell[0] = BigInteger.ONE;
                    }
                    if (a > 1) {
                        cell[0] = prev[b][c][1].add(prev[b][c][2]);
                    }
                    if (b > 0) {
                        cell[1] = cur[b - 1][c][0].add(cur[b - 1][c][2]);
                    }
                    if (c > 0) {
                        cell[2] = cur[b][c - 1][0].add(cur[b][c - 1][1]);
                    }
                }
            }
            prev = cur;
        }
        // the trip closes back on island 0, so it must not end there
        BigInteger total = prev[n][n][1].add(prev[n][n][2]);
        // cities fill the island slots in any order, except the fixed start,
        // and every trip is counted once in each direction; (n-1)! n!^2 is
        // the product of k^2 (k-1) over k from 2 to n
        for (long k = 2; k <= n; k++) {
            total = total.multiply(BigInteger.valueOf(k * k * (k - 1)));
        }
        System.out.println(total.shiftRight(1));
    }
}
