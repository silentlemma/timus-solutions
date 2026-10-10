import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] where = new int[n + 1];
        for (int i = 0; i < n; i++) {
            where[in.nextInt()] = i;
        }
        // rank of the order of 1..k among themselves: element k sweeps once
        // across the order of 1..k-1, to the left in even sweeps and to the
        // right in odd ones, and that order's rank counts the sweeps before
        BigInteger rank = BigInteger.ZERO;
        for (int k = 2; k <= n; k++) {
            int smallerLeft = 0;
            for (int v = 1; v < k; v++) {
                if (where[v] < where[k]) {
                    smallerLeft++;
                }
            }
            int step = rank.testBit(0) ? smallerLeft : k - 1 - smallerLeft;
            rank = rank.multiply(BigInteger.valueOf(k)).add(BigInteger.valueOf(step));
        }
        System.out.println(rank.add(BigInteger.ONE));
    }
}
