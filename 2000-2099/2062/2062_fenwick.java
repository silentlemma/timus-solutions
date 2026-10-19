import java.io.IOException;
import java.io.InputStream;

public class Main {
  private static final int INPUT_BUFFER = 65536;
  private static final int OUTPUT_BATCH = 1024;

  private static class FastInput {
    private final InputStream input = System.in;
    private final byte[] buffer = new byte[INPUT_BUFFER];
    private int at = 0, length = 0;
    private int read() throws IOException {
      if (at == length) {
        length = input.read(buffer);
        at = 0;
        if (length < 0)
          return -1;
      }
      return buffer[at++];
    }
    int next() throws IOException {
      int symbol;
      do {
        symbol = read();
      } while (symbol <= ' ' && symbol >= 0);
      int value = 0;
      while (symbol >= '0' && symbol <= '9') {
        value = value * 10 + symbol - '0';
        symbol = read();
      }
      return value;
    }
  }

  private static class Charges {
    private final int size;
    private final long[] initial, tree;
    private final int[] offsets;
    private final short[] divisors;
    Charges(long[] initial) {
      this.initial = initial;
      size = initial.length - 1;
      tree = new long[size + 1];
      offsets = new int[size + 2];
      for (int divisor = 1; divisor * divisor <= size; divisor++)
        for (int multiple = divisor * divisor; multiple <= size; multiple += divisor)
          offsets[multiple + 1]++;
      for (int index = 1; index <= size + 1; index++) offsets[index] += offsets[index - 1];
      divisors = new short[offsets[size + 1]];
      int[] cursor = offsets.clone();
      for (int divisor = 1; divisor * divisor <= size; divisor++)
        for (int multiple = divisor * divisor; multiple <= size; multiple += divisor)
          divisors[cursor[multiple]++] = (short) divisor;
    }
    void irradiate(int left, int right, long power) {
      for (int index = left; index <= size; index += index & -index) tree[index] += power;
      for (int index = right + 1; index <= size; index += index & -index) tree[index] -= power;
    }
    private long point(int index) {
      long result = 0;
      while (index > 0) {
        result += tree[index];
        index &= index - 1;
      }
      return result;
    }
    long measure(int index) {
      long result = initial[index];
      for (int at = offsets[index]; at < offsets[index + 1]; at++) {
        int divisor = divisors[at];
        int partner = index / divisor;
        result += point(divisor);
        if (partner != divisor)
          result += point(partner);
      }
      return result;
    }
  }

  public static void main(String[] args) throws IOException {
    FastInput input = new FastInput();
    int size = input.next();
    long[] initial = new long[size + 1];
    for (int index = 1; index <= size; index++) initial[index] = input.next();
    Charges charges = new Charges(initial);
    int count = input.next();
    StringBuilder output = new StringBuilder();
    int pending = 0;
    while (count-- > 0) {
      if (input.next() == 1) {
        output.append(charges.measure(input.next())).append('\n');
        if (++pending == OUTPUT_BATCH) {
          System.out.print(output);
          output.setLength(0);
          pending = 0;
        }
      } else {
        int left = input.next(), right = input.next();
        charges.irradiate(left, right, input.next());
      }
    }
    System.out.print(output);
  }
}
