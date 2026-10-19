import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;

public class Main {
  private static final int BUF_SIZE = 1 << 16;
  private static final DataInputStream IN = new DataInputStream(System.in);
  private static final byte[] BUF = new byte[BUF_SIZE];
  private static int bufLen;
  private static int bufPos;

  private static int readByte() throws IOException {
    if (bufPos == bufLen) {
      bufLen = IN.read(BUF, 0, BUF_SIZE);
      bufPos = 0;
      if (bufLen <= 0) return -1;
    }
    return BUF[bufPos++];
  }

  private static int readToken() throws IOException {
    int c = readByte();
    while (c == ' ' || c == '\n' || c == '\r') c = readByte();
    return c;
  }

  private static long readLong() throws IOException {
    int c = readToken();
    long x = 0;
    while (c >= '0' && c <= '9') {
      x = x * 10 + (c - '0');
      c = readByte();
    }
    return x;
  }

  private static int n;
  private static int[] tin;
  private static int[] order;
  private static int[] lg;
  private static int[][] table;
  private static long[] depth;
  private static int[] fen;

  // The LCA of u != v is the parent with the smallest preorder number among the
  // vertices in the preorder range (tin[u], tin[v]].
  private static long dist(int u, int v) {
    if (u == v) return 0;
    int lo = Math.min(tin[u], tin[v]) + 1;
    int hi = Math.max(tin[u], tin[v]);
    int k = lg[hi - lo + 1];
    int x = Math.min(table[k][lo], table[k][hi - (1 << k) + 1]);
    return depth[u] + depth[v] - 2 * depth[order[x]];
  }

  private static int kth(int k) {
    int p = 0;
    for (int step = 1 << lg[n]; step > 0; step >>= 1) {
      if (p + step <= n && fen[p + step] < k) {
        p += step;
        k -= fen[p];
      }
    }
    return order[p];
  }

  private static void add(int p, int d) {
    for (int i = p + 1; i <= n; i += i & -i) fen[i] += d;
  }

  public static void main(String[] args) throws IOException {
    n = (int) readLong();
    int[] head = new int[n + 1];
    java.util.Arrays.fill(head, -1);
    int[] nxt = new int[2 * n];
    int[] to = new int[2 * n];
    long[] wt = new long[2 * n];
    for (int e = 0; e < 2 * (n - 1); e += 2) {
      int u = (int) readLong();
      int v = (int) readLong();
      long w = readLong();
      to[e] = v;
      wt[e] = w;
      nxt[e] = head[u];
      head[u] = e;
      to[e + 1] = u;
      wt[e + 1] = w;
      nxt[e + 1] = head[v];
      head[v] = e + 1;
    }

    tin = new int[n + 1];
    int[] parent = new int[n + 1];
    depth = new long[n + 1];
    order = new int[n];
    int visited = 0;
    parent[1] = 1;
    int[] stack = new int[n];
    int sp = 0;
    stack[sp++] = 1;
    while (sp > 0) {
      int v = stack[--sp];
      tin[v] = visited;
      order[visited++] = v;
      for (int e = head[v]; e >= 0; e = nxt[e]) {
        int u = to[e];
        if (u != parent[v]) {
          parent[u] = v;
          depth[u] = depth[v] + wt[e];
          stack[sp++] = u;
        }
      }
    }

    lg = new int[n + 1];
    for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
    table = new int[lg[n] + 1][];
    table[0] = new int[n];
    for (int i = 0; i < n; i++) table[0][i] = tin[parent[order[i]]];
    for (int k = 1; k <= lg[n]; k++) {
      int[] prev = table[k - 1];
      int half = 1 << (k - 1);
      int[] row = new int[n - (1 << k) + 1];
      for (int i = 0; i < row.length; i++) row[i] = Math.min(prev[i], prev[i + half]);
      table[k] = row;
    }
    fen = new int[n + 1];

    int q = (int) readLong();
    int total = 0;
    long doubled = 0; // the sum of distances around the marked vertices in preorder
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < q; i++) {
      boolean adding = readToken() == '+';
      int v = (int) readLong();
      int p = tin[v];
      if (!adding) {
        add(p, -1);
        total--;
      }
      if (total > 0) {
        int before = 0;
        for (int j = p; j > 0; j -= j & -j) before += fen[j];
        int a = kth(before > 0 ? before : total);
        int b = kth(before < total ? before + 1 : 1);
        long change = dist(a, v) + dist(v, b) - dist(a, b);
        doubled += adding ? change : -change;
      }
      if (adding) {
        add(p, 1);
        total++;
      }
      out.append(doubled / 2).append('\n');
    }
    PrintWriter writer = new PrintWriter(System.out);
    writer.print(out);
    writer.flush();
  }
}
