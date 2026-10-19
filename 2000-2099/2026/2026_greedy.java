import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int ALPHABET = 26;

  static String solve(String pattern, int limit) {
    char[] answer = pattern.toCharArray();
    boolean[] fixed = new boolean[ALPHABET + 1];
    int[] positive = new int[answer.length];
    int[] negative = new int[answer.length];
    int plus = 0;
    int minus = 0;
    for (int index = 0; index < answer.length; index++) {
      if (answer[index] != '?')
        fixed[answer[index] - 'a' + 1] = true;
      else if (index % 2 == 0)
        positive[plus++] = index;
      else
        negative[minus++] = index;
    }
    int[] missing = new int[ALPHABET];
    int count = 0;
    int fixedCount = 0;
    for (int value = 1; value <= ALPHABET; value++) {
      if (fixed[value])
        fixedCount++;
      else
        missing[count++] = value;
    }
    int needed = Math.max(0, limit - fixedCount);
    if (plus + minus < needed)
      return "-1";
    int[] low = new int[count + 1];
    int[] high = new int[count + 1];
    for (int index = 0; index < count; index++) {
      low[index + 1] = low[index] + missing[index] - 1;
      high[index + 1] = high[index] + ALPHABET - missing[count - 1 - index];
    }
    int lower = Math.max(0, needed - minus);
    int upper = Math.min(needed, plus);
    int bestCost = ALPHABET * ALPHABET;
    int chosen = 0;
    for (int take = lower; take <= upper; take++) {
      int cost = high[take] + low[needed - take];
      if (cost < bestCost) {
        bestCost = cost;
        chosen = take;
      }
    }
    for (int index = 0; index < plus; index++) answer[positive[index]] = 'z';
    for (int index = 0; index < minus; index++) answer[negative[index]] = 'a';
    for (int index = 0; index < chosen; index++)
      answer[positive[index]] = (char) ('a' + missing[count - 1 - index] - 1);
    for (int index = 0; index < needed - chosen; index++)
      answer[negative[index]] = (char) ('a' + missing[index] - 1);
    return new String(answer);
  }

  static String readToken(BufferedInputStream in) throws IOException {
    StringBuilder token = new StringBuilder();
    int character;
    do {
      character = in.read();
    } while (character >= 0 && character <= ' ');
    while (character > ' ') {
      token.append((char) character);
      character = in.read();
    }
    return token.toString();
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    String pattern = readToken(in);
    int limit = Integer.parseInt(readToken(in));
    System.out.println(solve(pattern, limit));
  }
}
