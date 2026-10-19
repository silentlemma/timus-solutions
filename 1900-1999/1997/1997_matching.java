import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
  static final int DECIMAL_BASE = 10;
  static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

  static int next() throws IOException {
    int ch;
    do {
      ch = INPUT.read();
    } while (ch <= ' ' && ch >= 0);
    int value = 0;
    while (ch > ' ') {
      value = value * DECIMAL_BASE + ch - '0';
      ch = INPUT.read();
    }
    return value;
  }

  static class Matcher {
    int[][] edges;
    int[] left, right, distance, cursor, queue;
    int count, shortest;

    Matcher(int[][] graph) {
      edges = graph;
      count = graph.length;
      left = new int[count];
      right = new int[count];
      distance = new int[count];
      cursor = new int[count];
      queue = new int[count];
      Arrays.fill(left, -1);
      Arrays.fill(right, -1);
    }

    boolean layer() {
      Arrays.fill(distance, -1);
      Arrays.fill(cursor, 0);
      shortest = count + 1;
      int head = 0, tail = 0;
      for (int u = 0; u < count; u++)
        if (left[u] < 0) {
          distance[u] = 0;
          queue[tail++] = u;
        }
      while (head < tail) {
        int u = queue[head++];
        if (distance[u] >= shortest)
          continue;
        for (int v : edges[u]) {
          int mate = right[v];
          if (mate < 0)
            shortest = distance[u] + 1;
          else if (distance[mate] < 0) {
            distance[mate] = distance[u] + 1;
            queue[tail++] = mate;
          }
        }
      }
      return shortest <= count;
    }

    boolean augment(int u) {
      while (cursor[u] < edges[u].length) {
        int v = edges[u][cursor[u]++], mate = right[v];
        if ((mate < 0 && distance[u] + 1 == shortest)
            || (mate >= 0 && distance[mate] == distance[u] + 1 && augment(mate))) {
          left[u] = v;
          right[v] = u;
          return true;
        }
      }
      distance[u] = -1;
      return false;
    }
  }

  static int[][] solve(int a, int b, int[][] records) {
    int[] entries = new int[records.length], exits = new int[records.length];
    int count = 0, outCount = 0;
    for (int[] record : records) {
      if (record[1] == 0)
        entries[count++] = record[0];
      else
        exits[outCount++] = record[0];
    }
    if (count != outCount)
      return null;
    int[][] edges = new int[count][];
    int[] buffer = new int[count];
    for (int u = 0; u < count; u++) {
      int length = 0;
      for (int v = 0; v < count; v++) {
        int duration = exits[v] - entries[u];
        if (duration > 0 && (duration <= b || duration >= a))
          buffer[length++] = v;
      }
      edges[u] = Arrays.copyOf(buffer, length);
    }
    Matcher h = new Matcher(edges);
    int total = 0;
    while (h.layer())
      for (int u = 0; u < count; u++)
        if (h.left[u] < 0 && h.augment(u))
          total++;
    if (total != count)
      return null;
    int[][] answer = new int[count][2];
    for (int u = 0; u < count; u++) {
      answer[u][0] = entries[u];
      answer[u][1] = exits[h.left[u]];
    }
    return answer;
  }

  public static void main(String[] args) throws IOException {
    int a = next(), b = next(), n = next();
    int[][] records = new int[n][2];
    for (int i = 0; i < n; i++) {
      records[i][0] = next();
      records[i][1] = next();
    }
    int[][] answer = solve(a, b, records);
    if (answer == null)
      System.out.println("Liar");
    else {
      StringBuilder output = new StringBuilder("No reason\n");
      for (int[] pair : answer) output.append(pair[0]).append(' ').append(pair[1]).append('\n');
      System.out.print(output);
    }
  }
}
