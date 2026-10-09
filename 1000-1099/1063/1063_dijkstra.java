import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class Main {
    static final int FACES = 6, MASKS = 1 << FACES;

    // the faces split into connected groups, the faces that have dominoes and
    // the faces of odd degree
    static class State {
        int[] group = new int[FACES];
        int active, odd;

        State copy() {
            State s = new State();
            s.group = group.clone();
            s.active = active;
            s.odd = odd;
            return s;
        }
    }

    // relabels the groups in order of first appearance and packs the state
    static long normalize(State s) {
        int[] name = new int[FACES];
        Arrays.fill(name, -1);
        int next = 0;
        long code = 0;
        for (int v = 0; v < FACES; v++) {
            if (name[s.group[v]] < 0) {
                name[s.group[v]] = next++;
            }
            code = code * FACES + name[s.group[v]];
        }
        for (int v = 0; v < FACES; v++) {
            s.group[v] = name[s.group[v]];
        }
        return (code * MASKS + s.active) * MASKS + s.odd;
    }

    static void join(State s, int a, int b) {
        int ga = s.group[a], gb = s.group[b];
        for (int v = 0; v < FACES; v++) {
            if (s.group[v] == gb) {
                s.group[v] = ga;
            }
        }
        s.active |= 1 << a | 1 << b;
        s.odd ^= 1 << a ^ 1 << b;
    }

    static boolean done(State s) {
        int group = -1;
        for (int v = 0; v < FACES; v++) {
            if ((s.active >> v & 1) == 1) {
                if (group >= 0 && s.group[v] != group) {
                    return false;
                }
                group = s.group[v];
            }
        }
        return Integer.bitCount(s.odd) <= 2;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        State start = new State();
        for (int v = 0; v < FACES; v++) {
            start.group[v] = v;
        }
        for (int k = 0; k < n; k++) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            join(start, a - 1, b - 1);
        }
        // Dijkstra over the states: adding the domino (a, b) costs a + b, joins
        // the groups of a and b and flips the parity of both faces
        Map<Long, Integer> dist = new HashMap<>();
        Map<Long, State> states = new HashMap<>();
        Map<Long, long[]> parent = new HashMap<>();
        long key = normalize(start);
        dist.put(key, 0);
        states.put(key, start);
        PriorityQueue<long[]> heap = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));
        heap.add(new long[] {0, key});
        while (!heap.isEmpty()) {
            long[] top = heap.poll();
            long k = top[1];
            int d = (int)top[0];
            if (d > dist.get(k)) {
                continue;
            }
            if (done(states.get(k))) {
                key = k;
                break;
            }
            for (int a = 0; a < FACES; a++) {
                for (int b = a + 1; b < FACES; b++) {
                    State next = states.get(k).copy();
                    join(next, a, b);
                    long nk = normalize(next);
                    int cost = d + (a + 1) + (b + 1);
                    Integer old = dist.get(nk);
                    if (old == null || cost < old) {
                        dist.put(nk, cost);
                        states.put(nk, next);
                        parent.put(nk, new long[] {k, a + 1, b + 1});
                        heap.add(new long[] {cost, nk});
                    }
                }
            }
        }
        List<long[]> added = new ArrayList<>();
        for (long k = key; parent.containsKey(k); k = parent.get(k)[0]) {
            added.add(parent.get(k));
        }
        StringBuilder out = new StringBuilder();
        out.append(dist.get(key)).append('\n').append(added.size()).append('\n');
        for (long[] e : added) {
            out.append(e[1]).append(' ').append(e[2]).append('\n');
        }
        System.out.print(out);
    }
}
