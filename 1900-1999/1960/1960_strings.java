import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  static final int ALPHABET_SIZE = 26;
  static final int EMPTY_ROOT = 1;
  static final int ROOT_COUNT = 2;

  static int[] distinctCounts(String text) {
    int[] lengths = new int[text.length() + ROOT_COUNT],
          links = new int[text.length() + ROOT_COUNT];
    int[] next = new int[(text.length() + ROOT_COUNT) * ALPHABET_SIZE];
    lengths[0] = -1;
    int count = ROOT_COUNT, last = EMPTY_ROOT;
    int[] answer = new int[text.length()];
    for (int position = 0; position < text.length(); position++) {
      char letter = text.charAt(position);
      int code = letter - 'a', parent = last;
      while (true) {
        int left = position - lengths[parent] - 1;
        if (left >= 0 && text.charAt(left) == letter)
          break;
        parent = links[parent];
      }
      int key = parent * ALPHABET_SIZE + code, node = next[key];
      if (node == 0) {
        node = count++;
        lengths[node] = lengths[parent] + 2;
        next[key] = node;
        if (lengths[node] == 1)
          links[node] = EMPTY_ROOT;
        else {
          int candidate = links[parent];
          while (true) {
            int left = position - lengths[candidate] - 1;
            if (left >= 0 && text.charAt(left) == letter)
              break;
            candidate = links[candidate];
          }
          links[node] = next[candidate * ALPHABET_SIZE + code];
        }
      }
      last = node;
      answer[position] = count - ROOT_COUNT;
    }
    return answer;
  }

  static void appendCounts(StringBuilder output, int[] values) {
    for (int i = 0; i < values.length; i++) {
      if (i > 0)
        output.append(' ');
      output.append(values[i]);
    }
    output.append('\n');
  }

  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    int[] answer = distinctCounts(input.readLine().trim());
    StringBuilder output = new StringBuilder();
    appendCounts(output, answer);
    System.out.print(output);
  }
}
