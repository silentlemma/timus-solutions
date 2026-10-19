import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
  static final long GRAVITY = 10;
  static final long HALF_GRAVITY = GRAVITY / 2;
  static final long QUADRATIC_FACTOR = 4;
  static final double MARGIN = 1e-6;
  static final int SPACE = 32;
  static final int RADIX = 10;

  static long readLong(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= SPACE && c >= 0);
    long value = 0;
    while (c > SPACE) {
      value = value * RADIX + c - '0';
      c = in.read();
    }
    return value;
  }

  static class Polynomial {
    long a, b, c;
    Polynomial(long a, long b, long c) {
      this.a = a;
      this.b = b;
      this.c = c;
    }
  }
  static class Interval {
    double lo, hi;
    Interval(double lo, double hi) {
      this.lo = lo;
      this.hi = hi;
    }
  }
  static class Piece {
    double left, right;
    Polynomial polynomial;
    Piece(double left, double right, Polynomial p) {
      this.left = left;
      this.right = right;
      polynomial = p;
    }
  }

  static Interval roots(Polynomial p) {
    long delta = p.b * p.b + QUADRATIC_FACTOR * p.a * p.c;
    if (delta < 0)
      return null;
    if (delta == 0) {
      double value = (double) p.b / (2 * p.a);
      return new Interval(value, value);
    }
    double q = (p.b + Math.copySign(Math.sqrt((double) delta), p.b)) / 2;
    double x = q / p.a, y = -(double) p.c / q;
    return new Interval(Math.min(x, y), Math.max(x, y));
  }

  static Polynomial face(long x, long level, long vx, long vy, long ux, long uy) {
    return new Polynomial(HALF_GRAVITY * (ux * ux + vx * vx),
        vy * ux * ux - uy * vx * ux + GRAVITY * x * vx,
        uy * x * ux - HALF_GRAVITY * x * x - level * ux * ux);
  }

  static double solve(long distance, long height, long thickness, long diameter, long vx, long vy,
      long ux, long uy) {
    double lo = 0, hi = Math.min(2.0 * vy / GRAVITY, (double) distance / vx);
    for (long x : new long[] {distance, distance + thickness}) {
      Interval pair = roots(face(x, height, vx, vy, ux, uy));
      if (pair == null)
        return -1;
      lo = Math.max(lo, pair.lo);
      hi = Math.min(hi, pair.hi);
      if (lo >= hi)
        return -1;
    }
    long ceiling = height + diameter;
    double before = (double) (GRAVITY * distance - ux * uy) / (GRAVITY * vx);
    double after = (double) (GRAVITY * (distance + thickness) - ux * uy) / (GRAVITY * vx);
    Piece[] pieces = {new Piece(lo, Math.min(hi, before), face(distance, ceiling, vx, vy, ux, uy)),
        new Piece(Math.max(lo, before), Math.min(hi, after),
            new Polynomial(GRAVITY * GRAVITY, 2 * GRAVITY * vy, uy * uy - 2 * GRAVITY * ceiling)),
        new Piece(Math.max(lo, after), hi, face(distance + thickness, ceiling, vx, vy, ux, uy))};
    boolean found = false;
    double badLo = hi, badHi = lo;
    for (Piece p : pieces) {
      if (p.left > p.right)
        continue;
      Interval pair = roots(p.polynomial);
      if (pair == null)
        continue;
      double a = Math.max(p.left, pair.lo), b = Math.min(p.right, pair.hi);
      if (a <= b) {
        found = true;
        badLo = Math.min(badLo, a);
        badHi = Math.max(badHi, b);
      }
    }
    List<Interval> feasible = new ArrayList<>();
    if (!found)
      feasible.add(new Interval(lo, hi));
    else {
      if (lo < badLo)
        feasible.add(new Interval(lo, badLo));
      if (badHi < hi)
        feasible.add(new Interval(badHi, hi));
    }
    double bestWidth = 2 * MARGIN, answer = -1;
    for (Interval part : feasible) {
      if (part.hi - part.lo > bestWidth) {
        bestWidth = part.hi - part.lo;
        answer = (part.lo + part.hi) / 2;
      }
    }
    return answer;
  }

  static void run(BufferedInputStream in, StringBuilder out) throws IOException {
    double answer = solve(readLong(in), readLong(in), readLong(in), readLong(in), readLong(in),
        readLong(in), readLong(in), readLong(in));
    out.append(answer < 0 ? "-1" : Double.toString(answer)).append('\n');
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    StringBuilder out = new StringBuilder();
    run(in, out);
    System.out.print(out);
  }
}
