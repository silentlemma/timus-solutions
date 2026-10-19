import java.util.Arrays;
import java.util.Scanner;

public class Main {
  private static final int FRAMES = 10;
  private static final int PINS = 10;
  private static final int ROLL = PINS + 1; // a roll knocks down 0 to 10 pins

  // low[x][y], high[x][y]: the least and the most points of the frames from the
  // current one on, when the rolls from the current frame on start with x and y
  private static int[][] low;
  private static int[][] high;

  private static void reset() {
    low = new int[ROLL][ROLL];
    high = new int[ROLL][ROLL];
    for (int[] row : low) Arrays.fill(row, Integer.MAX_VALUE);
    for (int[] row : high) Arrays.fill(row, Integer.MIN_VALUE);
  }

  private static void put(int x, int y, int a, int b) {
    low[x][y] = Math.min(low[x][y], a);
    high[x][y] = Math.max(high[x][y], b);
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int[] total = new int[FRAMES];
    for (int i = 0; i < FRAMES; i++) total[i] = in.nextInt();
    reset();
    // rolls of the last frame: two, and a third one after a strike or a spare
    int last = total[FRAMES - 1];
    for (int r1 = 0; r1 <= PINS; r1++)
      for (int r2 = 0; r2 <= (r1 == PINS ? PINS : PINS - r1); r2++) {
        if (r1 < PINS && r1 + r2 < PINS) {
          if (r1 + r2 == last) put(r1, r2, last, last);
          continue;
        }
        boolean fresh = r1 < PINS || r2 == PINS;
        int r3 = last - r1 - r2;
        if (r3 >= 0 && r3 <= (fresh ? PINS : PINS - r2)) put(r1, r2, last, last);
      }
    for (int f = FRAMES - 2; f >= 0; f--) {
      int t = total[f];
      int[][] curLow = low;
      int[][] curHigh = high;
      reset();
      for (int x = 0; x < ROLL; x++)
        for (int y = 0; y < ROLL; y++) {
          if (curLow[x][y] == Integer.MAX_VALUE) continue;
          int a = curLow[x][y] + t;
          int b = curHigh[x][y] + t;
          if (t < PINS) {
            for (int r1 = 0; r1 <= t; r1++) put(r1, t - r1, a, b);
            continue;
          }
          // a strike takes the next two rolls, a spare the next one
          put(PINS, x, a + x + y, b + x + y);
          for (int r1 = 0; r1 < PINS; r1++) put(r1, PINS - r1, a + x, b + x);
        }
    }
    int lo = Integer.MAX_VALUE;
    int hi = Integer.MIN_VALUE;
    for (int x = 0; x < ROLL; x++)
      for (int y = 0; y < ROLL; y++) {
        lo = Math.min(lo, low[x][y]);
        hi = Math.max(hi, high[x][y]);
      }
    System.out.println(lo + " " + hi);
  }
}
