import java.io.*;
import java.util.*;

public class Main {
    static int[] head, to, cap, nxt, level, current;
    static int arcs, sink;

    static void arc(int a, int b, int c) {
        to[arcs] = b;
        cap[arcs] = c;
        nxt[arcs] = head[a];
        head[a] = arcs++;
        to[arcs] = a;
        cap[arcs] = 0;
        nxt[arcs] = head[b];
        head[b] = arcs++;
    }

    static int push(int u, int limit) {
        if (u == sink)
            return limit;
        for (; current[u] >= 0; current[u] = nxt[current[u]]) {
            int e = current[u], v = to[e];
            if (cap[e] > 0 && level[v] == level[u] + 1) {
                int got = push(v, Math.min(limit, cap[e]));
                if (got > 0) {
                    cap[e] -= got;
                    cap[e ^ 1] += got;
                    return got;
                }
            }
        }
        return 0;
    }

    static int next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int k = next(in), n = next(in), m = next(in), s = next(in), f = next(in);
        int[] cost = new int[n];
        for (int i = 0; i < n; i++)
            cost[i] = next(in);
        if (s == f) {
            System.out.println("NO");
            return;
        }
        // station v enters at 2v and leaves at 2v + 1; the arc between them
        // costs the police needed there. Museum and refuge cannot be taken,
        // and anything above K counts as too much
        int big = k + 1;
        head = new int[2 * n];
        Arrays.fill(head, -1);
        int size = 2 * (n + 2 * m);
        to = new int[size];
        cap = new int[size];
        nxt = new int[size];
        for (int v = 0; v < n; v++)
            arc(2 * v, 2 * v + 1, v + 1 == s || v + 1 == f ? big : Math.min(cost[v], big));
        for (int i = 0; i < m; i++) {
            int a = next(in) - 1, b = next(in) - 1;
            arc(2 * a + 1, 2 * b, big);
            arc(2 * b + 1, 2 * a, big);
        }
        int source = 2 * (s - 1) + 1;
        sink = 2 * (f - 1);
        // Dinic's blocking flows until the flow exceeds K or nothing gets through
        int flow = 0;
        while (flow <= k) {
            level = new int[2 * n];
            Arrays.fill(level, -1);
            level[source] = 0;
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            queue.add(source);
            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int e = head[u]; e >= 0; e = nxt[e])
                    if (cap[e] > 0 && level[to[e]] < 0) {
                        level[to[e]] = level[u] + 1;
                        queue.add(to[e]);
                    }
            }
            if (level[sink] < 0)
                break;
            current = head.clone();
            while (flow <= k) {
                int got = push(source, big);
                if (got == 0)
                    break;
                flow += got;
            }
        }
        System.out.println(flow <= k ? "YES" : "NO");
    }
}
