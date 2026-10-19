import java.io.BufferedOutputStream;

public class Main {
  static final int MAX_WORD_LENGTH = 200000;
  static final int MAX_NODES = 2 * MAX_WORD_LENGTH + 2;
  static final int MAX_INPUT_BYTES = 8 * 1024 * 1024;
  static final int OUTPUT_BATCH = 65536;
  static final int DIGITS = 10;
  static final int BYTE_MASK = 0xff;

  static class Tree {
    int[] length = new int[MAX_NODES], link = new int[MAX_NODES];
    int[] first = new int[MAX_NODES], next = new int[MAX_NODES];
    int[] label = new int[MAX_NODES], a = new int[MAX_NODES], b = new int[MAX_NODES];
    int x, y, z;
    Tree() {
      length[0] = -1;
    }
    void solve(byte[] data, int aStart, int aEnd, int bStart, int bEnd) {
      x = y = z = 0;
      if (aEnd - aStart == 1 && bEnd - bStart == 1) {
        if (data[aStart] == data[bStart])
          y = 1;
        else {
          x = 1;
          z = 1;
        }
        return;
      }
      first[0] = first[1] = 0;
      a[0] = a[1] = b[0] = b[1] = 0;
      int nodes = 2;
      for (int pass = 0; pass < 2; ++pass) {
        int start = pass == 0 ? aStart : bStart, stop = pass == 0 ? aEnd : bEnd;
        int[] counts = pass == 0 ? a : b;
        int last = 1;
        for (int end = start; end < stop; ++end) {
          int letter = data[end] & BYTE_MASK, node = last;
          while (end - length[node] - 1 < start
              || (data[end - length[node] - 1] & BYTE_MASK) != letter)
            node = link[node];
          int found = first[node];
          while (found != 0 && label[found] != letter) found = next[found];
          if (found == 0) {
            found = nodes++;
            int size = length[node] + 2, suffix = 1;
            if (size != 1) {
              int candidate = link[node];
              while (end - length[candidate] - 1 < start
                  || (data[end - length[candidate] - 1] & BYTE_MASK) != letter)
                candidate = link[candidate];
              suffix = first[candidate];
              while (label[suffix] != letter) suffix = next[suffix];
            }
            length[found] = size;
            link[found] = suffix;
            first[found] = 0;
            next[found] = first[node];
            label[found] = letter;
            first[node] = found;
            a[found] = b[found] = 0;
          }
          last = found;
          ++counts[found];
        }
      }
      for (int node = nodes - 1; node >= 2; --node) {
        int ca = a[node], cb = b[node], suffix = link[node];
        a[suffix] += ca;
        b[suffix] += cb;
        if (ca > cb)
          ++x;
        else if (ca == cb)
          ++y;
        else
          ++z;
      }
    }
  }

  static class Input {
    byte[] data = new byte[MAX_INPUT_BYTES];
    int size, position, end;
    Input() throws Exception {
      while (size < data.length) {
        int got = System.in.read(data, size, data.length - size);
        if (got < 0)
          break;
        size += got;
      }
    }
    int line() {
      int begin = position;
      while (position < size && data[position] != '\n') ++position;
      end = position;
      if (position < size)
        ++position;
      if (end > begin && data[end - 1] == '\r')
        --end;
      return begin;
    }
  }

  static class Output {
    BufferedOutputStream stream = new BufferedOutputStream(System.out, OUTPUT_BATCH);
    byte[] digits = new byte[DIGITS];
    void number(int value) throws Exception {
      int used = 0;
      do {
        digits[used++] = (byte) ('0' + value % 10);
        value /= 10;
      } while (value != 0);
      while (used > 0) stream.write(digits[--used]);
    }
    void row(int index, Tree tree) throws Exception {
      stream.write('C');
      stream.write('a');
      stream.write('s');
      stream.write('e');
      stream.write(' ');
      stream.write('#');
      number(index);
      stream.write(':');
      stream.write(' ');
      number(tree.x);
      stream.write(' ');
      number(tree.y);
      stream.write(' ');
      number(tree.z);
      stream.write('\n');
    }
  }

  public static void main(String[] args) throws Exception {
    Input input = new Input();
    int begin = input.line(), tests = 0;
    for (int i = begin; i < input.end; ++i) {
      int digit = input.data[i] - '0';
      if (digit >= 0 && digit < 10)
        tests = tests * 10 + digit;
    }
    Tree tree = new Tree();
    Output output = new Output();
    for (int index = 1; index <= tests; ++index) {
      int aStart = input.line(), aEnd = input.end;
      int bStart = input.line(), bEnd = input.end;
      tree.solve(input.data, aStart, aEnd, bStart, bEnd);
      output.row(index, tree);
    }
    output.stream.flush();
  }
}
