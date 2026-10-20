import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  // The largest value over all knights but one, from the two largest; a missing
  // value is -1, so a lone knight needs nothing.
  private static final class TopTwo {
    long first = -1;
    long second = -1;
    int where = -1;

    void add(long value, int index) {
      if (value > first) {
        second = first;
        first = value;
        where = index;
      } else if (value > second) {
        second = value;
      }
    }

    long without(int index) {
      return index == where ? second : first;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(in.readLine().trim());
    long[] a = new long[n];
    long[] d = new long[n];
    long[] g = new long[n];
    TopTwo attack = new TopTwo(); // the strongest attack each rival can afford
    TopTwo shield = new TopTwo(); // and the strongest shield
    for (int i = 0; i < n; i++) {
      StringTokenizer line = new StringTokenizer(in.readLine());
      a[i] = Long.parseLong(line.nextToken());
      d[i] = Long.parseLong(line.nextToken());
      g[i] = Long.parseLong(line.nextToken());
      attack.add(a[i] + g[i], i);
      shield.add(d[i] + g[i], i);
    }
    for (int i = 0; i < n; i++) {
      // The shield must exceed every rival's best attack and the attack must
      // reach every rival's best shield, whatever the rivals do.
      long needShield = Math.max(0, attack.without(i) + 1 - d[i]);
      long cost = needShield + Math.max(0, shield.without(i) - a[i]);
      if (cost <= g[i]) {
        System.out.println(i + 1);
        return;
      }
    }
    System.out.println(-1);
  }
}
