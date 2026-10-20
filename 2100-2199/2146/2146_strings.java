import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  private static final int LETTERS = 26;

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer first = new StringTokenizer(in.readLine());
    int n = Integer.parseInt(first.nextToken());
    int k = Integer.parseInt(first.nextToken());
    char[] s = in.readLine().trim().toCharArray();
    // On a circle every period can be replaced by its gcd with n, so only the
    // divisors of n are tried, from the smallest.
    for (int d = 1; d <= n; d++) {
      if (n % d != 0) continue;
      int[] count = new int[d * LETTERS];
      for (int i = 0; i < n; i++) count[(i % d) * LETTERS + (s[i] - 'a')]++;
      char[] best = new char[d];
      int changes = n;
      for (int r = 0; r < d; r++) {
        int top = 0;
        for (int c = 1; c < LETTERS; c++) {
          if (count[r * LETTERS + c] > count[r * LETTERS + top]) top = c;
        }
        best[r] = (char) ('a' + top);
        changes -= count[r * LETTERS + top];
      }
      if (changes <= k) {
        for (int i = 0; i < n; i++) s[i] = best[i % d];
        System.out.println(d);
        System.out.println(new String(s));
        return;
      }
    }
  }
}
