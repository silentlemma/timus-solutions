import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
  private static final int KINDS = 8; // cocktails as masks of three juices; 0 is unused
  private static final int INF = 1 << 30;
  private static final String JUICES = "ABP";

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(in.readLine().trim());
    List<List<Integer>> glasses = new ArrayList<>();
    for (int k = 0; k < KINDS; k++) glasses.add(new ArrayList<>());
    for (int i = 1; i <= n; i++) {
      int mask = 0;
      for (char c : in.readLine().trim().toCharArray()) mask |= 1 << JUICES.indexOf(c);
      glasses.get(mask).add(i);
    }
    // equal cocktails stand together; the cocktails present are ordered by a DP over
    // subsets, where best[used][last] counts the pourings, and a juice needs a new pouring
    // when a cocktail contains it and the previous one does not
    int present = 0;
    for (int k = 1; k < KINDS; k++) if (!glasses.get(k).isEmpty()) present |= 1 << k;
    int[][] best = new int[1 << KINDS][KINDS];
    int[][] from = new int[1 << KINDS][KINDS];
    for (int[] row : best) Arrays.fill(row, INF);
    for (int k = 1; k < KINDS; k++)
      if ((present >> k & 1) == 1) best[1 << k][k] = Integer.bitCount(k);
    for (int used = 0; used < 1 << KINDS; used++)
      for (int last = 1; last < KINDS; last++) {
        if (best[used][last] == INF) continue;
        for (int k = 1; k < KINDS; k++) {
          if ((present >> k & 1) == 0 || (used >> k & 1) == 1) continue;
          int cost = best[used][last] + Integer.bitCount(k & ~last);
          int next = used | 1 << k;
          if (cost < best[next][k]) {
            best[next][k] = cost;
            from[next][k] = last;
          }
        }
      }
    int last = 1;
    for (int k = 1; k < KINDS; k++) if (best[present][k] < best[present][last]) last = k;
    StringBuilder sb = new StringBuilder();
    sb.append(best[present][last]).append('\n');
    List<Integer> order = new ArrayList<>();
    for (int used = present; last != 0; ) {
      order.add(last);
      int prev = from[used][last];
      used ^= 1 << last;
      last = prev;
    }
    boolean first = true;
    for (int i = order.size() - 1; i >= 0; i--)
      for (int g : glasses.get(order.get(i))) {
        if (!first) sb.append(' ');
        sb.append(g);
        first = false;
      }
    System.out.println(sb);
  }
}
