import java.io.DataInputStream;
import java.io.IOException;

public class Main {
  private static final int BUFFER_SIZE = 1 << 16;
  private static DataInputStream in = new DataInputStream(System.in);
  private static byte[] buffer = new byte[BUFFER_SIZE];
  private static int length = 0;
  private static int pointer = 0;

  private static int read() throws IOException {
    if (pointer == length) {
      length = in.read(buffer, 0, buffer.length);
      pointer = 0;
      if (length <= 0) {
        return -1;
      }
    }
    return buffer[pointer++];
  }

  private static int nextInt() throws IOException {
    int c = read();
    while (c < '0') {
      c = read();
    }
    int value = 0;
    while (c >= '0') {
      value = value * 10 + (c - '0');
      c = read();
    }
    return value;
  }

  public static void main(String[] args) throws IOException {
    int n = nextInt();
    int m = nextInt();
    int q = nextInt();
    int[] from = new int[m];
    int[] to = new int[m];
    long[] s = new long[m];
    long[] w = new long[m];
    int size = n;
    for (int i = 0; i < m; i++) {
      from[i] = nextInt();
      to[i] = nextInt();
      s[i] = nextInt();
      w[i] = nextInt();
      size = Math.max(size, Math.max(from[i], to[i]));
    }
    // Edges leaving each glade, stored contiguously by their start.
    int[] start = new int[size + 2];
    int[] indegree = new int[size + 1];
    for (int i = 0; i < m; i++) {
      start[from[i] + 1]++;
      indegree[to[i]]++;
    }
    for (int v = 1; v <= size + 1; v++) {
      start[v] += start[v - 1];
    }
    int[] fill = start.clone();
    int[] byStart = new int[m];
    for (int i = 0; i < m; i++) {
      byStart[fill[from[i]]++] = i;
    }

    // The best route maximizes its smallest ratio s / w, stored as a
    // numerator and denominator; 1 / 0 stands for the empty route at 1.
    long[] num = new long[size + 1];
    long[] den = new long[size + 1];
    boolean[] reached = new boolean[size + 1];
    reached[1] = true;
    num[1] = 1;
    int[] order = new int[size];
    int tail = 0;
    for (int v = 1; v <= size; v++) {
      if (indegree[v] == 0) {
        order[tail++] = v;
      }
    }
    for (int head = 0; head < tail; head++) {
      int u = order[head];
      for (int k = start[u]; k < start[u + 1]; k++) {
        int e = byStart[k];
        int v = to[e];
        if (--indegree[v] == 0) {
          order[tail++] = v;
        }
        if (!reached[u]) {
          continue;
        }
        long a = num[u];
        long b = den[u];
        if (s[e] * b < a * w[e]) {
          a = s[e];
          b = w[e];
        }
        if (!reached[v] || num[v] * b < a * den[v]) {
          reached[v] = true;
          num[v] = a;
          den[v] = b;
        }
      }
    }

    StringBuilder out = new StringBuilder();
    for (int i = 0; i < q; i++) {
      long priceS = nextInt();
      long priceW = nextInt();
      boolean good = reached[n] && priceS * num[n] > priceW * den[n];
      out.append(good ? "YES\n" : "NO\n");
    }
    System.out.print(out);
  }
}
