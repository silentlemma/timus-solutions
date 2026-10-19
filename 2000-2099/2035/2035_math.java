import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static long[] solve(long x, long y, long total) {
    long a = Math.min(x, total), b = total - a;
    if (b > y)
      return null;
    return new long[] {a, b};
  }

  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    String line = input.readLine();
    if (line == null)
      return;
    StringTokenizer tokens = new StringTokenizer(line);
    long x = Long.parseLong(tokens.nextToken()), y = Long.parseLong(tokens.nextToken());
    long total = Long.parseLong(tokens.nextToken());
    long[] answer = solve(x, y, total);
    if (answer == null)
      System.out.println("Impossible");
    else
      System.out.println(answer[0] + " " + answer[1]);
  }
}
