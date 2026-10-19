import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  private static final int UNREACHED = -2;
  private static final int UNKNOWN = -1;
  private static final int MAX_EDGES = 100000;

  private static int[] solve(int[] values, int[] offsets, int[] edges) {
    int n = values.length;
    int[] entry = new int[n];
    java.util.Arrays.fill(entry, UNREACHED);
    entry[0] = 0;
    int[] pending = new int[2 * n];
    int tail = 1;
    for (int head = 0; head < tail; ++head) {
      int vertex = pending[head];
      int offered = values[vertex] != 0 ? values[vertex] : entry[vertex];
      for (int at = offsets[vertex]; at < offsets[vertex + 1]; ++at) {
        int target = edges[at], old = entry[target];
        int merged = old == UNREACHED ? offered : old == offered ? old : UNKNOWN;
        if (old != merged) {
          entry[target] = merged;
          pending[tail++] = target;
        }
      }
    }
    return entry;
  }

  private static String word(int value) {
    if (value == UNKNOWN)
      return "unknown";
    return value != 0 ? Integer.toString(value) : "sober";
  }

  private static int readInt(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= ' ' && c >= 0);
    int value = 0;
    while (c > ' ') {
      value = value * 10 + c - '0';
      c = in.read();
    }
    return value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int n = readInt(in), used = 0;
    int[] values = new int[n], offsets = new int[n + 1], edges = new int[MAX_EDGES];
    for (int i = 0; i < n; ++i) {
      values[i] = readInt(in);
      int degree = readInt(in);
      for (int j = 0; j < degree; ++j) edges[used++] = readInt(in) - 1;
      offsets[i + 1] = used;
    }
    int[] entry = solve(values, offsets, edges);
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < n; ++i) {
      out.append(word(entry[i])).append(' ');
      out.append(word(values[i] != 0 ? values[i] : entry[i])).append('\n');
    }
    System.out.print(out);
  }
}
