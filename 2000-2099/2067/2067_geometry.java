import java.io.DataInputStream;
import java.io.IOException;

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

  private static long readLong() throws IOException {
    int c = read();
    while (c != '-' && (c < '0' || c > '9')) c = read();
    boolean negative = c == '-';
    if (negative) c = read();
    long v = 0;
    for (; c >= '0' && c <= '9'; c = read()) v = v * 10 + (c - '0');
    return negative ? -v : v;
  }

  public static void main(String[] args) throws IOException {
    int n = (int) readLong();
    long[] s = new long[n], r = new long[n];
    for (int i = 0; i < n; ++i) {
      s[i] = readLong();
      r[i] = readLong();
    }
    // v, u are best friends exactly when every other point lies on the
    // segment vu: all points collinear, v and u the two extreme ones
    int low = 0, high = 0;
    for (int i = 1; i < n; ++i) {
      if ((s[1] - s[0]) * (r[i] - r[0]) != (s[i] - s[0]) * (r[1] - r[0])) {
        System.out.println(0);
        return;
      }
      if (s[i] < s[low] || (s[i] == s[low] && r[i] < r[low])) low = i;
      if (s[i] > s[high] || (s[i] == s[high] && r[i] > r[high])) high = i;
    }
    System.out.println(1);
    System.out.println((low + 1) + " " + (high + 1));
  }
}
