import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  private static StringTokenizer tokens;
  private static BufferedReader in;

  private static long next() throws IOException {
    while (tokens == null || !tokens.hasMoreTokens()) tokens = new StringTokenizer(in.readLine());
    return Long.parseLong(tokens.nextToken());
  }

  private static long[] secondDifferences(long[] h) {
    long[] d = new long[Math.max(0, h.length - 2)];
    for (int i = 0; i < d.length; i++) d[i] = h[i + 2] - 2 * h[i + 1] + h[i];
    return d;
  }

  public static void main(String[] args) throws IOException {
    in = new BufferedReader(new InputStreamReader(System.in));
    int n = (int) next();
    int m = (int) next();
    long[] x = new long[m + 1];
    for (int i = 0; i <= m; i++) x[i] = next();
    // a section is similar exactly when the second differences agree, and then
    // a is the difference of the first steps of the two sections
    long[] pattern = secondDifferences(x);
    int len = pattern.length;
    int[] pi = new int[len];
    for (int i = 1; i < len; i++) {
      int k = pi[i - 1];
      while (k > 0 && pattern[i] != pattern[k]) k = pi[k - 1];
      if (pattern[i] == pattern[k]) k++;
      pi[i] = k;
    }
    boolean found = false;
    long bestA = 0;
    int bestSlope = 0;
    int bestStart = 0;
    for (int slope = 1; slope <= n; slope++) {
      int length = (int) next();
      long[] y = new long[length + 1];
      for (int i = 0; i <= length; i++) y[i] = next();
      if (length < m) continue;
      long[] text = secondDifferences(y);
      int k = 0;
      for (int i = 0; i <= text.length; i++) {
        if (k == len) {
          int start = i - len;
          long a = Math.abs((x[1] - x[0]) - (y[start + 1] - y[start]));
          if (!found || a < bestA) {
            found = true;
            bestA = a;
            bestSlope = slope;
            bestStart = start;
          }
          if (len > 0) k = pi[k - 1];
        }
        if (i == text.length || len == 0) continue;
        while (k > 0 && text[i] != pattern[k]) k = pi[k - 1];
        if (text[i] == pattern[k]) k++;
      }
    }
    System.out.println(found ? bestSlope + " " + bestStart : "-1");
  }
}
