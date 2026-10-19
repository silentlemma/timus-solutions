import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  private static final int BASE = 10;
  private static final int LIMIT = BASE * BASE - 1;
  private static final String TURN = "01????9?86";

  static String solve(int count) {
    int run = 0;
    for (int value = 1; value <= LIMIT; value++) {
      if (TURN.charAt(value / BASE) != '?' && TURN.charAt(value % BASE) != '?')
        run++;
      else
        run = 0;
      if (run >= count) {
        StringBuilder answer = new StringBuilder();
        for (int target = value; target > value - count; target--) {
          if (answer.length() != 0)
            answer.append(' ');
          answer.append(TURN.charAt(target % BASE));
          answer.append(TURN.charAt(target / BASE));
        }
        return answer.toString();
      }
    }
    return "Glupenky Pierre";
  }

  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    String line = input.readLine();
    if (line != null)
      System.out.println(solve(Integer.parseInt(line.trim())));
  }
}
