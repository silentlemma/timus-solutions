import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int[] eu = new int[m], ev = new int[m];
        long[] ea = new long[m];
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            in.nextToken();
            eu[i] = (int)in.nval - 1;
            in.nextToken();
            ev[i] = (int)in.nval - 1;
            in.nextToken();
            ea[i] = (long)in.nval;
            adj.get(eu[i]).add(new int[] {ev[i], i});
            adj.get(ev[i]).add(new int[] {eu[i], i});
        }
        // in halves of a rouble, each debt in a component is sign * t + base for
        // the debt t of its first student; an edge closing an odd cycle fixes t
        long[] sign = new long[n], base = new long[n], twice = new long[n];
        for (int start = 0; start < n; start++) {
            if (sign[start] != 0)
                continue;
            sign[start] = 1;
            List<Integer> comp = new ArrayList<>();
            comp.add(start);
            boolean fixed = false;
            long t = 0;
            for (int head = 0; head < comp.size(); head++) {
                int v = comp.get(head);
                for (int[] e : adj.get(v)) {
                    int u = e[0];
                    long a = ea[e[1]];
                    if (sign[u] == 0) {
                        sign[u] = -sign[v];
                        base[u] = 2 * a - base[v];
                        comp.add(u);
                    } else if (sign[u] == sign[v] && !fixed) {
                        fixed = true;
                        t = (2 * a - base[u] - base[v]) / (2 * sign[v]);
                    }
                }
            }
            if (!fixed) {
                // no odd cycle: one debt can move freely against its neighbours
                System.out.println("IMPOSSIBLE");
                return;
            }
            for (int v : comp)
                twice[v] = sign[v] * t + base[v];
        }
        // the claims may also contradict each other
        for (int i = 0; i < m; i++)
            if (twice[eu[i]] + twice[ev[i]] != 2 * ea[i]) {
                System.out.println("IMPOSSIBLE");
                return;
            }
        StringBuilder out = new StringBuilder();
        for (long t : twice)
            out.append(t < 0 ? "-" : "")
                .append(Math.abs(t) / 2)
                .append(Math.abs(t) % 2 != 0 ? ".50" : ".00")
                .append('\n');
        System.out.print(out);
    }
}
