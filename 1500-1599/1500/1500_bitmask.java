import java.util.Scanner;

public class Main {
    static final int HALF = 10; // categories are split into a low and a high half of the mask
    static int lowSize;
    static int[][] low, high; // neighbours of a crossing under half a set

    // whether the roads of the categories in s lead from crossing 0 to 1
    static boolean connects(int s) {
        int lo = s & ((1 << lowSize) - 1), hi = s >> lowSize;
        int reach = 1, todo = 1;
        while (todo != 0) {
            int u = Integer.numberOfTrailingZeros(todo);
            todo &= todo - 1;
            int fresh = (low[u][lo] | high[u][hi]) & ~reach;
            reach |= fresh;
            todo |= fresh;
            if ((reach & 2) != 0)
                return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt(), n = in.nextInt(), m = in.nextInt();
        // byCategory[u][c]: the crossings next to u along roads of category c
        int[][] byCategory = new int[n][k];
        for (int i = 0; i < m; i++) {
            int a = in.nextInt(), b = in.nextInt(), c = in.nextInt();
            byCategory[a][c] |= 1 << b;
            byCategory[b][c] |= 1 << a;
        }
        lowSize = Math.min(k, HALF);
        int highSize = k - lowSize;
        low = new int[n][1 << lowSize];
        high = new int[n][1 << highSize];
        for (int u = 0; u < n; u++) {
            for (int s = 1; s < (1 << lowSize); s++)
                low[u][s] = low[u][s & (s - 1)] | byCategory[u][Integer.numberOfTrailingZeros(s)];
            for (int s = 1; s < (1 << highSize); s++)
                high[u][s] = high[u][s & (s - 1)] |
                             byCategory[u][lowSize + Integer.numberOfTrailingZeros(s)];
        }
        // fewer permits first
        for (int size = 1; size <= k; size++)
            for (int s = 0; s < (1 << k); s++)
                if (Integer.bitCount(s) == size && connects(s)) {
                    StringBuilder out = new StringBuilder().append(size).append('\n');
                    for (int c = 0, first = 1; c < k; c++)
                        if ((s >> c & 1) == 1) {
                            out.append(first == 1 ? "" : " ").append(c);
                            first = 0;
                        }
                    System.out.println(out);
                    return;
                }
    }
}
