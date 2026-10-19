import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  private static final int ALPHABET = 26;
  private static final char FIRST = 'a';

  private static String solve(String source, String modifiers) {
    int size = source.length();
    int[] frequency = new int[ALPHABET], counts = new int[ALPHABET];
    for (int at = 0; at < size; at++) frequency[source.charAt(at) - FIRST]++;
    for (int at = 0; at < modifiers.length(); at++) counts[modifiers.charAt(at) - FIRST]++;
    int[][] positions = new int[ALPHABET][];
    for (int c = 0; c < ALPHABET; c++) {
      positions[c] = new int[frequency[c] + 1];
      positions[c][frequency[c]] = size;
    }
    int[] fill = new int[ALPHABET];
    for (int at = 0; at < size; at++) {
      int c = source.charAt(at) - FIRST;
      positions[c][fill[c]++] = at;
    }
    int[] head = new int[ALPHABET], cut = counts.clone(), nextPosition = new int[ALPHABET];
    int[] nextCut = new int[ALPHABET], delta = new int[ALPHABET];
    int bad = 0, available = 0, present = 0;
    for (int c = 0; c < ALPHABET; c++) {
      nextPosition[c] = positions[c][0];
      nextCut[c] = cut[c] < frequency[c] ? positions[c][cut[c]] : size;
      delta[c] = counts[c] - frequency[c];
      if (delta[c] < 0 || (delta[c] & 1) != 0)
        bad |= 1 << c;
      if (counts[c] > 0)
        available |= 1 << c;
      if (frequency[c] > 0)
        present |= 1 << c;
    }
    int at = 0, original = ALPHABET, length = 0;
    boolean dirty = true;
    char[] answer = new char[source.length() + modifiers.length()];
    while (bad != 0) {
      if (dirty) {
        if (at == size)
          original = ALPHABET;
        else if (counts[source.charAt(at) - FIRST] == 0)
          original = source.charAt(at) - FIRST;
        else {
          int limit = size;
          for (int value : nextCut) limit = Math.min(limit, value);
          for (int candidates = present; candidates != 0; candidates &= candidates - 1) {
            int c = Integer.numberOfTrailingZeros(candidates);
            if (nextPosition[c] <= limit) {
              original = c;
              break;
            }
          }
        }
        dirty = false;
      }
      int modifier = available != 0 ? Integer.numberOfTrailingZeros(available) : ALPHABET;
      int c;
      if (original <= modifier) {
        c = original;
        int to = nextPosition[c];
        while (at < to) {
          int removed = source.charAt(at++) - FIRST;
          counts[removed]--;
          nextPosition[removed] = positions[removed][++head[removed]];
          if (counts[removed] == 0)
            available &= ~(1 << removed);
          if (head[removed] == frequency[removed])
            present &= ~(1 << removed);
        }
        nextPosition[c] = positions[c][++head[c]];
        at++;
        if (head[c] == frequency[c])
          present &= ~(1 << c);
        cut[c]++;
        delta[c]++;
        dirty = true;
      } else {
        c = modifier;
        if (--counts[c] == 0)
          available &= ~(1 << c);
        cut[c]--;
        delta[c]--;
      }
      nextCut[c] = cut[c] < frequency[c] ? positions[c][cut[c]] : size;
      if (delta[c] < 0 || (delta[c] & 1) != 0)
        bad |= 1 << c;
      else
        bad &= ~(1 << c);
      answer[length++] = (char) (FIRST + c);
    }
    return new String(answer, 0, length);
  }

  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    System.out.println(solve(input.readLine(), input.readLine()));
  }
}
