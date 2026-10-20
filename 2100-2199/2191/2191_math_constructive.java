import java.io.DataInputStream;
import java.io.IOException;

public class Main {
  private static final int BUFFER_SIZE = 1 << 16;
  private static final int DIGITS = 18;
  private static DataInputStream in = new DataInputStream(System.in);
  private static byte[] buffer = new byte[BUFFER_SIZE];
  private static int length = 0;
  private static int pointer = 0;
  private static StringBuilder out = new StringBuilder();

  private static int read() throws IOException {
    if (pointer == length) {
      length = in.read(buffer, 0, buffer.length);
      pointer = 0;
      if (length <= 0) {
        return -1;
      }
    }
    return buffer[pointer++];
  }

  private static long nextLong() throws IOException {
    int c = read();
    while (c != '-' && (c < '0' || c > '9')) {
      c = read();
    }
    boolean negative = c == '-';
    if (negative) {
      c = read();
    }
    long value = 0;
    while (c >= '0' && c <= '9') {
      value = value * 10 + (c - '0');
      c = read();
    }
    return negative ? -value : value;
  }

  /** Appends a nonnegative fraction with at most DIGITS decimals, truncated. */
  private static void number(long numerator, long denominator) {
    out.append(numerator / denominator);
    long rest = numerator % denominator;
    if (rest == 0) {
      return;
    }
    out.append('.');
    for (int i = 0; i < DIGITS; i++) {
      rest *= 10;
      out.append((char) ('0' + rest / denominator));
      rest %= denominator;
    }
    int end = out.length();
    while (out.charAt(end - 1) == '0') {
      end--;
    }
    if (out.charAt(end - 1) == '.') {
      end--;
    }
    out.setLength(end);
  }

  /** Writes c |x - root| with c = numerator / denominator as one term. */
  private static void term(long numerator, long denominator, long root, boolean constant) {
    if (numerator < 0) {
      out.append('-');
      numerator = -numerator;
    } else if (out.length() > 0) {
      out.append('+');
    }
    out.append('|');
    if (constant) {
      out.append("0x+");
      number(numerator, denominator);
    } else {
      long shift = numerator * root;
      number(numerator, denominator);
      out.append(shift >= 0 ? "x-" : "x+");
      number(Math.abs(shift), denominator);
    }
    out.append('|');
  }

  public static void main(String[] args) throws IOException {
    int n = (int) nextLong();
    long[] xs = new long[n];
    long[] ys = new long[n];
    for (int i = 0; i < n; i++) {
      xs[i] = nextLong();
      ys[i] = nextLong();
    }
    // A kink at x_i where the slope turns from s to t is (t - s) / 2 |x - x_i|.
    for (int i = 1; i + 1 < n; i++) {
      long leftDx = xs[i] - xs[i - 1];
      long leftDy = ys[i] - ys[i - 1];
      long rightDx = xs[i + 1] - xs[i];
      long rightDy = ys[i + 1] - ys[i];
      term(rightDy * leftDx - leftDy * rightDx, 2 * leftDx * rightDx, xs[i], false);
    }
    long firstDx = xs[1] - xs[0];
    long firstDy = ys[1] - ys[0];
    long lastDx = xs[n - 1] - xs[n - 2];
    long lastDy = ys[n - 1] - ys[n - 2];
    // On [x_1, x_N] the kinks add (t - s) / 2 times x - x_i; the term at x_1
    // restores the first slope and a constant fixes the value at x_1.
    term(firstDy * lastDx + lastDy * firstDx, 2 * firstDx * lastDx, xs[0], false);
    long span = xs[n - 2] - xs[0];
    term(2 * ys[0] * lastDx - lastDy * span + (ys[n - 2] - ys[0]) * lastDx, 2 * lastDx, 0, true);
    out.append('\n');
    byte[] bytes = new byte[out.length()];
    for (int i = 0; i < bytes.length; i++) {
      bytes[i] = (byte) out.charAt(i);
    }
    System.out.write(bytes, 0, bytes.length);
    System.out.flush();
  }
}
