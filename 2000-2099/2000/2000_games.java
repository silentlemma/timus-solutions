import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int BASE = 10;
  static final BufferedInputStream INPUT = new BufferedInputStream(System.in);
  static int next() throws IOException {
    int ch;
    do {
      ch = INPUT.read();
    } while (ch <= ' ' && ch >= 0);
    int value = 0;
    while (ch > ' ') {
      value = value * BASE + ch - '0';
      ch = INPUT.read();
    }
    return value;
  }
  static long[] solve(long[] values, int first, int second) {
    long total = 0, score = 0;
    for (long value : values) total += value;
    if (first == second) {
      long left = 0;
      for (int i = 0; i < first; i++) left += values[i];
      long right = total - left - values[first];
      score = values[first] + Math.max(left, right);
    } else if (first < second) {
      int boundary = (first + second) / 2;
      for (int i = 0; i <= boundary; i++) score += values[i];
    } else {
      int boundary = (first + second + 1) / 2;
      for (int i = boundary; i < values.length; i++) score += values[i];
    }
    return new long[] {score, total - score};
  }
  public static void main(String[] args) throws IOException {
    int n = next();
    long[] values = new long[n];
    for (int i = 0; i < n; i++) values[i] = next();
    int first = next() - 1, second = next() - 1;
    long[] result = solve(values, first, second);
    System.out.println(result[0] + " " + result[1]);
  }
}
