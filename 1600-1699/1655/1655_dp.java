import java.io.*;
import java.util.*;

public class Main {
    static final double FULL = 360, MINUTES = 60, EPS = 1e-9;
    static final double INF = Double.POSITIVE_INFINITY;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        double a = in.nval;
        in.nextToken();
        double w = in.nval;
        in.nextToken();
        int n = (int)in.nval;
        List<Integer> first = new ArrayList<>(); // ships right in front of the gun
        List<double[]> ships = new ArrayList<>(); // angle, deadline, number
        for (int k = 1; k <= n; k++) {
            in.nextToken();
            double b = in.nval;
            in.nextToken();
            double d = in.nval;
            in.nextToken();
            double v = in.nval;
            double deadline = (d - 1) / v * MINUTES; // when the ship reaches one mile
            double turn = ((b - a) % FULL + FULL) % FULL;
            if (turn <= EPS || FULL - turn <= EPS)
                first.add(k);
            else
                ships.add(new double[] {turn, deadline, k});
        }
        ships.sort(Comparator.comparingDouble(s -> s[0]));
        int m = ships.size(), size = m + 1;
        double degPerMin = FULL * w;
        // the shot ships form an arc around the start: i taken turning left
        // (from the end of the sorted list), j turning right; left and right
        // keep the earliest time with the gun at that end of the arc
        double[] left = new double[size * size], right = new double[size * size];
        int[] cameLeft = new int[size * size], cameRight = new int[size * size];
        Arrays.fill(left, INF);
        Arrays.fill(right, INF);
        left[0] = right[0] = 0;
        for (int i = 0; i < size; i++)
            for (int j = 0; i + j < m; j++) {
                int here = i * size + j;
                double tl = left[here], tr = right[here];
                if (tl == INF && tr == INF)
                    continue;
                double atLeft = i > 0 ? FULL - ships.get(m - i)[0] : 0;
                double atRight = j > 0 ? ships.get(j - 1)[0] : 0;
                double next = ships.get(j)[0]; // the next ship turning right
                double due = ships.get(j)[1];
                int there = here + 1;
                double[][] moves = {
                    {tr + (next - atRight) / degPerMin, 1},
                    {tl + (atLeft + next) / degPerMin, 0}};
                for (double[] mv : moves)
                    if (mv[0] <= due + EPS && mv[0] + EPS < right[there]) {
                        right[there] = mv[0];
                        cameRight[there] = (int)mv[1];
                    }
                next = FULL - ships.get(m - i - 1)[0]; // the next ship turning left
                due = ships.get(m - i - 1)[1];
                there = here + size;
                double[][] back = {
                    {tl + (next - atLeft) / degPerMin, 0},
                    {tr + (atRight + next) / degPerMin, 1}};
                for (double[] mv : back)
                    if (mv[0] <= due + EPS && mv[0] + EPS < left[there]) {
                        left[there] = mv[0];
                        cameLeft[there] = (int)mv[1];
                    }
            }
        // ending at the left end wins ties, then the fewest ships taken leftwards
        double best = INF;
        int side = 0;
        double[][] ends = {left, right};
        for (int s = 0; s < 2; s++)
            for (int i = 0; i < size; i++)
                if (ends[s][i * size + m - i] < best) {
                    best = ends[s][i * size + m - i];
                    side = s;
                }
        if (best == INF) {
            System.out.println("Impossible");
            return;
        }
        int i = 0;
        while (Math.abs(ends[side][i * size + m - i] - best) > EPS)
            i++;
        int j = m - i;
        List<Integer> order = new ArrayList<>();
        while (i > 0 || j > 0) {
            int here = i * size + j;
            if (side == 1) {
                order.add((int)ships.get(j - 1)[2]);
                side = cameRight[here];
                j--;
            } else {
                order.add((int)ships.get(m - i)[2]);
                side = cameLeft[here];
                i--;
            }
        }
        Collections.reverse(order);
        StringBuilder sb = new StringBuilder(String.format(Locale.US, "%.3f", best));
        sb.append('\n');
        for (int k : first)
            sb.append(k).append('\n');
        for (int k : order)
            sb.append(k).append('\n');
        System.out.print(sb);
    }
}
