import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class Main {
  private static final long SEED = 31337;
  private static final int BUFFER = 1 << 16;
  private static final DataInputStream IN = new DataInputStream(System.in);
  private static final byte[] BUF = new byte[BUFFER];
  private static int len;
  private static int ptr;

  private static int read() throws IOException {
    if (ptr == len) {
      len = IN.read(BUF, 0, BUFFER);
      ptr = 0;
      if (len <= 0) return -1;
    }
    return BUF[ptr++];
  }

  private static int nextInt() throws IOException {
    int c = read();
    while (c < '0') c = read();
    int r = 0;
    for (; c >= '0'; c = read()) r = r * 10 + c - '0';
    return r;
  }

  public static void main(String[] args) throws IOException {
    int n = nextInt();
    int m = nextInt();
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
    for (int i = 0; i < n - 1; i++) {
      int u = nextInt() - 1;
      int v = nextInt() - 1;
      adj.get(u).add(v);
      adj.get(v).add(u);
    }
    // every technology gets a random weight; a path uses each one exactly once
    // when (with overwhelming probability) its weights add up to the sum of all
    Random rng = new Random(SEED);
    long[] weight = new long[m + 1];
    long goal = 0;
    for (int t = 1; t <= m; t++) goal += weight[t] = rng.nextLong();
    long[] own = new long[n];
    for (int v = 0; v < n; v++) for (int a = nextInt(); a > 0; a--) own[v] += weight[nextInt()];
    // depth[v]: the weights on the path from the root to v
    int[] parent = new int[n];
    int[] order = new int[n];
    long[] depth = new long[n];
    parent[0] = -1;
    depth[0] = own[0];
    int size = 1;
    for (int k = 0; k < size; k++) {
      int v = order[k];
      for (int u : adj.get(v)) {
        if (u == parent[v]) continue;
        parent[u] = v;
        depth[u] = depth[v] + own[u];
        order[size++] = u;
      }
    }
    // small to large: below[v] maps depth -> a vertex of the subtree of v; two
    // vertices from different children of x (or x itself) join through x
    List<Map<Long, Integer>> below = new ArrayList<>();
    for (int i = 0; i < n; i++) below.add(null);
    for (int k = n - 1; k >= 0; k--) {
      int x = order[k];
      if (own[x] == goal) {
        System.out.println((x + 1) + " " + (x + 1));
        return;
      }
      Map<Long, Integer> mine = new HashMap<>();
      mine.put(depth[x], x);
      long target = goal + 2 * depth[x] - own[x];
      for (int y : adj.get(x)) {
        if (y == parent[x]) continue;
        Map<Long, Integer> other = below.get(y);
        below.set(y, null);
        if (other.size() > mine.size()) {
          Map<Long, Integer> t = mine;
          mine = other;
          other = t;
        }
        for (Map.Entry<Long, Integer> e : other.entrySet()) {
          Integer v = mine.get(target - e.getKey());
          if (v != null) {
            System.out.println((e.getValue() + 1) + " " + (v + 1));
            return;
          }
        }
        mine.putAll(other);
      }
      below.set(x, mine);
    }
    System.out.println("No solution");
  }
}
