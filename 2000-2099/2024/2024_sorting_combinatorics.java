import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
  static final int ALPHABET = 26;

  static long[] solve(String text, int limit) {
    int[] counts = new int[ALPHABET];
    for (int index = 0; index < text.length(); index++) counts[text.charAt(index) - 'a']++;
    Arrays.sort(counts);
    int size = 0;
    for (int index = ALPHABET - limit; index < ALPHABET; index++) size += counts[index];
    int boundary = counts[ALPHABET - limit];
    if (boundary == 0)
      return new long[] {size, 1};
    int greater = 0;
    int tied = 0;
    for (int count : counts) {
      if (count > boundary)
        greater++;
      if (count == boundary)
        tied++;
    }
    int chosen = Math.min(limit - greater, tied - (limit - greater));
    long ways = 1;
    for (int index = 1; index <= chosen; index++) ways = ways * (tied - index + 1) / index;
    return new long[] {size, ways};
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
    String text = readToken(in);
    int limit = Integer.parseInt(readToken(in));
    long[] answer = solve(text, limit);
    System.out.println(answer[0] + " " + answer[1]);
  }
}
