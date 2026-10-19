import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {
  private static final long ENDLESS = 1L << 62;

  // layers in order of names (the densest at the bottom), with a Fenwick tree of heights
  private static int m;
  private static int top;
  private static long[] tree;
  private static long[] height;
  private static long total;
  private static long straw;
  private static long clock;
  private static final List<long[]> SIPS = new ArrayList<>(); // from, to, layer

  private static void add(int i, long delta) {
    height[i] += delta;
    for (i++; i <= m; i += i & -i) tree[i] += delta;
  }

  // the layer that contains level h; h becomes the part of the layer below the level
  private static int layerAt(long[] h) {
    int pos = 0;
    for (int step = top; step > 0; step >>= 1)
      if (pos + step <= m && tree[pos + step] <= h[0]) {
        pos += step;
        h[0] -= tree[pos];
      }
    return pos;
  }

  private static void drink(long amount) {
    long[] h = new long[1];
    while (amount > 0 && total > straw) {
      h[0] = straw;
      int layer = layerAt(h);
      long take = Math.min(height[layer] - h[0], amount);
      add(layer, -take);
      total -= take;
      amount -= take;
      long[] last = SIPS.isEmpty() ? null : SIPS.get(SIPS.size() - 1);
      if (last != null && last[2] == layer && last[1] == clock) last[1] = clock + take;
      else SIPS.add(new long[] {clock, clock + take, layer});
      clock += take;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(in.readLine().trim());
    long[] times = new long[n];
    String[] words = new String[n];
    long[] values = new long[n];
    TreeSet<String> sorted = new TreeSet<>();
    for (int i = 0; i < n; i++) {
      StringTokenizer st = new StringTokenizer(in.readLine());
      times[i] = Long.parseLong(st.nextToken());
      words[i] = st.nextToken();
      if (st.hasMoreTokens()) values[i] = Long.parseLong(st.nextToken());
      if (!words[i].equals("Oleg") && !words[i].equals("fire")) sorted.add(words[i]);
    }
    List<String> names = new ArrayList<>(sorted);
    Map<String, Integer> index = new HashMap<>();
    for (int i = 0; i < names.size(); i++) index.put(names.get(i), i);
    m = names.size();
    tree = new long[m + 1];
    height = new long[m];
    top = 1;
    while (top * 2 <= m) top *= 2;
    boolean drinking = false;
    for (int i = 0; i < n; i++) {
      if (drinking) {
        drink(times[i] - clock);
        // running dry before this moment stops him; running dry exactly now does not
        // matter: a pour lets him go on, and Oleg or fire set the state anyway
        drinking = clock == times[i];
      }
      clock = times[i];
      if (words[i].equals("Oleg")) {
        straw = values[i];
        drinking = true;
      } else if (words[i].equals("fire")) {
        drinking = false;
      } else {
        add(index.get(words[i]), values[i]);
        total += values[i];
      }
    }
    if (drinking) drink(ENDLESS);
    StringBuilder out = new StringBuilder();
    for (long[] s : SIPS)
      out.append(s[0]).append('-').append(s[1]).append(' ').append(names.get((int) s[2]))
          .append('\n');
    System.out.print(out);
  }
}
