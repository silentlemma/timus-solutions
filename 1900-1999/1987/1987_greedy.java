import java.io.IOException;
import java.io.InputStream;

public class Main {
  static final int BUFFER_SIZE = 65536;
  static class Reader {
    InputStream input = System.in;
    byte[] buffer = new byte[BUFFER_SIZE];
    int at, size;
    int read() throws IOException {
      if (at == size) {
        size = input.read(buffer);
        at = 0;
        if (size < 0)
          return -1;
      }
      return buffer[at++];
    }
    int next() throws IOException {
      int ch = read();
      while (ch <= ' ' && ch >= 0) ch = read();
      int value = 0;
      while (ch > ' ') {
        value = value * 10 + ch - '0';
        ch = read();
      }
      return value;
    }
  }
  static int[] locate(int[] left, int[] right, int[] queries) {
    int[] stack = new int[left.length], answers = new int[queries.length];
    int size = 0, index = 0;
    for (int q = 0; q < queries.length; q++) {
      int point = queries[q];
      while (index < left.length && left[index] <= point) {
        while (size > 0 && right[stack[size - 1]] < left[index]) size--;
        stack[size++] = index++;
      }
      while (size > 0 && right[stack[size - 1]] < point) size--;
      answers[q] = size == 0 ? -1 : stack[size - 1] + 1;
    }
    return answers;
  }
  public static void main(String[] args) throws IOException {
    Reader in = new Reader();
    int n = in.next();
    int[] left = new int[n], right = new int[n];
    for (int i = 0; i < n; i++) {
      left[i] = in.next();
      right[i] = in.next();
    }
    int m = in.next();
    int[] queries = new int[m];
    for (int i = 0; i < m; i++) queries[i] = in.next();
    StringBuilder out = new StringBuilder();
    for (int answer : locate(left, right, queries)) out.append(answer).append('\n');
    System.out.print(out);
  }
}
