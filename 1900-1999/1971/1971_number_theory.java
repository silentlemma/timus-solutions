import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

public class Main {
  static final int FACTOR_LIMIT = 100;
  static final int LOW_FPS = 10;
  static final int HIGH_FPS = 60;
  static final int NAME_BASE = 27;
  static final int BUFFER_SIZE = 65536;
  static final int DECIMAL_BASE = 10;

  static class FastInput {
    final InputStream input = System.in;
    final byte[] buffer = new byte[BUFFER_SIZE];
    int position, length;

    int read() throws IOException {
      if (position == length) {
        length = input.read(buffer);
        position = 0;
        if (length < 0)
          return -1;
      }
      return buffer[position++];
    }

    int first() throws IOException {
      int c;
      do {
        c = read();
      } while (c >= 0 && c <= ' ');
      return c;
    }

    int nextInt() throws IOException {
      int c = first(), value = 0;
      while (c > ' ') {
        value = value * DECIMAL_BASE + c - '0';
        c = read();
      }
      return value;
    }

    long nextName() throws IOException {
      int c = first();
      long value = 0;
      while (c > ' ') {
        value = value * NAME_BASE + c - 'a' + 1;
        c = read();
      }
      return value;
    }

    int nextAction() throws IOException {
      int first = first(), second = read();
      int result = first == 'R' ? 0 : second == 'n' ? 1 : -1;
      int c = second;
      while (c > ' ') c = read();
      return result;
    }
  }

  static class FactorTable {
    final int[][] factors = new int[FACTOR_LIMIT + 1][FACTOR_LIMIT + 1];
    final int[] primes = new int[FACTOR_LIMIT];
    int size;

    FactorTable() {
      for (int value = 2; value <= FACTOR_LIMIT; value++) {
        int remaining = value;
        for (int i = 0; i < size; i++) {
          int prime = primes[i];
          while (remaining % prime == 0) {
            remaining /= prime;
            factors[value][prime]++;
          }
        }
        if (remaining > 1) {
          factors[value][remaining]++;
          if (remaining == value)
            primes[size++] = value;
        }
      }
    }
  }

  static String classify(int width, int height, int power, int[] counts, FactorTable table) {
    int area = width * height, limit = power / (LOW_FPS * area);
    if (limit == 0)
      return "Slideshow";
    int product = 1;
    for (int i = 0; i < table.size; i++) {
      int prime = table.primes[i];
      for (int step = 0; step < counts[prime]; step++) {
        if (product > limit / prime)
          return "Slideshow";
        product *= prime;
      }
    }
    return product <= power / (HIGH_FPS * area) ? "Perfect" : "So-so";
  }

  static void update(int[] counts, FactorTable table, int factor, int change) {
    for (int i = 0; i < table.size; i++) {
      int prime = table.primes[i];
      counts[prime] += change * table.factors[factor][prime];
    }
  }

  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    FactorTable table = new FactorTable();
    int[] counts = new int[FACTOR_LIMIT + 1];
    int n = in.nextInt();
    Map<Long, Integer> options = new HashMap<>();
    for (int i = 0; i < n; i++) {
      long name = in.nextName();
      int factor = in.nextInt();
      options.put(name, factor);
      update(counts, table, factor, 1);
    }
    int width = in.nextInt(), height = in.nextInt(), power = in.nextInt();
    int changes = in.nextInt();
    StringBuilder out = new StringBuilder();
    out.append(classify(width, height, power, counts, table)).append('\n');
    for (int i = 0; i < changes; i++) {
      int action = in.nextAction();
      if (action == 0) {
        width = in.nextInt();
        height = in.nextInt();
      } else {
        int factor = options.get(in.nextName());
        update(counts, table, factor, action);
      }
      out.append(classify(width, height, power, counts, table)).append('\n');
    }
    System.out.print(out);
  }
}
