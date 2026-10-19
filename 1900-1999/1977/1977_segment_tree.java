import java.io.*;
import java.util.Arrays;

public class Main {
  static final double HALF = 0.5;
  static final int BOUNDARIES_PER_EVENT = 3;
  static final int BUFFER_SIZE = 1 << 16;
  static final int STACK_CAPACITY = 128;
  static final int MANTISSA_DIGITS = 9;
  static final double MANTISSA_SCALE = 1e9;

  static class Input {
    final InputStream stream = System.in;
    final byte[] buffer = new byte[BUFFER_SIZE];
    int at, size;
    int read() throws IOException {
      if (at == size) {
        size = stream.read(buffer);
        at = 0;
        if (size < 0)
          return -1;
      }
      return buffer[at++];
    }
    int number() throws IOException {
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
    boolean enforce() throws IOException {
      int c;
      do {
        c = read();
      } while (c >= 0 && c <= ' ');
      boolean result = c == 'e';
      while (c > ' ') c = read();
      return result;
    }
  }

  static class EnergyTree {
    final int[] xs;
    final int[] stackNode = new int[STACK_CAPACITY];
    final int[] stackLeft = new int[STACK_CAPACITY];
    final int[] stackRight = new int[STACK_CAPACITY];
    int top;
    void queue(int node, int left, int right) {
      stackNode[top] = node;
      stackLeft[top] = left;
      stackRight[top++] = right;
    }
    final double[] total, low, high;
    final boolean[] cleared;
    EnergyTree(int[] coordinates, int count) {
      xs = coordinates;
      int nodes = 2 * (count - 1) - 1;
      total = new double[nodes];
      low = new double[nodes];
      high = new double[nodes];
      cleared = new boolean[nodes];
    }
    void apply(int node, int length, double first, double last) {
      total[node] += (first + last) * HALF * length;
      low[node] += first;
      high[node] += last;
    }
    void push(int node, int left, int middle, int right) {
      int child = node + 1, other = node + 2 * (middle - left);
      if (cleared[node]) {
        total[child] = low[child] = high[child] = 0;
        total[other] = low[other] = high[other] = 0;
        cleared[child] = cleared[other] = true;
        cleared[node] = false;
      }
      double first = low[node], last = high[node];
      if (first == 0 && last == 0)
        return;
      int length = xs[right] - xs[left], a = xs[middle] - xs[left], b = length - a;
      if (first == last) {
        apply(child, a, first, first);
        apply(other, b, first, first);
      } else {
        double denominator = length - 1;
        double leftLast = (first * b + last * (a - 1)) / denominator;
        double rightFirst = (first * (b - 1) + last * a) / denominator;
        apply(child, a, first, leftLast);
        apply(other, b, rightFirst, last);
      }
      low[node] = high[node] = 0;
    }
    void add(int node, int left, int right, int begin, int end, int origin, int direction,
        double scale) {
      top = 0;
      queue(node, left, right);
      while (top > 0) {
        --top;
        node = stackNode[top];
        left = stackLeft[top];
        right = stackRight[top];
        int middle = (left + right) / 2;
        if (node < 0) {
          node = ~node;
          total[node] = total[node + 1] + total[node + 2 * (middle - left)];
          continue;
        }
        if (begin <= left && right <= end) {
          double first = scale * (origin + direction * xs[left]);
          double last = scale * (origin + direction * (xs[right] - 1));
          apply(node, xs[right] - xs[left], first, last);
          continue;
        }
        push(node, left, middle, right);
        queue(~node, left, right);
        if (end > middle)
          queue(node + 2 * (middle - left), middle, right);
        if (begin < middle)
          queue(node + 1, left, middle);
      }
    }
    double take(int node, int left, int right, int begin, int end) {
      top = 0;
      queue(node, left, right);
      double answer = 0;
      while (top > 0) {
        --top;
        node = stackNode[top];
        left = stackLeft[top];
        right = stackRight[top];
        int middle = (left + right) / 2;
        if (node < 0) {
          node = ~node;
          total[node] = total[node + 1] + total[node + 2 * (middle - left)];
          continue;
        }
        if (begin <= left && right <= end) {
          answer += total[node];
          total[node] = low[node] = high[node] = 0;
          cleared[node] = true;
          continue;
        }
        push(node, left, middle, right);
        queue(~node, left, right);
        if (end > middle)
          queue(node + 2 * (middle - left), middle, right);
        if (begin < middle)
          queue(node + 1, left, middle);
      }
      return answer;
    }
  }

  static int index(int[] xs, int count, int value) {
    return Arrays.binarySearch(xs, 0, count, value);
  }
  static void solve(Input in, BufferedWriter out) throws IOException {
    int length = in.number(), rate = in.number(), count = in.number();
    int[] times = new int[count], first = new int[count], second = new int[count];
    boolean[] enforce = new boolean[count];
    int[] xs = new int[BOUNDARIES_PER_EVENT * count + 2];
    xs[0] = 1;
    xs[1] = length + 1;
    int used = 2;
    for (int j = 0; j < count; j++) {
      times[j] = in.number();
      enforce[j] = in.enforce();
      first[j] = in.number();
      second[j] = in.number();
      if (enforce[j]) {
        xs[used++] = first[j] - second[j] + 1;
        xs[used++] = first[j] + 1;
        xs[used++] = first[j] + second[j];
      } else {
        xs[used++] = first[j];
        xs[used++] = second[j] + 1;
      }
    }
    Arrays.sort(xs, 0, used);
    int unique = 0;
    for (int j = 0; j < used; j++) {
      if (unique == 0 || xs[unique - 1] != xs[j])
        xs[unique++] = xs[j];
    }
    EnergyTree tree = new EnergyTree(xs, unique);
    int leaves = unique - 1, previous = 0;
    double reserve = 0;
    StringBuilder text = new StringBuilder(BUFFER_SIZE);
    char[] chars = new char[BUFFER_SIZE];
    for (int j = 0; j < count; j++) {
      double growth = (double) rate * (times[j] - previous);
      if (growth != 0)
        tree.apply(0, length, growth, growth);
      previous = times[j];
      if (enforce[j]) {
        if (reserve == 0)
          continue;
        int begin = first[j] - second[j] + 1, middle = first[j] + 1;
        int end = first[j] + second[j];
        int a = index(xs, unique, begin), b = index(xs, unique, middle);
        int c = index(xs, unique, end);
        double scale = reserve / ((double) second[j] * second[j]);
        tree.add(0, 0, leaves, a, b, 1 - begin, 1, scale);
        if (b < c)
          tree.add(0, 0, leaves, b, c, end, -1, scale);
        reserve = 0;
      } else {
        reserve +=
            tree.take(0, 0, leaves, index(xs, unique, first[j]), index(xs, unique, second[j] + 1));
        if (reserve == 0) {
          text.append('0');
        } else {
          int exponent = (int) Math.floor(Math.log10(reserve));
          long mantissa = Math.round(reserve / Math.pow(10, exponent) * MANTISSA_SCALE);
          text.append(mantissa).append('e').append(exponent - MANTISSA_DIGITS);
        }
        text.append('\n');
        if (text.length() > BUFFER_SIZE / 2) {
          text.getChars(0, text.length(), chars, 0);
          out.write(chars, 0, text.length());
          text.setLength(0);
        }
      }
    }
    text.getChars(0, text.length(), chars, 0);
    out.write(chars, 0, text.length());
  }
  public static void main(String[] args) throws IOException {
    Input in = new Input();
    BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
    solve(in, out);
    out.flush();
  }
}
