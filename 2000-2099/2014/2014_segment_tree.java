import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
  private static final int DAY_SLOTS = 32;
  private static final int HOURS_PER_DAY = 24;
  private static final int MINUTES_PER_HOUR = 60;

  private static long[] solve(int[] keys, long[] amounts) {
    int n = keys.length;
    long[] order = new long[n];
    for (int i = 0; i < n; ++i) order[i] = (long) keys[i] * n + i;
    Arrays.sort(order);
    int[] ranks = new int[n];
    for (int i = 0; i < n; ++i) ranks[(int) (order[i] % n)] = i;
    int size = 1;
    while (size < n) size <<= 1;
    long[] sums = new long[2 * size], prefixes = new long[2 * size], result = new long[n];
    for (int i = 0; i < n; ++i) {
      int index = size + ranks[i];
      sums[index] = amounts[i];
      prefixes[index] = Math.min(0L, amounts[i]);
      for (index >>= 1; index > 0; index >>= 1) {
        int left = index << 1, right = left + 1;
        sums[index] = sums[left] + sums[right];
        prefixes[index] = Math.min(prefixes[left], sums[left] + prefixes[right]);
      }
      result[i] = prefixes[1];
    }
    return result;
  }

  private static int number(BufferedInputStream in) throws IOException {
    int c = in.read();
    while (c >= 0 && (c < '0' || c > '9') && c != '-' && c != '+') c = in.read();
    int sign = 1;
    if (c == '-' || c == '+') {
      sign = c == '-' ? -1 : 1;
      c = in.read();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
      value = value * 10 + c - '0';
      c = in.read();
    }
    return sign * value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int n = number(in);
    int[] keys = new int[n];
    long[] amounts = new long[n];
    for (int i = 0; i < n; ++i) {
      amounts[i] = number(in);
      int day = number(in), month = number(in), hour = number(in), minute = number(in);
      keys[i] = ((month * DAY_SLOTS + day) * HOURS_PER_DAY + hour) * MINUTES_PER_HOUR + minute;
    }
    StringBuilder out = new StringBuilder();
    for (long value : solve(keys, amounts)) out.append(value).append('\n');
    System.out.print(out);
  }
}
