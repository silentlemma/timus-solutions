import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    in.nextToken();
    long a = (long) in.nval;
    // plus and minus are the best sums of segments ending at the current dish
    // whose last dish counts with a plus or with a minus; before the second
    // dish no minus segment exists, and 0 there only means "start anew"
    long plus = a;
    long minus = 0;
    long best = Math.max(0, a);
    for (int i = 1; i < n; i++) {
      in.nextToken();
      a = (long) in.nval;
      long nextPlus = a + Math.max(0, minus);
      minus = plus - a;
      plus = nextPlus;
      best = Math.max(best, Math.max(plus, minus));
    }
    System.out.println(best);
  }
}
