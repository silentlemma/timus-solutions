import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int CASE_BIT = 32;
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

  static int[] solve(int n, String word) {
    int[] answer = new int[n];
    char[] letters = new char[word.length()];
    int[] ids = new int[word.length()];
    int size = 0, upper = 0, lower = 0;
    for (int i = 0; i < word.length(); i++) {
      char code = word.charAt(i);
      boolean isUpper = code >= 'A' && code <= 'Z';
      int index = isUpper ? upper++ : lower++;
      if (size > 0 && (letters[size - 1] ^ code) == CASE_BIT) {
        int previous = ids[--size];
        if (isUpper)
          answer[index] = previous;
        else
          answer[previous] = index;
      } else {
        letters[size] = code;
        ids[size++] = index;
      }
    }
    return size == 0 ? answer : null;
  }

  static void run(BufferedInputStream in, StringBuilder out) throws IOException {
    int n = Integer.parseInt(readToken(in));
    int[] answer = solve(n, readToken(in));
    if (answer == null)
      out.append("Impossible\n");
    else {
      for (int i = 0; i < answer.length; i++) {
        if (i > 0)
          out.append(' ');
        out.append(answer[i] + 1);
      }
      out.append('\n');
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    StringBuilder out = new StringBuilder();
    run(in, out);
    System.out.print(out);
  }
}
