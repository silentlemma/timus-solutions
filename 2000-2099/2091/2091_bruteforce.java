import java.util.Scanner;

public class Main {
  private static final int GROUPS = 4; // both courses, only the first, only the second, neither

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int m = in.nextInt();
    int[][] column = new int[m][n];
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) column[j][i] = in.nextInt();
    int best = n + 1;
    int bestA = 0;
    int bestB = 0;
    // every pair of courses is tried: the four groups of a pair are counted
    // in one pass over the programs
    for (int a = 0; a < m; a++)
      for (int b = a + 1; b < m; b++) {
        int[] count = new int[GROUPS];
        for (int i = 0; i < n; i++) count[2 * column[a][i] + column[b][i]]++;
        int worst = 0;
        for (int c : count) worst = Math.max(worst, c);
        if (worst < best) {
          best = worst;
          bestA = a + 1;
          bestB = b + 1;
        }
      }
    System.out.println(best);
    System.out.println(bestA + " " + bestB);
  }
}
