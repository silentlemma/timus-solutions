import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static int people;
    static int[] adj;
    static int[] callerOf; // callee of each caller already busy, or -1
    static int seen;

    static boolean place(int person, int informed) {
        for (int caller = 0; caller < people; caller++) {
            if ((adj[person] >> caller & 1) == 1 && (informed >> caller & 1) == 1 &&
                (seen >> caller & 1) == 0) {
                seen |= 1 << caller;
                if (callerOf[caller] < 0 || place(callerOf[caller], informed)) {
                    callerOf[caller] = person;
                    return true;
                }
            }
        }
        return false;
    }

    // who calls whom so that every person in fresh is called by a different
    // informed neighbour; null if that cannot be done
    static List<int[]> calls(int informed, int fresh) {
        callerOf = new int[people];
        Arrays.fill(callerOf, -1);
        for (int person = 0; person < people; person++) {
            seen = 0;
            if ((fresh >> person & 1) == 1 && !place(person, informed))
                return null;
        }
        List<int[]> plan = new ArrayList<>();
        for (int caller = 0; caller < people; caller++) {
            if (callerOf[caller] >= 0)
                plan.add(new int[] {caller, callerOf[caller]});
        }
        return plan;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine())
            all.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(all.toString());
        words.nextToken();
        int m = Integer.parseInt(words.nextToken());
        Map<String, Integer> index = new HashMap<>();
        List<String> names = new ArrayList<>();
        int[] ends = new int[2 * m + 1];
        for (int i = 0; i <= 2 * m; i++) {
            String name = words.nextToken();
            if (!index.containsKey(name)) {
                index.put(name, names.size());
                names.add(name);
            }
            ends[i] = index.get(name);
        }
        people = names.size();
        adj = new int[people];
        for (int i = 0; i < m; i++) {
            adj[ends[2 * i]] |= 1 << ends[2 * i + 1];
            adj[ends[2 * i + 1]] |= 1 << ends[2 * i];
        }
        int full = (1 << people) - 1, start = 1 << ends[2 * m];
        // breadth-first search over the sets of people who know the news
        int[] from = new int[full + 1];
        Arrays.fill(from, -1);
        List<List<int[]>> how = new ArrayList<>();
        for (int s = 0; s <= full; s++)
            how.add(null);
        int[] queue = new int[full + 1];
        int head = 0, tail = 0;
        queue[tail++] = start;
        from[start] = start;
        while (head < tail && from[full] < 0) {
            int informed = queue[head++], reach = 0;
            for (int p = 0; p < people; p++) {
                if ((informed >> p & 1) == 1)
                    reach |= adj[p];
            }
            reach &= ~informed;
            for (int fresh = reach; fresh > 0; fresh = (fresh - 1) & reach) {
                int next = informed | fresh;
                if (from[next] >= 0)
                    continue;
                List<int[]> plan = calls(informed, fresh);
                if (plan != null) {
                    from[next] = informed;
                    how.set(next, plan);
                    queue[tail++] = next;
                }
            }
        }
        List<Integer> path = new ArrayList<>();
        for (int state = full; state != start; state = from[state])
            path.add(state);
        StringBuilder out = new StringBuilder();
        out.append(path.size()).append('\n');
        for (int i = path.size() - 1; i >= 0; i--) {
            List<int[]> plan = how.get(path.get(i));
            out.append(plan.size()).append('\n');
            for (int[] c : plan)
                out.append(names.get(c[0])).append(' ').append(names.get(c[1])).append('\n');
        }
        System.out.print(out);
    }
}
