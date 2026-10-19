import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;

public class Main {
  private static final int BUFFER = 1 << 16;
  private static final DataInputStream IN = new DataInputStream(System.in);
  private static final byte[] DATA = new byte[BUFFER];
  private static int length = 0, position = 0;

  private static int read() throws IOException {
    if (position == length) {
      length = IN.read(DATA, 0, BUFFER);
      position = 0;
      if (length <= 0) return -1;
    }
    return DATA[position++];
  }

  private static int readInt() throws IOException {
    int c = read();
    while (c < '0') c = read();
    int v = 0;
    for (; c >= '0'; c = read()) v = v * 10 + (c - '0');
    return v;
  }

  public static void main(String[] args) throws IOException {
    int n = readInt();
    int[] tall = new int[n];
    for (int i = 0; i < n; ++i) tall[i] = readInt();
    int q = readInt();
    int[] x = new int[q];
    int most = 0;
    for (int i = 0; i < q; ++i) most = Math.max(most, x[i] = readInt());
    // tent of height t at every odd multiple of t; the envelope of all
    // tents is the answer, and centres beyond 2 * most never matter
    int limit = 2 * most;
    int[] height = new int[limit + 1];
    Arrays.sort(tall);
    for (int i = 0; i < n; ++i) {
      int t = tall[i];
      if (i > 0 && t == tall[i - 1]) continue;
      if (t >= most) {
        height[most] = most;
        break;
      }
      for (int c = t; c <= limit; c += 2 * t) height[c] = t;
    }
    // best[x] = max over c of height[c] - |x - c|, by two sweeps
    for (int i = 1; i <= limit; ++i) height[i] = Math.max(height[i], height[i - 1] - 1);
    for (int i = limit - 1; i >= 0; --i) height[i] = Math.max(height[i], height[i + 1] - 1);
    StringBuilder out = new StringBuilder();
    for (int v : x) out.append(height[v]).append('\n');
    PrintWriter writer = new PrintWriter(System.out);
    writer.print(out);
    writer.flush();
  }
}
