import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int SPACE = 32;

  static String readToken(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= SPACE && c >= 0);
    StringBuilder token = new StringBuilder();
    while (c > SPACE) {
      token.append((char) c);
      c = in.read();
    }
    return token.toString();
  }

  static int solve(String south, String north) {
    int i = 0, j = 0, elapsed = 0;
    while (i < south.length() && j < north.length()) {
      char a = south.charAt(i), b = north.charAt(j);
      boolean goA = a != 'L' || b == 'L';
      boolean goB = b != 'L' || a == 'L';
      if (goA)
        i++;
      if (goB)
        j++;
      elapsed++;
    }
    return elapsed + south.length() - i + north.length() - j;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    String south = readToken(in), north = readToken(in);
    System.out.println(solve(south, north));
  }
}
