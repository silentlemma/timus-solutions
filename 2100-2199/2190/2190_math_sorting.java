import java.io.DataInputStream;
import java.io.IOException;

public class Main {
  private static DataInputStream in = new DataInputStream(System.in);
  private static final int BUFFER_SIZE = 1 << 16;
  private static byte[] buffer = new byte[BUFFER_SIZE];
  private static int length = 0;
  private static int pointer = 0;

  private static int read() throws IOException {
    if (pointer == length) {
      length = in.read(buffer, 0, buffer.length);
      pointer = 0;
      if (length <= 0) {
        return -1;
      }
    }
    return buffer[pointer++];
  }

  private static long nextLong() throws IOException {
    int c = read();
    while (c < '0') {
      c = read();
    }
    long value = 0;
    while (c >= '0') {
      value = value * 10 + (c - '0');
      c = read();
    }
    return value;
  }

  private static long gcd(long a, long b) {
    while (b != 0) {
      long t = a % b;
      a = b;
      b = t;
    }
    return a;
  }

  private static long[] s;
  private static long[] q;

  private static long cost(long k) {
    long sum = 0;
    for (int i = 0; i < s.length; i++) {
      sum += Math.abs(s[i] - k * q[i]);
    }
    return sum;
  }

  private static void mergeSort(int[] order, int[] tmp, int from, int to) {
    if (to - from < 2) {
      return;
    }
    int mid = (from + to) >>> 1;
    mergeSort(order, tmp, from, mid);
    mergeSort(order, tmp, mid, to);
    int a = from;
    int b = mid;
    int k = from;
    while (a < mid && b < to) {
      int i = order[a];
      int j = order[b];
      if (s[j] * q[i] < s[i] * q[j]) {
        tmp[k++] = order[b++];
      } else {
        tmp[k++] = order[a++];
      }
    }
    while (a < mid) {
      tmp[k++] = order[a++];
    }
    while (b < to) {
      tmp[k++] = order[b++];
    }
    System.arraycopy(tmp, from, order, from, to - from);
  }

  public static void main(String[] args) throws IOException {
    int n = (int) nextLong();
    s = new long[n];
    q = new long[n];
    for (int i = 0; i < n; i++) {
      s[i] = nextLong();
    }
    long g = 0;
    for (int i = 0; i < n; i++) {
      q[i] = nextLong();
      g = gcd(g, q[i]);
    }
    long total = 0;
    for (int i = 0; i < n; i++) {
      q[i] /= g;
      total += q[i];
    }
    // The heaps become k * q for an integer k >= 1, and the cost
    // sum |s - k q| = sum q |s / q - k| is convex in k with its real minimum
    // at the median of the ratios s / q weighted by q.
    int[] order = new int[n];
    for (int i = 0; i < n; i++) {
      order[i] = i;
    }
    mergeSort(order, new int[n], 0, n);
    long weight = 0;
    int median = order[n - 1];
    for (int i : order) {
      weight += q[i];
      if (2 * weight >= total) {
        median = i;
        break;
      }
    }
    long low = s[median] / q[median];
    long best = cost(low + 1);
    if (low >= 1) {
      best = Math.min(best, cost(low));
    }
    System.out.println(best);
  }
}
