import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
  private static final int SHORT = 32; // cycles up to this length are summed directly
  private static final long[] MODS = {998244353, 167772161, 469762049}; // NTT primes, root 3
  private static final long ROOT = 3;
  private static final int SPAN = 3; // a product of L and 2L numbers has fewer than 3L

  private static long power(long b, long e, long mod) {
    long r = 1;
    for (b %= mod; e > 0; e >>= 1, b = b * b % mod) if ((e & 1) == 1) r = r * b % mod;
    return r;
  }

  private static void ntt(long[] a, boolean invert, long mod) {
    int n = a.length;
    for (int i = 1, j = 0; i < n; i++) {
      int bit = n >> 1;
      for (; (j & bit) != 0; bit >>= 1) j ^= bit;
      j ^= bit;
      if (i < j) {
        long t = a[i];
        a[i] = a[j];
        a[j] = t;
      }
    }
    for (int len = 2; len <= n; len <<= 1) {
      long w = power(ROOT, (mod - 1) / len, mod);
      if (invert) w = power(w, mod - 2, mod);
      int half = len / 2;
      for (int i = 0; i < n; i += len) {
        long wn = 1;
        for (int k = 0; k < half; k++, wn = wn * w % mod) {
          long u = a[i + k];
          long v = a[i + k + half] * wn % mod;
          a[i + k] = (u + v) % mod;
          a[i + k + half] = (u + mod - v) % mod;
        }
      }
    }
    if (invert) {
      long inv = power(n, mod - 2, mod);
      for (int i = 0; i < n; i++) a[i] = a[i] * inv % mod;
    }
  }

  // out[s] = sum over r of fold[r] * cycle[(s + r) mod L]; every sum is below 2^63
  private static long[] cyclic(long[] fold, long[] cycle) {
    int size = cycle.length;
    long[] out = new long[size];
    if (size <= SHORT) {
      for (int s = 0; s < size; s++)
        for (int r = 0; r < size; r++) out[s] += fold[r] * cycle[(s + r) % size];
      return out;
    }
    // reversed fold times the cycle written twice, modulo three primes,
    // put together by Garner's method; wrapping 64-bit arithmetic is exact here
    int n = 1;
    while (n < SPAN * size) n <<= 1;
    long[][] residue = new long[MODS.length][];
    for (int k = 0; k < MODS.length; k++) {
      long mod = MODS[k];
      long[] a = new long[n];
      long[] b = new long[n];
      for (int r = 0; r < size; r++) a[size - 1 - r] = fold[r] % mod;
      for (int i = 0; i < 2 * size; i++) b[i] = cycle[i % size] % mod;
      ntt(a, false, mod);
      ntt(b, false, mod);
      for (int i = 0; i < n; i++) a[i] = a[i] * b[i] % mod;
      ntt(a, true, mod);
      residue[k] = a;
    }
    long m0 = MODS[0];
    long m1 = MODS[1];
    long m2 = MODS[2];
    long inv01 = power(m0 % m1, m1 - 2, m1);
    long inv012 = power(m0 * m1 % m2, m2 - 2, m2);
    for (int s = 0; s < size; s++) {
      int i = s + size - 1;
      long x0 = residue[0][i];
      long x1 = (residue[1][i] + m1 - x0 % m1) % m1 * inv01 % m1;
      long low = (x0 + x1 * m0) % m2;
      long x2 = (residue[2][i] + m2 - low) % m2 * inv012 % m2;
      out[s] = x0 + x1 * m0 + x2 * m0 * m1;
    }
    return out;
  }

  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int m = (int) in.nval;
    in.nextToken();
    int n = (int) in.nval;
    int[] p = new int[n];
    for (int i = 0; i < n; i++) {
      in.nextToken();
      p[i] = (int) in.nval - 1;
    }
    long[] byYear = new long[m + 1]; // byYear[t] = q_t
    for (int t = 1; t <= m; t++) {
      in.nextToken();
      byYear[t] = (long) in.nval;
    }
    // the year t row is p applied t times, so the answer at j is the sum of
    // q_t p^t(j); along a cycle of p this is a cyclic correlation
    long[] answer = new long[n];
    boolean[] seen = new boolean[n];
    Map<Integer, long[]> folds = new HashMap<>(); // cycle length -> sums over equal remainders
    for (int start = 0; start < n; start++) {
      if (seen[start]) continue;
      List<Integer> cycle = new ArrayList<>();
      for (int j = start; !seen[j]; j = p[j]) {
        seen[j] = true;
        cycle.add(j);
      }
      int size = cycle.size();
      long[] fold = folds.get(size);
      if (fold == null) {
        fold = new long[size];
        for (int t = 1; t <= m; t++) fold[t % size] += byYear[t];
        folds.put(size, fold);
      }
      long[] values = new long[size];
      for (int s = 0; s < size; s++) values[s] = cycle.get(s) + 1;
      values = cyclic(fold, values);
      for (int s = 0; s < size; s++) answer[cycle.get(s)] = values[s];
    }
    StringBuilder out = new StringBuilder();
    for (int j = 0; j < n; j++) out.append(j > 0 ? " " : "").append(answer[j]);
    System.out.println(out);
  }
}
