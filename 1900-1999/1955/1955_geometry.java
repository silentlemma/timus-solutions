import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Locale;
import java.util.Scanner;
import java.util.Set;

public strictfp class Main {
  static final int COORDINATE_LIMIT = 1000;
  static final int DIRECTION_BITS = 12;
  static final int CONSTANT_BITS = 23;
  static final long DIRECTION_SHIFT = 2 * COORDINATE_LIMIT;
  static final long CONSTANT_SHIFT = 4L * COORDINATE_LIMIT * COORDINATE_LIMIT;
  static final class Interval {
    double left, right;
  }
  static final Comparator<Interval> ORDER = (a, b) -> {
    int first = Double.compare(a.left, b.left);
    return first != 0 ? first : Double.compare(a.right, b.right);
  };
  static final class Span {
    final double length;
    final boolean visible;
    Span(double length, boolean visible) {
      this.length = length;
      this.visible = visible;
    }
  }
  static long gcd(long a, long b) {
    while (b != 0) {
      long next = a % b;
      a = b;
      b = next;
    }
    return Math.abs(a);
  }
  static final class Solver {
    final int n;
    final long[] x, y, ex, ey, constants, heights;
    final double[] hits;
    final Interval[] intervals;
    Solver(long[] x, long[] y) {
      this.x = x;
      this.y = y;
      n = x.length;
      ex = new long[n];
      ey = new long[n];
      constants = new long[n];
      heights = new long[n];
      hits = new double[n];
      intervals = new Interval[2 * n];
      for (int i = 0; i < intervals.length; i++) intervals[i] = new Interval();
      for (int i = 0; i < n; i++) {
        int a = (i + n - 1) % n;
        ex[i] = x[i] - x[a];
        ey[i] = y[i] - y[a];
        constants[i] = x[a] * y[i] - y[a] * x[i];
      }
    }
    Span lineSpan(long px, long py, long dx, long dy) {
      long offset = dx * py - dy * px, squared = dx * dx + dy * dy;
      for (int i = 0; i < n; i++) heights[i] = dx * y[i] - dy * x[i] - offset;
      int hitCount = 0, count = 0;
      long previous = heights[n - 1];
      for (int i = 0; i < n; i++) {
        long height = heights[i];
        if ((previous > 0) != (height > 0)) {
          hits[hitCount++] =
              (double) (constants[i] - px * ey[i] + py * ex[i]) / (height - previous);
        } else if (height == 0 && previous == 0) {
          int a = (i + n - 1) % n;
          double first = (double) ((x[a] - px) * dx + (y[a] - py) * dy) / squared;
          double second = (double) ((x[i] - px) * dx + (y[i] - py) * dy) / squared;
          intervals[count].left = Math.min(first, second);
          intervals[count++].right = Math.max(first, second);
        }
        previous = height;
      }
      Arrays.sort(hits, 0, hitCount);
      for (int i = 0; i < hitCount; i += 2) {
        intervals[count].left = hits[i];
        intervals[count++].right = hits[i + 1];
      }
      if (count == 0)
        return new Span(0, false);
      Arrays.sort(intervals, 0, count, ORDER);
      double left = intervals[0].left, right = intervals[0].right, best = 0;
      boolean visible = false;
      for (int i = 1; i < count; i++) {
        if (intervals[i].left <= right)
          right = Math.max(right, intervals[i].right);
        else {
          best = Math.max(best, right - left);
          visible |= left <= 0 && right >= 1;
          left = intervals[i].left;
          right = intervals[i].right;
        }
      }
      return new Span(Math.max(best, right - left), visible || (left <= 0 && right >= 1));
    }
    double solve() {
      long lower = 0, diameter = 0, px = 0, py = 0, dx = 0, dy = 0;
      long minX = x[0], maxX = x[0], minY = y[0], maxY = y[0];
      for (int i = 0; i < n; i++) {
        lower = Math.max(lower, ex[i] * ex[i] + ey[i] * ey[i]);
        minX = Math.min(minX, x[i]);
        maxX = Math.max(maxX, x[i]);
        minY = Math.min(minY, y[i]);
        maxY = Math.max(maxY, y[i]);
        for (int j = 0; j < i; j++) {
          long ax = x[j] - x[i], ay = y[j] - y[i], squared = ax * ax + ay * ay;
          if (squared > diameter) {
            diameter = squared;
            px = x[i];
            py = y[i];
            dx = ax;
            dy = ay;
          }
        }
      }
      Span initial = lineSpan(px, py, dx, dy);
      if (initial.visible)
        return Math.sqrt(diameter);
      double best = Math.max(lower, initial.length * initial.length * diameter);
      long widthSquared = (maxX - minX) * (maxX - minX);
      long heightSquared = (maxY - minY) * (maxY - minY);
      Set<Long> seen = new HashSet<>();
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
          dx = x[j] - x[i];
          dy = y[j] - y[i];
          long squared = dx * dx + dy * dy;
          if (widthSquared * squared < lower * dx * dx || heightSquared * squared < lower * dy * dy)
            continue;
          long divisor = gcd(dx, dy), nx = dx / divisor, ny = dy / divisor;
          if (nx < 0 || (nx == 0 && ny < 0)) {
            nx = -nx;
            ny = -ny;
          }
          long constant = nx * y[i] - ny * x[i];
          long key = (nx << (DIRECTION_BITS + CONSTANT_BITS))
              | ((ny + DIRECTION_SHIFT) << CONSTANT_BITS) | (constant + CONSTANT_SHIFT);
          if (!seen.add(key))
            continue;
          Span current = lineSpan(x[i], y[i], dx, dy);
          if (current.visible) {
            lower = Math.max(lower, squared);
            if (lower == diameter)
              return Math.sqrt(diameter);
          }
          best = Math.max(best, Math.max(current.length * current.length * squared, lower));
        }
      }
      return Math.sqrt(best);
    }
  }
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    long[] x = new long[n], y = new long[n];
    for (int i = 0; i < n; i++) {
      x[i] = input.nextLong();
      y[i] = input.nextLong();
    }
    System.out.printf(Locale.US, "%.12f%n", new Solver(x, y).solve());
  }
}
