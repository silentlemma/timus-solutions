import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
  private static final int SHIFT = 20; // positions are below 2^20

  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    // dryness and position packed into one long, so a sort orders by both
    long[] flowers = new long[n];
    for (int i = 0; i < n; i++) {
      in.nextToken();
      flowers[i] = ((long) in.nval << SHIFT) | i;
    }
    Arrays.sort(flowers);
    long mask = (1L << SHIFT) - 1;
    // a group of equal dryness is a segment of positions, watered by walking it once.
    // The walk ends at its left or right end, and those two states carry over
    long atLeft = 0;
    long atRight = 0;
    long left = 0; // the previous group, starting from the leftmost flower
    long right = 0;
    for (int i = 0; i < n; ) {
      int j = i;
      while (j < n && flowers[j] >> SHIFT == flowers[i] >> SHIFT) j++;
      long l = flowers[i] & mask;
      long r = flowers[j - 1] & mask;
      long toLeft = Math.min(atLeft + Math.abs(left - r), atRight + Math.abs(right - r)) + r - l;
      long toRight = Math.min(atLeft + Math.abs(left - l), atRight + Math.abs(right - l)) + r - l;
      atLeft = toLeft;
      atRight = toRight;
      left = l;
      right = r;
      i = j;
    }
    System.out.println(Math.min(atLeft, atRight) + n);
  }
}
