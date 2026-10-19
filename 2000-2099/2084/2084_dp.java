import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
  private static final long NONE = Long.MIN_VALUE; // an unreachable state

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int x = in.nextInt();
    int n = in.nextInt();
    int[] a = new int[n];
    int[] b = new int[n];
    for (int i = 0; i < n; i++) a[i] = in.nextInt();
    for (int i = 0; i < n; i++) b[i] = in.nextInt();
    // utility above x is earned whatever the order; with b capped at x a task
    // done at repaired volume r (debt x - r) earns max(0, min(x, r) - (x - b))
    long extra = 0;
    int[] need = new int[n];
    Integer[] order = new Integer[n];
    for (int i = 0; i < n; i++) {
      extra += Math.max(0, b[i] - x);
      need[i] = x - Math.min(b[i], x);
      order[i] = i;
    }
    Arrays.sort(order, (i, j) -> Integer.compare(a[i], a[j]));
    // some tasks are given up: they go first and only repair. The rest go by a
    // descending, so task i (ascending a) sees the given up ones before it and
    // every task from it on. best[s]: s = repair of given up tasks so far, capped
    int[] suffix = new int[n + 1];
    for (int k = n - 1; k >= 0; k--) suffix[k] = suffix[k + 1] + a[order[k]];
    long[] best = new long[x + 1];
    Arrays.fill(best, NONE);
    best[0] = 0;
    int[][] prev = new int[n][x + 1];
    boolean[][] up = new boolean[n][x + 1];
    for (int k = 0; k < n; k++) {
      int i = order[k];
      long[] nxt = new long[x + 1];
      Arrays.fill(nxt, NONE);
      for (int s = 0; s <= x; s++) {
        if (best[s] == NONE) continue;
        long gain = best[s] + Math.min(x, s + suffix[k]) - need[i];
        if (gain > nxt[s]) {
          nxt[s] = gain;
          prev[k][s] = s;
          up[k][s] = false;
        }
        int t = Math.min(x, s + a[i]);
        if (best[s] > nxt[t]) {
          nxt[t] = best[s];
          prev[k][t] = s;
          up[k][t] = true;
        }
      }
      best = nxt;
    }
    int s = 0;
    for (int v = 0; v <= x; v++) if (best[v] > best[s]) s = v;
    StringBuilder out = new StringBuilder();
    out.append(best[s] + extra).append('\n');
    List<Integer> givenUp = new ArrayList<>();
    List<Integer> kept = new ArrayList<>(); // kept comes out by a descending
    for (int k = n - 1; k >= 0; k--) {
      (up[k][s] ? givenUp : kept).add(order[k] + 1);
      s = prev[k][s];
    }
    givenUp.addAll(kept);
    for (int k = 0; k < n; k++) out.append(k > 0 ? " " : "").append(givenUp.get(k));
    System.out.println(out);
  }
}
