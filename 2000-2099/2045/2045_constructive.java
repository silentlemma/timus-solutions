import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
  static final String TAIL = "bcd";

  static String wordFor(int n, int count, String tail) {
    if (count < Math.min(n, TAIL.length()))
      return "NO";
    char[] word = new char[n];
    int prefix = n < TAIL.length() ? n : count - TAIL.length();
    for (int at = 0; at < n; at++) word[at] = at < prefix ? 'a' : tail.charAt(at - prefix);
    return new String(word);
  }

  static void solve(int n, BufferedWriter out) throws IOException {
    StringBuilder repeated = new StringBuilder();
    while (repeated.length() < n) repeated.append(TAIL);
    String tail = repeated.toString();
    for (int count = 1; count <= n; count++) {
      out.write(Integer.toString(count));
      out.write(" : ");
      out.write(wordFor(n, count, tail));
      out.newLine();
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
    solve(Integer.parseInt(in.readLine().trim()), out);
    out.flush();
  }
}
