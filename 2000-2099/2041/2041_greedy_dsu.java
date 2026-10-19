import java.io.IOException;
import java.util.Arrays;

public class Main {
  static final int FIELDS = 3;
  static final int BUFFER_SIZE = 1 << 16;
  static class Input {
    final byte[] buffer = new byte[BUFFER_SIZE];
    int at, size;
    int read() throws IOException {
      if (at == size) {
        size = System.in.read(buffer);
        at = 0;
        if (size < 0)
          return -1;
      }
      return buffer[at++];
    }
    int next() throws IOException {
      int c;
      do {
        c = read();
      } while (c >= 0 && c <= ' ');
      int value = 0;
      while (c > ' ') {
        value = value * 10 + c - '0';
        c = read();
      }
      return value;
    }
  }
  static class Predecessor {
    final int[] parent, best;
    final byte[] rank;
    Predecessor(int n) {
      parent = new int[n + 1];
      best = new int[n + 1];
      rank = new byte[n + 1];
      for (int i = 0; i <= n; i++) {
        parent[i] = i;
        best[i] = i;
      }
    }
    int find(int x) {
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    }
    void erase(int x) {
      int a = find(x), b = find(x - 1);
      if (rank[a] < rank[b]) {
        int temporary = a;
        a = b;
        b = temporary;
      }
      parent[b] = a;
      best[a] = Math.min(best[a], best[b]);
      if (rank[a] == rank[b])
        rank[a]++;
    }
  }

  static int[] solve(int[][] items) {
    int n = items.length, limit = 0;
    for (int[] item : items) limit = Math.max(limit, item[1]);
    limit++;
    Arrays.sort(items, (a, b) -> {
      int order = Integer.compare(a[0], b[0]);
      if (order != 0)
        return order;
      order = Integer.compare(a[1], b[1]);
      return order != 0 ? order : Integer.compare(a[2], b[2]);
    });
    Predecessor available = new Predecessor(n);
    int[] answer = new int[n];
    for (int step = 0; step < n; step++) {
      int lo = 0, hi = n;
      while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (items[mid][0] < limit)
          lo = mid + 1;
        else
          hi = mid;
      }
      int position = available.best[available.find(lo)];
      if (position == 0)
        return null;
      int[] item = items[position - 1];
      answer[step] = item[2];
      limit = item[1];
      available.erase(position);
    }
    return answer;
  }

  public static void main(String[] args) throws IOException {
    Input input = new Input();
    int n = input.next();
    int[][] items = new int[n][FIELDS];
    for (int i = 0; i < n; i++) {
      items[i][0] = input.next();
      items[i][1] = input.next();
      items[i][2] = i + 1;
    }
    int[] answer = solve(items);
    if (answer == null)
      System.out.println("No");
    else {
      StringBuilder output = new StringBuilder("Yes\n");
      for (int i = 0; i < n; i++) {
        if (i > 0)
          output.append(' ');
        output.append(answer[i]);
      }
      System.out.println(output);
    }
  }
}
