import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1 << 30;
    static final int WORD = 64; // documents per word of a set

    static StreamTokenizer in;
    static int m, week, bestDay;
    static int[] off, tail, topo, waiting;
    static int[][] pre, succ;
    static boolean[] done;
    static List<Integer> bestPlan = new ArrayList<>(), path = new ArrayList<>();
    static HashMap<List<Long>, Integer> seen = new HashMap<>();

    static int next() throws IOException {
        in.nextToken();
        return (int)in.nval;
    }

    static List<Integer> listed() throws IOException {
        List<Integer> items = new ArrayList<>();
        for (int v = next(); v != 0; v = next())
            items.add(v);
        return items;
    }

    // the first day from t on when the official of v receives
    static int firstDay(int t, int v) { return t + Math.floorMod(off[v] - t, week); }

    // no plan from day t on can fetch the last document earlier
    static int lowerBound(int t) {
        int[] earliest = new int[m];
        List<List<int[]>> bySlot = new ArrayList<>();
        for (int i = 0; i < week; i++)
            bySlot.add(new ArrayList<>());
        for (int v : topo) {
            if (done[v])
                continue;
            int base = t;
            for (int p : pre[v])
                if (!done[p])
                    base = Math.max(base, earliest[p] + 1);
            earliest[v] = firstDay(base, v);
            bySlot.get(off[v]).add(new int[] {earliest[v], tail[v]});
        }
        // k documents of one reception day that cannot come before day r
        // take k such days from r on, and the last still has a tail ahead
        int bound = 0;
        for (List<int[]> here : bySlot) {
            here.sort((a, b) -> a[0] != b[0] ? b[0] - a[0] : b[1] - a[1]);
            int count = 0, shortest = INF;
            for (int[] d : here) {
                count++;
                shortest = Math.min(shortest, d[1]);
                bound = Math.max(bound, d[0] + (count - 1) * week + shortest);
            }
        }
        return bound;
    }

    // the first day with a document to fetch; the documents go to cands
    static int choices(int t, int[] wait, boolean[] taken, List<Integer> cands) {
        int day = INF;
        cands.clear();
        for (int v = 0; v < m; v++) {
            if (taken[v] || wait[v] != 0)
                continue;
            int d = firstDay(t, v);
            if (d < day) {
                day = d;
                cands.clear();
            }
            if (d == day)
                cands.add(v);
        }
        cands.sort((a, b) -> tail[a] != tail[b] ? tail[b] - tail[a] : a - b);
        return day;
    }

    // fetch the document with the longest chain behind it each time
    static int greedy(int t, int count, List<Integer> plan) {
        int[] wait = waiting.clone();
        boolean[] taken = done.clone();
        int last = t - 1;
        List<Integer> cands = new ArrayList<>();
        plan.clear();
        for (int i = 0; i < count; i++) {
            last = choices(t, wait, taken, cands);
            int v = cands.get(0);
            taken[v] = true;
            plan.add(v);
            for (int u : succ[v])
                wait[u]--;
            t = last + 1;
        }
        return last;
    }

    static void search(int t, long lo, long hi, int count) {
        if (count == 0) {
            if (t - 1 < bestDay) {
                bestDay = t - 1;
                bestPlan = new ArrayList<>(path);
            }
            return;
        }
        // the same documents in hand by an earlier day were already tried
        List<Long> mask = Arrays.asList(lo, hi);
        Integer old = seen.get(mask);
        if (old != null && old <= t)
            return;
        seen.put(mask, t);
        if (lowerBound(t) >= bestDay)
            return;
        // fetching nothing on a day when something can be fetched never helps
        List<Integer> cands = new ArrayList<>(), rest = new ArrayList<>();
        int day = choices(t, waiting, done, cands);
        for (int v : cands) {
            done[v] = true;
            for (int u : succ[v])
                waiting[u]--;
            path.add(v);
            int last = greedy(day + 1, count - 1, rest);
            if (last < bestDay) {
                bestDay = last;
                bestPlan = new ArrayList<>(path);
                bestPlan.addAll(rest);
            }
            if (day < bestDay) {
                if (v < WORD)
                    search(day + 1, lo | 1L << v, hi, count - 1);
                else
                    search(day + 1, lo, hi | 1L << (v - WORD), count - 1);
            }
            path.remove(path.size() - 1);
            for (int u : succ[v])
                waiting[u]++;
            done[v] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        int n = next();
        week = next();
        int[] dayOf = new int[n + 1];
        for (int i = 1; i <= n; i++)
            dayOf[i] = next();
        List<List<Integer>> needs = new ArrayList<>();
        needs.add(new ArrayList<>());
        for (int i = 1; i <= n; i++)
            needs.add(listed());
        int today = next();
        boolean[] held = new boolean[n + 1], todo = new boolean[n + 1];
        for (int d : listed())
            held[d] = true;
        // every document still to get: the wanted ones and, behind them, the
        // papers they need, stopping at papers already held
        Deque<Integer> stack = new ArrayDeque<>();
        for (int d : listed())
            if (!held[d])
                stack.push(d);
        while (!stack.isEmpty()) {
            int doc = stack.pop();
            if (todo[doc])
                continue;
            todo[doc] = true;
            for (int p : needs.get(doc))
                if (!held[p])
                    stack.push(p);
        }
        List<Integer> docs = new ArrayList<>();
        int[] index = new int[n + 1];
        for (int d = 1; d <= n; d++)
            if (todo[d]) {
                index[d] = docs.size();
                docs.add(d);
            }
        m = docs.size();
        List<List<Integer>> preList = new ArrayList<>(), succList = new ArrayList<>();
        for (int v = 0; v < m; v++) {
            preList.add(new ArrayList<>());
            succList.add(new ArrayList<>());
        }
        off = new int[m];
        for (int v = 0; v < m; v++) {
            for (int p : needs.get(docs.get(v)))
                if (todo[p]) {
                    preList.get(v).add(index[p]);
                    succList.get(index[p]).add(v);
                }
            // day t (today is day 0) belongs to an official when t = off mod week
            off[v] = Math.floorMod(dayOf[docs.get(v)] - today, week);
        }
        pre = new int[m][];
        succ = new int[m][];
        for (int v = 0; v < m; v++) {
            pre[v] = preList.get(v).stream().mapToInt(Integer::intValue).toArray();
            succ[v] = succList.get(v).stream().mapToInt(Integer::intValue).toArray();
        }
        // a cycle among them makes the set impossible to get
        waiting = new int[m];
        for (int v = 0; v < m; v++)
            waiting[v] = pre[v].length;
        int[] left = waiting.clone();
        topo = new int[m];
        int size = 0;
        for (int v = 0; v < m; v++)
            if (left[v] == 0)
                topo[size++] = v;
        for (int i = 0; i < size; i++)
            for (int u : succ[topo[i]])
                if (--left[u] == 0)
                    topo[size++] = u;
        if (size < m) {
            System.out.println("No Solution");
            return;
        }
        // tail[v]: days that must pass after v is fetched, along its longest chain
        tail = new int[m];
        for (int i = m - 1; i >= 0; i--) {
            int v = topo[i];
            for (int u : succ[v]) {
                int gap = Math.floorMod(off[u] - off[v], week);
                if (gap == 0)
                    gap = week;
                tail[v] = Math.max(tail[v], gap + tail[u]);
            }
        }
        done = new boolean[m];
        if (m == 0) {
            System.out.print("0\n\n");
            return;
        }
        bestDay = greedy(0, m, bestPlan);
        search(0, 0, 0, m);
        StringBuilder out = new StringBuilder();
        out.append(bestDay).append('\n');
        for (int i = 0; i < bestPlan.size(); i++)
            out.append(i > 0 ? " " : "").append(docs.get(bestPlan.get(i)));
        System.out.println(out);
    }
}
