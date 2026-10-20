import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    long[] a = new long[n];
    for (int i = 0; i < n; i++) {
      in.nextToken();
      a[i] = (long) in.nval;
    }
    // Around the circle the rises and the falls cancel out, so the
    // conversations where the next friend is less interesting sum to the same
    // as those where the next one is more interesting; equal neighbours add 0.
    List<Integer> falls = new ArrayList<>();
    List<Integer> rises = new ArrayList<>();
    List<Integer> ties = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      long next = a[(i + 1) % n];
      if (a[i] > next) {
        falls.add(i + 1);
      } else if (a[i] < next) {
        rises.add(i + 1);
      } else {
        ties.add(i + 1);
      }
    }
    if (falls.isEmpty()) {
      // every difference is 0: one conversation against all the others
      falls.add(ties.remove(ties.size() - 1));
    }
    rises.addAll(ties);
    StringBuilder out = new StringBuilder("YES\n");
    for (List<Integer> part : Arrays.asList(falls, rises)) {
      out.append(part.size()).append('\n');
      for (int i = 0; i < part.size(); i++) {
        out.append(part.get(i)).append(i + 1 < part.size() ? ' ' : '\n');
      }
    }
    System.out.print(out);
  }
}
