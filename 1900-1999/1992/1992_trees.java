import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
  private static final int LEARN = 0, ROLLBACK = 1, RELEARN = 2, CLONE = 3, CHECK = 4;
  private static final class Reader {
    final byte[] buffer = new byte[65536];
    int position, length;
    int next() throws Exception {
      if (position == length) {
        length = System.in.read(buffer);
        position = 0;
        if (length < 0)
          return -1;
      }
      return buffer[position++];
    }
    int number() throws Exception {
      int c;
      do {
        c = next();
      } while (c >= 0 && c <= 32);
      int result = 0;
      while (c > 32) {
        result = result * 10 + c - '0';
        c = next();
      }
      return result;
    }
    int command() throws Exception {
      int first;
      do {
        first = next();
      } while (first >= 0 && first <= 32);
      int second = next(), c = second;
      while (c > 32) c = next();
      if (first == 'l')
        return LEARN;
      if (first == 'r')
        return second == 'o' ? ROLLBACK : RELEARN;
      return second == 'l' ? CLONE : CHECK;
    }
  }
  private static void writeProgram(BufferedWriter output, int value, char[] digits)
      throws Exception {
    int start = digits.length;
    do {
      digits[--start] = (char) ('0' + value % 10);
      value /= 10;
    } while (value != 0);
    output.write(digits, start, digits.length - start);
  }
  public static void main(String[] args) throws Exception {
    Reader input = new Reader();
    int count = input.number();
    input.number();
    int[] value = new int[count + 2], previous = new int[count + 2];
    int[] learned = new int[count + 2], redo = new int[count + 2];
    int used = 0, entities = 1;
    BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
    char[] digits = new char[10];
    for (int step = 0; step < count; ++step) {
      int command = input.command(), entity = input.number();
      if (command == LEARN) {
        ++used;
        value[used] = input.number();
        previous[used] = learned[entity];
        learned[entity] = used;
        redo[entity] = 0;
      } else if (command == ROLLBACK) {
        int head = learned[entity];
        ++used;
        value[used] = value[head];
        previous[used] = redo[entity];
        learned[entity] = previous[head];
        redo[entity] = used;
      } else if (command == RELEARN) {
        int head = redo[entity];
        ++used;
        value[used] = value[head];
        previous[used] = learned[entity];
        redo[entity] = previous[head];
        learned[entity] = used;
      } else if (command == CLONE) {
        ++entities;
        learned[entities] = learned[entity];
        redo[entities] = redo[entity];
      } else {
        int head = learned[entity];
        if (head == 0)
          output.write("basic");
        else
          writeProgram(output, value[head], digits);
        output.newLine();
      }
    }
    output.flush();
  }
}
