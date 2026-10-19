import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Locale;

public class Main {
  static class Direction implements Comparable<Direction> {
    double key;
    long x, y;
    int other;
    public int compareTo(Direction b) {
      return Double.compare(key, b.key);
    }
  }

  static double minimumDistance(long[] x, long[] y) {
    double best = Double.POSITIVE_INFINITY;
    Direction[] directions = new Direction[x.length];
    for (int i = 0; i < directions.length; i++) directions[i] = new Direction();
    for (int pivot = 0; pivot + 1 < x.length; pivot++) {
      int count = 0;
      long totalX = 0, totalY = 0;
      for (int other = 0; other < x.length; other++) {
        long dx = x[other] - x[pivot], dy = y[other] - y[pivot];
        if (dx == 0 && dy == 0)
          continue;
        if (dy < 0 || (dy == 0 && dx < 0)) {
          dx = -dx;
          dy = -dy;
        }
        Direction d = directions[count++];
        d.key = -(double) dx / (Math.abs(dx) + dy);
        d.x = dx;
        d.y = dy;
        d.other = other;
        totalX += dx;
        totalY += dy;
      }
      Arrays.sort(directions, 0, count);
      for (int i = 0; i < count; i++) {
        Direction d = directions[i];
        if (d.other > pivot) {
          long numerator = d.x * totalY - d.y * totalX;
          if (numerator == 0)
            return 0.0;
          double value = numerator / Math.sqrt(d.x * d.x + d.y * d.y);
          best = Math.min(best, value);
        }
        totalX -= 2 * d.x;
        totalY -= 2 * d.y;
      }
    }
    return Double.isInfinite(best) ? 0.0 : best;
  }

  static class FastInput {
    final BufferedInputStream input = new BufferedInputStream(System.in);
    int nextInt() throws IOException {
      int c;
      do {
        c = input.read();
      } while (c <= ' ' && c != -1);
      int sign = 1;
      if (c == '-') {
        sign = -1;
        c = input.read();
      }
      int value = 0;
      while (c > ' ') {
        value = value * 10 + c - '0';
        c = input.read();
      }
      return value * sign;
    }
  }

  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = in.nextInt();
    long[] x = new long[n], y = new long[n];
    for (int i = 0; i < n; i++) {
      x[i] = in.nextInt();
      y[i] = in.nextInt();
    }
    System.out.printf(Locale.US, "%.12f%n", minimumDistance(x, y));
  }
}
