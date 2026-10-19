import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final String[] KEYS = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    static final int SLOWEST = 4;

    // a growable list of ints
    static int[] push(int[] list, int size, int value) {
        if (size == list.length) {
            list = Arrays.copyOf(list, Math.max(1, size * 2));
        }
        list[size] = value;
        return list;
    }

    public static void main(String[] args) throws IOException {
        int[] presses = new int['z' + 1];
        for (String key : KEYS) {
            for (int k = 0; k < key.length(); k++) {
                presses[key.charAt(k)] = k + 1;
            }
        }
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = in.readLine().trim();
        }
        // state offset[x] + d: name x is current and its first d letters are
        // typed; nodeOf[state] is the trie node of the typed letters
        int[] offset = new int[n + 1];
        for (int x = 0; x < n; x++) {
            offset[x + 1] = offset[x] + words[x].length() + 1;
        }
        int states = offset[n];
        int[] nodeOf = new int[states];
        int[] owner = new int[states];
        // the names below a node form a range low..high
        int[] low = new int[states + 1];
        int[] high = new int[states + 1];
        List<List<int[]>> children = new ArrayList<>();
        children.add(new ArrayList<>());
        int nodes = 1;
        high[0] = n - 1;
        int[] path = new int[states + 1];
        int depth = 0;
        for (int x = 0; x < n; x++) {
            String w = words[x];
            int same = 0;
            if (x > 0) {
                String p = words[x - 1];
                while (same < w.length() && same < p.length() && w.charAt(same) == p.charAt(same)) {
                    same++;
                }
            }
            depth = same;
            for (int d = same + 1; d <= w.length(); d++) {
                int v = nodes++;
                low[v] = x;
                high[v] = x;
                children.add(new ArrayList<>());
                children.get(path[depth]).add(new int[] {offset[x] + d, presses[w.charAt(d - 1)]});
                path[++depth] = v;
            }
            for (int d = 0; d <= w.length(); d++) {
                nodeOf[offset[x] + d] = path[d];
                owner[offset[x] + d] = x;
                high[path[d]] = x;
            }
        }
        int[] dist = new int[states + nodes];
        Arrays.fill(dist, Integer.MAX_VALUE);
        // every move costs at most SLOWEST, so SLOWEST + 1 buckets in a circle
        int[][] buckets = new int[SLOWEST + 1][1];
        int[] sizes = new int[SLOWEST + 1];
        dist[0] = 0;
        buckets[0][0] = 0;
        sizes[0] = 1;
        long pending = 1;
        int[] to = new int[SLOWEST];
        int[] cost = new int[SLOWEST];
        for (int now = 0; pending > 0; now++) {
            int b = now % (SLOWEST + 1);
            while (sizes[b] > 0) {
                int s = buckets[b][--sizes[b]];
                pending--;
                if (dist[s] != now) {
                    continue;
                }
                int count = 0;
                if (s >= states) {
                    for (int[] child : children.get(s - states)) {
                        int t = child[0];
                        if (now + child[1] < dist[t]) {
                            dist[t] = now + child[1];
                            int c = dist[t] % (SLOWEST + 1);
                            buckets[c] = push(buckets[c], sizes[c]++, t);
                            pending++;
                        }
                    }
                    continue;
                }
                int x = owner[s];
                int d = s - offset[x];
                int v = nodeOf[s];
                to[count] = offset[x < high[v] ? x + 1 : low[v]] + d;
                cost[count++] = 1;
                to[count] = offset[x > low[v] ? x - 1 : high[v]] + d;
                cost[count++] = 1;
                to[count] = states + v;
                cost[count++] = 0;
                if (d > 0) {
                    to[count] = s - 1;
                    cost[count++] = 1;
                }
                for (int k = 0; k < count; k++) {
                    if (now + cost[k] < dist[to[k]]) {
                        dist[to[k]] = now + cost[k];
                        int c = dist[to[k]] % (SLOWEST + 1);
                        buckets[c] = push(buckets[c], sizes[c]++, to[k]);
                        pending++;
                    }
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int x = 0; x < n; x++) {
            int best = Integer.MAX_VALUE;
            for (int s = offset[x]; s < offset[x + 1]; s++) {
                best = Math.min(best, dist[s]);
            }
            out.append(best).append(x + 1 < n ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
