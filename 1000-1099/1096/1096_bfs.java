import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt();
        int[] route = new int[k], back = new int[k];
        Map<Integer, List<Integer>> byRoute = new HashMap<>();
        for (int j = 0; j < k; j++) {
            route[j] = in.nextInt();
            back[j] = in.nextInt();
            byRoute.computeIfAbsent(route[j], r -> new ArrayList<>()).add(j);
        }
        int t = in.nextInt(), s1 = in.nextInt(), s2 = in.nextInt();
        // a state is the plate in hand: the first one, or the plate of bus j; a
        // driver swaps when the plate in hand shows the route of his bus
        int[] came = new int[k];
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {s1, s2, -1});
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int r : new int[] {cur[0], cur[1]}) {
                List<Integer> buses = byRoute.remove(r);
                if (buses == null) {
                    continue;
                }
                for (int i : buses) {
                    came[i] = cur[2];
                    if (route[i] == t || back[i] == t) {
                        List<Integer> path = new ArrayList<>();
                        for (int b = i; b >= 0; b = came[b]) {
                            path.add(b + 1);
                        }
                        StringBuilder out = new StringBuilder();
                        out.append(path.size()).append("\n");
                        for (int p = path.size() - 1; p >= 0; p--) {
                            out.append(path.get(p)).append("\n");
                        }
                        System.out.print(out);
                        return;
                    }
                    queue.add(new int[] {route[i], back[i], i});
                }
            }
        }
        System.out.println("IMPOSSIBLE");
    }
}
