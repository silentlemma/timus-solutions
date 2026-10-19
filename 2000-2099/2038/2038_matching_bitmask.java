import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
  static final int WORD_BITS = 64;
  static long[][] matrix(int n, int m) {
    return new long[n][(m + WORD_BITS - 1) / WORD_BITS];
  }
  static final class Matching {
    final int[] left, right;
    Matching(int[] a, int[] b) {
      left = a;
      right = b;
    }
  }
  static Matching maximumMatching(long[][] rows, int m) {
    int n = rows.length, words = (m + WORD_BITS - 1) / WORD_BITS, remaining = m;
    int[] left = new int[n], right = new int[m];
    Arrays.fill(left, -1);
    Arrays.fill(right, -1);
    long[] free = new long[words];
    Arrays.fill(free, -1L);
    if (m % WORD_BITS != 0)
      free[words - 1] = (1L << (m % WORD_BITS)) - 1;
    for (int start = 0; start < n && remaining > 0; start++) {
      int direct = -1;
      for (int w = 0; w < words; w++) {
        long mask = rows[start][w] & free[w];
        if (mask != 0) {
          direct = w * WORD_BITS + Long.numberOfTrailingZeros(mask);
          break;
        }
      }
      if (direct >= 0) {
        left[start] = direct;
        right[direct] = start;
        free[direct / WORD_BITS] &= ~(1L << (direct % WORD_BITS));
        remaining--;
        continue;
      }
      int[] queue = new int[n], parent = new int[m];
      queue[0] = start;
      int end = 1, finish = -1;
      long[] seen = new long[words];
      for (int at = 0; at < end && finish < 0; at++) {
        int u = queue[at];
        for (int w = 0; w < words && finish < 0; w++) {
          long mask = rows[u][w] & ~seen[w];
          while (mask != 0) {
            long bit = Long.lowestOneBit(mask);
            mask &= mask - 1;
            seen[w] |= bit;
            int v = w * WORD_BITS + Long.numberOfTrailingZeros(bit);
            parent[v] = u;
            if (right[v] < 0) {
              finish = v;
              break;
            }
            queue[end++] = right[v];
          }
        }
      }
      if (finish >= 0) {
        free[finish / WORD_BITS] &= ~(1L << (finish % WORD_BITS));
        remaining--;
        while (finish >= 0) {
          int u = parent[finish], old = left[u];
          left[u] = finish;
          right[finish] = u;
          finish = old;
        }
      }
    }
    return new Matching(left, right);
  }
  static final class Reach {
    final boolean[] own, other;
    Reach(int n, int m) {
      own = new boolean[n];
      other = new boolean[m];
    }
  }
  static Reach reach(long[][] rows, int[] opposite, int[] ownMatch) {
    Reach result = new Reach(rows.length, opposite.length);
    int[] queue = new int[rows.length];
    int end = 0;
    for (int u = 0; u < ownMatch.length; u++)
      if (ownMatch[u] < 0) {
        result.own[u] = true;
        queue[end++] = u;
      }
    int words = (opposite.length + WORD_BITS - 1) / WORD_BITS;
    long[] seen = new long[words];
    for (int at = 0; at < end; at++) {
      int u = queue[at];
      for (int w = 0; w < words; w++) {
        long mask = rows[u][w] & ~seen[w];
        while (mask != 0) {
          long bit = Long.lowestOneBit(mask);
          mask &= mask - 1;
          seen[w] |= bit;
          int v = w * WORD_BITS + Long.numberOfTrailingZeros(bit), partner = opposite[v];
          result.other[v] = true;
          if (partner >= 0 && !result.own[partner]) {
            result.own[partner] = true;
            queue[end++] = partner;
          }
        }
      }
    }
    return result;
  }
  static String[] solve(long[][] rows, long[][] reverse) {
    Matching matching = maximumMatching(rows, reverse.length);
    Reach forward = reach(rows, matching.right, matching.left),
          backward = reach(reverse, matching.left, matching.right);
    char[] a = new char[rows.length], b = new char[reverse.length];
    for (int u = 0; u < a.length; u++) a[u] = forward.own[u] ? 'N' : backward.other[u] ? 'A' : 'E';
    for (int v = 0; v < b.length; v++) b[v] = backward.own[v] ? 'N' : forward.other[v] ? 'A' : 'E';
    return new String[] {new String(a), new String(b)};
  }
  static final class FastInput {
    static final int BUFFER_SIZE = 1 << 16, DECIMAL = 10, BYTE_MASK = 255;
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[BUFFER_SIZE];
    private int at = 0, size = 0;
    private int read() throws IOException {
      if (at == size) {
        size = in.read(buffer);
        at = 0;
        if (size < 0)
          return -1;
      }
      return buffer[at++] & BYTE_MASK;
    }
    int next() throws IOException {
      int c;
      do {
        c = read();
      } while (c <= ' ' && c >= 0);
      int value = 0;
      while (c > ' ') {
        value = value * DECIMAL + c - '0';
        c = read();
      }
      return value;
    }
  }
  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = in.next(), m = in.next(), k = in.next();
    long[][] rows = matrix(n, m), reverse = matrix(m, n);
    for (int i = 0; i < k; i++) {
      int u = in.next() - 1, v = in.next() - 1;
      rows[u][v / WORD_BITS] |= 1L << (v % WORD_BITS);
      reverse[v][u / WORD_BITS] |= 1L << (u % WORD_BITS);
    }
    String[] answer = solve(rows, reverse);
    System.out.println(answer[0]);
    System.out.println(answer[1]);
  }
}
