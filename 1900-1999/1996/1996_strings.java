import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
  static final int MOD = 998244353;
  static final int ROOT = 3;
  static final int DIRECT_LIMIT = 32;
  static final int DECIMAL_BASE = 10;
  static final int INPUT_BUFFER = 1 << 16;
  static final BufferedInputStream INPUT = new BufferedInputStream(System.in, INPUT_BUFFER);

  static int next(int base) throws IOException {
    int ch;
    do {
      ch = INPUT.read();
    } while (ch <= ' ' && ch >= 0);
    int value = 0;
    while (ch > ' ') {
      value = value * base + ch - '0';
      ch = INPUT.read();
    }
    return value;
  }

  static int power(int base, int exponent) {
    int result = 1;
    while (exponent > 0) {
      if ((exponent & 1) != 0)
        result = (int) ((long) result * base % MOD);
      base = (int) ((long) base * base % MOD);
      exponent >>= 1;
    }
    return result;
  }

  static void transform(int[] data, boolean inverse) {
    int n = data.length;
    for (int i = 1, j = 0; i < n; i++) {
      int bit = n >> 1;
      while ((j & bit) != 0) {
        j ^= bit;
        bit >>= 1;
      }
      j ^= bit;
      if (i < j) {
        int swap = data[i];
        data[i] = data[j];
        data[j] = swap;
      }
    }
    for (int length = 2; length <= n; length <<= 1) {
      int root = power(ROOT, (MOD - 1) / length);
      if (inverse)
        root = power(root, MOD - 2);
      for (int start = 0; start < n; start += length) {
        int factor = 1;
        for (int j = 0; j < length / 2; j++) {
          int first = data[start + j];
          int second = (int) ((long) data[start + j + length / 2] * factor % MOD);
          int sum = first + second;
          if (sum >= MOD)
            sum -= MOD;
          int difference = first - second;
          if (difference < 0)
            difference += MOD;
          data[start + j] = sum;
          data[start + j + length / 2] = difference;
          factor = (int) ((long) factor * root % MOD);
        }
      }
    }
    if (inverse) {
      int scale = power(n, MOD - 2);
      for (int i = 0; i < n; i++) data[i] = (int) ((long) data[i] * scale % MOD);
    }
  }

  static int[] matches(int[] a, int[] b) {
    int[] prefix = new int[b.length];
    for (int i = 1, j = 0; i < b.length; i++) {
      while (j > 0 && (b[i] >> 1) != (b[j] >> 1)) j = prefix[j - 1];
      if ((b[i] >> 1) == (b[j] >> 1))
        j++;
      prefix[i] = j;
    }
    int[] starts = new int[a.length];
    int count = 0;
    for (int i = 0, j = 0; i < a.length; i++) {
      while (j > 0 && (a[i] >> 1) != (b[j] >> 1)) j = prefix[j - 1];
      if ((a[i] >> 1) == (b[j] >> 1))
        j++;
      if (j == b.length) {
        starts[count++] = i - b.length + 1;
        j = prefix[j - 1];
      }
    }
    return Arrays.copyOf(starts, count);
  }

  static int[] solve(int[] a, int[] b) {
    int n = a.length, m = b.length;
    if (m > n)
      return null;
    int[] starts = matches(a, b);
    if (starts.length == 0)
      return null;
    int best = m + 1, answer = -1;
    if (starts.length <= DIRECT_LIMIT) {
      for (int start : starts) {
        int changes = 0;
        for (int j = 0; j < m; j++) changes += (a[start + j] ^ b[j]) & 1;
        if (changes < best) {
          best = changes;
          answer = start + 1;
        }
      }
      return new int[] {best, answer};
    }
    int size = 1;
    while (size < n + m - 1) size <<= 1;
    int[] first = new int[size], second = new int[size], prefix = new int[n + 1];
    for (int i = 0; i < n; i++) {
      first[i] = a[i] & 1;
      prefix[i + 1] = prefix[i] + first[i];
    }
    int ones = 0;
    for (int i = 0; i < m; i++) {
      second[m - 1 - i] = b[i] & 1;
      ones += b[i] & 1;
    }
    transform(first, false);
    transform(second, false);
    for (int i = 0; i < size; i++) first[i] = (int) ((long) first[i] * second[i] % MOD);
    transform(first, true);
    for (int start : starts) {
      int changes = prefix[start + m] - prefix[start] + ones - 2 * first[start + m - 1];
      if (changes < best) {
        best = changes;
        answer = start + 1;
      }
    }
    return new int[] {best, answer};
  }

  public static void main(String[] args) throws IOException {
    int n = next(DECIMAL_BASE), m = next(DECIMAL_BASE);
    int[] a = new int[n], b = new int[m];
    for (int i = 0; i < n; i++) a[i] = next(2);
    for (int i = 0; i < m; i++) b[i] = next(2);
    int[] result = solve(a, b);
    if (result == null)
      System.out.println("No");
    else
      System.out.println("Yes\n" + result[0] + " " + result[1]);
  }
}
