import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    static final int SHAVES = 2;
    static List<int[]> edges = new ArrayList<>();
    static List<List<Integer>> out = new ArrayList<>();
    static int[] level, at;

    static int add(int a, int b, int cap) {
        out.get(a).add(edges.size());
        edges.add(new int[] {b, cap});
        out.get(b).add(edges.size());
        edges.add(new int[] {a, 0});
        return edges.size() - 2;
    }

    static int push(int v, int sink, int limit) {
        if (v == sink) return limit;
        for (; at[v] < out.get(v).size(); at[v]++) {
            int e = out.get(v).get(at[v]);
            int[] edge = edges.get(e);
            if (edge[1] > 0 && level[edge[0]] == level[v] + 1) {
                int got = push(edge[0], sink, Math.min(limit, edge[1]));
                if (got > 0) {
                    edge[1] -= got;
                    edges.get(e ^ 1)[1] += got;
                    return got;
                }
            }
        }
        return 0;
    }

    static int maxFlow(int source, int sink) {
        int total = 0;
        while (true) {
            level = new int[out.size()];
            Arrays.fill(level, -1);
            level[source] = 0;
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            queue.add(source);
            while (!queue.isEmpty()) {
                int v = queue.poll();
                for (int e : out.get(v)) {
                    int[] edge = edges.get(e);
                    if (edge[1] > 0 && level[edge[0]] < 0) {
                        level[edge[0]] = level[v] + 1;
                        queue.add(edge[0]);
                    }
                }
            }
            if (level[sink] < 0) return total;
            at = new int[out.size()];
            for (int got = push(source, sink, SHAVES); got > 0; got = push(source, sink, SHAVES)) {
                total += got;
            }
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        int[] come = new int[n], stay = new int[n];
        TreeSet<Integer> cutSet = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            come[i] = in.nextInt();
            stay[i] = in.nextInt();
            cutSet.add(come[i]);
            cutSet.add(come[i] + stay[i]);
        }
        // minutes between consecutive arrivals and departures see the same mages,
        // so they form blocks: a block of L minutes shaves k L times, at most
        // min(L, 2) of them on one mage
        Integer[] cuts = cutSet.toArray(new Integer[0]);
        int blocks = cuts.length - 1, source = n + blocks, sink = source + 1;
        for (int v = 0; v <= sink; v++) out.add(new ArrayList<>());
        List<List<int[]>> links = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            links.add(new ArrayList<>());
            add(source, i, SHAVES);
            for (int j = 0; j < blocks; j++) {
                if (come[i] <= cuts[j] && cuts[j + 1] <= come[i] + stay[i]) {
                    int cap = Math.min(cuts[j + 1] - cuts[j], SHAVES);
                    links.get(i).add(new int[] {j, add(i, n + j, cap)});
                }
            }
        }
        for (int j = 0; j < blocks; j++) add(n + j, sink, k * (cuts[j + 1] - cuts[j]));
        if (maxFlow(source, sink) < SHAVES * n) {
            System.out.println("No");
            return;
        }
        // inside a block the shaves are dealt out round the minutes, so the two
        // shaves of one mage fall on different minutes and no minute gets more
        // than k of them
        int[] dealt = new int[blocks];
        StringBuilder sb = new StringBuilder("Yes\n");
        for (int i = 0; i < n; i++) {
            List<Integer> times = new ArrayList<>();
            for (int[] link : links.get(i)) {
                int j = link[0];
                for (int u = 0; u < edges.get(link[1] ^ 1)[1]; u++) {
                    times.add(cuts[j] + dealt[j]++ % (cuts[j + 1] - cuts[j]));
                }
            }
            times.sort(null);
            sb.append(times.get(0)).append(' ').append(times.get(1)).append('\n');
        }
        System.out.print(sb);
    }
}
