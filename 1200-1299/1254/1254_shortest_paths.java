import java.io.*;
import java.util.*;

public class Main {
    static final double ROOT2 = Math.sqrt(2);
    static int w;
    static boolean[] free;
    static int[] steps;
    static double[] costs, dist;

    // the octile distance, which never exceeds the true length
    static double guess(int c, int to) {
        int dy = Math.abs(c / w - to / w), dx = Math.abs(c % w - to % w);
        return Math.max(dx, dy) + (ROOT2 - 1) * Math.min(dx, dy);
    }

    // shortest walk by A*; a heap entry holds the walked plus estimated
    // length, then the cell
    static double walk(int from, int to) {
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[from] = 0;
        PriorityQueue<double[]> q = new PriorityQueue<>((a, b) -> Double.compare(a[0], b[0]));
        q.add(new double[] {guess(from, to), from});
        while (true) {
            double[] it = q.poll();
            int c = (int)it[1];
            if (c == to)
                return dist[to];
            if (it[0] > dist[c] + guess(c, to))
                continue;
            for (int i = 0; i < steps.length; i++) {
                int b = c + steps[i];
                double d = dist[c] + costs[i];
                if (free[b] && d < dist[b]) {
                    dist[b] = d;
                    q.add(new double[] {d + guess(b, to), b});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        double v = Double.parseDouble(st.nextToken());
        // cells over a grid with a border of buildings, so no move needs a
        // bounds check
        w = n + 2;
        free = new boolean[(m + 2) * w];
        for (int r = 1; r <= m; r++) {
            String row = in.readLine().trim();
            for (int c = 1; c <= n && c <= row.length(); c++)
                free[r * w + c] = row.charAt(c - 1) == '.';
        }
        StringBuilder rest = new StringBuilder();
        for (String line; (line = in.readLine()) != null;)
            rest.append(line).append(' ');
        st = new StringTokenizer(rest.toString());
        int at = Integer.parseInt(st.nextToken());
        at += Integer.parseInt(st.nextToken()) * w;
        free[at] = true; // John stands there, whatever the map shows
        // a step along a side costs 1, along a diagonal sqrt 2, and a diagonal
        // may pass a building's corner
        steps = new int[] {1, -1, w, -w, w + 1, w - 1, -w + 1, -w - 1};
        costs = new double[] {1, 1, 1, 1, ROOT2, ROOT2, ROOT2, ROOT2};
        dist = new double[free.length];
        // parts of the town joined by moves, so an unreachable bomb costs nothing
        int[] part = new int[free.length], stack = new int[free.length];
        for (int c = 0; c < free.length; c++) {
            if (!free[c] || part[c] != 0)
                continue;
            part[c] = c + 1;
            int top = 0;
            stack[top++] = c;
            while (top > 0) {
                int a = stack[--top];
                for (int s : steps)
                    if (free[a + s] && part[a + s] == 0) {
                        part[a + s] = c + 1;
                        stack[top++] = a + s;
                    }
            }
        }
        Map<Long, Double> known = new HashMap<>();
        double total = 0;
        for (int i = 0; i < k; i++) {
            int target = Integer.parseInt(st.nextToken());
            target += Integer.parseInt(st.nextToken()) * w;
            // an unreachable bomb is skipped and John stays where he is
            if (part[target] != part[at])
                continue;
            long pair = (long)at * free.length + target;
            Double d = known.get(pair);
            if (d == null) {
                d = walk(at, target);
                known.put(pair, d);
                known.put((long)target * free.length + at, d);
            }
            total += d;
            at = target;
        }
        System.out.println(String.format(Locale.ROOT, "%.2f", total / v));
    }
}
