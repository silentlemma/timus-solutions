import java.util.Scanner;

public class Main {
  static class Point {
    final long x, y;
    Point(long x, long y) {
      this.x = x;
      this.y = y;
    }
  }

  static long cross(Point a, Point b, Point c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
  }

  static boolean between(long value, long a, long b) {
    return (a <= value && value <= b) || (b <= value && value <= a);
  }

  static boolean overlap(long a, long b, long c, long d) {
    return Math.max(Math.min(a, b), Math.min(c, d)) <= Math.min(Math.max(a, b), Math.max(c, d));
  }

  static boolean onSegment(Point point, Point a, Point b) {
    return cross(a, b, point) == 0 && between(point.x, a.x, b.x) && between(point.y, a.y, b.y);
  }

  static boolean straddles(long first, long second) {
    return (first <= 0 && second >= 0) || (second <= 0 && first >= 0);
  }

  static boolean intersects(Point a, Point b, Point c, Point d) {
    return overlap(a.x, b.x, c.x, d.x) && overlap(a.y, b.y, c.y, d.y)
        && straddles(cross(a, b, c), cross(a, b, d)) && straddles(cross(c, d, a), cross(c, d, b));
  }

  static class DisjointSets {
    final int[] parent, weights;
    DisjointSets(int size) {
      parent = new int[size];
      weights = new int[size];
      for (int i = 0; i < size; i++) {
        parent[i] = i;
        weights[i] = 1;
      }
    }
    int find(int vertex) {
      while (parent[vertex] != vertex) {
        parent[vertex] = parent[parent[vertex]];
        vertex = parent[vertex];
      }
      return vertex;
    }
    void unite(int first, int second) {
      first = find(first);
      second = find(second);
      if (first == second)
        return;
      if (weights[first] < weights[second]) {
        int temporary = first;
        first = second;
        second = temporary;
      }
      parent[second] = first;
      weights[first] += weights[second];
    }
  }

  static boolean allReachable(Point[] points, int[][] edges) {
    DisjointSets sets = new DisjointSets(points.length);
    for (int[] edge : edges) sets.unite(edge[0], edge[1]);
    for (int i = 0; i < edges.length; i++) {
      int a = edges[i][0], b = edges[i][1];
      for (int j = 0; j < i; j++) {
        int c = edges[j][0], d = edges[j][1];
        if (intersects(points[a], points[b], points[c], points[d]))
          sets.unite(a, c);
      }
      for (int vertex = 0; vertex < points.length; vertex++) {
        if (onSegment(points[vertex], points[a], points[b]))
          sets.unite(a, vertex);
      }
    }
    int root = sets.find(0);
    for (int vertex = 0; vertex < points.length; vertex++) {
      if (sets.find(vertex) != root)
        return false;
    }
    return true;
  }

  public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
      int size = input.nextInt(), count = input.nextInt();
      Point[] points = new Point[size];
      for (int i = 0; i < size; i++) points[i] = new Point(input.nextLong(), input.nextLong());
      int[][] edges = new int[count][2];
      for (int[] edge : edges) {
        edge[0] = input.nextInt() - 1;
        edge[1] = input.nextInt() - 1;
      }
      System.out.println(allReachable(points, edges) ? "YES" : "NO");
    }
  }
}
