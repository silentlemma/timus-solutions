import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static class Builder {
    final int[] path;
    int size;

    Builder(int capacity) {
      path = new int[capacity];
    }

    void visit(int first, int last, int dimensions) {
      if ((dimensions & (dimensions - 1)) == 0) {
        path[size++] = first;
        if (last != first)
          path[size++] = last;
        return;
      }
      int difference = first ^ last;
      int split = difference & -difference;
      int remaining = dimensions ^ split;
      int bridge = remaining & -remaining;
      if ((first ^ bridge ^ split) == last && remaining != bridge) {
        int choices = remaining ^ bridge;
        bridge = choices & -choices;
      }
      int middle = first ^ bridge;
      visit(first, middle, remaining);
      visit(middle ^ split, last, remaining);
    }
  }

  static int[] buildPath(int start, int finish, int free) {
    Builder builder = new Builder(1 << Integer.bitCount(free));
    builder.visit(start, finish, free);
    return Arrays.copyOf(builder.path, builder.size);
  }

  static int readMask(Scanner in) {
    int count = in.nextInt(), mask = 0;
    for (int i = 0; i < count; i++) mask |= 1 << (in.nextInt() - 1);
    return mask;
  }

  public static void main(String[] args) {
    try (Scanner in = new Scanner(System.in)) {
      int dimensions = in.nextInt();
      int start = readMask(in), finish = readMask(in);
      int[] path = buildPath(start, finish, (1 << dimensions) - 1);
      StringBuilder out = new StringBuilder();
      out.append(path.length).append('\n');
      for (int mask : path) {
        out.append(Integer.bitCount(mask));
        while (mask != 0) {
          int bit = mask & -mask;
          out.append(' ').append(Integer.numberOfTrailingZeros(bit) + 1);
          mask ^= bit;
        }
        out.append('\n');
      }
      System.out.print(out);
    }
  }
}
