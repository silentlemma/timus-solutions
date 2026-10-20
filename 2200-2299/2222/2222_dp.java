import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final int ROWS = 3;
    static final int FRONTIER = 2 * ROWS;
    static final int CELLS = FRONTIER + ROWS;
    static final int MASKS = 1 << ROWS;
    static final int GAIN = ROWS - 1;
    static final int UNREACHABLE = -1;
    static final int RADIX = FRONTIER + 1;

    static class Edge {
        int target, mask, weight;

        Edge(int target, int mask, int weight) {
            this.target = target;
            this.mask = mask;
            this.weight = weight;
        }
    }

    static class Layer {
        int[] previous, masks;

        Layer(int size) {
            previous = new int[size];
            Arrays.fill(previous, UNREACHABLE);
            masks = new int[size];
        }
    }

    static class Sets {
        int[] parent = new int[CELLS];

        Sets() {
            for (int i = 0; i < CELLS; ++i) {
                parent[i] = i;
            }
        }

        int root(int v) {
            while (v != parent[v]) {
                parent[v] = parent[parent[v]];
                v = parent[v];
            }
            return v;
        }
    }

    static int encode(int[] state) {
        int code = 0;
        for (int label : state) {
            code = code * RADIX + label;
        }
        return code;
    }

    static int[] transition(int[] state, int mask, int[] finished) {
        Sets sets = new Sets();
        for (int i = 0; i < FRONTIER; ++i) {
            for (int j = 0; j < i; ++j) {
                if (state[i] != 0 && state[i] == state[j]) {
                    sets.parent[sets.root(i)] = sets.root(j);
                }
            }
        }
        boolean[] active = new boolean[CELLS];
        for (int i = 0; i < FRONTIER; ++i) {
            active[i] = state[i] != 0;
        }
        for (int r = 0; r < ROWS; ++r) {
            active[FRONTIER + r] = (mask >> r & 1) != 0;
        }
        for (int r = 0; r < ROWS; ++r) {
            if (!active[FRONTIER + r]) {
                continue;
            }
            for (int c = 0; c < 2; ++c) {
                for (int s = 0; s < ROWS; ++s) {
                    int old = c * ROWS + s;
                    if (Math.abs(r - s) != c + 1 || !active[old]) {
                        continue;
                    }
                    int a = sets.root(old), b = sets.root(FRONTIER + r);
                    if (a == b) {
                        return null;
                    }
                    sets.parent[a] = b;
                }
            }
        }
        boolean[] oldRoots = new boolean[CELLS], newRoots = new boolean[CELLS];
        for (int i = 0; i < CELLS; ++i) {
            if (active[i]) {
                if (i < ROWS) {
                    oldRoots[sets.root(i)] = true;
                } else {
                    newRoots[sets.root(i)] = true;
                }
            }
        }
        boolean lost = false;
        int oldCount = 0, newCount = 0;
        for (int i = 0; i < CELLS; ++i) {
            lost |= oldRoots[i] && !newRoots[i];
            oldCount += oldRoots[i] ? 1 : 0;
            newCount += newRoots[i] ? 1 : 0;
        }
        if (lost) {
            return newCount == 0 && oldCount == 1 ? finished : null;
        }
        int[] labels = new int[CELLS], result = new int[FRONTIER];
        int count = 0;
        for (int i = ROWS; i < CELLS; ++i) {
            if (active[i]) {
                int root = sets.root(i);
                if (labels[root] == 0) {
                    labels[root] = ++count;
                }
                result[i - ROWS] = labels[root];
            }
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int n = 0, ch = input.read();
        while (ch <= ' ') {
            ch = input.read();
        }
        while (ch >= '0' && ch <= '9') {
            n = n * 10 + ch - '0';
            ch = input.read();
        }
        int[] empty = new int[FRONTIER], finished = new int[FRONTIER];
        Arrays.fill(finished, -1);
        List<int[]> states = new ArrayList<>();
        states.add(empty);
        states.add(finished);
        Map<Integer, Integer> indices = new HashMap<>();
        indices.put(encode(empty), 0);
        indices.put(encode(finished), 1);
        List<List<Edge>> edges = new ArrayList<>();
        for (int i = 0; i < states.size(); ++i) {
            int[] state = states.get(i);
            List<Edge> outgoing = new ArrayList<>();
            if (Arrays.equals(state, finished)) {
                outgoing.add(new Edge(i, 0, 0));
            } else {
                for (int mask = 0; mask < MASKS; ++mask) {
                    if (Arrays.equals(state, empty) && mask == 0) {
                        continue;
                    }
                    int[] target = transition(state, mask, finished);
                    if (target == null) {
                        continue;
                    }
                    int code = encode(target);
                    if (!indices.containsKey(code)) {
                        indices.put(code, states.size());
                        states.add(target);
                    }
                    outgoing.add(new Edge(indices.get(code), mask, Integer.bitCount(mask)));
                }
            }
            edges.add(outgoing);
        }
        int size = states.size();
        int[] scores = new int[size];
        Arrays.fill(scores, UNREACHABLE);
        scores[0] = 0;
        List<Layer> history = new ArrayList<>();
        boolean stable = false;
        while (history.size() < n && !stable) {
            int[] following = new int[size];
            Arrays.fill(following, UNREACHABLE);
            Layer layer = new Layer(size);
            for (int source = 0; source < size; ++source) {
                if (scores[source] == UNREACHABLE) {
                    continue;
                }
                for (Edge edge : edges.get(source)) {
                    int candidate = scores[source] + edge.weight;
                    if (candidate > following[edge.target]) {
                        following[edge.target] = candidate;
                        layer.previous[edge.target] = source;
                        layer.masks[edge.target] = edge.mask;
                    }
                }
            }
            // An equal score shift is preserved by every subsequent DP step.
            stable = true;
            for (int i = 0; i < size; ++i) {
                if (!(scores[i] == UNREACHABLE && following[i] == UNREACHABLE) &&
                    !(scores[i] != UNREACHABLE && following[i] == scores[i] + GAIN)) {
                    stable = false;
                }
            }
            scores = following;
            history.add(layer);
        }
        int best = UNREACHABLE, vertex = 0;
        for (int i = 0; i < size; ++i) {
            int[] state = states.get(i);
            int maximum = state[0];
            for (int label : state) {
                maximum = Math.max(maximum, label);
            }
            if ((Arrays.equals(state, finished) || maximum == 1) && scores[i] > best) {
                best = scores[i];
                vertex = i;
            }
        }
        int[] board = new int[n];
        for (int column = n - 1; column >= 0; --column) {
            Layer layer = history.get(Math.min(column, history.size() - 1));
            board[column] = layer.masks[vertex];
            vertex = layer.previous[vertex];
        }
        StringBuilder output = new StringBuilder(2 * ROWS * n);
        for (int row = 0; row < ROWS; ++row) {
            for (int column = 0; column < n; ++column) {
                if (column != 0) {
                    output.append(' ');
                }
                output.append(board[column] >> row & 1);
            }
            output.append('\n');
        }
        System.out.print(output);
    }
}
