import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        int total = 2 * n;
        List<List<Integer>> near = new ArrayList<>();
        for (int v = 0; v <= total; v++) {
            near.add(new ArrayList<>());
        }
        for (int k = 0; k < m; k++) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            near.get(a).add(b);
            near.get(b).add(a);
        }
        // similar problems must go to different rounds: colour every component
        // of the conflict graph in two colours, or give up on an odd cycle
        int[] colour = new int[total + 1];
        Arrays.fill(colour, -1);
        List<List<Integer>> comps = new ArrayList<>();
        for (int start = 1; start <= total; start++) {
            if (colour[start] >= 0) {
                continue;
            }
            colour[start] = 0;
            List<Integer> members = new ArrayList<>();
            members.add(start);
            ArrayDeque<Integer> stack = new ArrayDeque<>();
            stack.push(start);
            while (!stack.isEmpty()) {
                int v = stack.pop();
                for (int w : near.get(v)) {
                    if (colour[w] < 0) {
                        colour[w] = 1 - colour[v];
                        members.add(w);
                        stack.push(w);
                    } else if (colour[w] == colour[v]) {
                        System.out.println("IMPOSSIBLE");
                        return;
                    }
                }
            }
            comps.add(members);
        }
        // each component sends one of its colours to the first round, and
        // reach[k][s] tells whether the first k components can give it s problems
        int c = comps.size();
        int[][] sizes = new int[c][2];
        for (int k = 0; k < c; k++) {
            for (int v : comps.get(k)) {
                sizes[k][colour[v]]++;
            }
        }
        boolean[][] reach = new boolean[c + 1][n + 1];
        reach[0][0] = true;
        for (int k = 0; k < c; k++) {
            for (int s = 0; s <= n; s++) {
                if (reach[k][s]) {
                    for (int size : sizes[k]) {
                        if (s + size <= n) {
                            reach[k + 1][s + size] = true;
                        }
                    }
                }
            }
        }
        if (!reach[c][n]) {
            System.out.println("IMPOSSIBLE");
            return;
        }
        boolean[] first = new boolean[total + 1];
        for (int k = c - 1, s = n; k >= 0; k--) {
            int side = s >= sizes[k][0] && reach[k][s - sizes[k][0]] ? 0 : 1;
            for (int v : comps.get(k)) {
                if (colour[v] == side) {
                    first[v] = true;
                }
            }
            s -= sizes[k][side];
        }
        StringBuilder out = new StringBuilder();
        for (int round = 0; round < 2; round++) {
            StringBuilder line = new StringBuilder();
            for (int v = 1; v <= total; v++) {
                if (first[v] == (round == 0)) {
                    line.append(line.length() > 0 ? " " : "").append(v);
                }
            }
            out.append(line).append('\n');
        }
        System.out.print(out);
    }
}
