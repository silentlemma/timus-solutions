import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] rating = new int[n + 1];
        int[] parent = new int[n + 1];
        for (int v = 1; v <= n; v++) {
            in.nextToken();
            rating[v] = (int)in.nval;
        }
        // children as linked lists: first[v], then next[c] for the next sibling
        int[] first = new int[n + 1];
        int[] next = new int[n + 1];
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            int child = (int)in.nval;
            in.nextToken();
            int boss = (int)in.nval;
            if (child == 0) {
                break;
            }
            parent[child] = boss;
            next[child] = first[boss];
            first[boss] = child;
        }
        // a breadth-first order from the roots puts every boss before the subordinates
        int[] order = new int[n];
        int size = 0;
        for (int v = 1; v <= n; v++) {
            if (parent[v] == 0) {
                order[size++] = v;
            }
        }
        for (int i = 0; i < size; i++) {
            for (int c = first[order[i]]; c != 0; c = next[c]) {
                order[size++] = c;
            }
        }
        // take[v], skip[v]: the best sum in the subtree of v with v invited or not
        int[] take = new int[n + 1];
        int[] skip = new int[n + 1];
        int total = 0;
        for (int i = size - 1; i >= 0; i--) {
            int v = order[i];
            take[v] += rating[v];
            int best = Math.max(take[v], skip[v]);
            if (parent[v] == 0) {
                total += best;
            } else {
                take[parent[v]] += skip[v];
                skip[parent[v]] += best;
            }
        }
        System.out.println(total);
    }
}
