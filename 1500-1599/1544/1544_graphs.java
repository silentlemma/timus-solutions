import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer st =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();
        int n = (int)st.nval;
        st.nextToken();
        int m = (int)st.nval;
        String[] protocol = new String[n];
        for (int i = 0; i < n; i++) {
            st.nextToken();
            protocol[i] = st.sval;
        }
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            st.nextToken();
            int a = (int)st.nval - 1;
            st.nextToken();
            int b = (int)st.nval - 1;
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        // glue neighbours with the same protocol into regions
        int[] region = new int[n];
        Arrays.fill(region, -1);
        int regions = 0;
        for (int s = 0; s < n; s++) {
            if (region[s] >= 0)
                continue;
            region[s] = regions;
            Deque<Integer> stack = new ArrayDeque<>(Collections.singleton(s));
            while (!stack.isEmpty()) {
                int v = stack.pop();
                for (int u : adj.get(v))
                    if (region[u] < 0 && protocol[u].equals(protocol[v])) {
                        region[u] = regions;
                        stack.push(u);
                    }
            }
            regions++;
        }
        List<Set<Integer>> near = new ArrayList<>();
        for (int r = 0; r < regions; r++)
            near.add(new HashSet<>());
        for (int v = 0; v < n; v++)
            for (int u : adj.get(v))
                if (region[u] != region[v])
                    near.get(region[v]).add(region[u]);
        // switching a region merges it with all its neighbours, so switching the
        // same region again and again takes its eccentricity in steps, and no
        // plan does better than the radius of the region graph
        int best = regions, centre = 0;
        for (int start = 0; start < regions; start++) {
            int[] dist = new int[regions];
            Arrays.fill(dist, -1);
            dist[start] = 0;
            ArrayDeque<Integer> queue = new ArrayDeque<>(Collections.singleton(start));
            int far = 0;
            while (!queue.isEmpty()) {
                int r = queue.poll();
                far = Math.max(far, dist[r]);
                for (int x : near.get(r))
                    if (dist[x] < 0) {
                        dist[x] = dist[r] + 1;
                        queue.add(x);
                    }
            }
            if (far < best) {
                best = far;
                centre = start;
            }
        }
        int computer = 0;
        while (region[computer] != centre)
            computer++;
        String current = protocol[computer];
        StringBuilder out = new StringBuilder().append(best).append('\n');
        for (int i = 0; i < best; i++) {
            current = current.equals("J") ? "E" : "J";
            out.append(computer + 1).append(' ').append(current).append('\n');
        }
        System.out.print(out);
    }
}
