import java.io.BufferedInputStream;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
  static final int DECIMAL_BASE = 10;
  static final int MAX_NUMBER_DIGITS = 7;

  static class Input {
    final BufferedInputStream stream = new BufferedInputStream(System.in);
    int integer() throws Exception {
      int c;
      do {
        c = stream.read();
      } while (c <= ' ' && c >= 0);
      int value = 0;
      while (c >= '0' && c <= '9') {
        value = value * DECIMAL_BASE + c - '0';
        stream.mark(1);
        c = stream.read();
      }
      if (c >= 0)
        stream.reset();
      return value;
    }
    boolean base() throws Exception {
      int c;
      do {
        c = stream.read();
      } while (c <= ' ' && c >= 0);
      return c == '1';
    }
  }

  public static void main(String[] args) throws Exception {
    Input in = new Input();
    int height = in.integer(), width = in.integer(), far = height + width;
    int[] distances = new int[height * width], last = new int[width];
    Arrays.fill(last, -far);
    for (int row = 0; row < height; row++) {
      for (int column = 0; column < width; column++) {
        if (in.base())
          last[column] = row;
        distances[row * width + column] = row - last[column];
      }
    }
    int[] following = new int[width];
    Arrays.fill(following, height + far);
    for (int row = height - 1; row >= 0; row--) {
      for (int column = 0; column < width; column++) {
        int at = row * width + column, value = distances[at];
        if (value == 0)
          following[column] = row;
        else if (following[column] - row < value)
          distances[at] = following[column] - row;
      }
    }
    int[] costs = new int[width], intercepts = new int[width];
    int[] sites = new int[width], starts = new int[width];
    BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
    StringBuilder line = new StringBuilder();
    char[] outputRow = new char[width * (MAX_NUMBER_DIGITS + 1)];
    for (int row = 0; row < height; row++) {
      int used = 0;
      for (int q = 0; q < width; q++) {
        int vertical = distances[row * width + q];
        if (vertical >= far)
          continue;
        costs[q] = vertical * vertical;
        intercepts[q] = costs[q] + q * q;
        int first = 0;
        while (used > 0) {
          int p = sites[used - 1];
          first = -Math.floorDiv(-(intercepts[q] - intercepts[p]), 2 * (q - p));
          if (first > starts[used - 1])
            break;
          used--;
        }
        if (used == 0)
          first = 0;
        sites[used] = q;
        starts[used++] = first;
      }
      int current = 0;
      line.setLength(0);
      for (int x = 0; x < width; x++) {
        while (current + 1 < used && starts[current + 1] <= x) current++;
        int p = sites[current], delta = x - p;
        if (x != 0)
          line.append(' ');
        line.append(delta * delta + costs[p]);
      }
      line.getChars(0, line.length(), outputRow, 0);
      out.write(outputRow, 0, line.length());
      out.newLine();
    }
    out.flush();
  }
}
