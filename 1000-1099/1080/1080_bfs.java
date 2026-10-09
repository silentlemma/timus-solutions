import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 1; i <= n; i++) {
            for (int v = in.nextInt(); v != 0; v = in.nextInt()) {
                adj.get(i).add(v);
                adj.get(v).add(i);
            }
        }
        // the map is connected, so the colour of the first country decides all
        int[] color = new int[n + 1];
        Arrays.fill(color, -1);
        color[1] = 0;
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(1);
        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : adj.get(u)) {
                if (color[v] < 0) {
                    color[v] = 1 - color[u];
                    queue.add(v);
                } else if (color[v] == color[u]) {
                    System.out.println(-1);
                    return;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            out.append(color[i]);
        }
        System.out.println(out);
    }
}
