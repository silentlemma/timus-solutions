import java.io.*;
import java.util.*;

public class Main {
    static final int WRAP = 4; // a fifth bacterium leaves one: counts go 1, 2, 3, 4, 1, ...
    static final int BAD = 0, FIRST = 1, LAST = 2, EITHER = 3, WAIT = 4;
    static int n, m;
    // need[v]: how many free neighbours v must see settled after it, modulo
    // 4, stored as 1..4 like the picture; deg[v]: free neighbours
    static int[] need, deg;
    static boolean[] alive;
    static int[][] adj;

    static int kind(int v) {
        int d = deg[v], k = need[v];
        if (k != 1 && k - 1 > d)
            return BAD;
        if (d < WRAP && k == d + 1)
            return FIRST; // before all free neighbours
        if (d < WRAP && k == 1)
            return LAST; // after all of them
        if (d == WRAP && k == 1)
            return EITHER; // an inner cell showing 1: before all or after all
        return WAIT;
    }

    // settle v before (first) or after all its free neighbours
    static void take(int v, boolean first) {
        alive[v] = false;
        for (int u : adj[v])
            if (alive[u]) {
                deg[u]--;
                if (!first && --need[u] == 0) // u now sees v settle after it
                    need[u] = WRAP;
            }
    }

    // necessary: the later-neighbour counts must add up to the edges, and
    // touching undecided cells must split into firsts and lasts
    static boolean countsFit(List<Integer> cells) {
        int edges = 0, fixed = 0;
        boolean[] open = new boolean[n * m], seen = new boolean[n * m];
        List<Integer> openCells = new ArrayList<>();
        for (int v : cells) {
            edges += deg[v];
            if (kind(v) == EITHER) {
                open[v] = true;
                openCells.add(v);
            } else {
                fixed += need[v] - 1;
            }
        }
        int rest = edges / 2 - fixed;
        if (rest < 0 || rest % WRAP != 0 || rest / WRAP > openCells.size())
            return false;
        boolean[] reach = new boolean[openCells.size() + 1]; // s firsts possible so far
        reach[0] = true;
        for (int s : openCells) {
            if (seen[s])
                continue;
            seen[s] = true;
            List<Integer> group = new ArrayList<>();
            group.add(s);
            int[] colour = new int[2];
            for (int i = 0; i < group.size(); i++) {
                int v = group.get(i);
                colour[(v / m + v % m) % 2]++;
                for (int u : adj[v])
                    if (alive[u] && open[u] && !seen[u]) {
                        seen[u] = true;
                        group.add(u);
                    }
            }
            boolean[] next = new boolean[reach.length];
            for (int t = 0; t < reach.length; t++)
                if (reach[t])
                    for (int c : colour)
                        if (t + c < next.length)
                            next[t + c] = true;
            reach = next;
        }
        return reach[rest / WRAP];
    }

    static List<List<Integer>> components(List<Integer> cells) {
        boolean[] inside = new boolean[n * m], seen = new boolean[n * m];
        for (int v : cells)
            inside[v] = true;
        List<List<Integer>> parts = new ArrayList<>();
        for (int s : cells) {
            if (seen[s])
                continue;
            seen[s] = true;
            List<Integer> part = new ArrayList<>();
            part.add(s);
            for (int i = 0; i < part.size(); i++)
                for (int u : adj[part.get(i)])
                    if (inside[u] && alive[u] && !seen[u]) {
                        seen[u] = true;
                        part.add(u);
                    }
            parts.add(part);
        }
        return parts;
    }

    // an order of the free cells, or null if there is none
    static List<Integer> solve(List<Integer> cells) {
        List<Integer> head = new ArrayList<>(), tail = new ArrayList<>();
        while (true) {
            Deque<Integer> queue = new ArrayDeque<>();
            for (int v : cells)
                if (kind(v) != EITHER && kind(v) != WAIT)
                    queue.push(v);
            boolean moved = false;
            while (!queue.isEmpty()) {
                int v = queue.pop();
                if (!alive[v])
                    continue;
                int k = kind(v);
                if (k == BAD)
                    return null;
                if (k != FIRST && k != LAST)
                    continue;
                take(v, k == FIRST);
                (k == FIRST ? head : tail).add(v);
                moved = true;
                for (int u : adj[v])
                    if (alive[u])
                        queue.push(u);
            }
            List<Integer> left = new ArrayList<>();
            for (int v : cells)
                if (alive[v])
                    left.add(v);
            cells = left;
            if (!moved || cells.isEmpty())
                break;
        }
        List<Integer> middle = new ArrayList<>();
        if (!cells.isEmpty()) {
            List<List<Integer>> parts = components(cells);
            if (parts.size() > 1) {
                for (List<Integer> part : parts) {
                    List<Integer> order = solve(part);
                    if (order == null)
                        return null;
                    middle.addAll(order);
                }
            } else {
                // the first cell of any order comes before all its
                // neighbours, so with no forced cell left it must be undecided
                int pick = -1;
                for (int v : cells)
                    if (kind(v) == EITHER) {
                        pick = v;
                        break;
                    }
                if (pick < 0 || !countsFit(cells))
                    return null;
                // an undecided cell comes before or after all neighbours in any
                // order, so trying both ways for one of them misses nothing
                List<Integer> rest = new ArrayList<>(cells);
                rest.remove(Integer.valueOf(pick));
                List<Integer> found = null;
                for (boolean first : new boolean[] {true, false}) {
                    int[] savedNeed = need.clone(), savedDeg = deg.clone();
                    boolean[] savedAlive = alive.clone();
                    take(pick, first);
                    List<Integer> order = solve(rest);
                    need = savedNeed;
                    deg = savedDeg;
                    alive = savedAlive;
                    if (order != null) {
                        if (first)
                            order.add(0, pick);
                        else
                            order.add(pick);
                        found = order;
                        break;
                    }
                }
                if (found == null)
                    return null;
                middle = found;
            }
        }
        List<Integer> result = new ArrayList<>(head);
        result.addAll(middle);
        Collections.reverse(tail);
        result.addAll(tail);
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        n = (int)in.nval;
        in.nextToken();
        m = (int)in.nval;
        need = new int[n * m];
        for (int v = 0; v < n * m; v++) {
            in.nextToken();
            need[v] = (int)in.nval;
        }
        adj = new int[n * m][];
        deg = new int[n * m];
        alive = new boolean[n * m];
        List<Integer> cells = new ArrayList<>();
        for (int v = 0; v < n * m; v++) {
            int r = v / m, c = v % m;
            List<Integer> near = new ArrayList<>();
            if (r > 0)
                near.add(v - m);
            if (r + 1 < n)
                near.add(v + m);
            if (c > 0)
                near.add(v - 1);
            if (c + 1 < m)
                near.add(v + 1);
            adj[v] = near.stream().mapToInt(Integer::intValue).toArray();
            deg[v] = adj[v].length;
            alive[v] = true;
            cells.add(v);
        }
        List<Integer> order = solve(cells);
        if (order == null) {
            System.out.println("No");
            return;
        }
        StringBuilder sb = new StringBuilder("Yes\n");
        for (int v : order)
            sb.append(v / m + 1).append(' ').append(v % m + 1).append('\n');
        System.out.print(sb);
    }
}
