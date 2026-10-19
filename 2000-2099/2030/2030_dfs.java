import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
  private static final int MODULUS = 1000000007;
  private static final int BUFFER_SIZE = 1 << 16;

  static class Network {
    private final int[] direct, broadcast, parent;
    private final int root;

    Network(int[] initial, int[] edges, int start) {
      int size = initial.length;
      root = start;
      direct = initial.clone();
      broadcast = new int[size];
      parent = new int[size];
      Arrays.fill(parent, -1);
      int[] head = new int[size];
      Arrays.fill(head, -1);
      int[] to = new int[edges.length];
      int[] next = new int[edges.length];
      for (int i = 0; i < edges.length; i += 2) {
        int a = edges[i], b = edges[i + 1];
        to[i] = b;
        next[i] = head[a];
        head[a] = i;
        to[i + 1] = a;
        next[i + 1] = head[b];
        head[b] = i + 1;
      }
      int[] order = new int[size];
      int used = 1;
      order[0] = root;
      parent[root] = root;
      for (int at = 0; at < used; at++) {
        int vertex = order[at];
        for (int edge = head[vertex]; edge != -1; edge = next[edge]) {
          int neighbor = to[edge];
          if (parent[neighbor] == -1) {
            parent[neighbor] = vertex;
            order[used++] = neighbor;
          }
        }
      }
    }

    int process(int kind, int vertex) {
      int value = direct[vertex];
      if (vertex != root) {
        value += broadcast[parent[vertex]];
        if (value >= MODULUS)
          value -= MODULUS;
      }
      if (kind == 2)
        return value;
      broadcast[vertex] += value;
      if (broadcast[vertex] >= MODULUS)
        broadcast[vertex] -= MODULUS;
      if (vertex != root) {
        int above = parent[vertex];
        direct[above] += value;
        if (direct[above] >= MODULUS)
          direct[above] -= MODULUS;
      }
      return -1;
    }
  }

  static class FastInput {
    private final byte[] buffer = new byte[BUFFER_SIZE];
    private int at, length;

    private int read() throws IOException {
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
    int size = input.nextInt();
    if (size < 0)
      return;
    int[] initial = new int[size];
    for (int i = 0; i < size; i++) initial[i] = input.nextInt();
    int[] edges = new int[2 * (size - 1)];
    for (int i = 0; i < edges.length; i++) edges[i] = input.nextInt() - 1;
    Network network = new Network(initial, edges, 0);
    int count = input.nextInt();
    BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
    for (int i = 0; i < count; i++) {
      int kind = input.nextInt(), vertex = input.nextInt() - 1;
      int answer = network.process(kind, vertex);
      if (answer >= 0) {
        output.write(Integer.toString(answer));
        output.newLine();
      }
    }
    output.flush();
  }
}
