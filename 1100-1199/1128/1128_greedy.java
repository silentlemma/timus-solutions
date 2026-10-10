import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[][] enemies = new int[n][];
        for (int v = 0; v < n; v++) {
            in.nextToken();
            enemies[v] = new int[(int)in.nval];
            for (int i = 0; i < enemies[v].length; i++) {
                in.nextToken();
                enemies[v][i] = (int)in.nval - 1;
            }
        }
        int[] side = new int[n];
        ArrayDeque<Integer> work = new ArrayDeque<>();
        for (int v = 0; v < n; v++) {
            work.push(v);
        }
        // a child with two or more enemies on its side has at most one on the
        // other, so moving it removes at least one pair of enemies sharing a
        // group; the moves stop after at most as many steps as there are pairs
        while (!work.isEmpty()) {
            int v = work.pop();
            int same = 0;
            for (int u : enemies[v]) {
                if (side[u] == side[v]) {
                    same++;
                }
            }
            if (same >= 2) {
                side[v] ^= 1;
                for (int u : enemies[v]) {
                    work.push(u);
                }
                work.push(v);
            }
        }
        List<Integer> group = new ArrayList<>(), other = new ArrayList<>();
        for (int v = 0; v < n; v++) {
            (side[v] == side[0] ? group : other).add(v + 1);
        }
        List<Integer> small = group.size() <= other.size() ? group : other;
        StringBuilder out = new StringBuilder().append(small.size()).append('\n');
        for (int i = 0; i < small.size(); i++) {
            out.append(i > 0 ? " " : "").append(small.get(i));
        }
        System.out.println(out);
    }
}
