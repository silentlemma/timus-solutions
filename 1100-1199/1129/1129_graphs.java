import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    // slots of a door record: room and position of each of its two ends
    static final int ROOM_A = 0, POS_A = 1, ROOM_B = 2, POS_B = 3;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[][] rows = new int[n][];
        for (int u = 0; u < n; u++) {
            in.nextToken();
            rows[u] = new int[(int)in.nval];
            for (int i = 0; i < rows[u].length; i++) {
                in.nextToken();
                rows[u][i] = (int)in.nval - 1;
            }
        }
        // pair the k-th mention of v in room u with the k-th mention of u in room
        // v; a door to the room itself is mentioned twice in its own row
        List<int[]> ends = new ArrayList<>();
        Map<Long, ArrayDeque<Integer>> waiting = new HashMap<>();
        for (int u = 0; u < n; u++) {
            for (int i = 0; i < rows[u].length; i++) {
                int v = rows[u][i];
                long key = (long)Math.min(u, v) * (n + 1) + Math.max(u, v);
                ArrayDeque<Integer> queue = waiting.computeIfAbsent(key, k -> new ArrayDeque<>());
                if (!queue.isEmpty()) {
                    int[] e = ends.get(queue.poll());
                    e[ROOM_B] = u;
                    e[POS_B] = i;
                } else {
                    queue.add(ends.size());
                    ends.add(new int[] {u, i, -1, -1});
                }
            }
        }
        // a dummy room joined to every room of odd degree makes all degrees even
        int dummy = n, edges = ends.size();
        List<List<int[]>> adj = new ArrayList<>();
        for (int u = 0; u <= n; u++) {
            adj.add(new ArrayList<>());
        }
        for (int e = 0; e < edges; e++) {
            int u = ends.get(e)[ROOM_A], v = ends.get(e)[ROOM_B];
            adj.get(u).add(new int[] {v, e});
            adj.get(v).add(new int[] {u, e});
        }
        for (int u = 0; u < n; u++) {
            if (adj.get(u).size() % 2 == 1) {
                adj.get(u).add(new int[] {dummy, edges});
                adj.get(dummy).add(new int[] {u, edges});
                edges++;
            }
        }
        // walk Euler circuits and orient each door along the walk
        boolean[] used = new boolean[edges];
        int[] tail = new int[edges], ptr = new int[n + 1];
        for (int start = 0; start <= n; start++) {
            ArrayDeque<Integer> stack = new ArrayDeque<>();
            stack.push(start);
            while (!stack.isEmpty()) {
                int u = stack.peek();
                List<int[]> list = adj.get(u);
                while (ptr[u] < list.size() && used[list.get(ptr[u])[1]]) {
                    ptr[u]++;
                }
                if (ptr[u] == list.size()) {
                    stack.pop();
                    continue;
                }
                int[] next = list.get(ptr[u]);
                used[next[1]] = true;
                tail[next[1]] = u;
                stack.push(next[0]);
            }
        }
        char[][] colours = new char[n][];
        for (int u = 0; u < n; u++) {
            colours[u] = new char[rows[u].length];
        }
        for (int e = 0; e < ends.size(); e++) {
            int[] d = ends.get(e);
            // green on the side the walk leaves from, orange where it enters
            boolean outFirst = tail[e] == d[ROOM_A];
            colours[d[ROOM_A]][d[POS_A]] = outFirst ? 'G' : 'Y';
            colours[d[ROOM_B]][d[POS_B]] = outFirst ? 'Y' : 'G';
        }
        StringBuilder out = new StringBuilder();
        for (int u = 0; u < n; u++) {
            for (int i = 0; i < colours[u].length; i++) {
                out.append(i > 0 ? " " : "").append(colours[u][i]);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
