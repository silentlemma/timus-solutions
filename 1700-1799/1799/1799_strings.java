import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final int ALPHABET = 26;

    // suffix automaton; first[v] is the end of the first occurrence of v,
    // and prefix[i] the state of the prefix ending at i
    static int[] next, link, len, first, prefix;
    static int states, last;

    static int add(int parent, int length, int end) {
        Arrays.fill(next, states * ALPHABET, (states + 1) * ALPHABET, -1);
        link[states] = parent;
        len[states] = length;
        first[states] = end;
        return states++;
    }

    static void extend(int c, int end) {
        int cur = add(0, len[last] + 1, end), p = last;
        while (p != -1 && next[p * ALPHABET + c] == -1) {
            next[p * ALPHABET + c] = cur;
            p = link[p];
        }
        if (p != -1) {
            int q = next[p * ALPHABET + c];
            if (len[p] + 1 == len[q]) {
                link[cur] = q;
            } else {
                int clone = add(link[q], len[p] + 1, first[q]);
                System.arraycopy(next, q * ALPHABET, next, clone * ALPHABET, ALPHABET);
                while (p != -1 && next[p * ALPHABET + c] == q) {
                    next[p * ALPHABET + c] = clone;
                    p = link[p];
                }
                link[q] = clone;
                link[cur] = clone;
            }
        }
        last = cur;
    }

    // adds to a range of positions and sums a prefix
    static long[] plain, scaled;

    static void point(long[] tree, int at, long value) {
        for (at++; at < tree.length; at += at & -at) tree[at] += value;
    }

    static long sum(int count) {
        long a = 0, b = 0;
        for (int at = count; at > 0; at -= at & -at) {
            a += plain[at];
            b += scaled[at];
        }
        return a * count - b;
    }

    static void addRange(int from, int to, long value) {
        if (from >= to) return;
        point(plain, from, value);
        point(plain, to, -value);
        point(scaled, from, value * from);
        point(scaled, to, -value * to);
    }

    static long swagness(String s) {
        int n = s.length(), cap = 2 * n + 2;
        next = new int[cap * ALPHABET];
        link = new int[cap];
        len = new int[cap];
        first = new int[cap];
        prefix = new int[n];
        states = 0;
        last = 0;
        add(-1, 0, 0);
        for (int i = 0; i < n; i++) {
            extend(s.charAt(i) - 'a', i);
            prefix[i] = last;
        }
        // the states in order of length, by counting
        int[] byLen = new int[n + 2];
        for (int v = 0; v < states; v++) byLen[len[v] + 1]++;
        for (int l = 1; l <= n + 1; l++) byLen[l] += byLen[l - 1];
        int[] order = new int[states];
        for (int v = 0; v < states; v++) order[byLen[len[v]]++] = v;

        // a state with exactly one way out is squeezed into the edge through it
        int[] only = new int[states], target = new int[states], extra = new int[states];
        boolean[] keep = new boolean[states];
        for (int v = 0; v < states; v++) {
            int ways = 0;
            for (int c = 0; c < ALPHABET; c++) {
                if (next[v * ALPHABET + c] != -1) {
                    ways++;
                    only[v] = next[v * ALPHABET + c];
                }
            }
            keep[v] = v == 0 || ways != 1;
        }
        for (int k = states - 1; k >= 0; k--) {
            int v = order[k];
            if (keep[v]) {
                target[v] = v;
            } else {
                target[v] = target[only[v]];
                extra[v] = 1 + extra[only[v]];
            }
        }
        // the compressed edges and, for each, its label s[from .. to]
        int edgeCap = states * 2;
        int[] source = new int[edgeCap], dest = new int[edgeCap], from = new int[edgeCap];
        int[] to = new int[edgeCap];
        long[] distinct = new long[edgeCap];
        int edges = 0;
        for (int u = 0; u < states; u++) {
            if (!keep[u]) continue;
            for (int c = 0; c < ALPHABET; c++) {
                int t = next[u * ALPHABET + c];
                if (t == -1) continue;
                if (edges == source.length) {
                    source = Arrays.copyOf(source, 2 * edges);
                    dest = Arrays.copyOf(dest, 2 * edges);
                    from = Arrays.copyOf(from, 2 * edges);
                    to = Arrays.copyOf(to, 2 * edges);
                    distinct = Arrays.copyOf(distinct, 2 * edges);
                }
                source[edges] = u;
                dest[edges] = target[t];
                to[edges] = first[target[t]];
                from[edges] = to[edges] - extra[t];
                edges++;
            }
        }

        // the suffix link tree in Euler order
        int[] childStart = new int[states + 1], children = new int[states];
        for (int v = 1; v < states; v++) childStart[link[v] + 1]++;
        for (int v = 0; v < states; v++) childStart[v + 1] += childStart[v];
        int[] fill = Arrays.copyOf(childStart, states);
        for (int v = 1; v < states; v++) children[fill[link[v]]++] = v;
        int[] tin = new int[states], tout = new int[states];
        int[] stackV = new int[states], stackAt = new int[states];
        int depth = 1, timer = 1;
        stackAt[0] = childStart[0];
        while (depth > 0) {
            int v = stackV[depth - 1];
            if (stackAt[depth - 1] == childStart[v + 1]) {
                tout[v] = timer;
                depth--;
                continue;
            }
            int child = children[stackAt[depth - 1]++];
            tin[child] = timer++;
            stackV[depth] = child;
            stackAt[depth++] = childStart[child];
        }
        // the latest end seen in a subtree, as a segment tree of maxima
        int size = 1;
        while (size < states) size *= 2;
        int[] latest = new int[2 * size];

        int[] queryStart = new int[n + 2], queries = new int[edges];
        for (int e = 0; e < edges; e++) queryStart[to[e] + 2]++;
        for (int i = 1; i <= n + 1; i++) queryStart[i] += queryStart[i - 1];
        for (int e = 0; e < edges; e++) queries[queryStart[to[e] + 1]++] = e;
        // count[p]: distinct substrings of s[0 .. end) whose last occurrence
        // starts at p; the states on one suffix link path that share their
        // last end form chains, and top[end] is the state just above a chain
        plain = new long[n + 1];
        scaled = new long[n + 1];
        boolean[] seen = new boolean[states];
        seen[0] = true;
        int[] top = new int[n + 1];
        for (int end = 1; end <= n; end++) {
            int v = prefix[end - 1];
            addRange(end - len[v], end, 1);
            int u = v;
            while (!seen[u]) {
                seen[u] = true;
                u = link[u];
            }
            while (u != 0) {
                int was = 0;
                for (int lo = tin[u] + size, hi = tout[u] + size; lo < hi; lo /= 2, hi /= 2) {
                    if ((lo & 1) == 1) was = Math.max(was, latest[lo++]);
                    if ((hi & 1) == 1) was = Math.max(was, latest[--hi]);
                }
                int above = top[was];
                addRange(was - len[u], was - len[above], -1);
                top[was] = u;
                u = above;
            }
            int at = tin[v] + size;
            latest[at] = end;
            for (; at > 1; at /= 2) latest[at / 2] = Math.max(latest[at], latest[at ^ 1]);
            top[end] = 0;
            for (int k = queryStart[end - 1]; k < queryStart[end]; k++) {
                int e = queries[k];
                distinct[e] = sum(end) - sum(from[e]);
            }
        }

        // each compressed edge stands for as many tree edges as there are
        // paths from the root to its source
        int[] outStart = new int[states + 1], outEdges = new int[edges];
        for (int e = 0; e < edges; e++) outStart[source[e] + 1]++;
        for (int v = 0; v < states; v++) outStart[v + 1] += outStart[v];
        int[] outFill = Arrays.copyOf(outStart, states);
        for (int e = 0; e < edges; e++) outEdges[outFill[source[e]]++] = e;
        long[] paths = new long[states];
        paths[0] = 1;
        long total = 0;
        for (int v : order) {
            if (!keep[v] || paths[v] == 0) continue;
            for (int k = outStart[v]; k < outStart[v + 1]; k++) {
                int e = outEdges[k];
                total += paths[v] * distinct[e];
                paths[dest[e]] += paths[v];
            }
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(new StringTokenizer(in.readLine()).nextToken());
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String line = in.readLine().trim();
            out.append(swagness(line)).append('\n');
        }
        System.out.print(out);
    }
}
