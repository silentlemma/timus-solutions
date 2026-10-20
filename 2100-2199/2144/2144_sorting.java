import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    long[][] boxes = new long[n][];
    boolean ok = true;
    for (int i = 0; i < n; i++) {
      int k = in.nextInt();
      long prev = 0;
      long first = 0;
      for (int j = 0; j < k; j++) {
        long value = in.nextLong();
        if (j == 0) first = value;
        if (value < prev) ok = false;
        prev = value;
      }
      boxes[i] = new long[] {first, prev};
    }
    // Sorting by the first size, and then by the last, gives a valid order if any exists.
    Arrays.sort(
        boxes, (x, y) -> x[0] != y[0] ? Long.compare(x[0], y[0]) : Long.compare(x[1], y[1]));
    for (int i = 1; i < n; i++) {
      if (boxes[i - 1][1] > boxes[i][0]) ok = false;
    }
    System.out.println(ok ? "YES" : "NO");
  }
}
