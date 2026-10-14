import java.io.*;
import java.util.*;

public class Main {
    static final long INF = 1L << 62;
    static final int MAX_PIPES = 100000, CHUNK = 1 << 16;

    static byte[] data;
    static int pos;

    static long number() {
        while (data[pos] < '0' || data[pos] > '9')
            pos++;
        long v = 0;
        while (pos < data.length && data[pos] >= '0' && data[pos] <= '9')
            v = v * 10 + (data[pos++] - '0');
        return v;
    }

    public static void main(String[] args) throws IOException {
        ByteArrayOutputStream buf = new ByteArrayOutputStream();
        byte[] chunk = new byte[CHUNK];
        for (int r; (r = System.in.read(chunk)) > 0;)
            buf.write(chunk, 0, r);
        data = buf.toByteArray();
        int n = (int)number();
        int[] origin = new int[MAX_PIPES], target = new int[MAX_PIPES];
        long[] cap = new long[MAX_PIPES], flow = new long[MAX_PIPES], cost = new long[MAX_PIPES];
        int m = 0;
        List<List<Integer>> out = new ArrayList<>(), into = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            out.add(new ArrayList<>());
            into.add(new ArrayList<>());
        }
        long[] balance = new long[n + 1]; // outflow minus inflow
        // each pipe ends with a comma or a dot, each station with a dot
        for (int i = 1; i <= n;) {
            byte c = data[pos];
            if (c >= '0' && c <= '9') {
                int a = (int)number();
                out.get(i).add(m);
                into.get(a).add(m);
                origin[m] = i;
                target[m] = a;
                cap[m] = number();
                flow[m] = number();
                cost[m] = number();
                balance[i] += flow[m];
                balance[a] -= flow[m++];
                continue;
            }
            if (c == '.')
                i++;
            pos++;
        }

        // one more unit from any station with a well to station n through
        // the residual network: a pipe with spare room is free, a full one
        // costs d, and pushing back existing flow is free
        long[] dist = new long[n + 1];
        int[] cameBy = new int[n + 1], step = new int[n + 1];
        Arrays.fill(dist, INF);
        Arrays.fill(cameBy, -1);
        PriorityQueue<long[]> heap = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));
        for (int i = 1; i < n; i++)
            if (balance[i] > 0) {
                dist[i] = 0;
                heap.add(new long[] {0, i});
            }
        while (!heap.isEmpty()) {
            long[] cur = heap.poll();
            long du = cur[0];
            int u = (int)cur[1];
            if (du > dist[u])
                continue;
            for (int e : out.get(u)) {
                long nd = du + (flow[e] == cap[e] ? cost[e] : 0);
                int v = target[e];
                if (nd < dist[v]) {
                    dist[v] = nd;
                    cameBy[v] = e;
                    step[v] = 1;
                    heap.add(new long[] {nd, v});
                }
            }
            for (int e : into.get(u)) {
                int v = origin[e];
                if (flow[e] > 0 && du < dist[v]) {
                    dist[v] = du;
                    cameBy[v] = e;
                    step[v] = -1;
                    heap.add(new long[] {du, v});
                }
            }
        }
        if (dist[n] == INF) {
            System.out.println("Impossible");
            return;
        }
        for (int v = n; cameBy[v] >= 0;) {
            int e = cameBy[v];
            flow[e] += step[v];
            v = step[v] == 1 ? origin[e] : target[e];
        }
        StringBuilder sb = new StringBuilder();
        sb.append(dist[n]).append('\n');
        for (int i = 1; i <= n; i++) {
            List<Integer> pipes = out.get(i);
            for (int k = 0; k < pipes.size(); k++) {
                int e = pipes.get(k);
                if (k > 0)
                    sb.append(", ");
                sb.append(target[e]).append(' ').append(flow[e]);
            }
            sb.append(".\n");
        }
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        pw.print(sb);
        pw.flush();
    }
}
