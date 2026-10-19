import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int DECIMAL_BASE = 10;
  static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

  static long next() throws IOException {
    int ch;
    do {
      ch = INPUT.read();
    } while (ch <= ' ' && ch >= 0);
    long value = 0;
    while (ch > ' ') {
      value = value * DECIMAL_BASE + ch - '0';
      ch = INPUT.read();
    }
    return value;
  }

  static long solve(long[] weights, long[] events, long limit) {
    int size = weights.length;
    long[] prefix = new long[size + 1];
    for (int i = 0; i < size; i++) prefix[i + 1] = prefix[i] + weights[i];
    int[] retreat = new int[size + 1];
    int left = 0;
    for (int height = 1; height <= size; height++) {
      while (left + 1 < height && prefix[height] - prefix[left + 1] > limit) left++;
      retreat[height] = left;
    }
    long time = 0;
    int height = 0;
    for (long event : events) {
      long ordinary = event - time - 1;
      if (ordinary >= size - height)
        return time + size - height;
      height += (int) ordinary;
      height = retreat[height];
      time = event;
    }
    return time + size - height;
  }

  public static void main(String[] args) throws IOException {
    int n = (int) next(), m = (int) next();
    long limit = next();
    long[] weights = new long[n], events = new long[m];
    for (int i = 0; i < n; i++) weights[i] = next();
    for (int i = 0; i < m; i++) events[i] = next();
    System.out.println(solve(weights, events, limit));
  }
}
