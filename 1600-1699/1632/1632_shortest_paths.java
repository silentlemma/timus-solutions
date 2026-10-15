import java.io.*;
import java.util.*;

public class Main {
    static final double LIMIT = 1e6;
    static final double TIGHT = 1e-7; // a smaller slack counts as an equality

    static class Laser {
        long x, y, u, v, w;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int)in.nval;
        Laser[] lasers = new Laser[n];
        for (int i = 0; i < n; i++) {
            Laser l = new Laser();
            in.nextToken();
            l.x = (long)in.nval;
            in.nextToken();
            l.y = (long)in.nval;
            in.nextToken();
            l.u = (long)in.nval;
            in.nextToken();
            l.v = (long)in.nval;
            in.nextToken();
            l.w = (long)in.nval;
            lasers[i] = l;
        }
        in.nextToken();
        int m = (int)in.nval;
        // z[hi] - z[lo] must exceed lift: the gap of the beams where they cross
        int[] los = new int[m], his = new int[m];
        double[] lifts = new double[m];
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < n; i++)
            out.add(new ArrayList<>());
        for (int k = 0; k < m; k++) {
            in.nextToken();
            int a = (int)in.nval - 1;
            in.nextToken();
            int b = (int)in.nval - 1;
            Laser la = lasers[a], lb = lasers[b];
            long det = la.u * lb.v - la.v * lb.u;
            long dx = lb.x - la.x, dy = lb.y - la.y;
            long top = lb.w * (la.v * dx - la.u * dy) - la.w * (dx * lb.v - dy * lb.u);
            los[k] = b;
            his[k] = a;
            lifts[k] = (double)top / det;
            out.get(b).add(k);
        }
        // longest paths from an imaginary source tied to every laser by 0.
        // Only lasers raised in the last round can raise others.
        double[] z = new double[n];
        int[] active = new int[n];
        for (int i = 0; i < n; i++)
            active[i] = i;
        int activeCount = n;
        boolean[] mark = new boolean[n];
        int[] raised = new int[n];
        for (int round = 0; round < n && activeCount > 0; round++) {
            int raisedCount = 0;
            for (int t = 0; t < activeCount; t++) {
                int lo = active[t];
                for (int k : out.get(lo)) {
                    int hi = his[k];
                    if (z[lo] + lifts[k] > z[hi]) {
                        z[hi] = z[lo] + lifts[k];
                        if (!mark[hi]) {
                            mark[hi] = true;
                            raised[raisedCount++] = hi;
                        }
                    }
                }
            }
            for (int t = 0; t < raisedCount; t++)
                mark[raised[t]] = false;
            int[] swap = active;
            active = raised;
            raised = swap;
            activeCount = raisedCount;
        }
        // equalities form an acyclic graph; a step per level of it makes them
        // strict, small enough to keep the other constraints and the bounds
        List<List<Integer>> tight = new ArrayList<>();
        for (int i = 0; i < n; i++)
            tight.add(new ArrayList<>());
        int[] indegree = new int[n], level = new int[n];
        double slackMin = -1;
        for (int k = 0; k < m; k++) {
            double slack = z[his[k]] - z[los[k]] - lifts[k];
            if (slack < TIGHT) {
                tight.get(los[k]).add(his[k]);
                indegree[his[k]]++;
            } else if (slackMin < 0 || slack < slackMin) {
                slackMin = slack;
            }
        }
        int[] queue = new int[n];
        int tail = 0;
        for (int i = 0; i < n; i++)
            if (indegree[i] == 0)
                queue[tail++] = i;
        for (int head = 0; head < tail; head++) {
            int at = queue[head];
            for (int to : tight.get(at)) {
                level[to] = Math.max(level[to], level[at] + 1);
                if (--indegree[to] == 0)
                    queue[tail++] = to;
            }
        }
        int levels = 0;
        for (int l : level)
            levels = Math.max(levels, l);
        double step = 0;
        if (levels > 0) {
            double room = 2 * LIMIT - (max(z) - min(z));
            if (slackMin >= 0)
                room = Math.min(room, slackMin);
            step = room / (2 * levels + 2);
        }
        for (int i = 0; i < n; i++)
            z[i] += step * level[i];
        double middle = (max(z) + min(z)) / 2;
        StringBuilder sb = new StringBuilder();
        for (double h : z)
            sb.append(String.format(Locale.US, "%.10f", h - middle)).append('\n');
        System.out.print(sb);
    }

    static double max(double[] z) {
        double best = z[0];
        for (double h : z)
            best = Math.max(best, h);
        return best;
    }

    static double min(double[] z) {
        double best = z[0];
        for (double h : z)
            best = Math.min(best, h);
        return best;
    }
}
