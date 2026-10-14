import java.io.*;
import java.util.*;

public class Main {
    static final int NONE = -1;
    static int n, s, f, budget, limit;
    static int[] ru, rv, rToll, rTime, rHeight;
    static List<List<Integer>> out = new ArrayList<>();
    static StreamTokenizer in;

    static int next() throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    // a route from s to f within the limits using roads no higher than height,
    // as road numbers, or null
    static List<Integer> route(int height) {
        // best[v][c]: the least time to v with c tolls paid
        int[][] best = new int[n + 1][budget + 1], cameBy = new int[n + 1][budget + 1];
        for (int v = 0; v <= n; v++) {
            Arrays.fill(best[v], NONE);
            Arrays.fill(cameBy[v], NONE);
        }
        best[s][0] = 0;
        PriorityQueue<int[]> heap =
            new PriorityQueue<>((x, y) -> x[0] != y[0] ? x[0] - y[0] :
                x[1] != y[1] ? x[1] - y[1] : x[2] - y[2]);
        heap.add(new int[] {0, 0, s});
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int time = cur[0], paid = cur[1], v = cur[2];
            if (best[v][paid] != time)
                continue;
            // a state is useless if fewer tolls already reach v as fast
            boolean beaten = false;
            for (int c = 0; c < paid && !beaten; c++)
                beaten = best[v][c] != NONE && best[v][c] <= time;
            if (beaten)
                continue;
            if (v == f) {
                List<Integer> path = new ArrayList<>();
                while (cameBy[v][paid] != NONE) {
                    int idx = cameBy[v][paid];
                    path.add(idx + 1);
                    paid -= rToll[idx];
                    v = ru[idx];
                }
                Collections.reverse(path);
                return path;
            }
            for (int idx : out.get(v)) {
                int nt = time + rTime[idx], np = paid + rToll[idx], w = rv[idx];
                if (rHeight[idx] <= height && np <= budget && nt <= limit &&
                    (best[w][np] == NONE || nt < best[w][np])) {
                    best[w][np] = nt;
                    cameBy[w][np] = idx;
                    heap.add(new int[] {nt, np, w});
                }
            }
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        n = next();
        int m = next();
        s = next();
        f = next();
        budget = next();
        limit = next();
        ru = new int[m];
        rv = new int[m];
        rToll = new int[m];
        rTime = new int[m];
        rHeight = new int[m];
        for (int v = 0; v <= n; v++)
            out.add(new ArrayList<>());
        int[] heights = new int[m];
        for (int i = 0; i < m; i++) {
            int[][] fields = {ru, rv, rToll, rTime, rHeight};
            for (int[] field : fields)
                field[i] = next();
            out.get(ru[i]).add(i);
            heights[i] = rHeight[i];
        }
        if (s == f) {
            System.out.print("0\n0\n\n");
            return;
        }
        // shorter parallel roads first, to avoid obsolete heap entries
        for (List<Integer> edges : out)
            edges.sort((a, b) -> rTime[a] - rTime[b]);
        // a cheapest route repeats no city, so it pays at most n - 1 tolls
        budget = Math.min(budget, n - 1);
        Arrays.sort(heights);
        if (route(heights[m - 1]) == null) {
            System.out.println(-1);
            return;
        }
        int lo = 0, hi = m - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (route(heights[mid]) != null)
                hi = mid;
            else
                lo = mid + 1;
        }
        List<Integer> path = route(heights[lo]);
        StringBuilder sb = new StringBuilder();
        sb.append(heights[lo]).append('\n').append(path.size()).append('\n');
        for (int i = 0; i < path.size(); i++)
            sb.append(i > 0 ? " " : "").append(path.get(i));
        System.out.println(sb);
    }
}
