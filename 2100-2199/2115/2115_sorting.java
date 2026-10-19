import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
  private static final int SWAPPED = 2; // a single swap changes exactly two places

  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    long[] a = new long[n];
    for (int i = 0; i < n; i++) {
      in.nextToken();
      a[i] = (long) in.nval;
    }
    long[] ascending = a.clone();
    Arrays.sort(ascending);
    long[] descending = new long[n];
    for (int i = 0; i < n; i++) descending[n - 1 - i] = ascending[i];
    if (Arrays.equals(a, ascending) || Arrays.equals(a, descending)) {
      System.out.println("Nothing to do here");
      return;
    }
    // one swap can only fix a line that differs from a sorted one in exactly
    // two places, and then the swap of those two places does it
    for (long[] t : new long[][] {ascending, descending}) {
      int[] wrong = new int[SWAPPED + 1];
      int count = 0;
      for (int i = 0; i < n && count <= SWAPPED; i++) if (a[i] != t[i]) wrong[count++] = i;
      if (count != SWAPPED) continue;
      int i = wrong[0];
      int j = wrong[1];
      if (a[i] == t[j] && a[j] == t[i]) {
        System.out.println("Yes");
        System.out.println((i + 1) + " " + (j + 1));
        return;
      }
    }
    System.out.println("No hope");
  }
}
