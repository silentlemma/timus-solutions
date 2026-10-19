import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

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

  static class Machine {
    int[] terminal;
    int[][] rows;
    Machine(int[] flags, int[][] transitions) {
      terminal = flags;
      rows = transitions;
    }
  }

  static Machine construct(int[][] old, int[] flags, int offset) {
    int n = old.length, stride = n + 1, maximum = 2 * n * stride;
    int[] identifiers = new int[maximum], keys = new int[maximum], terminal = new int[maximum];
    Arrays.fill(identifiers, -1);
    keys[0] = 2 * n;
    identifiers[keys[0]] = 0;
    int count = 1;
    int[][] rows = new int[maximum][];
    for (int head = 0; head < count; head++) {
      int key = keys[head], pair = key / 2, normal = pair / stride, previous = pair % stride;
      terminal[head] = key & 1;
      int[] row = new int[BASE];
      for (int digit = 0; digit < BASE; digit++) {
        int nextNormal = old[normal][digit];
        int nextPrevious =
            digit > 0 ? old[normal][digit - 1] : (previous == n ? n : old[previous][BASE - 1]);
        int accepted = 0;
        if (digit >= offset)
          accepted = flags[old[normal][digit - offset]];
        else if (previous != n)
          accepted = flags[old[previous][digit + BASE - offset]];
        int target = 2 * (nextNormal * stride + nextPrevious) + accepted;
        if (identifiers[target] < 0) {
          identifiers[target] = count;
          keys[count++] = target;
        }
        row[digit] = identifiers[target];
      }
      rows[head] = row;
    }
    return new Machine(Arrays.copyOf(terminal, count), Arrays.copyOf(rows, count));
  }

  public static void main(String[] args) throws IOException {
    int offset = next(), n = next();
    int[] flags = new int[n];
    for (int i = 0; i < n; i++) flags[i] = next();
    int[][] old = new int[n][BASE];
    for (int i = 0; i < n; i++)
      for (int d = 0; d < BASE; d++) old[i][d] = next() - 1;
    Machine result = construct(old, flags, offset);
    StringBuilder out = new StringBuilder("Success\n").append(result.rows.length).append('\n');
    for (int i = 0; i < result.terminal.length; i++) {
      if (i > 0)
        out.append(' ');
      out.append(result.terminal[i]);
    }
    out.append('\n');
    for (int[] row : result.rows) {
      for (int d = 0; d < BASE; d++) {
        if (d > 0)
          out.append(' ');
        out.append(row[d] + 1);
      }
      out.append('\n');
    }
    System.out.print(out);
  }
}
