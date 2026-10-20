import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  private static final int SIDE = 3; // seats on each side of the aisle
  private static final int MASKS = 1 << SIDE;
  private static final int RIGHT_START = 6; // the right seats in a row description
  private static final String LETTERS = "ABCDEF";

  // The largest set of free, pairwise non-adjacent seats on one side, as a mask
  // per row; seats in a row and in the next row may not share a column or stand
  // next to each other.
  private static int[] bestSide(String[] rows, int offset) {
    int n = rows.length;
    int[][] best = new int[n + 1][MASKS];
    int[][] from = new int[n + 1][MASKS];
    for (int[] line : best) java.util.Arrays.fill(line, -1);
    best[0][0] = 0;
    for (int r = 0; r < n; r++) {
      int free = 0;
      for (int s = 0; s < SIDE; s++) {
        if (rows[r].charAt(offset + s) == '.') free |= 1 << s;
      }
      for (int cur = 0; cur < MASKS; cur++) {
        if ((cur & ~free) != 0 || (cur & (cur << 1)) != 0) continue;
        int count = Integer.bitCount(cur);
        for (int prev = 0; prev < MASKS; prev++) {
          if (best[r][prev] < 0 || ((prev | prev << 1 | prev >> 1) & cur) != 0) continue;
          if (best[r][prev] + count > best[r + 1][cur]) {
            best[r + 1][cur] = best[r][prev] + count;
            from[r + 1][cur] = prev;
          }
        }
      }
    }
    int mask = 0;
    for (int m = 0; m < MASKS; m++) {
      if (best[n][m] > best[n][mask]) mask = m;
    }
    int[] chosen = new int[n];
    for (int r = n; r > 0; r--) {
      chosen[r - 1] = mask;
      mask = from[r][mask];
    }
    return chosen;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int k = in.nextInt();
    String[] rows = new String[n];
    for (int r = 0; r < n; r++) rows[r] = in.next();
    List<String> seats = new ArrayList<>();
    for (int half = 0; half < 2; half++) {
      int[] chosen = bestSide(rows, half * RIGHT_START);
      for (int r = 0; r < n; r++) {
        for (int s = 0; s < SIDE; s++) {
          if ((chosen[r] >> s & 1) == 1) seats.add((r + 1) + "" + LETTERS.charAt(half * SIDE + s));
        }
      }
    }
    if (seats.size() < k) {
      System.out.println("PORAZHENIE");
      return;
    }
    StringBuilder out = new StringBuilder("POBEDA\n");
    for (int i = 0; i < k; i++) out.append(seats.get(i)).append('\n');
    System.out.print(out);
  }
}
