import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  private static final int ALICE = 1;
  private static final int DRAW = 0;
  private static final int BOB = -1;
  private static final int NONE = 2; // the strip still shows both colours

  private static boolean single(String s, char colour) {
    for (int i = 0; i < s.length(); i++) if (s.charAt(i) != colour) return false;
    return true;
  }

  private static int winner(String top, String bottom) {
    if (single(top, 'A') && single(bottom, 'A')) return ALICE;
    if (single(top, 'B') && single(bottom, 'B')) return BOB;
    return NONE;
  }

  private static String reversed(String s) {
    return new StringBuilder(s).reverse().toString();
  }

  // the result of optimal play from this strip with this player to move
  private static int play(String top, String bottom, boolean alice) {
    int n = top.length();
    if (n % 2 == 1) return DRAW;
    int half = n / 2;
    // folding brings the right half over or under the left one; the faces that
    // end up inside are hidden
    String[][] folds = {
      {top.substring(0, half), reversed(top.substring(half))},
      {reversed(bottom.substring(half)), bottom.substring(0, half)}
    };
    int best = NONE;
    for (String[] f : folds) {
      int result = winner(f[0], f[1]);
      if (result == NONE) result = play(f[0], f[1], !alice);
      if (best == NONE || (alice ? result > best : result < best)) best = result;
      if (best == (alice ? ALICE : BOB)) break;
    }
    return best;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    in.readLine();
    String top = in.readLine().trim();
    String bottom = in.readLine().trim();
    int result = play(top, bottom, true);
    System.out.println(result == ALICE ? "Alice" : result == BOB ? "Bob" : "Draw");
  }
}
