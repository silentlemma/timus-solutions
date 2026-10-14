import java.io.*;
import java.util.*;

public class Main {
    // every piece that can ever appear is a maximal run of rings above some
    // content; such runs nest, and the children of a run are the runs above its
    // smallest content
    static class Chain {
        int[] rings;
        List<Integer> low = new ArrayList<>(), grundy = new ArrayList<>();
        List<List<Integer>> children = new ArrayList<>();

        int build(int left, int right) {
            int node = low.size(), m = rings[left];
            for (int i = left; i <= right; i++)
                m = Math.min(m, rings[i]);
            low.add(m);
            children.add(new ArrayList<>());
            grundy.add(0);
            for (int i = left; i <= right; i++)
                if (rings[i] > m) {
                    int j = i;
                    while (j + 1 <= right && rings[j + 1] > m)
                        j++;
                    int child = build(i, j);
                    children.get(node).add(child);
                    i = j;
                }
            return node;
        }

        // {x: xor of the pieces left by removing rings up to x} in node
        Map<Integer, Integer> afterMoves(int node) {
            Map<Integer, Integer> result = new HashMap<>();
            PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.comparingInt(low::get));
            int x = 0;
            for (int c : children.get(node)) {
                heap.add(c);
                x ^= grundy.get(c);
            }
            result.put(low.get(node), x);
            while (!heap.isEmpty()) {
                int content = low.get(heap.peek());
                while (!heap.isEmpty() && low.get(heap.peek()) == content) {
                    int c = heap.poll();
                    x ^= grundy.get(c);
                    for (int d : children.get(c)) {
                        x ^= grundy.get(d);
                        heap.add(d);
                    }
                }
                result.put(content, x);
            }
            return result;
        }

        int analyse() {
            build(0, rings.length - 1);
            // children are built after their parents, so go backwards
            for (int node = low.size() - 1; node >= 0; node--) {
                Set<Integer> options = new HashSet<>(afterMoves(node).values());
                int g = 0;
                while (options.contains(g))
                    g++;
                grundy.set(node, g);
            }
            return grundy.get(0);
        }
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer st =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();
        int k = (int)st.nval, total = 0;
        Chain[] chains = new Chain[k];
        int[] g = new int[k];
        for (int i = 0; i < k; i++) {
            st.nextToken();
            chains[i] = new Chain();
            chains[i].rings = new int[(int)st.nval];
            for (int j = 0; j < chains[i].rings.length; j++) {
                st.nextToken();
                chains[i].rings[j] = (int)st.nval;
            }
            g[i] = chains[i].analyse();
            total ^= g[i];
        }
        if (total == 0) {
            System.out.println("S");
            return;
        }
        // a winning move leaves the chain with the xor of all other chains
        for (int i = 0; i < k; i++) {
            Map<Integer, Integer> after = chains[i].afterMoves(0);
            for (int j = 0; j < chains[i].rings.length; j++)
                if (after.get(chains[i].rings[j]) == (total ^ g[i])) {
                    System.out.println("G\n" + (i + 1) + " " + (j + 1));
                    return;
                }
        }
    }
}
