import java.util.Scanner;

public class Main {
  private static final String[] DIGITS = {
    "._.|.||_|", ".....|..|", "._.._||_.", "._.._|._|", "...|_|..|",
    "._.|_.._|", "._.|_.|_|", "._...|..|", "._.|_||_|", "._.|_|._|"
  };
  private static final int[] COLUMNS = {0, 4, 10, 14}; // where the four digits start
  private static final int WIDTH = 3;
  private static final int SECONDS = 60; // MM:SS runs from 00:00 to 59:59

  // every lit segment must belong to the digit
  private static boolean fits(String shown, int digit) {
    for (int i = 0; i < shown.length(); i++) {
      char c = shown.charAt(i);
      if (c != '.' && c != DIGITS[digit].charAt(i)) return false;
    }
    return true;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    StringBuilder out = new StringBuilder();
    int previous = SECONDS * SECONDS;
    for (int r = 0; r < n; r++) {
      String[] rows = new String[WIDTH];
      for (int i = 0; i < WIDTH; i++) rows[i] = in.next();
      boolean[][] ok = new boolean[COLUMNS.length][10];
      for (int k = 0; k < COLUMNS.length; k++) {
        StringBuilder cell = new StringBuilder();
        for (String row : rows) cell.append(row, COLUMNS[k], COLUMNS[k] + WIDTH);
        for (int d = 0; d < 10; d++) ok[k][d] = fits(cell.toString(), d);
      }
      // the largest time that fits and stays below the previous one leaves the
      // most room for the rest, so it never spoils a solution
      int value = previous - 1;
      while (true) {
        int m = value / SECONDS;
        int s = value % SECONDS;
        int[] digits = {m / 10, m % 10, s / 10, s % 10};
        boolean all = true;
        for (int k = 0; k < COLUMNS.length; k++) all &= ok[k][digits[k]];
        if (all) {
          out.append(String.format("%02d:%02d", m, s)).append('\n');
          break;
        }
        value--;
      }
      previous = value;
    }
    System.out.print(out);
  }
}
