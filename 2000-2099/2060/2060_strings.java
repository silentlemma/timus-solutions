import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class Main {
  static int[][] palindromeCounts(byte[] word) {
    int n = word.length;
    int[] radii = new int[n], ending = new int[n + 1], starting = new int[n + 1];
    int left = 0, right = -1;
    for (int center = 0; center < n; ++center) {
      int radius = center > right ? 1 : Math.min(radii[left + right - center], right - center + 1);
      while (center - radius >= 0 && center + radius < n
          && word[center - radius] == word[center + radius])
        ++radius;
      radii[center] = radius;
      if (center + radius - 1 > right) {
        left = center - radius + 1;
        right = center + radius - 1;
      }
      ++ending[center];
      --ending[center + radius];
      ++starting[center - radius + 1];
      --starting[center + 1];
    }
    left = 0;
    right = -1;
    for (int center = 0; center < n; ++center) {
      int radius =
          center > right ? 0 : Math.min(radii[left + right - center + 1], right - center + 1);
      while (center - radius - 1 >= 0 && center + radius < n
          && word[center - radius - 1] == word[center + radius])
        ++radius;
      radii[center] = radius;
      if (center + radius - 1 > right) {
        left = center - radius;
        right = center + radius - 1;
      }
      if (radius != 0) {
        ++ending[center];
        --ending[center + radius];
        ++starting[center - radius];
        --starting[center];
      }
    }
    int countEnding = 0, countStarting = 0;
    for (int i = 0; i < n; ++i) {
      countEnding += ending[i];
      countStarting += starting[i];
      ending[i] = countEnding;
      starting[i] = countStarting;
    }
    return new int[][] {ending, starting};
  }

  static long solve(byte[] word) {
    int[][] counts = palindromeCounts(word);
    long answer = 0;
    for (int cut = 0; cut + 1 < word.length; ++cut)
      answer += (long) counts[0][cut] * counts[1][cut + 1];
    return answer;
  }

  public static void main(String[] args) throws Exception {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    System.out.println(solve(input.readLine().trim().getBytes(StandardCharsets.US_ASCII)));
  }
}
