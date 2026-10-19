import java.io.IOException;

public class Main {
  static final long MOD = 1000000007;
  static final int BUFFER_SIZE = 1 << 16;

  static long gcd(long a, long b) {
    while (b != 0) {
      long rest = a % b;
      a = b;
      b = rest;
    }
    return a;
  }
  static long columns(long n, long m, long k) {
    long end = n * m - 1, total = 0;
    for (long c = 0; c < n; c++) {
      long lower = c * m, upper = lower + m;
      long first = lower / k + 1, last = Math.min(upper, end) / k;
      if (last < first)
        continue;
      long count = last - first + 1, a, b;
      if (c % 2 == 0) {
        a = first * k - lower;
        b = last * k - lower;
      } else {
        a = upper - first * k;
        b = upper - last * k;
        if (b == 0)
          total++;
      }
      long pair = a + b;
      if (count % 2 == 0)
        count /= 2;
      else
        pair /= 2;
      total += (count % MOD) * (pair % MOD) % MOD;
      if (total >= MOD)
        total -= MOD;
    }
    return total;
  }
  static long residues(long n, long m, long k) {
    long period = 2 * m, g = gcd(k, period), length = period / g;
    long refills = (n * m - 1) / k, remainder = refills % length;
    long reverse = length - remainder - 1, work = Math.min(remainder, reverse), half = length / 2;
    long cycle = (g % MOD * (half % MOD) % MOD * ((length - half) % MOD) + 1) % MOD;
    long at = 0, step = k % period, prefix = 0;
    for (long i = 0; i < work; i++) {
      at += step;
      if (at >= period)
        at -= period;
      prefix += Math.min(at, period - at);
    }
    prefix %= MOD;
    if (reverse < remainder)
      prefix = (cycle - 1 - prefix + MOD) % MOD;
    return ((refills / length % MOD) * cycle % MOD + prefix) % MOD;
  }
  static long solve(long n, long m, long k) {
    long base = n * m - 1;
    if (k > base)
      return base % MOD;
    long length = 2 * m / gcd(k, 2 * m), remainder = base / k % length;
    long work = Math.min(remainder, length - remainder - 1);
    long extra = n < work ? columns(n, m, k) : residues(n, m, k);
    return (base % MOD + 2 * extra) % MOD;
  }
  static class Input {
    final byte[] buffer = new byte[BUFFER_SIZE];
    int at, size;
    int read() throws IOException {
      if (at == size) {
        size = System.in.read(buffer);
        at = 0;
        if (size < 0)
          return -1;
      }
      return buffer[at++];
    }
    long next() throws IOException {
      int c;
      do {
        c = read();
      } while (c >= 0 && c <= ' ');
      long value = 0;
      while (c > ' ') {
        value = 10 * value + c - '0';
        c = read();
      }
      return value;
    }
  }
  public static void main(String[] args) throws IOException {
    Input in = new Input();
    int tests = (int) in.next();
    StringBuilder out = new StringBuilder();
    for (int t = 0; t < tests; t++) out.append(solve(in.next(), in.next(), in.next())).append('\n');
    System.out.print(out);
  }
}
