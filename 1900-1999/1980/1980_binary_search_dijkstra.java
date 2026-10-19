import java.io.IOException;
import java.util.Arrays;

public class Main {
  private static final int SEARCH_STEPS = 60;
  private static final double SAFETY_MARGIN = 1e-8;
  private static final int BUFFER_BITS = 16;

  private static final class FastInput {
    private final byte[] data = new byte[1 << BUFFER_BITS];
    private int at, size;
    private int read() throws IOException {
      if (at == size) {
        size = System.in.read(data);
        at = 0;
        if (size < 0)
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

  private static final class Solver {
    private final int n;
    private final int[] a, b, speed, length, head, to, road, next, parent, heapVertex;
    private final double[] cost, distance, heapTime;
    private final double deadline;
    private int arc, heapSize, poppedVertex;
    private double poppedTime;

    Solver(int n, int m, int[] a, int[] b, int[] speed, int[] length, double deadline) {
      this.n = n;
      this.a = a;
      this.b = b;
      this.speed = speed;
      this.length = length;
      this.deadline = deadline;
      head = new int[n];
      Arrays.fill(head, -1);
      to = new int[2 * m];
      road = new int[2 * m];
      next = new int[2 * m];
      parent = new int[n];
      distance = new double[n];
      cost = new double[m];
      heapTime = new double[2 * m + 1];
      heapVertex = new int[2 * m + 1];
      for (int i = 0; i < m; i++) {
        add(a[i], b[i], i);
        add(b[i], a[i], i);
      }
    }

    private void add(int from, int target, int id) {
      to[arc] = target;
      road[arc] = id;
      next[arc] = head[from];
      head[from] = arc++;
    }

    private void push(double time, int vertex) {
      int at = heapSize++;
      while (at > 0) {
        int p = (at - 1) / 2;
        if (heapTime[p] <= time)
          break;
        heapTime[at] = heapTime[p];
        heapVertex[at] = heapVertex[p];
        at = p;
      }
      heapTime[at] = time;
      heapVertex[at] = vertex;
    }

    private void pop() {
      poppedTime = heapTime[0];
      poppedVertex = heapVertex[0];
      --heapSize;
      if (heapSize == 0)
        return;
      double time = heapTime[heapSize];
      int vertex = heapVertex[heapSize];
      int at = 0;
      while (2 * at + 1 < heapSize) {
        int child = 2 * at + 1;
        if (child + 1 < heapSize && heapTime[child + 1] < heapTime[child])
          child++;
        if (heapTime[child] >= time)
          break;
        heapTime[at] = heapTime[child];
        heapVertex[at] = heapVertex[child];
        at = child;
      }
      heapTime[at] = time;
      heapVertex[at] = vertex;
    }

    private boolean shortest(double extra) {
      for (int i = 0; i < cost.length; i++) cost[i] = length[i] / (speed[i] + extra);
      Arrays.fill(distance, Double.POSITIVE_INFINITY);
      Arrays.fill(parent, -1);
      distance[0] = 0;
      heapSize = 0;
      push(0, 0);
      while (heapSize > 0) {
        pop();
        double time = poppedTime;
        int vertex = poppedVertex;
        if (time != distance[vertex])
          continue;
        if (vertex == n - 1)
          return true;
        for (int at = head[vertex]; at >= 0; at = next[at]) {
          int neighbor = to[at], id = road[at];
          double candidate = time + cost[id];
          if (candidate <= deadline && candidate < distance[neighbor]) {
            distance[neighbor] = candidate;
            parent[neighbor] = id;
            push(candidate, neighbor);
          }
        }
      }
      return false;
    }

    void writeAnswer(StringBuilder out) {
      double low = 0, high = 0;
      if (!shortest(0)) {
        int total = 0;
        for (int value : length) total += value;
        high = total / deadline;
        for (int step = 0; step < SEARCH_STEPS; step++) {
          double middle = (low + high) / 2;
          if (middle == low || middle == high)
            break;
          if (shortest(middle))
            high = middle;
          else
            low = middle;
        }
        shortest(high);
      }
      double extra = high + SAFETY_MARGIN * Math.max(1, high);
      int[] path = new int[n];
      int used = 0;
      for (int vertex = n - 1; vertex != 0;) {
        int id = parent[vertex];
        path[used++] = id + 1;
        vertex = a[id] ^ b[id] ^ vertex;
      }
      out.append(extra).append(' ').append(used).append('\n');
      for (int i = used - 1; i >= 0; i--) {
        if (i != used - 1)
          out.append(' ');
        out.append(path[i]);
      }
      out.append('\n');
    }
  }

  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = in.nextInt();
    if (n < 0)
      return;
    int m = in.nextInt();
    int[] a = new int[m], b = new int[m], speed = new int[m], length = new int[m];
    for (int i = 0; i < m; i++) {
      a[i] = in.nextInt() - 1;
      b[i] = in.nextInt() - 1;
      speed[i] = in.nextInt();
      length[i] = in.nextInt();
    }
    int deadline = in.nextInt();
    Solver solver = new Solver(n, m, a, b, speed, length, deadline);
    StringBuilder out = new StringBuilder();
    solver.writeAnswer(out);
    System.out.print(out);
  }
}
