import java.util.Random;

public class Main {
  static final int BUFFER = 1 << 16; // bytes read from the input at a time
  private static final int MINIMUM_BASE = 2;
  private static final int EXCLUDED_BASES = 3;
  private static final int[] MODULI = {1000000007, 1000000009, 998244353, 1000000033};
  private static final class Reader {
    private final byte[] buffer = new byte[BUFFER];
    private int position;
    private int length;

    private int next() throws Exception {
      if (position == length) {
        length = System.in.read(buffer);
        position = 0;
        if (length < 0)
          return -1;
      }
      return buffer[position++];
    }

    String token() throws Exception {
      StringBuilder result = new StringBuilder();
      int value;
      do {
        value = next();
      } while (value >= 0 && value <= 32);
      while (value > 32) {
        result.append((char) value);
        value = next();
      }
      return result.toString();
    }

    int first() throws Exception {
      int value;
      do {
        value = next();
      } while (value >= 0 && value <= 32);
      int result = value;
      while (value > 32) value = next();
      return result;
    }

    int number() throws Exception {
      int value;
      do {
        value = next();
      } while (value >= 0 && value <= 32);
      int result = 0;
      while (value > 32) {
        result = 10 * result + value - '0';
        value = next();
      }
      return result;
    }
  }

  private static final class Field {
    final int modulus;
    final int[] powers, forward, backward;
    Field(byte[] word, int prime, int base) {
      modulus = prime;
      int size = word.length;
      powers = new int[size];
      forward = new int[size + 1];
      backward = new int[size + 1];
      powers[0] = 1;
      for (int i = 1; i < size; ++i) powers[i] = (int) ((long) powers[i - 1] * base % prime);
      for (int i = 1; i <= size; ++i) {
        forward[i] = (int) ((long) word[i - 1] * powers[i - 1] % prime);
        backward[i] = (int) ((long) word[i - 1] * powers[size - i] % prime);
      }
      for (int i = 1; i <= size; ++i) {
        int parent = i + (i & -i);
        if (parent <= size) {
          forward[parent] = add(forward[parent], forward[i]);
          backward[parent] = add(backward[parent], backward[i]);
        }
      }
    }
    int add(int a, int b) {
      int sum = a + b;
      return sum >= modulus ? sum - modulus : sum;
    }
    void change(int position, int delta) {
      int first = (int) ((long) delta * powers[position] % modulus);
      int second = (int) ((long) delta * powers[powers.length - 1 - position] % modulus);
      if (first < 0)
        first += modulus;
      if (second < 0)
        second += modulus;
      for (int i = position + 1; i < forward.length; i += i & -i) {
        forward[i] = add(forward[i], first);
        backward[i] = add(backward[i], second);
      }
    }
    long prefix(int[] tree, int end) {
      long sum = 0;
      for (int i = end; i > 0; i -= i & -i) sum += tree[i];
      return sum;
    }
    boolean palindrome(int left, int end) {
      long first = (prefix(forward, end) - prefix(forward, left)) % modulus;
      long second = (prefix(backward, end) - prefix(backward, left)) % modulus;
      if (first < 0)
        first += modulus;
      if (second < 0)
        second += modulus;
      return first * powers[powers.length - end] % modulus == second * powers[left] % modulus;
    }
  }
  public static void main(String[] args) throws Exception {
    Reader input = new Reader();
    byte[] word = input.token().getBytes("US-ASCII");
    Random random = new Random();
    Field[] fields = new Field[MODULI.length];
    for (int i = 0; i < fields.length; ++i) {
      int prime = MODULI[i];
      fields[i] = new Field(word, prime, MINIMUM_BASE + random.nextInt(prime - EXCLUDED_BASES));
    }
    StringBuilder answer = new StringBuilder();
    int operations = input.number();
    for (int step = 0; step < operations; ++step) {
      int operation = input.first();
      int left = input.number() - 1;
      if (operation == 'c') {
        byte value = (byte) input.first();
        int delta = value - word[left];
        word[left] = value;
        for (Field field : fields) field.change(left, delta);
      } else {
        int end = input.number();
        boolean equal = true;
        for (Field field : fields) {
          if (!field.palindrome(left, end)) {
            equal = false;
            break;
          }
        }
        answer.append(equal ? "Yes\n" : "No\n");
      }
    }
    System.out.print(answer);
  }
}
