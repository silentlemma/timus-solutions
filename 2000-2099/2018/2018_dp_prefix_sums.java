import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final long MOD = 1000000007L;
  static final int SPACE = 32;
  static final int RADIX = 10;

  static int readInt(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= SPACE && c >= 0);
    int value = 0;
    while (c > SPACE) {
      value = value * RADIX + c - '0';
      c = in.read();
    }
    return value;
  }

  static long solve(int n, int a, int b) {
    long[] endsOne = new long[b + 1];
    long[] endsTwo = new long[a + 1];
    endsOne[0] = endsTwo[0] = 1;
    long windowOne = 1, windowTwo = 1, lastOne = 0, lastTwo = 0;
    for (int length = 1; length <= n; length++) {
      lastOne = windowOne;
      lastTwo = windowTwo;
      long expiredTwo = length >= a ? endsTwo[(length - a) % (a + 1)] : 0;
      long expiredOne = length >= b ? endsOne[(length - b) % (b + 1)] : 0;
      windowOne = (windowOne + lastTwo + MOD - expiredTwo) % MOD;
      windowTwo = (windowTwo + lastOne + MOD - expiredOne) % MOD;
      endsOne[length % (b + 1)] = lastOne;
      endsTwo[length % (a + 1)] = lastTwo;
    }
    return (lastOne + lastTwo) % MOD;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int n = readInt(in), a = readInt(in), b = readInt(in);
    System.out.println(solve(n, a, b));
  }
}
