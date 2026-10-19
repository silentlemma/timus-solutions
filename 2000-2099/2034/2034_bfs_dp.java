import java.io.IOException;
import java.util.Arrays;

public class Main {
  private static final int BUFFER_SIZE = 1 << 16;

  static class Graph {
    final int[] head, to, next;
    Graph(int size, int[] edges) {
      head = new int[size];
      Arrays.fill(head, -1);
      to = new int[edges.length];
      next = new int[edges.length];
      for (int i = 0; i < edges.length; i += 2) {
        int a = edges[i], b = edges[i + 1];
        to[i] = b;
        next[i] = head[a];
        head[a] = i;
        to[i + 1] = a;
        next[i + 1] = head[b];
        head[b] = i + 1;
      }
    }
    int[][] bfs(int source) {
      int[] distance = new int[head.length], order = new int[head.length];
      Arrays.fill(distance, -1);
      distance[source] = 0;
      order[0] = source;
      int used = 1;
      for (int at = 0; at < used; at++) {
        int vertex = order[at];
        for (int edge = head[vertex]; edge != -1; edge = next[edge]) {
          int following = to[edge];
          if (distance[following] < 0) {
            distance[following] = distance[vertex] + 1;
            order[used++] = following;
          }
        }
      }
      return new int[][] {distance, order};
    }
  }

  static int solve(int size, int[] edges, int start, int finish, int origin) {
    Graph graph = new Graph(size, edges);
    int[][] first = graph.bfs(start);
    int[] depth = first[0], order = first[1], clearance = graph.bfs(origin)[0];
    int[] best = new int[size];
    Arrays.fill(best, -1);
    best[start] = clearance[start];
    for (int vertex : order) {
      for (int edge = graph.head[vertex]; edge != -1; edge = graph.next[edge]) {
        int following = graph.to[edge];
        if (depth[following] == depth[vertex] + 1)
          best[following] = Math.max(best[following], Math.min(best[vertex], clearance[following]));
      }
    }
    return best[finish];
  }

  static class FastInput {
    final byte[] buffer = new byte[BUFFER_SIZE];
    int at, length;
    int read() throws IOException {
      if (at == length) {
        length = System.in.read(buffer);
        at = 0;
        if (length < 0)
          return -1;
      }
      return buffer[at++];
    }
    int nextInt() throws IOException {
      int ch = read();
      while (ch >= 0 && ch <= ' ') ch = read();
      if (ch < 0)
        return -1;
      int value = 0;
      while (ch >= '0' && ch <= '9') {
        value = value * 10 + ch - '0';
        ch = read();
      }
      return value;
    }
  }

  public static void main(String[] args) throws IOException {
    FastInput input = new FastInput();
    int size = input.nextInt(), count = input.nextInt();
    if (size < 0)
      return;
    int[] edges = new int[2 * count];
    for (int i = 0; i < edges.length; i++) edges[i] = input.nextInt() - 1;
    int start = input.nextInt() - 1, finish = input.nextInt() - 1, origin = input.nextInt() - 1;
    System.out.println(solve(size, edges, start, finish, origin));
  }
}
