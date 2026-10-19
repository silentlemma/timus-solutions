import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  static int lookup(int[] first, int[] next, int[] label, int node, int code) {
    int child = first[node];
    while (child != 0 && label[child] != code) child = next[child];
    return child;
  }

  static final int MAX_ROW_BYTES = 14;

  static class Answer {
    byte[] bytes;
    int size;
    Answer(int n) {
      bytes = new byte[n * MAX_ROW_BYTES];
    }
    void number(int value) {
      if (value < 0) {
        bytes[size++] = '-';
        value = -value;
      }
      int begin = size;
      do {
        bytes[size++] = (byte) ('0' + value % 10);
        value /= 10;
      } while (value != 0);
      for (int l = begin, r = size - 1; l < r; ++l, --r) {
        byte temporary = bytes[l];
        bytes[l] = bytes[r];
        bytes[r] = temporary;
      }
    }
  }

  static Answer solve(String word) {
    int n = word.length(), infinity = n + 1;
    char[] data = new char[n + 1];
    word.getChars(0, n, data, 1);
    int[] length = new int[n + 2], link = new int[n + 2];
    int[] difference = new int[n + 2], series = new int[n + 2];
    int[] cacheOdd = new int[n + 2], cacheEven = new int[n + 2];
    int[] odd = new int[n + 1], even = new int[n + 1];
    Arrays.fill(cacheOdd, infinity);
    Arrays.fill(cacheEven, infinity);
    Arrays.fill(odd, infinity);
    Arrays.fill(even, infinity);
    int[] first = new int[n + 2], next = new int[n + 2], label = new int[n + 2];
    length[0] = -1;
    even[0] = 0;
    int nodes = 2, last = 1;
    Answer output = new Answer(n);
    for (int end = 1; end <= n; ++end) {
      char letter = data[end];
      int code = letter - 'a', node = last;
      while (data[end - length[node] - 1] != letter) node = link[node];
      int found = lookup(first, next, label, node, code);
      if (found == 0) {
        found = nodes++;
        length[found] = length[node] + 2;
        int suffix = 1;
        if (length[found] != 1) {
          int candidate = link[node];
          while (data[end - length[candidate] - 1] != letter) candidate = link[candidate];
          suffix = lookup(first, next, label, candidate, code);
        }
        link[found] = suffix;
        difference[found] = length[found] - length[suffix];
        series[found] = difference[found] == difference[suffix] ? series[suffix] : suffix;
        next[found] = first[node];
        first[node] = found;
        label[found] = code;
      }
      last = found;
      for (node = last; length[node] > 0; node = series[node]) {
        int suffix = link[node], before = end - length[series[node]] - difference[node];
        cacheOdd[node] = odd[before];
        cacheEven[node] = even[before];
        if (difference[node] == difference[suffix]) {
          cacheOdd[node] = Math.min(cacheOdd[node], cacheOdd[suffix]);
          cacheEven[node] = Math.min(cacheEven[node], cacheEven[suffix]);
        }
        odd[end] = Math.min(odd[end], cacheEven[node] + 1);
        even[end] = Math.min(even[end], cacheOdd[node] + 1);
      }
      output.number(odd[end] < infinity ? odd[end] : -1);
      output.bytes[output.size++] = ' ';
      output.number(even[end] < infinity ? even[end] : -2);
      output.bytes[output.size++] = '\n';
    }
    return output;
  }

  public static void main(String[] args) throws Exception {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    Answer answer = solve(input.readLine().trim());
    System.out.write(answer.bytes, 0, answer.size);
  }
}
