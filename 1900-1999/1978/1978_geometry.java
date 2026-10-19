import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
  private static final int INDEX_BITS = 10;
  private static final int INDEX_MASK = (1 << INDEX_BITS) - 1;
  private static long[] x;
  private static long[] y;

  private static boolean less(int a, int b) {
    int ah = a >> INDEX_BITS, al = a & INDEX_MASK;
    int bh = b >> INDEX_BITS, bl = b & INDEX_MASK;
    return (x[al] - x[ah]) * (y[bh] - y[bl]) < (x[bl] - x[bh]) * (y[ah] - y[al]);
  }

  private static void sortEvents(int[] events, int size) {
    int[] buffer = new int[size];
    int[] source = events, target = buffer;
    for (int width = 1; width < size; width *= 2) {
      for (int start = 0; start < size; start += 2 * width) {
        int mid = Math.min(size, start + width);
        int end = Math.min(size, start + 2 * width);
        int a = start, b = mid, at = start;
        while (a < mid && b < end) {
          if (less(source[b], source[a]))
            target[at++] = source[b++];
          else
            target[at++] = source[a++];
        }
        while (a < mid) target[at++] = source[a++];
        while (b < end) target[at++] = source[b++];
      }
      int[] swap = source;
      source = target;
      target = swap;
    }
    if (source != events)
      System.arraycopy(source, 0, events, 0, size);
  }

  private static void record(long[] best, int k, long a, long b, long tx, long ty) {
    best[k] = Math.max(best[k], a * a + b * b);
    a = tx - a;
    b = ty - b;
    int complement = best.length - 1 - k;
    best[complement] = Math.max(best[complement], a * a + b * b);
  }

  private static long[] solve(long[] inputX, long[] inputY) {
    x = inputX;
    y = inputY;
    int n = x.length;
    Integer[] initial = new Integer[n];
    for (int i = 0; i < n; i++) initial[i] = i;
    Arrays.sort(initial, (a, b) -> {
      if (y[a] != y[b])
        return Long.compare(y[b], y[a]);
      if (x[a] != x[b])
        return Long.compare(x[a], x[b]);
      return Integer.compare(a, b);
    });
    int[] order = new int[n], position = new int[n];
    long[] px = new long[n + 1], py = new long[n + 1], best = new long[n + 1];
    for (int i = 0; i < n; i++) {
      order[i] = initial[i];
      position[order[i]] = i;
      px[i + 1] = px[i] + x[order[i]];
      py[i + 1] = py[i] + y[order[i]];
    }
    long tx = px[n], ty = py[n];
    for (int k = 0; k <= n; k++) record
    (best, k, px[k], py[k], tx, ty);
    int[] events = new int[n * (n - 1) / 2];
    int size = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (y[i] == y[j])
          continue;
        int high = y[i] > y[j] ? i : j;
        int low = i + j - high;
        events[size++] = (high << INDEX_BITS) | low;
      }
    }
    sortEvents(events, size);
    int[] ends = new int[n], starts = new int[n];
    int[] lefts = new int[n], rights = new int[n];
    Arrays.fill(ends, -1);
    for (int at = 0; at < size;) {
      int after = at + 1;
      while (after < size && !less(events[at], events[after])) after++;
      if (after == at + 1) {
        int a = position[events[at] >> INDEX_BITS], b = position[events[at] & INDEX_MASK];
        int left = Math.min(a, b);
        int first = order[left], second = order[left + 1];
        order[left] = second;
        order[left + 1] = first;
        position[first] = left + 1;
        position[second] = left;
        int k = left + 1;
        px[k] += x[second] - x[first];
        py[k] += y[second] - y[first];
        record
        (best, k, px[k], py[k], tx, ty);
      } else {
        int used = 0;
        for (int i = at; i < after; i++) {
          int a = position[events[i] >> INDEX_BITS], b = position[events[i] & INDEX_MASK];
          if (a > b) {
            int swap = a;
            a = b;
            b = swap;
          }
          if (ends[a] < 0)
            starts[used++] = a;
          ends[a] = Math.max(ends[a], b);
        }
        Arrays.sort(starts, 0, used);
        int blocks = 0;
        for (int i = 0; i < used; i++) {
          int left = starts[i], right = ends[left];
          ends[left] = -1;
          if (blocks > 0 && left <= rights[blocks - 1]) {
            rights[blocks - 1] = Math.max(rights[blocks - 1], right);
          } else {
            lefts[blocks] = left;
            rights[blocks++] = right;
          }
        }
        for (int block = 0; block < blocks; block++) {
          int left = lefts[block], right = rights[block];
          for (int a = left, b = right; a < b; a++, b--) {
            int swap = order[a];
            order[a] = order[b];
            order[b] = swap;
          }
          long a = px[left], b = py[left];
          for (int i = left; i <= right; i++) {
            int id = order[i];
            position[id] = i;
            a += x[id];
            b += y[id];
            px[i + 1] = a;
            py[i + 1] = b;
            if (i < right)
              record
            (best, i + 1, a, b, tx, ty);
          }
        }
      }
      at = after;
    }
    return Arrays.copyOfRange(best, 1, best.length);
  }

  private static final class FastInput {
    private final BufferedInputStream in = new BufferedInputStream(System.in);
    int nextInt() throws IOException {
      int c;
      do {
        c = in.read();
      } while (c >= 0 && c <= ' ');
      if (c < 0)
        return Integer.MIN_VALUE;
      int sign = 1;
      if (c == '-') {
        sign = -1;
        c = in.read();
      }
      int value = 0;
      while (c > ' ') {
        value = value * 10 + c - '0';
        c = in.read();
      }
      return value * sign;
    }
  }

  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = in.nextInt();
    if (n == Integer.MIN_VALUE)
      return;
    long[] inputX = new long[n], inputY = new long[n];
    for (int i = 0; i < n; i++) {
      inputX[i] = in.nextInt();
      inputY[i] = in.nextInt();
    }
    StringBuilder out = new StringBuilder();
    for (long value : solve(inputX, inputY)) out.append(Math.sqrt(value)).append('\n');
    System.out.print(out);
  }
}
