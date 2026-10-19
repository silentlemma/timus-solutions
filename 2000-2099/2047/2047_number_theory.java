import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
  static final int MAX_TERM = 300;
  static final int BLOCK_SIZE = 1 << 16;
  static final int RING_SIZE = MAX_TERM + 1;

  static List<Integer> primesUpTo(int bound) {
    boolean[] composite = new boolean[bound + 1];
    List<Integer> primes = new ArrayList<>();
    for (int p = 2; p <= bound; p++)
      if (!composite[p]) {
        primes.add(p);
        for (int multiple = p * p; multiple <= bound; multiple += p) composite[multiple] = true;
      }
    return primes;
  }

  static short[] divisorBlock(int left, int right, List<Integer> primes) {
    int size = right - left + 1;
    int[] remaining = new int[size];
    short[] counts = new short[size];
    Arrays.fill(counts, (short) 1);
    for (int i = 0; i < size; i++) remaining[i] = left + i;
    for (int p : primes) {
      if (p * p > right)
        break;
      for (int offset = (p - left % p) % p; offset < size; offset += p) {
        int exponent = 0;
        while (remaining[offset] % p == 0) {
          remaining[offset] /= p;
          exponent++;
        }
        counts[offset] *= exponent + 1;
      }
    }
    for (int i = 0; i < size; i++)
      if (remaining[i] > 1)
        counts[i] *= 2;
    return counts;
  }

  static int[] solve(int n) {
    int limit = MAX_TERM * n, root = 1;
    while ((root + 1) * (root + 1) <= limit) root++;
    List<Integer> primes = primesUpTo(root);
    short[] history = new short[BLOCK_SIZE];
    int used = 0;
    int[] depth = new int[RING_SIZE];
    for (int left = 1; left <= limit; left += BLOCK_SIZE) {
      int right = Math.min(limit, left + BLOCK_SIZE - 1);
      short[] counts = divisorBlock(left, right, primes);
      for (int offset = 0; offset < counts.length; offset++) {
        int total = left + offset, term = counts[offset];
        if (used == history.length)
          history = Arrays.copyOf(history, history.length * 2);
        history[used++] = counts[offset];
        int current = total <= MAX_TERM ? 1 : 0;
        if (term <= MAX_TERM && total > term) {
          int previous = depth[(total - term) % RING_SIZE];
          if (previous > 0)
            current = Math.max(current, previous + 1);
        }
        depth[total % RING_SIZE] = current;
        if (current >= n) {
          int[] answer = new int[n];
          for (int i = n - 1; i > 0; i--) {
            answer[i] = history[total - 1];
            total -= answer[i];
          }
          answer[0] = total;
          return answer;
        }
      }
    }
    return new int[0];
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    int[] answer = solve(Integer.parseInt(in.readLine().trim()));
    if (answer.length == 0) {
      System.out.println("Impossible");
      return;
    }
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < answer.length; i++) {
      if (i > 0)
        out.append(' ');
      out.append(answer[i]);
    }
    System.out.println(out);
  }
}
