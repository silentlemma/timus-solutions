import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    // arcs in pairs e, e ^ 1: an undirected edge is two arcs of full
    // capacity, each the reverse of the other; the arcs of a node form a
    // linked list through next
    static int[] first;
    static int[] next;
    static int[] target;
    static int[] cap;
    static int arcs;
    static int[] level;
    static int[] arc;

    static void link(int a, int b, int forward, int backward) {
        target[arcs] = b;
        cap[arcs] = forward;
        next[arcs] = first[a];
        first[a] = arcs++;
        target[arcs] = a;
        cap[arcs] = backward;
        next[arcs] = first[b];
        first[b] = arcs++;
    }

    static boolean levels(int source, int sink) {
        Arrays.fill(level, -1);
        level[source] = 0;
        int[] queue = new int[level.length];
        int size = 0;
        queue[size++] = source;
        for (int i = 0; i < size; i++) {
            int v = queue[i];
            for (int e = first[v]; e >= 0; e = next[e]) {
                if (cap[e] > 0 && level[target[e]] < 0) {
                    level[target[e]] = level[v] + 1;
                    queue[size++] = target[e];
                }
            }
        }
        return level[sink] >= 0;
    }

    static int push(int v, int sink, int amount) {
        if (v == sink) {
            return amount;
        }
        for (; arc[v] >= 0; arc[v] = next[arc[v]]) {
            int e = arc[v];
            if (cap[e] > 0 && level[target[e]] == level[v] + 1) {
                int got = push(target[e], sink, Math.min(amount, cap[e]));
                if (got > 0) {
                    cap[e] -= got;
                    cap[e ^ 1] += got;
                    return got;
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        char[] s = st.nextToken().toCharArray();
        char[] p = st.nextToken().toCharArray();
        int n = s.length;
        int m = p.length;
        // every erased character is a node; a node on the source side
        // becomes 1, on the sink side 0. Characters s[j] and p[i] meet once
        // in every window where j - i is between 0 and n - m.
        int[] nodeS = new int[n];
        int[] nodeP = new int[m];
        int count = 0;
        for (int j = 0; j < n; j++) {
            nodeS[j] = s[j] == '?' ? count++ : -1;
        }
        for (int i = 0; i < m; i++) {
            nodeP[i] = p[i] == '?' ? count++ : -1;
        }
        int source = count;
        int sink = count + 1;
        int most = 2 * (m * (n - m + 1) + 2 * count);
        first = new int[count + 2];
        Arrays.fill(first, -1);
        next = new int[most];
        target = new int[most];
        cap = new int[most];
        level = new int[count + 2];
        // pairs with a fixed 1 cost when the node is 0, with a fixed 0 when 1
        int[] ones = new int[count];
        int[] zeros = new int[count];
        long base = 0;
        for (int i = 0; i < m; i++) {
            for (int j = i; j <= i + n - m; j++) {
                int u = nodeP[i];
                int v = nodeS[j];
                if (u < 0 && v < 0) {
                    base += p[i] != s[j] ? 1 : 0;
                } else if (u < 0 || v < 0) {
                    int w = u < 0 ? v : u;
                    char c = u < 0 ? p[i] : s[j];
                    if (c == '1') {
                        ones[w]++;
                    } else {
                        zeros[w]++;
                    }
                } else {
                    link(u, v, 1, 1);
                }
            }
        }
        for (int w = 0; w < count; w++) {
            // a node with both kinds of fixed partners pays the smaller anyway
            int both = Math.min(ones[w], zeros[w]);
            base += both;
            if (ones[w] > both) {
                link(source, w, ones[w] - both, 0);
            }
            if (zeros[w] > both) {
                link(w, sink, zeros[w] - both, 0);
            }
        }
        long flow = 0;
        while (levels(source, sink)) {
            arc = first.clone();
            for (int got = push(source, sink, n * m); got > 0; got = push(source, sink, n * m)) {
                flow += got;
            }
        }
        // the source side of the last search is a minimum cut
        levels(source, sink);
        for (int j = 0; j < n; j++) {
            if (nodeS[j] >= 0) {
                s[j] = level[nodeS[j]] >= 0 ? '1' : '0';
            }
        }
        for (int i = 0; i < m; i++) {
            if (nodeP[i] >= 0) {
                p[i] = level[nodeP[i]] >= 0 ? '1' : '0';
            }
        }
        System.out.println((base + flow) + "\n" + new String(s) + "\n" + new String(p));
    }
}
