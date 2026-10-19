import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Main {
  static final int TREE_FACTOR = 4;
  static final int WINDOW_FACTOR = 3;
  static final int BUFFER_SIZE = 1 << 16;
  static void radii(byte[] s, int n, int oddCap, int evenCap, int[] odd, int[] even) {
    int left = 0, right = -1;
    for (int i = 0; i < n; i++) {
      int d = i > right ? 1 : Math.min(odd[left + right - i], right - i + 1);
      while (d < oddCap && i >= d && i + d < n && s[i - d] == s[i + d]) d++;
      odd[i] = d;
      if (i + d - 1 > right) {
        left = i - d + 1;
        right = i + d - 1;
      }
    }
    left = 0;
    right = -1;
    for (int i = 0; i < n; i++) {
      int d = i > right ? 0 : Math.min(even[left + right - i + 1], right - i + 1);
      while (d < evenCap && i > d && i + d < n && s[i - d - 1] == s[i + d]) d++;
      even[i] = d;
      if (i + d - 1 > right) {
        left = i - d;
        right = i + d - 1;
      }
    }
  }
  static class Characters {
    final int n;
    final byte[] tag;
    Characters(byte[] s) {
      n = s.length;
      tag = new byte[TREE_FACTOR * n];
      build(1, 0, n, s);
    }
    void build(int v, int a, int b, byte[] s) {
      if (b - a == 1) {
        tag[v] = s[a];
        return;
      }
      int mid = (a + b) / 2;
      build(2 * v, a, mid, s);
      build(2 * v + 1, mid, b, s);
      if (tag[2 * v] == tag[2 * v + 1])
        tag[v] = tag[2 * v];
    }
    void assign(int v, int a, int b, int left, int right, byte c) {
      if (left <= a && b <= right) {
        tag[v] = c;
        return;
      }
      int mid = (a + b) / 2;
      if (tag[v] != 0) {
        tag[2 * v] = tag[2 * v + 1] = tag[v];
        tag[v] = 0;
      }
      if (left < mid)
        assign(2 * v, a, mid, left, right, c);
      if (mid < right)
        assign(2 * v + 1, mid, b, left, right, c);
      if (tag[2 * v] == tag[2 * v + 1])
        tag[v] = tag[2 * v];
    }
    int extract(int v, int a, int b, int left, int right, byte[] out, int at) {
      if (tag[v] != 0) {
        int count = Math.min(b, right) - Math.max(a, left);
        for (int i = 0; i < count; i++) out[at++] = tag[v];
        return at;
      }
      int mid = (a + b) / 2;
      if (left < mid)
        at = extract(2 * v, a, mid, left, right, out, at);
      if (mid < right)
        at = extract(2 * v + 1, mid, b, left, right, out, at);
      return at;
    }
  }
  static class Counts {
    final int n;
    final int[] total;
    final byte[] tag;
    Counts(int[] values) {
      n = values.length;
      total = new int[TREE_FACTOR * n];
      tag = new byte[TREE_FACTOR * n];
      build(1, 0, n, values);
    }
    void pull(int v) {
      total[v] = total[2 * v] + total[2 * v + 1];
      tag[v] = tag[2 * v] == tag[2 * v + 1] ? tag[2 * v] : 0;
    }
    void build(int v, int a, int b, int[] values) {
      if (b - a == 1) {
        total[v] = values[a];
        tag[v] = (byte) (values[a] + 1);
        return;
      }
      int mid = (a + b) / 2;
      build(2 * v, a, mid, values);
      build(2 * v + 1, mid, b, values);
      pull(v);
    }
    void replace(int v, int a, int b, int left, int right, int value, int[] values) {
      if ((value >= 0 && left <= a && b <= right) || b - a == 1) {
        int chosen = value >= 0 ? value : values[a - left];
        total[v] = (b - a) * chosen;
        tag[v] = (byte) (chosen + 1);
        return;
      }
      int mid = (a + b) / 2;
      if (tag[v] != 0) {
        int old = tag[v] - 1;
        total[2 * v] = (mid - a) * old;
        total[2 * v + 1] = (b - mid) * old;
        tag[2 * v] = tag[2 * v + 1] = tag[v];
        tag[v] = 0;
      }
      if (left < mid)
        replace(2 * v, a, mid, left, right, value, values);
      if (mid < right)
        replace(2 * v + 1, mid, b, left, right, value, values);
      pull(v);
    }
    int query(int v, int a, int b, int left, int right) {
      if (left <= a && b <= right)
        return total[v];
      if (tag[v] != 0)
        return (tag[v] - 1) * (Math.min(b, right) - Math.max(a, left));
      int mid = (a + b) / 2, answer = 0;
      if (left < mid)
        answer += query(2 * v, a, mid, left, right);
      if (mid < right)
        answer += query(2 * v + 1, mid, b, left, right);
      return answer;
    }
  }
  static class Solver {
    final int n, k, oddCap, evenCap;
    final Characters characters;
    final Counts counts;
    final byte[] work;
    final int[] odd, even, values;
    Solver(byte[] text, int limit) {
      n = text.length;
      k = limit;
      oddCap = (k + 1) / 2;
      evenCap = k / 2;
      characters = new Characters(text);
      int[] first = new int[n], second = new int[n];
      radii(text, n, oddCap, evenCap, first, second);
      for (int i = 0; i < n; i++) first[i] += second[i];
      counts = new Counts(first);
      work = new byte[WINDOW_FACTOR * k];
      odd = new int[WINDOW_FACTOR * k];
      even = new int[WINDOW_FACTOR * k];
      values = new int[2 * k];
    }
    void prepare(int left, int right) {
      int length = characters.extract(1, 0, n, left, right, work, 0);
      radii(work, length, oddCap, evenCap, odd, even);
    }
    void repair(int left, int right) {
      if (left > right)
        return;
      int start = Math.max(0, left - evenCap), end = Math.min(n, right + oddCap);
      prepare(start, end);
      for (int i = left; i <= right; i++) values[i - left] = odd[i - start] + even[i - start];
      counts.replace(1, 0, n, left, right + 1, -1, values);
    }
    void assign(int left, int right, byte c) {
      characters.assign(1, 0, n, left, right + 1, c);
      int a = Math.max(0, left - oddCap + 1), b = Math.min(n - 1, right + evenCap);
      int x = left + evenCap, y = right - oddCap + 1;
      if (x <= y) {
        counts.replace(1, 0, n, x, y + 1, k, values);
        repair(a, x - 1);
        repair(y + 1, b);
      } else {
        repair(a, b);
      }
    }
    int partial(int left, int right, int first, int last) {
      prepare(left, right);
      int answer = 0;
      for (int i = first; i < last; i++) answer += odd[i] + even[i];
      return answer;
    }
    int query(int left, int right) {
      int length = right - left + 1;
      if (length < k)
        return partial(left, right + 1, 0, length);
      int answer = counts.query(1, 0, n, left + evenCap, right - oddCap + 2);
      if (evenCap > 0)
        answer += partial(left, left + k - 1, 0, evenCap);
      if (oddCap > 1)
        answer += partial(right - k + 2, right + 1, evenCap, k - 1);
      return answer;
    }
  }
  static class Input {
    final byte[] buffer = new byte[BUFFER_SIZE];
    int at, size;
    int read() throws IOException {
      if (at == size) {
        size = System.in.read(buffer);
        at = 0;
        if (size < 0)
          return -1;
      }
      return buffer[at++];
    }
    int first() throws IOException {
      int c;
      do {
        c = read();
      } while (c >= 0 && c <= ' ');
      return c;
    }
    int integer() throws IOException {
      int c = first(), answer = 0;
      while (c > ' ') {
        answer = 10 * answer + c - '0';
        c = read();
      }
      return answer;
    }
    byte[] word() throws IOException {
      int c = first();
      StringBuilder out = new StringBuilder();
      while (c > ' ') {
        out.append((char) c);
        c = read();
      }
      return out.toString().getBytes(StandardCharsets.US_ASCII);
    }
  }
  public static void main(String[] args) throws IOException {
    Input input = new Input();
    byte[] text = input.word();
    int k = input.integer();
    Solver model = new Solver(text, k);
    StringBuilder out = new StringBuilder();
    for (int q = input.integer(); q > 0; q--) {
      int type = input.integer(), left = input.integer() - 1, right = input.integer() - 1;
      if (type == 1)
        model.assign(left, right, (byte) input.first());
      else
        out.append(model.query(left, right)).append('\n');
    }
    System.out.print(out);
  }
}
