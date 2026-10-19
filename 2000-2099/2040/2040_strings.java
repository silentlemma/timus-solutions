import java.io.IOException;

public class Main {
  static final int MAXIMUM_LENGTH = 5000000;
  static final int FIELD_BYTES = 3;
  static final int RECORD_BYTES = 4 * FIELD_BYTES;
  static final int BYTE_BITS = Byte.SIZE;
  static final int BYTE_MASK = (1 << BYTE_BITS) - 1;
  static final int LINK_OFFSET = FIELD_BYTES;
  static final int EDGE_OFFSET = 2 * FIELD_BYTES;
  static final int NEW_PALINDROME = 4;
  static final int LETTER_MASK = BYTE_MASK ^ NEW_PALINDROME;

  static int get(byte[] nodes, int id, int field) {
    int at = id * RECORD_BYTES + field;
    return (nodes[at] & BYTE_MASK) | ((nodes[at + 1] & BYTE_MASK) << BYTE_BITS)
        | ((nodes[at + 2] & BYTE_MASK) << (2 * BYTE_BITS));
  }

  static void put(byte[] nodes, int id, int field, int value) {
    int at = id * RECORD_BYTES + field;
    nodes[at] = (byte) value;
    nodes[at + 1] = (byte) (value >>> BYTE_BITS);
    nodes[at + 2] = (byte) (value >>> (2 * BYTE_BITS));
  }

  static byte[] solve(byte[] word, int begin, int length) {
    byte[] nodes = new byte[(length + 2) * RECORD_BYTES];
    put(nodes, 1, 0, 1);
    int last = 1, used = 2;
    for (int pos = 0; pos < length; pos++) {
      byte letter = word[begin + pos];
      int edge = EDGE_OFFSET + (letter - 'a') * FIELD_BYTES;
      int parent = last;
      while (true) {
        int before = pos - get(nodes, parent, 0);
        if (before >= 0 && (word[begin + before] & LETTER_MASK) == letter)
          break;
        parent = get(nodes, parent, LINK_OFFSET);
      }
      int current = get(nodes, parent, edge);
      if (current == 0) {
        current = used++;
        int newLength = get(nodes, parent, 0) + 1;
        put(nodes, current, 0, newLength + 1);
        put(nodes, parent, edge, current);
        if (newLength == 1) {
          put(nodes, current, LINK_OFFSET, 1);
        } else {
          int candidate = get(nodes, parent, LINK_OFFSET);
          while (true) {
            int before = pos - get(nodes, candidate, 0);
            if (before >= 0 && (word[begin + before] & LETTER_MASK) == letter)
              break;
            candidate = get(nodes, candidate, LINK_OFFSET);
          }
          put(nodes, current, LINK_OFFSET, get(nodes, candidate, edge));
        }
        word[begin + pos] |= NEW_PALINDROME;
      }
      last = current;
    }
    for (int pos = begin; pos < begin + length; pos++)
      word[pos] = (byte) ('0' + ((word[pos] & NEW_PALINDROME) != 0 ? 1 : 0));
    return word;
  }

  public static void main(String[] args) throws IOException {
    byte[] input = new byte[MAXIMUM_LENGTH + 2];
    int used = 0;
    while (used < input.length) {
      int got = System.in.read(input, used, input.length - used);
      if (got < 0)
        break;
      used += got;
    }
    int begin = 0, end = used;
    while (begin < end && input[begin] <= ' ') begin++;
    while (end > begin && input[end - 1] <= ' ') end--;
    byte[] output = solve(input, begin, end - begin);
    System.out.write(output, begin, end - begin);
    System.out.write('\n');
  }
}
