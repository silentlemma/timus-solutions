import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final int PERIODS = 3; // a cycle always closes by the number 3k
    static int[] parent;

    static int find(int x) {
        int root = x;
        while (parent[root] != root) {
            root = parent[root];
        }
        while (parent[x] != root) {
            int next = parent[x];
            parent[x] = root;
            x = next;
        }
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        long k = Long.parseLong(in.readLine().trim());
        // roots[v]: the residues s with v + s * s = 0 (mod k), the residues of
        // the earlier numbers b joined to a number a = v by a + b * b = 0
        List<List<Integer>> roots = new ArrayList<>();
        List<List<Integer>> written = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            roots.add(new ArrayList<>());
            written.add(new ArrayList<>());
        }
        for (long s = 0; s < k; s++) {
            roots.get((int) ((k - s * s % k) % k)).add((int) s);
        }
        parent = new int[PERIODS * (int) k + 2];
        for (int a = 1;; a++) {
            parent[a] = a;
            long r = a % k;
            int square = (int) ((k - r * r % k) % k);
            List<Integer> near = new ArrayList<>(roots.get((int) r));
            if (!near.contains(square)) {
                near.add(square);
            }
            for (int s : near) {
                for (int b : written.get(s)) {
                    // every edge either joins two trees or closes the first cycle
                    int ra = find(a);
                    int rb = find(b);
                    if (ra == rb) {
                        System.out.println(a);
                        return;
                    }
                    parent[rb] = ra;
                }
            }
            written.get((int) r).add(a);
        }
    }
}
