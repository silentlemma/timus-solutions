import java.util.Scanner;

public class Main {
    static final int SHORTEST = 3; // a route has at least three stops

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        int[] adj = new int[n];
        for (int i = 0; i < m; i++) {
            int a = in.nextInt() - 1, b = in.nextInt() - 1;
            adj[a] |= 1 << b;
            adj[b] |= 1 << a;
        }

        // paths[mask * n + v]: simple paths from the lowest stop of mask through
        // all of mask, ending at v; a path that can close counts its cycle twice
        int full = (1 << n) - 1;
        long[] paths = new long[(full + 1) * n];
        long[] cycles = new long[full + 1];
        for (int s = 0; s < n; s++)
            paths[(1 << s) * n + s] = 1;
        for (int mask = 1; mask <= full; mask++) {
            int low = mask & -mask, start = Integer.numberOfTrailingZeros(mask);
            int free = ~mask & ~((low << 1) - 1) & full; // stops that may still join
            long closing = 0;
            for (int v = 0; v < n; v++) {
                long count = paths[mask * n + v];
                if (count == 0)
                    continue;
                if ((adj[v] >> start & 1) == 1)
                    closing += count;
                for (int step = adj[v] & free; step != 0; step &= step - 1) {
                    int u = Integer.numberOfTrailingZeros(step);
                    paths[(mask | 1 << u) * n + u] += count;
                }
            }
            if (Integer.bitCount(mask) >= SHORTEST)
                cycles[mask] = closing / 2;
        }

        // the bipartite graph of routes and stops needs as many rows as its
        // largest degree: the longest route or the busiest stop
        long best = 0;
        long[] through = new long[n];
        for (int mask = 1; mask <= full; mask++) {
            if (cycles[mask] == 0)
                continue;
            best = Math.max(best, Integer.bitCount(mask));
            for (int v = 0; v < n; v++)
                if ((mask >> v & 1) == 1)
                    through[v] += cycles[mask];
        }
        for (long t : through)
            best = Math.max(best, t);
        System.out.println(best);
    }
}
