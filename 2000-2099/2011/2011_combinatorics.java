import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  private static final int ALPHABET = 3;
  private static final int TARGET = 6;

  private static boolean solve(int[] values) {
    int[] counts = new int[ALPHABET];
    int ways = 1, length = 0;
    for (int value : values) {
      ++length;
      ++counts[value - 1];
      ways = ways * length / counts[value - 1];
      if (ways >= TARGET)
        return true;
    }
    return false;
  }

  private static int readInt(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= ' ' && c >= 0);
    int value = 0;
    while (c > ' ') {
      value = value * 10 + c - '0';
      c = in.read();
    }
    return value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int n = readInt(in);
    int[] values = new int[n];
    for (int i = 0; i < n; ++i) values[i] = readInt(in);
    System.out.println(solve(values) ? "Yes" : "No");
  }
}
