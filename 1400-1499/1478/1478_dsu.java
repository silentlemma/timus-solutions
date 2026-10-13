import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final int INDEX_BITS = 10; // edges are packed as length, then both indices
    static final long INDEX_MASK = (1 << INDEX_BITS) - 1;
    static final int WORD_BITS = 64;

    static int[] parent;

    static int find(int x) {
        while (parent[x] != x)
            x = parent[x] = parent[parent[x]];
        return x;
    }

    // counts are bit sets: bit k says that k bases are possible; res |= a << k
    static void orShifted(long[] res, long[] a, int k) {
        int words = k / WORD_BITS, bits = k % WORD_BITS;
        for (int i = res.length - 1; i >= words; i--) {
            long v = a[i - words] << bits;
            if (bits > 0 && i - words - 1 >= 0)
                v |= a[i - words - 1] >>> (WORD_BITS - bits);
            res[i] |= v;
        }
    }

    static String solve(long[] xs, long[] ys) {
        int n = xs.length;
        long[] edges = new long[n * (n - 1) / 2];
        int m = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                long dx = xs[i] - xs[j], dy = ys[i] - ys[j];
                edges[m++] = (dx * dx + dy * dy) << (2 * INDEX_BITS) | (long)i << INDEX_BITS | j;
            }
        Arrays.sort(edges);

        // the single-linkage tree: nodes 0 .. n-1 are the objects, then each
        // component formed after a group of equal distances is a new node
        List<List<Integer>> kids = new ArrayList<>();
        List<Long> width = new ArrayList<>(), out = new ArrayList<>();
        parent = new int[n];
        List<List<Integer>> members = new ArrayList<>();
        long[] compWidth = new long[n];
        int[] compNode = new int[n];
        for (int i = 0; i < n; i++) {
            kids.add(new ArrayList<>());
            width.add(0L);
            out.add(-1L);
            parent[i] = i;
            members.add(new ArrayList<>(Arrays.asList(i)));
            compNode[i] = i;
        }
        for (int e = 0; e < m;) {
            long w = edges[e] >> (2 * INDEX_BITS);
            Map<Integer, List<Integer>> grown = new HashMap<>(); // root -> swallowed nodes
            for (; e < m && edges[e] >> (2 * INDEX_BITS) == w; e++) {
                int ra = find((int)(edges[e] >> INDEX_BITS & INDEX_MASK));
                int rb = find((int)(edges[e] & INDEX_MASK));
                if (ra == rb)
                    continue;
                long far = Math.max(compWidth[ra], compWidth[rb]);
                for (int p : members.get(ra))
                    for (int q : members.get(rb)) {
                        long dx = xs[p] - xs[q], dy = ys[p] - ys[q];
                        far = Math.max(far, dx * dx + dy * dy);
                    }
                parent[rb] = ra;
                members.get(ra).addAll(members.get(rb));
                compWidth[ra] = far;
                List<Integer> swallowed = grown.containsKey(ra)
                                              ? grown.get(ra)
                                              : new ArrayList<>(Arrays.asList(compNode[ra]));
                List<Integer> more = grown.remove(rb);
                if (more != null)
                    swallowed.addAll(more);
                else
                    swallowed.add(compNode[rb]);
                grown.put(ra, swallowed);
            }
            for (Map.Entry<Integer, List<Integer>> g : grown.entrySet()) {
                for (int c : g.getValue())
                    out.set(c, w);
                compNode[g.getKey()] = kids.size();
                kids.add(g.getValue());
                width.add(compWidth[g.getKey()]);
                out.add(-1L);
            }
        }

        // a node can be a base when it is narrower than its distance to the rest
        int size = (n + WORD_BITS) / WORD_BITS;
        long[][] all = new long[kids.size()][];
        for (int v = 0; v < kids.size(); v++) {
            all[v] = new long[size];
            if (out.get(v) < 0 || width.get(v) < out.get(v))
                all[v][0] |= 1L << 1;
            if (kids.get(v).isEmpty())
                continue;
            long[] total = new long[size];
            total[0] = 1;
            for (int c : kids.get(v)) {
                long[] combined = new long[size];
                for (int k = 1; k <= n; k++)
                    if ((all[c][k / WORD_BITS] >>> (k % WORD_BITS) & 1) == 1)
                        orShifted(combined, total, k);
                total = combined;
            }
            for (int i = 0; i < size; i++)
                all[v][i] |= total[i];
        }
        long[] root = all[all.length - 1];
        StringBuilder s = new StringBuilder();
        for (int k = 1; k <= n; k++)
            s.append((root[k / WORD_BITS] >>> (k % WORD_BITS) & 1) == 1 ? '1' : '0');
        return s.toString();
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        StringBuilder out = new StringBuilder();
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int n = (int)in.nval;
            if (n == 0)
                break;
            long[] xs = new long[n], ys = new long[n];
            for (int i = 0; i < n; i++) {
                in.nextToken();
                xs[i] = (long)in.nval;
                in.nextToken();
                ys[i] = (long)in.nval;
            }
            out.append(solve(xs, ys)).append('\n');
        }
        System.out.print(out);
    }
}
