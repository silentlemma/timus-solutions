import java.io.IOException;
import java.util.Arrays;

public class Main {
  private static final int BUFFER_BITS = 16;
  private static final class FastInput {
    private final byte[] data = new byte[1 << BUFFER_BITS];
    private int at, size;
    private int read() throws IOException {
      if (at >= size) {
        size = System.in.read(data);
        at = 0;
        if (size <= 0)
          return -1;
      }
      return data[at++];
    }
    int nextInt() throws IOException {
      int c;
      do {
        c = read();
      } while (c >= 0 && c <= ' ');
      if (c < 0)
        return -1;
      int value = 0;
      while (c > ' ') {
        value = value * 10 + c - '0';
        c = read();
      }
      return value;
    }
  }

  private static long solve(long[][] cost, int[] plants) {
    int n = cost.length;
    long[] best = new long[n];
    Arrays.fill(best, Long.MAX_VALUE);
    boolean[] used = new boolean[n];
    for (int v : plants) best[v] = 0;
    long answer = 0;
    for (int step = 0; step < n; step++) {
      int vertex = -1;
      for (int v = 0; v < n; v++)
        if (!used[v] && (vertex < 0 || best[v] < best[vertex]))
          vertex = v;
      answer += best[vertex];
      used[vertex] = true;
      for (int v = 0; v < n; v++)
        if (!used[v] && cost[vertex][v] < best[v])
          best[v] = cost[vertex][v];
    }
    return answer;
  }

  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = in.nextInt();
    if (n < 0)
      return;
    int k = in.nextInt();
    int[] plants = new int[k];
    for (int i = 0; i < k; i++) plants[i] = in.nextInt() - 1;
    long[][] cost = new long[n][n];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) cost[i][j] = in.nextInt();
    System.out.println(solve(cost, plants));
  }
}
