import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    static List<List<int[]>> adj = new ArrayList<>();
    static int q;

    // best[k]: the most apples on k branches kept in the subtree of v, all of
    // them connected to v; the array is only as long as k can go
    static long[] solve(int v, int parent) {
        long[] best = {0};
        for (int[] e : adj.get(v)) {
            if (e[0] == parent) {
                continue;
            }
            long[] sub = solve(e[0], v);
            long[] merged = new long[Math.min(q + 1, best.length + sub.length)];
            Arrays.fill(merged, -1);
            for (int i = 0; i < best.length; i++) {
                // taking j >= 1 branches on the child's side: its edge and j - 1 below
                for (int j = 0; j <= sub.length && i + j < merged.length; j++) {
                    long gain = j == 0 ? 0 : e[1] + sub[j - 1];
                    merged[i + j] = Math.max(merged[i + j], best[i] + gain);
                }
            }
            best = merged;
        }
        return best;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        q = in.nextInt();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 1; i < n; i++) {
            int a = in.nextInt(), b = in.nextInt(), apples = in.nextInt();
            adj.get(a).add(new int[] {b, apples});
            adj.get(b).add(new int[] {a, apples});
        }
        System.out.println(solve(1, 0)[q]);
    }
}
