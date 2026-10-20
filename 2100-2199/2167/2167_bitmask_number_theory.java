import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
  private static final int BITS = 20; // every number of the message is below 2^20

  public static void main(String[] args) throws IOException {
    int size = 1 << BITS;
    // has[j][x]: some prime below 2^20 has its top j bits equal to x
    boolean[][] has = new boolean[BITS + 1][];
    has[BITS] = new boolean[size];
    for (int i = 2; i < size; i++) has[BITS][i] = true;
    for (int i = 2; (long) i * i < size; i++) {
      if (has[BITS][i]) {
        for (int j = i * i; j < size; j += i) has[BITS][j] = false;
      }
    }
    for (int level = BITS - 1; level >= 0; level--) {
      has[level] = new boolean[1 << level];
      for (int x = 0; x < (1 << level); x++) {
        has[level][x] = has[level + 1][2 * x] || has[level + 1][2 * x + 1];
      }
    }
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int t = (int) in.nval;
    StringBuilder out = new StringBuilder();
    for (int q = 0; q < t; q++) {
      in.nextToken();
      int a = (int) in.nval;
      // The smallest key is the smallest a xor p over primes p below 2^20,
      // since a key below 2^20 reaches the prime 2; choose the bits of p
      // from the top, keeping the bit of a whenever some prime allows it.
      int prefix = 0;
      for (int bit = BITS - 1; bit >= 0; bit--) {
        int want = prefix * 2 + (a >> bit & 1);
        prefix = has[BITS - bit][want] ? want : want ^ 1;
      }
      out.append(a ^ prefix).append('\n');
    }
    System.out.print(out);
  }
}
