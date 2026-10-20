import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
  private static final long LIMIT = 1000000000L; // the largest absolute mood

  private static long[] a;
  private static long smallest = LIMIT;

  private static boolean possible(long x) {
    // Every mood below x must be flipped, so the shortest segment covers them
    // all, and every mood inside must become at least x.
    int first = -1;
    int last = -1;
    for (int i = 0; i < a.length; i++) {
      if (a[i] < x) {
        if (first < 0) first = i;
        last = i;
      }
    }
    if (first < 0) return smallest <= -x; // some single mood can still be flipped
    for (int i = first; i <= last; i++) {
      if (a[i] > -x) return false;
    }
    return true;
  }

  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    a = new long[n];
    for (int i = 0; i < n; i++) {
      in.nextToken();
      a[i] = (long) in.nval;
      smallest = Math.min(smallest, a[i]);
    }
    long lo = -LIMIT;
    long hi = LIMIT;
    while (lo < hi) {
      long middle = lo + (hi - lo + 1) / 2;
      if (possible(middle)) {
        lo = middle;
      } else {
        hi = middle - 1;
      }
    }
    System.out.println(lo);
  }
}
