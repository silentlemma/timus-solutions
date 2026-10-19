import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class Main {
  static final int OUTPUT_BUFFER = 1 << 16;
  static final int MAX_DIGITS = 10;

  static int edge(int parent, byte c, int[] head, int[] next, byte[] label) {
    for (int v = head[parent]; v != 0; v = next[v])
      if (label[v] == c)
        return v;
    return 0;
  }
  static int[] solve(byte[] word) {
    int n = word.length;
    byte[] text = new byte[n + 1];
    System.arraycopy(word, 0, text, 1, n);
    int[] length = new int[n + 2], link = new int[n + 2], diff = new int[n + 2];
    int[] series = new int[n + 2], cache = new int[n + 2];
    int[] head = new int[n + 2], next = new int[n + 2];
    byte[] label = new byte[n + 2];
    int[] dp = new int[n + 1];
    dp[0] = 1;
    length[0] = -1;
    int used = 2, last = 1;
    for (int i = 1; i <= n; i++) {
      int parent = last;
      while (text[i - 1 - length[parent]] != text[i]) parent = link[parent];
      int v = edge(parent, text[i], head, next, label);
      if (v == 0) {
        v = used++;
        next[v] = head[parent];
        head[parent] = v;
        label[v] = text[i];
        length[v] = length[parent] + 2;
        if (length[v] == 1)
          link[v] = 1;
        else {
          int candidate = link[parent];
          while (text[i - 1 - length[candidate]] != text[i]) candidate = link[candidate];
          link[v] = edge(candidate, text[i], head, next, label);
        }
        int suffix = link[v];
        diff[v] = length[v] - length[suffix];
        series[v] = diff[v] == diff[suffix] ? series[suffix] : suffix;
      }
      last = v;
      int value = 0;
      while (length[v] > 0) {
        int cut = i - length[series[v]] - diff[v], suffix = link[v];
        cache[v] = dp[cut];
        if (diff[v] == diff[suffix])
          cache[v] |= cache[suffix];
        value |= cache[v] << 1;
        v = series[v];
      }
      dp[i] = value;
    }
    return dp;
  }
  static class Output {
    final byte[] buffer = new byte[OUTPUT_BUFFER], digits = new byte[MAX_DIGITS];
    int size;
    void print(int value) throws IOException {
      if (size + MAX_DIGITS + 1 > buffer.length)
        flush();
      int count = 0;
      do {
        digits[count++] = (byte) ('0' + value % 10);
        value /= 10;
      } while (value > 0);
      while (count > 0) buffer[size++] = digits[--count];
      buffer[size++] = '\n';
    }
    void flush() throws IOException {
      System.out.write(buffer, 0, size);
      size = 0;
    }
  }
  public static void main(String[] args) throws IOException {
    BufferedReader in =
        new BufferedReader(new InputStreamReader(System.in, StandardCharsets.US_ASCII));
    byte[] word = in.readLine().trim().getBytes(StandardCharsets.US_ASCII);
    int[] dp = solve(word);
    Output out = new Output();
    for (int i = 1; i < dp.length; i++) out.print(dp[i] >>> 1);
    out.flush();
  }
}
