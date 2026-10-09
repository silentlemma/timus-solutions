import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        List<List<Integer>> adj = new ArrayList<>();
        for (int v = 0; v <= n; v++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i + 1 < n; i++) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        // the destroyed airports are exactly the ones on the way back to k, so a
        // move always goes down the tree rooted at k; a breadth-first order lists
        // parents before children
        int[] parent = new int[n + 1];
        int[] order = new int[n];
        parent[k] = -1;
        order[0] = k;
        int size = 1;
        for (int i = 0; i < size; i++) {
            int v = order[i];
            for (int w : adj.get(v)) {
                if (w != parent[v]) {
                    parent[w] = v;
                    order[size++] = w;
                }
            }
        }
        // win[v]: the player to move at v wins, that is, some child is a loss
        boolean[] win = new boolean[n + 1];
        for (int i = size - 1; i >= 1; i--) {
            if (!win[order[i]]) {
                win[parent[order[i]]] = true;
            }
        }
        int best = 0;
        for (int w : adj.get(k)) {
            if (!win[w] && (best == 0 || w < best)) {
                best = w;
            }
        }
        if (best == 0) {
            System.out.println("First player loses");
        } else {
            System.out.println("First player wins flying to airport " + best);
        }
    }
}
