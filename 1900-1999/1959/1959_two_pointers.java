import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static class Modes {
    final int[] frequency, previous, following, head;
    int maximum;
    Modes(int alphabet, int capacity) {
      frequency = new int[alphabet + 1];
      previous = new int[alphabet + 1];
      following = new int[alphabet + 1];
      head = new int[capacity + 1];
    }
    void change(int value, int delta) {
      int old = frequency[value];
      if (old != 0) {
        int left = previous[value], right = following[value];
        if (left != 0)
          following[left] = right;
        else
          head[old] = right;
        if (right != 0)
          previous[right] = left;
      }
      int count = old + delta;
      frequency[value] = count;
      if (count != 0) {
        int first = head[count];
        previous[value] = 0;
        following[value] = first;
        if (first != 0)
          previous[first] = value;
        head[count] = value;
      } else {
        previous[value] = 0;
        following[value] = 0;
      }
      maximum = Math.max(maximum, count);
      while (maximum > 0 && head[maximum] == 0) maximum--;
    }
    int mode() {
      return head[maximum];
    }
  }

  static void restore(int[] text, int[] pattern) {
    int n = text.length, m = pattern.length, gap = n - m, alphabet = 0;
    boolean textHoles = false, patternHoles = false;
    for (int value : text) {
      alphabet = Math.max(alphabet, value);
      textHoles |= value == 0;
    }
    for (int value : pattern) {
      alphabet = Math.max(alphabet, value);
      patternHoles |= value == 0;
    }
    if (textHoles) {
      Modes counter = new Modes(alphabet, m);
      for (int index = 0; index < n; index++) {
        if (index < m)
          counter.change(pattern[index], 1);
        if (index > gap)
          counter.change(pattern[index - gap - 1], -1);
        if (text[index] == 0)
          text[index] = counter.mode();
      }
    } else if (patternHoles) {
      int width = gap + 1;
      Modes counter = new Modes(alphabet, width);
      for (int index = 0; index < width; index++) counter.change(text[index], 1);
      for (int index = 0; index < m; index++) {
        if (pattern[index] == 0)
          pattern[index] = counter.mode();
        if (index + 1 < m) {
          counter.change(text[index], -1);
          counter.change(text[index + width], 1);
        }
      }
    }
  }

  static void appendRow(StringBuilder output, int[] values) {
    for (int i = 0; i < values.length; i++) {
      if (i > 0)
        output.append(' ');
      output.append(values[i]);
    }
    output.append('\n');
  }

  static class FastInput {
    final BufferedInputStream input = new BufferedInputStream(System.in);
    int nextInt() throws IOException {
      int c;
      do {
        c = input.read();
      } while (c <= ' ' && c != -1);
      int value = 0;
      while (c > ' ') {
        value = value * 10 + c - '0';
        c = input.read();
      }
      return value;
    }
  }

  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = in.nextInt();
    int[] text = new int[n];
    for (int i = 0; i < n; i++) text[i] = in.nextInt();
    int m = in.nextInt();
    int[] pattern = new int[m];
    for (int i = 0; i < m; i++) pattern[i] = in.nextInt();
    restore(text, pattern);
    StringBuilder output = new StringBuilder();
    appendRow(output, text);
    appendRow(output, pattern);
    System.out.print(output);
  }
}
