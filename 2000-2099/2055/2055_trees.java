import java.io.BufferedInputStream;
import java.util.Arrays;

public class Main {
  static final int DECIMAL_BASE = 10;
  static class Input {
    final BufferedInputStream stream = new BufferedInputStream(System.in);
    int nextInt() throws Exception {
      int value = 0, symbol;
      do {
        symbol = stream.read();
      } while (symbol <= ' ' && symbol >= 0);
      while (symbol > ' ') {
        value = value * DECIMAL_BASE + symbol - '0';
        symbol = stream.read();
      }
      return value;
    }
  }
  static class Edge implements Comparable<Edge> {
    int weight, first, second, id;
    Edge(int first, int second, int weight, int id) {
      this.first = first;
      this.second = second;
      this.weight = weight;
      this.id = id;
    }
    public int compareTo(Edge other) {
      if (weight != other.weight)
        return Integer.compare(weight, other.weight);
      if (first != other.first)
        return Integer.compare(first, other.first);
      if (second != other.second)
        return Integer.compare(second, other.second);
      return Integer.compare(id, other.id);
    }
  }
  static class DisjointSet {
    final int[] parent;
    DisjointSet(int size) {
      parent = new int[size];
      Arrays.fill(parent, -1);
    }
    int root(int vertex) {
      while (parent[vertex] >= 0) {
        if (parent[parent[vertex]] >= 0)
          parent[vertex] = parent[parent[vertex]];
        vertex = parent[vertex];
      }
      return vertex;
    }
    boolean unite(int first, int second) {
      first = root(first);
      second = root(second);
      if (first == second)
        return false;
      if (parent[first] > parent[second]) {
        int swap = first;
        first = second;
        second = swap;
      }
      parent[first] += parent[second];
      parent[second] = first;
      return true;
    }
  }
  static class LinkCut {
    final int[] left, right, parent, minimum, key, ancestors;
    final boolean[] reverse;
    LinkCut(int vertices, int edges) {
      int size = 2 * vertices;
      left = new int[size];
      right = new int[size];
      parent = new int[size];
      minimum = new int[size];
      key = new int[size];
      ancestors = new int[size];
      reverse = new boolean[size];
      Arrays.fill(key, edges + 1);
      for (int i = 0; i < size; i++) minimum[i] = i;
    }
    boolean auxiliaryRoot(int vertex) {
      int ancestor = parent[vertex];
      return ancestor == 0 || (left[ancestor] != vertex && right[ancestor] != vertex);
    }
    void pull(int vertex) {
      int best = vertex, first = minimum[left[vertex]], second = minimum[right[vertex]];
      if (key[first] < key[best])
        best = first;
      if (key[second] < key[best])
        best = second;
      minimum[vertex] = best;
    }
    void toggle(int vertex) {
      if (vertex != 0) {
        int swap = left[vertex];
        left[vertex] = right[vertex];
        right[vertex] = swap;
        reverse[vertex] = !reverse[vertex];
      }
    }
    void rotate(int vertex) {
      int ancestor = parent[vertex], grandparent = parent[ancestor], child;
      if (left[ancestor] == vertex) {
        child = right[vertex];
        left[ancestor] = child;
        right[vertex] = ancestor;
      } else {
        child = left[vertex];
        right[ancestor] = child;
        left[vertex] = ancestor;
      }
      if (child != 0)
        parent[child] = ancestor;
      if (grandparent != 0) {
        if (left[grandparent] == ancestor)
          left[grandparent] = vertex;
        else if (right[grandparent] == ancestor)
          right[grandparent] = vertex;
      }
      parent[vertex] = grandparent;
      parent[ancestor] = vertex;
      pull(ancestor);
      pull(vertex);
    }
    void splay(int vertex) {
      int size = 0, node = vertex;
      ancestors[size++] = node;
      while (!auxiliaryRoot(node)) {
        node = parent[node];
        ancestors[size++] = node;
      }
      while (size > 0) {
        node = ancestors[--size];
        if (reverse[node]) {
          toggle(left[node]);
          toggle(right[node]);
          reverse[node] = false;
        }
      }
      while (!auxiliaryRoot(vertex)) {
        int ancestor = parent[vertex], grandparent = parent[ancestor];
        if (!auxiliaryRoot(ancestor)) {
          boolean aligned = (left[grandparent] == ancestor) == (left[ancestor] == vertex);
          rotate(aligned ? ancestor : vertex);
        }
        rotate(vertex);
      }
    }
    void access(int vertex) {
      int last = 0;
      for (int node = vertex; node != 0; node = parent[node]) {
        splay(node);
        right[node] = last;
        if (last != 0)
          parent[last] = node;
        pull(node);
        last = node;
      }
      splay(vertex);
    }
    void makeRoot(int vertex) {
      access(vertex);
      toggle(vertex);
    }
    void add(int first, int second, int node, int rank) {
      key[node] = rank;
      makeRoot(first);
      parent[first] = node;
      makeRoot(second);
      parent[second] = node;
    }
    int replaceMinimum(int first, int second, int rank) {
      makeRoot(first);
      access(second);
      int edge = minimum[second];
      splay(edge);
      int old = key[edge];
      toggle(left[edge]);
      toggle(right[edge]);
      key[edge] = rank;
      pull(edge);
      return old;
    }
  }
  static int[] solve(int vertices, Edge[] edges) {
    LinkCut forest = new LinkCut(vertices, edges.length);
    DisjointSet components = new DisjointSet(vertices);
    boolean[] active = new boolean[edges.length];
    int count = 0, lower = 0, bestLeft = 0, bestRight = 0, bestWidth = -1;
    for (int rank = 0; rank < edges.length; rank++) {
      Edge edge = edges[rank];
      if (components.unite(edge.first, edge.second)) {
        count++;
        forest.add(edge.first + 1, edge.second + 1, vertices + count, rank);
      } else
        active[forest.replaceMinimum(edge.first + 1, edge.second + 1, rank)] = false;
      active[rank] = true;
      while (!active[lower]) lower++;
      if (count == vertices - 1) {
        int width = edge.weight - edges[lower].weight;
        if (bestWidth < 0 || width < bestWidth) {
          bestWidth = width;
          bestLeft = lower;
          bestRight = rank;
        }
        if (bestWidth == 0)
          break;
      }
    }
    components = new DisjointSet(vertices);
    int[] chosen = new int[vertices - 1];
    count = 0;
    for (int rank = bestLeft; rank <= bestRight; rank++) {
      Edge edge = edges[rank];
      if (components.unite(edge.first, edge.second)) {
        chosen[count++] = edge.id;
        if (count == vertices - 1)
          break;
      }
    }
    return chosen;
  }
  public static void main(String[] args) throws Exception {
    Input input = new Input();
    int vertices = input.nextInt(), count = input.nextInt();
    Edge[] edges = new Edge[count];
    for (int i = 0; i < count; i++) {
      int first = input.nextInt() - 1, second = input.nextInt() - 1, weight = input.nextInt();
      edges[i] = new Edge(first, second, weight, i + 1);
    }
    Arrays.sort(edges);
    StringBuilder output = new StringBuilder();
    for (int id : solve(vertices, edges)) {
      if (output.length() > 0)
        output.append(' ');
      output.append(id);
    }
    System.out.println(output);
  }
}
