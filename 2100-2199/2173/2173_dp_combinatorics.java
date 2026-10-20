import java.util.Scanner;

public class Main {
  private static final long MOD = 1000000007L;

  private static long power(long base, long exponent) {
    long result = 1;
    base %= MOD;
    while (exponent > 0) {
      if ((exponent & 1) == 1) result = result * base % MOD;
      base = base * base % MOD;
      exponent >>= 1;
    }
    return result;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int m = in.nextInt();
    int[] wishes = new int[n];
    for (int i = 0; i < n; i++) wishes[i] = in.nextInt();
    long[] fact = new long[m + 1];
    long[] inv = new long[m + 1];
    fact[0] = 1;
    for (int i = 1; i <= m; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[m] = power(fact[m], MOD - 2);
    for (int i = m; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;

    // ways[j]: the sponsors so far fill exactly j problems once; with t
    // mentions placed, (t - j) / 2 problems hold two sponsors and the rest none
    long[] ways = new long[m + 1];
    ways[0] = 1;
    int placed = 0;
    for (int s : wishes) {
      long[] next = new long[m + 1];
      for (int j = placed % 2; j <= m; j += 2) {
        if (ways[j] == 0) continue;
        int empty = m - j - (placed - j) / 2;
        // a of the new mentions go to problems with one sponsor, the
        // other s - a to empty problems
        long base = ways[j] * fact[j] % MOD * fact[empty] % MOD;
        int from = Math.max(0, s - empty);
        int to = Math.min(s, j);
        for (int a = from; a <= to; a++) {
          int rest = s - a;
          long term = base * inv[a] % MOD * inv[j - a] % MOD;
          term = term * inv[rest] % MOD * inv[empty - rest] % MOD;
          int target = j - a + rest;
          next[target] = (next[target] + term) % MOD;
        }
      }
      ways = next;
      placed += s;
    }
    long answer = 0;
    for (long w : ways) answer = (answer + w) % MOD;
    System.out.println(answer);
  }
}
