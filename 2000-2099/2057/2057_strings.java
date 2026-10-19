import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  static class Palindromes {
    final int[] odd, even;
    Palindromes(char[] word) {
      int size = word.length;
      odd = new int[size];
      even = new int[size];
      int left = 0, right = -1;
      for (int center = 0; center < size; center++) {
        int radius = center > right ? 1 : Math.min(odd[left + right - center], right - center + 1);
        while (center >= radius && center + radius < size
            && word[center - radius] == word[center + radius])
          radius++;
        odd[center] = radius;
        if (center + radius - 1 > right) {
          left = center - radius + 1;
          right = center + radius - 1;
        }
      }
      left = 0;
      right = -1;
      for (int center = 0; center < size; center++) {
        int radius =
            center > right ? 0 : Math.min(even[left + right - center + 1], right - center + 1);
        while (center > radius && center + radius < size
            && word[center - radius - 1] == word[center + radius])
          radius++;
        even[center] = radius;
        if (center + radius - 1 > right) {
          left = center - radius;
          right = center + radius - 1;
        }
      }
    }
    boolean palindrome(int start, int end) {
      int length = end - start, center = (start + end) / 2;
      return length % 2 != 0 ? odd[center] >= length / 2 + 1 : even[center] >= length / 2;
    }
  }
  static int[] solve(String word) {
    int size = word.length();
    Palindromes radii = new Palindromes(word.toCharArray());
    int[] maximum = new int[size + 1], first = new int[size / 2 + 1], last = new int[size / 2 + 1];
    Arrays.fill(maximum, -1);
    Arrays.fill(first, -1);
    Arrays.fill(last, -1);
    maximum[0] = 0;
    int highest = -1;
    for (int end = 1; end <= size; end++) {
      int position = end - 2;
      if (position >= 0 && maximum[position] >= 0) {
        int value = maximum[position];
        if (first[value] < 0)
          first[value] = position;
        last[value] = position;
        highest = Math.max(highest, value);
      }
      for (int value = highest; value >= 0 && value >= highest - 1; value--) {
        if (first[value] >= 0
            && (!radii.palindrome(first[value], end) || !radii.palindrome(last[value], end))) {
          maximum[end] = value + 1;
          break;
        }
      }
    }
    if (maximum[size] < 0)
      return new int[] {-1, -1};
    return new int[] {radii.palindrome(0, size) ? 2 : 1, maximum[size]};
  }
  public static void main(String[] args) throws Exception {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    int[] answer = solve(input.readLine().trim());
    if (answer[0] < 0)
      System.out.println(-1);
    else
      System.out.println(answer[0] + " " + answer[1]);
  }
}
