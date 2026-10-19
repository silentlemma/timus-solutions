import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int TRIANGLE = 3, CORNERS = 4, CLOSED = 5;
  static final class FastInput {
    private final BufferedInputStream in = new BufferedInputStream(System.in);
    long nextLong() throws IOException {
      int c;
      do {
        c = in.read();
      } while (c <= ' ' && c >= 0);
      long sign = 1, value = 0;
      if (c == '-') {
        sign = -1;
        c = in.read();
      }
      while (c > ' ') {
        value = value * DECIMAL + c - '0';
        c = in.read();
      }
      return value * sign;
    }
    static final int DECIMAL = 10;
  }
  static long cross(long[] x, long[] y, int a, int b, int p) {
    return (x[b] - x[a]) * (y[p] - y[a]) - (y[b] - y[a]) * (x[p] - x[a]);
  }
  static boolean sameSum(long[] x, long[] y, int a, int b, int c, int d) {
    return x[a] + x[b] == x[c] + x[d] && y[a] + y[b] == y[c] + y[d];
  }
  static boolean parallelogram(long[] x, long[] y) {
    return sameSum(x, y, 0, 1, 2, TRIANGLE) || sameSum(x, y, 0, 2, 1, TRIANGLE)
        || sameSum(x, y, 0, TRIANGLE, 1, 2);
  }
  static String solve(long[] x, long[] y) {
    int n = x.length;
    if (n <= TRIANGLE)
      return Integer.toString(n);
    for (int i = 0; i < TRIANGLE; i++)
      for (int j = i + 1; j < TRIANGLE; j++) {
        int outside = 0;
        for (int p = 0; p < n; p++)
          if (cross(x, y, i, j, p) != 0 && ++outside > 1)
            break;
        if (outside <= 1)
          return Integer.toString(n);
      }
    if (n == CORNERS)
      return parallelogram(x, y) ? Integer.toString(CLOSED) : "oo";
    if (n == CLOSED)
      for (int center = 0; center < n; center++) {
        long[] ox = new long[CORNERS], oy = new long[CORNERS];
        long sx = 0, sy = 0;
        int k = 0;
        for (int i = 0; i < n; i++)
          if (i != center) {
            ox[k] = x[i];
            oy[k++] = y[i];
            sx += x[i];
            sy += y[i];
          }
        if (parallelogram(ox, oy) && sx == CORNERS * x[center] && sy == CORNERS * y[center])
          return Integer.toString(CLOSED);
      }
    return "oo";
  }
  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = (int) in.nextLong();
    long[] x = new long[n], y = new long[n];
    for (int i = 0; i < n; i++) {
      x[i] = in.nextLong();
      y[i] = in.nextLong();
    }
    System.out.println(solve(x, y));
  }
}
