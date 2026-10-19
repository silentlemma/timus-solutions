import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class Main {
  private static final int PERSISTENT_COUNT = 3;
  private static final int BASE = 10;

  private static int readInt(BufferedInputStream input) throws IOException {
    int ch;
    do {
      ch = input.read();
    } while (ch <= ' ' && ch != -1);
    int value = 0;
    while (ch > ' ') {
      value = value * BASE + ch - '0';
      ch = input.read();
    }
    return value;
  }

  private static String solve(int[] values) {
    int maximum = 0;
    for (int value : values) maximum = Math.max(maximum, value);
    int limit = 0;
    while ((limit + 1) * (limit + 1) <= maximum) limit++;
    boolean[] composite = new boolean[limit + 1];
    ArrayList<Integer> primes = new ArrayList<>();
    for (int prime = 2; prime <= limit; prime++) {
      if (composite[prime])
        continue;
      primes.add(prime);
      for (int multiple = prime * prime; multiple <= limit; multiple += prime)
        composite[multiple] = true;
    }
    HashMap<Integer, Integer> counts = new HashMap<>();
    int best = 0;
    for (int value : values) {
      for (int prime : primes) {
        if (prime * prime > value)
          break;
        if (value % prime != 0)
          continue;
        int count = counts.getOrDefault(prime, 0) + 1;
        counts.put(prime, count);
        if (count == PERSISTENT_COUNT)
          return "infinity";
        best = Math.max(best, count);
        while (value % prime == 0) value /= prime;
      }
      if (value > 1) {
        int count = counts.getOrDefault(value, 0) + 1;
        counts.put(value, count);
        if (count == PERSISTENT_COUNT)
          return "infinity";
        best = Math.max(best, count);
      }
    }
    return Integer.toString(best);
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream input = new BufferedInputStream(System.in);
    int size = readInt(input);
    int[] values = new int[size];
    for (int i = 0; i < size; i++) values[i] = readInt(input);
    System.out.println(solve(values));
  }
}
