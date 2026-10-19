import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
  private static final int INFINITY_COST = 1000000000;
  private static final int PADDING = 2;

  private static final class Search {
    int[] distance, parent, order;
    int count;
    Search(int size) {
      distance = new int[size];
      parent = new int[size];
      order = new int[size];
      Arrays.fill(distance, -1);
      Arrays.fill(parent, -1);
    }
  }

  private static final class Item implements Comparable<Item> {
    final int cost, vertex;
    Item(int cost, int vertex) {
      this.cost = cost;
      this.vertex = vertex;
    }
    @Override
    public int compareTo(Item other) {
      return Integer.compare(cost, other.cost);
    }
  }

  private static final class Edge {
    final int first, second;
    Edge(int first, int second) {
      this.first = first;
      this.second = second;
    }
  }

  private static final class Interval {
    final int left, right, cost;
    Interval(int left, int right, int cost) {
      this.left = left;
      this.right = right;
      this.cost = cost;
    }
  }

  private static Search bfs(byte[] cells, int[] offsets, int start) {
    Search result = new Search(cells.length);
    result.distance[start] = 0;
    result.order[result.count++] = start;
    for (int head = 0; head < result.count; head++) {
      int vertex = result.order[head];
      for (int offset : offsets) {
        int other = vertex + offset;
        if (cells[other] == '.' && result.distance[other] < 0) {
          result.distance[other] = result.distance[vertex] + 1;
          result.parent[other] = vertex;
          result.order[result.count++] = other;
        }
      }
    }
    return result;
  }

  private static int[] coordinates(int vertex, int stride) {
    return new int[] {vertex / stride - 1, vertex % stride - 1};
  }

  private static int[] solve(String[] grid, int sr, int sc, int tr, int tc) {
    int rows = grid.length, cols = grid[0].length(), stride = cols + PADDING;
    byte[] cells = new byte[(rows + PADDING) * stride];
    for (int row = 0; row < rows; row++)
      for (int col = 0; col < cols; col++)
        cells[(row + 1) * stride + col + 1] = (byte) grid[row].charAt(col);
    int start = (sr + 1) * stride + sc + 1, target = (tr + 1) * stride + tc + 1;
    int[] offsets = {-stride, 1, stride, -1};
    Search first = bfs(cells, offsets, start);
    int[] ds = first.distance;
    if (ds[target] == 1) {
      for (int vertex = 0; vertex < cells.length; vertex++)
        if (cells[vertex] == '.' && vertex != start && vertex != target)
          return coordinates(vertex, stride);
    }
    int[] dt = bfs(cells, offsets, target).distance;
    ArrayList<Integer> path = new ArrayList<>();
    for (int vertex = target; vertex != -1; vertex = first.parent[vertex]) path.add(vertex);
    Collections.reverse(path);
    int length = path.size() - 1;
    int[] position = new int[cells.length], level = new int[cells.length];
    Arrays.fill(position, -1);
    Arrays.fill(level, -1);
    for (int at = 0; at <= length; at++) position[path.get(at)] = at;
    for (int at = 0; at < first.count; at++) {
      int vertex = first.order[at];
      level[vertex] = position[vertex] >= 0 ? position[vertex] : level[first.parent[vertex]];
    }
    ArrayList<Edge> edges = new ArrayList<>();
    int[] detour = new int[cells.length];
    Arrays.fill(detour, INFINITY_COST);
    for (int at = 0; at < first.count; at++) {
      int vertex = first.order[at];
      for (int offset : offsets) {
        int other = vertex + offset;
        if (level[vertex] >= level[other])
          continue;
        edges.add(new Edge(vertex, other));
        if (position[other] < 0)
          detour[other] = Math.min(detour[other], ds[vertex] + 1);
      }
    }
    PriorityQueue<Item> heap = new PriorityQueue<>();
    for (int at = 0; at < first.count; at++) {
      int vertex = first.order[at];
      if (detour[vertex] < INFINITY_COST)
        heap.add(new Item(detour[vertex], vertex));
    }
    while (!heap.isEmpty()) {
      Item current = heap.remove();
      int distance = current.cost, vertex = current.vertex;
      if (distance != detour[vertex])
        continue;
      for (int offset : offsets) {
        int other = vertex + offset;
        if (level[other] == level[vertex] && position[other] < 0 && distance + 1 < detour[other]) {
          detour[other] = distance + 1;
          heap.add(new Item(distance + 1, other));
        }
      }
    }
    int[] answer = new int[length + 1];
    Arrays.fill(answer, INFINITY_COST);
    ArrayList<Interval> intervals = new ArrayList<>();
    for (Edge edge : edges) {
      int x = edge.first, y = edge.second, left = level[x], right = level[y];
      if (left + 1 < right)
        intervals.add(new Interval(left + 1, right - 1, ds[x] + 1 + dt[y]));
      if (position[x] < 0 && 1 <= left && left < length)
        answer[left] = Math.min(answer[left], detour[x] + 1 + dt[y]);
    }
    intervals.sort((a, b) -> Integer.compare(a.left, b.left));
    int at = 0, best = 1;
    for (int failed = 1; failed < length; failed++) {
      while (at < intervals.size() && intervals.get(at).left <= failed) {
        Interval edge = intervals.get(at++);
        heap.add(new Item(edge.cost, edge.right));
      }
      while (!heap.isEmpty() && heap.peek().vertex < failed) heap.remove();
      if (!heap.isEmpty())
        answer[failed] = Math.min(answer[failed], heap.peek().cost);
      if (answer[failed] > answer[best])
        best = failed;
    }
    return coordinates(path.get(best), stride);
  }

  private static String next(BufferedInputStream input) throws IOException {
    int ch;
    do {
      ch = input.read();
    } while (ch <= ' ' && ch != -1);
    StringBuilder token = new StringBuilder();
    while (ch > ' ') {
      token.append((char) ch);
      ch = input.read();
    }
    return token.toString();
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream input = new BufferedInputStream(System.in);
    int rows = Integer.parseInt(next(input));
    Integer.parseInt(next(input));
    int sr = Integer.parseInt(next(input)) - 1, sc = Integer.parseInt(next(input)) - 1;
    int tr = Integer.parseInt(next(input)) - 1, tc = Integer.parseInt(next(input)) - 1;
    String[] grid = new String[rows];
    for (int row = 0; row < rows; row++) grid[row] = next(input);
    int[] answer = solve(grid, sr, sc, tr, tc);
    System.out.println((answer[0] + 1) + " " + (answer[1] + 1));
  }
}
