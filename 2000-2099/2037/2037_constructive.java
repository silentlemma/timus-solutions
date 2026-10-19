import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
  static final int SMALL_LIMIT = 7, STABLE_MIN = 8, EXTRA_COUNT = 6;
  static final String PERIOD = "babbaa";
  static String construct(int n, int count) {
    int minimum = n <= SMALL_LIMIT ? n : (n == STABLE_MIN ? SMALL_LIMIT : STABLE_MIN);
    if (count < minimum)
      return "NO";
    if (n == STABLE_MIN && count < n)
      return "aababbaa";
    char[] word = new char[n];
    Arrays.fill(word, 'a');
    if (count < n) {
      int run = count - EXTRA_COUNT;
      for (int at = run; at < n; at++) word[at] = PERIOD.charAt((at - run) % PERIOD.length());
    }
    return new String(word);
  }
  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(in.readLine().trim());
    BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
    for (int count = 1; count <= n; count++) {
      out.write(Integer.toString(count));
      out.write(" : ");
      out.write(construct(n, count));
      out.newLine();
    }
    out.flush();
  }
}
