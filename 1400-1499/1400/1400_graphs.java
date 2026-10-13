import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

public class Main {
    // key presses from the start to every character, by breadth-first search
    static int[] distances(int n, int m, int start) {
        int[] dist = new int[n], queue = new int[n];
        java.util.Arrays.fill(dist, -1);
        dist[start] = 0;
        queue[0] = start;
        for (int h = 0, size = 1; h < size; h++) {
            int v = queue[h];
            // left and right run on through the rows; up and down stop at the edges
            int[] next = {(v + n - 1) % n, (v + 1) % n, v >= m ? v - m : v, v + m < n ? v + m : v};
            for (int u : next)
                if (dist[u] < 0) {
                    dist[u] = dist[v] + 1;
                    queue[size++] = u;
                }
        }
        return dist;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        int[] best = null;
        long bestSum = -1;
        for (int s = 0; s < n; s++) {
            int[] d = distances(n, m, s);
            long sum = 0;
            for (int x : d)
                sum += x;
            if (bestSum < 0 || sum < bestSum) {
                bestSum = sum;
                best = d;
            }
        }
        // round the double itself, as printf does in C
        BigDecimal mean = new BigDecimal((double)bestSum / n).setScale(2, RoundingMode.HALF_EVEN);
        StringBuilder out = new StringBuilder("Mean = " + mean.toPlainString() + "\n");
        for (int i = 0; i < n; i++)
            out.append(best[i]).append(i % m == m - 1 || i == n - 1 ? '\n' : ' ');
        System.out.print(out);
    }
}
