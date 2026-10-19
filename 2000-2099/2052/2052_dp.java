import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int DECIMAL_BASE = 10;
  static final int MAX_DIGIT = DECIMAL_BASE - 1;

  static long[][] buildTables(int digits) {
    int maximum = MAX_DIGIT * digits;
    long[] ways = new long[maximum + 1];
    ways[0] = 1;
    long[][] prefix = new long[digits][maximum + 1];
    for (int length = 0; length < digits; length++) {
      long running = 0;
      for (int total = 0; total <= maximum; total++) {
        running += ways[total];
        prefix[length][total] = running;
      }
      if (length + 1 == digits)
        break;
      long[] nextWays = new long[maximum + 1];
      long window = 0;
      for (int total = 0; total <= maximum; total++) {
        window += ways[total];
        if (total >= DECIMAL_BASE)
          window -= ways[total - DECIMAL_BASE];
        nextWays[total] = window;
      }
      ways = nextWays;
    }
    return prefix;
  }

  static long countLeq(long value, int target, long[][] prefix) {
    String digits = Long.toString(value);
    int maximum = prefix[0].length - 1, remaining = target;
    long result = 0;
    for (int position = 0; position < digits.length(); position++) {
      int digit = digits.charAt(position) - '0';
      long[] row = prefix[digits.length() - position - 1];
      if (digit != 0 && remaining >= 0) {
        result += row[Math.min(maximum, remaining)];
        if (remaining >= digit)
          result -= row[Math.min(maximum, remaining - digit)];
      }
      remaining -= digit;
      if (remaining < 0)
        return result;
    }
    return result + (remaining == 0 ? 1 : 0);
  }

  static int digitSum(long value) {
    int total = 0;
    while (value != 0) {
      total += (int) (value % DECIMAL_BASE);
      value /= DECIMAL_BASE;
    }
    return total;
  }

  static int solve(long number) {
    int digits = Long.toString(number).length();
    long[][] prefix = buildTables(digits);
    long lower = 0;
    int answer = 0;
    for (int target = 1; target <= MAX_DIGIT * digits; target++) {
      long count = countLeq(number, target, prefix);
      if (count == 0)
        continue;
      long start = lower + 1, left = start, right = lower + count;
      while (left <= right) {
        long middle = (left + right) / 2;
        if (middle - countLeq(middle, target, prefix) <= lower)
          left = middle + 1;
        else
          right = middle - 1;
      }
      if (right >= start && digitSum(right) == target
          && right - countLeq(right, target, prefix) == lower)
        answer++;
      lower += count;
    }
    return answer;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int ch;
    do {
      ch = in.read();
    } while (ch <= ' ');
    long number = 0;
    while (ch > ' ') {
      number = number * DECIMAL_BASE + ch - '0';
      ch = in.read();
    }
    System.out.println(solve(number));
  }
}
