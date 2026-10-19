import java.io.BufferedInputStream;
import java.io.IOException;

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
  static int[] solve(int first, int second, int emptyFirst, int emptySecond) {
    return new int[] {first - emptyFirst, second - emptySecond};
  }
  public static void main(String[] args) throws IOException {
    int a1 = next(), b1 = next();
    next();
    int b2 = next(), a3 = next();
    next();
    int[] result = solve(a1, b1, a3, b2);
    System.out.println(result[0] + " " + result[1]);
  }
}
