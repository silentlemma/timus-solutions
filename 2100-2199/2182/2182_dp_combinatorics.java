import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  private static final int SMALL = 60; // only boxes up to the number of bits get extra bottles

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder all = new StringBuilder();
    String line;
    while ((line = in.readLine()) != null) all.append(line).append(' ');
    StringTokenizer tokens = new StringTokenizer(all.toString());
    int n = Integer.parseInt(tokens.nextToken());
    int q = Integer.parseInt(tokens.nextToken());
    long[][] binom = new long[n + 1][n + 1];
    for (int i = 0; i <= n; i++) {
      binom[i][0] = 1;
      for (int j = 1; j <= i; j++) binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
    }
    long top = (1L << n) - 1;
    int last = top < SMALL ? (int) top : SMALL;
    // Box k gets one bottle for every bottle placed in a box j != k with
    // popcount(j) = k; boxes above 60 hold only their own one, and the small
    // boxes are filled from the top down, as popcount(j) < j for j > 1.
    long[] count = new long[last + 1];
    for (int k = last; k >= 1; k--) {
      long total = 1 + (k <= n ? binom[n][k] : 0) - (k == 1 ? 1 : 0);
      for (int j = k + 1; j <= last; j++) {
        if (Integer.bitCount(j) == k) total += count[j] - 1;
      }
      count[k] = total;
    }
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < q; i++) {
      long a = Long.parseLong(tokens.nextToken());
      if (i > 0) out.append(' ');
      out.append(a <= last ? count[(int) a] : 1);
    }
    System.out.println(out);
  }
}
