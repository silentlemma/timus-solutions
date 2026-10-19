import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static long solve(long count, long groups) {
    long small = count / groups;
    long larger = count % groups;
    long squares = (groups - larger) * small * small + larger * (small + 1) * (small + 1);
    return (count * count - squares) / 2;
  }

  static long readNumber(BufferedInputStream in) throws IOException {
    int character;
    do {
      character = in.read();
    } while (character >= 0 && character <= ' ');
    long value = 0;
    while (character > ' ') {
      value = value * 10 + character - '0';
      character = in.read();
    }
    return value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int tests = (int) readNumber(in);
    StringBuilder out = new StringBuilder();
    while (tests-- > 0) {
      long count = readNumber(in);
      long groups = readNumber(in);
      out.append(solve(count, groups)).append('\n');
    }
    System.out.print(out);
  }
}
