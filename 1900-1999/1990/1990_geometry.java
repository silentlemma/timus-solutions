import java.util.Arrays;
import java.util.Locale;

public class Main {
  static final int BUFFER = 1 << 16; // bytes read from the input at a time
  private static final int INITIAL_GROUP_CAPACITY = 16;
  private static final class Reader {
    final byte[] buffer = new byte[BUFFER];
    int position, length;
    int next() throws Exception {
      if (position == length) {
        length = System.in.read(buffer);
        position = 0;
        if (length < 0)
          return -1;
      }
      return buffer[position++];
    }
    long number() throws Exception {
      int value;
      do {
        value = next();
      } while (value >= 0 && value <= 32);
      long sign = 1;
      if (value == '-') {
        sign = -1;
        value = next();
      }
      long result = 0;
      while (value > 32) {
        result = result * 10 + value - '0';
        value = next();
      }
      return result * sign;
    }
    long[][] wall() throws Exception {
      int count = (int) number();
      long[][] result = new long[count][2];
      for (long[] p : result) {
        p[0] = number();
        p[1] = number();
      }
      return result;
    }
  }
  private static double vertexClearance(long[][] vertices, long[][] other, long sign) {
    double result = Double.POSITIVE_INFINITY;
    int index = 0;
    for (long[] p : vertices) {
      while (index + 1 < other.length && other[index + 1][1] <= p[1]) ++index;
      double gap;
      if (index + 1 == other.length)
        gap = sign * (other[index][0] - p[0]);
      else {
        long[] a = other[index], b = other[index + 1];
        long numerator = (a[0] - p[0]) * (b[1] - p[1]) + (b[0] - p[0]) * (p[1] - a[1]);
        gap = (double) (sign * numerator) / (b[1] - a[1]);
      }
      result = Math.min(result, gap);
    }
    return result;
  }
  private static final class WallCursor {
    final long[][] vertices;
    int index;
    long numerator, denominator;
    WallCursor(long[][] wall) {
      vertices = wall;
    }
    void at(long y) {
      while (index + 1 < vertices.length && vertices[index + 1][1] <= y) ++index;
      if (index + 1 == vertices.length) {
        numerator = vertices[index][0];
        denominator = 1;
      } else {
        long[] a = vertices[index], b = vertices[index + 1];
        numerator = a[0] * (b[1] - y) + b[0] * (y - a[1]);
        denominator = b[1] - a[1];
      }
    }
  }
  private static void siftDown(long[] values, int count, int root) {
    long value = values[root];
    int child = 2 * root + 1;
    while (child < count) {
      if (child + 1 < count && values[child] < values[child + 1])
        ++child;
      if (value >= values[child])
        break;
      values[root] = values[child];
      root = child;
      child = 2 * root + 1;
    }
    values[root] = value;
  }
  private static void sortGroup(long[] values, int count) {
    for (int root = count / 2 - 1; root >= 0; --root) siftDown(values, count, root);
    for (int end = count - 1; end > 0; --end) {
      long value = values[0];
      values[0] = values[end];
      values[end] = value;
      siftDown(values, end, 0);
    }
  }
  private static double process(
      long y, long[] group, int count, WallCursor left, WallCursor right, double answer) {
    if (y < left.vertices[0][1] || y > left.vertices[left.vertices.length - 1][1])
      return answer;
    left.at(y);
    right.at(y);
    sortGroup(group, count);
    boolean found = false;
    long previous = 0;
    double best = 0;
    for (int i = 0; i < count; ++i) {
      long x = group[i];
      if (x * left.denominator < left.numerator || x * right.denominator > right.numerator)
        continue;
      double gap = found ? x - previous
                         : (double) (x * left.denominator - left.numerator) / left.denominator;
      best = Math.max(best, gap);
      previous = x;
      found = true;
    }
    if (found) {
      best = Math.max(
          best, (double) (right.numerator - previous * right.denominator) / right.denominator);
      answer = Math.min(answer, best);
    }
    return answer;
  }
  public static void main(String[] args) throws Exception {
    Reader input = new Reader();
    long[][] left = input.wall(), right = input.wall();
    double answer = Math.min(vertexClearance(left, right, 1), vertexClearance(right, left, -1));
    WallCursor first = new WallCursor(left), second = new WallCursor(right);
    int count = (int) input.number(), used = 0;
    long[] group = new long[INITIAL_GROUP_CAPACITY];
    long currentY = 0;
    for (int i = 0; i < count; ++i) {
      long x = input.number(), y = input.number();
      if (used > 0 && y != currentY) {
        answer = process(currentY, group, used, first, second, answer);
        used = 0;
      }
      if (used == group.length)
        group = Arrays.copyOf(group, 2 * group.length);
      currentY = y;
      group[used++] = x;
    }
    if (used > 0)
      answer = process(currentY, group, used, first, second, answer);
    System.out.printf(Locale.US, "%.12f%n", answer);
  }
}
